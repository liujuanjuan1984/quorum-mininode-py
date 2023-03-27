import logging
import os

from pyrage import decrypt, encrypt, passphrase, x25519

logger = logging.getLogger(__name__)


def age_encrypt(recipients: list, data: bytes) -> bytes:
    """recipients list of x25519.Recipient"""
    if not data:
        assert "invalid data"
    if not recipients:
        assert "invalid recipients"

    _recipients = []
    for item in recipients:
        if isinstance(item, str):
            _recipients.append(x25519.Recipient.from_str(item))
        else:
            _recipients.append(item)

    return encrypt(data, _recipients)


def age_decrypt(recipient: x25519.Recipient, data: bytes):
    if isinstance(recipient, str):
        recipient = x25519.Recipient.from_str(recipient)
    return decrypt(data, [recipient])


def age_pubkey_from_str(pubkey: str) -> x25519.Recipient:
    return x25519.Recipient.from_str(pubkey)


def age_privkey_from_str(key: str) -> x25519.Identity:
    identity = x25519.Identity.from_str(key)
    return identity


def age_privkey_from_file(path: str, password: str) -> x25519.Identity:
    if not os.path.exists(path):
        raise ValueError(f"can not find file path: {path}")

    with open(path, "rb") as fp:
        decrypted = passphrase.decrypt(fp.read(), password)
        return age_privkey_from_str(str(decrypted))
