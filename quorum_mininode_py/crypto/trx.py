import base64
import hashlib
import json
import logging
import time
import uuid
from typing import Any, Dict, Union

import eth_keys
from pyrage import x25519

from quorum_mininode_py.crypto.aes import aes_decrypt, aes_encrypt
from quorum_mininode_py.crypto.age import age_decrypt, age_encrypt
from quorum_mininode_py.proto import pbQuorum

logger = logging.getLogger(__name__)


def age_privkey_from_str(key: str) -> x25519.Identity:
    identity = x25519.Identity.from_str(key)
    return identity


def pack_obj(obj: Dict[str, str], aes_key) -> str:
    """pack obj with group cipher_key and return a string"""
    obj_bytes = json.dumps(obj).encode()
    obj_encrypted = aes_encrypt(aes_key, obj_bytes)
    req = base64.b64encode(obj_encrypted).decode()
    return req


def trx_encrypt(
    group_id: str,
    aes_key: bytes,
    data: Dict[str, Any] = None,
    private_key: bytes = None,
    age_pubkey=None,
    trx_id=None,
) -> Dict[str, str]:
    """trx encrypt"""
    # pylint: disable=too-many-locals

    data = json.dumps(data).encode()
    encrypted = None
    if not age_pubkey:
        encrypted = aes_encrypt(aes_key, data)
    else:
        encrypted = age_encrypt(age_pubkey, data)

    account = eth_keys.keys.PrivateKey(private_key)
    sender_pubkey = base64.urlsafe_b64encode(
        account.public_key.to_compressed_bytes()
    ).decode()

    trx = {
        "TrxId": trx_id or str(uuid.uuid4()),
        "GroupId": group_id,
        "Data": encrypted,
        "TimeStamp": int(time.time() * 1e9),
        "Version": "2.0.0",
        "SenderPubkey": sender_pubkey,
    }

    trx_without_sign_pb = pbQuorum.Trx(**trx)  # pylint: disable=no-member
    trx_without_sign_pb_bytes = trx_without_sign_pb.SerializeToString()
    trx_hash = hashlib.sha256(trx_without_sign_pb_bytes).digest()
    signature = account.sign_msg_hash(trx_hash).to_bytes()
    trx["SenderSign"] = signature

    for k, v in trx.items():
        if isinstance(v, bytes):
            trx[k] = base64.b64encode(v).decode()

    trx = {
        "trx_id": trx["TrxId"],
        "data": trx["Data"],
        "timestamp": str(trx["TimeStamp"]),
        "version": trx["Version"],
        "sender_pubkey": trx["SenderPubkey"],
        "sender_sign": trx["SenderSign"],
    }
    return trx


def _check_data(data):
    trx_data = b""
    if isinstance(data, str):
        trx_data = data.encode()
    elif isinstance(data, bytes):
        trx_data = data
    return trx_data


def decode_public_trx_data(aes_key: bytes, data: str):
    trx_data = _check_data(data)
    trx_enc_bytes = base64.b64decode(trx_data)
    trx_bytes = aes_decrypt(aes_key, trx_enc_bytes)
    return trx_bytes


def decode_private_trx_data(age_key: str, data: str):
    trx_data = _check_data(data)
    trx_enc_bytes = base64.b64decode(trx_data)
    age_key = age_privkey_from_str(age_key)
    trx_bytes = age_decrypt(age_key, trx_enc_bytes)
    return trx_bytes


def trx_decrypt(
    aes_key: Union[bytes, None], age_priv_key: Union[str, None], encrypted_trx: dict
):

    data = encrypted_trx.get("Data")
    if data is None:
        raise ValueError("Data is None")
    trx_enc_bytes = base64.b64decode(data)
    trx_bytes = None
    if aes_key:
        trx_bytes = aes_decrypt(aes_key, trx_enc_bytes)
    elif age_priv_key:
        age_key = age_privkey_from_str(age_priv_key)
        trx_bytes = age_decrypt(age_key, trx_enc_bytes)
    else:
        raise ValueError("aes_key and age_key both empty")

    return {**encrypted_trx, "Data": json.loads(trx_bytes)}


def get_sender_pubkey(private_key: bytes) -> str:
    pk = eth_keys.keys.PrivateKey(private_key)
    return base64.urlsafe_b64encode(pk.public_key.to_compressed_bytes()).decode()
