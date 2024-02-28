import base64
import json
import logging
import os
import uuid

from pyrage import decrypt, encrypt, passphrase, x25519

logger = logging.getLogger(__name__)


def create_age_keypair():
    """create age private key"""
    age_identity = x25519.Identity.generate()
    age_pvtkey = str(age_identity)
    age_pubkey = str(age_identity.to_public())
    return age_pvtkey, age_pubkey


def age_pubkey_from_str(pubkey: str) -> x25519.Recipient:
    return x25519.Recipient.from_str(pubkey)


def age_pvtkey_from_str(pvtkey: str) -> x25519.Identity:
    return x25519.Identity.from_str(pvtkey)


def age_pvtkey_to_pubkey(pvtkey: str) -> str:
    """age private key to public key"""
    identity = age_pvtkey_from_str(pvtkey)
    pubkey = str(identity.to_public())
    return pubkey


def age_pvtkey_from_file(path: str, password: str) -> x25519.Identity:
    if not os.path.exists(path):
        raise ValueError(f"can not find file path: {path}")

    with open(path, "rb") as fp:
        decrypted = passphrase.decrypt(fp.read(), password)
    return age_pvtkey_from_str(str(decrypted))


def age_encrypt(recipients: list, data: bytes) -> bytes:
    """recipients list of x25519.Recipient"""
    if not data:
        raise ValueError("invalid data")
    if not recipients:
        raise ValueError("invalid recipients")

    _recipients = []
    for item in recipients:
        if isinstance(item, str):
            _recipients.append(age_pubkey_from_str(item))
        elif isinstance(item, x25519.Recipient):
            _recipients.append(item)
        else:
            raise ValueError(f"invalid recipients {item}")

    return encrypt(data, _recipients)


def age_decrypt(identity: x25519.Identity, data: bytes):
    if isinstance(identity, str):
        identity = age_pvtkey_from_str(identity)
    elif not isinstance(identity, x25519.Identity):
        raise ValueError("invalid identity")

    try:
        return decrypt(data, [identity])
    except Exception as err:
        logger.warning("age_decrypt error: %s", err)
        return None


def trx_age_encrypt(data: dict, recipients: list, post_id: str = None):
    data = json.dumps(data).encode()
    encrypted = age_encrypt(recipients, data)
    return {
        "content": base64.b64encode(encrypted).decode(),
        "type": "age",
        "post_id": post_id or str(uuid.uuid4()),
        "recipients": recipients,
    }


def trx_age_decrypt(data: dict, identity: x25519.Identity):
    if isinstance(data, str):
        rlt = {"content": data}
        content = data
    if isinstance(data, dict):
        rlt = data.copy()
        content = data.get("content")
    if not content:
        raise ValueError("invalid content")
    recipients = data.get("recipients", [])
    if recipients and age_pvtkey_to_pubkey(identity) not in recipients:
        return data

    decrypted = age_decrypt(identity, base64.b64decode(content))
    rlt["content"] = json.loads(decrypted.decode())
    return rlt


def data_encrypt(age_pubkeys: list, data: dict):
    """把 dict 形式的 data 用一组 age 公钥加密"""
    databytes = json.dumps(data).encode()
    encrypted = age_encrypt(age_pubkeys, databytes)
    encrypted_str = base64.b64encode(encrypted).decode()
    return encrypted_str


def data_decrypt(age_pvtkey, encrypted_str: str):
    """把一组 age 公钥加密过的数据，用其中之一公钥对应的私钥解密"""
    decrypted = age_decrypt(age_pvtkey, base64.b64decode(encrypted_str))
    data = json.loads(decrypted.decode())
    return data
