import base64
import hashlib
import json
import logging
import time
import uuid
from typing import Any, Dict, Union

import eth_keys
from google.protobuf.json_format import MessageToDict

from quorum_mininode_py.crypto.account import pvtkey_to_pubkey
from quorum_mininode_py.crypto.aes import aes_decrypt, aes_encrypt
from quorum_mininode_py.proto import pbQuorum

logger = logging.getLogger(__name__)

# pylint: disable=no-member


def trx_encrypt(
    group_id: str,
    aes_key: bytes,
    data: Dict[str, Any] = None,
    private_key: bytes = None,
    trx_id: str = None,
) -> Dict[str, str]:
    """trx encrypt"""
    # pylint: disable=too-many-locals
    data = json.dumps(data).encode()
    encrypted = aes_encrypt(aes_key, data)

    trx = {
        "TrxId": trx_id or str(uuid.uuid4()),
        "GroupId": group_id,
        "Data": encrypted,
        "TimeStamp": int(time.time() * 1e9),
        "Version": "2.0.0",
        "SenderPubkey": pvtkey_to_pubkey(private_key),
    }

    trx_without_sign_pb = pbQuorum.Trx(**trx)  # pylint: disable=no-member
    trx_without_sign_pb_bytes = trx_without_sign_pb.SerializeToString()
    trx_hash = hashlib.sha256(trx_without_sign_pb_bytes).digest()
    account = eth_keys.keys.PrivateKey(private_key)
    trx["SenderSign"] = account.sign_msg_hash(trx_hash).to_bytes()

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


def trx_decrypt(aes_key: Union[bytes, None], encrypted_trx: dict):
    if "trx" in encrypted_trx:
        encrypted_trx = encrypted_trx["trx"]
    data = encrypted_trx.get("Data")
    if data is None:
        raise ValueError("Data is None")
    trx_enc_bytes = base64.b64decode(data)
    trx_bytes = aes_decrypt(aes_key, trx_enc_bytes)
    trx = {**encrypted_trx, "Data": json.loads(trx_bytes)}
    return trx


def get_announce_param(
    age_pubkey: str,
    private_key: bytes,
    group_id: str,
    action: str,
    _type: str,
    memo: Union[str, None] = None,
) -> Dict[str, Dict[str, Any]]:

    item = pbQuorum.AnnounceItem()
    item.GroupId = group_id
    if _type == "user":
        item.Type = pbQuorum.AS_USER
    elif _type == "producer":
        item.Type = pbQuorum.AS_PRODUCER
    else:
        raise ValueError("unsupport type")

    if action == "add":
        item.Action = pbQuorum.ADD
    elif action == "remove":
        item.Action = pbQuorum.REMOVE
    else:
        raise ValueError("unsupport action")

    item.SignPubkey = pvtkey_to_pubkey(private_key)
    if item.Type == pbQuorum.AS_USER:
        item.EncryptPubkey = age_pubkey

    item.OwnerPubkey = ""
    item.OwnerSignature = ""
    item.Result = pbQuorum.ANNOUNCED

    data = (
        item.GroupId
        + item.SignPubkey
        + item.EncryptPubkey
        + pbQuorum.AnnounceType.Name(item.Type)
    ).encode()
    _hash = hashlib.sha256(data).digest()
    signature = eth_keys.keys.PrivateKey(private_key).sign_msg_hash(_hash).to_bytes()

    item.AnnouncerSignature = signature.hex()
    item.TimeStamp = int(time.time() * 1e9)
    item.Memo = memo or "lightnode announce"

    payload = {
        "data": MessageToDict(item),
    }
    return payload
