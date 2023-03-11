import base64
import json
import logging
import time
from typing import Union

from quorum_mininode_py.api.base import BaseAPI
from quorum_mininode_py.crypto.account import check_private_key
from quorum_mininode_py.crypto.trx import aes_encrypt, trx_decrypt, trx_encrypt

logger = logging.getLogger(__name__)


class LightNodeAPI(BaseAPI):
    """the light node api for quorum"""

    def post_content(
        self,
        data: dict,
        timestamp: Union[str, int, float, None] = None,
    ):
        """
        data:dict
        timestamp:2022-10-05 12:34
        """
        if timestamp and isinstance(timestamp, str):
            timestamp = timestamp.replace("/", "-")[:16]
            timestamp = time.mktime(time.strptime(timestamp, "%Y-%m-%d %H:%M"))
        # 检查 group 的类型

        if self._group.encryption_type == "public":
            age_pubkey = None
        else:
            age_pubkey = self._account.age_pubkey
        trx = trx_encrypt(
            self.group_id,
            self._group.aes_key,
            data,
            timestamp,
            check_private_key(self._account.pvtkey),
            age_pubkey,
        )
        return super()._post_content(trx)

    def get_trx(self, trx_id: str):
        """get encrpyted trx"""
        return super()._get_trx(trx_id)

    def trx(self, trx_id: str):
        """get decrypted trx"""
        if self._group.encryption_type == "public":
            age_priv_key = None
        else:
            age_priv_key = self._account.age_privkey

        trx = trx_decrypt(self._group.aes_key, age_priv_key, self.get_trx(trx_id))
        return trx

    def get_content(
        self,
        start_trx: str = None,
        num: int = 20,
        reverse: bool = False,
        include_start_trx: bool = False,
        senders: list = None,
    ):
        """get content"""
        # TODO:如果把 senders 传入 quorum，会导致拿不到数据，或数据容易中断，所以实现时拿了全部数据，再筛选senders

        params = {
            "group_id": self.group_id,
            "reverse": "true" if reverse is True else "false",
            "num": num,
            "include_start_trx": "true" if include_start_trx is True else "false",
            "senders": [],
        }
        if start_trx:
            params["start_trx"] = start_trx
        get_group_ctn_item = {
            "Req": params,
        }

        get_group_ctn_item_str = json.dumps(get_group_ctn_item)
        encrypted = aes_encrypt(self._group.aes_key, get_group_ctn_item_str.encode())
        send_param = {
            "Req": base64.b64encode(encrypted).decode(),
        }

        encypted_trxs = super()._get_content(send_param)
        # chooce trxs:
        if self._group.encryption_type == "public":
            age_priv_key = None
        else:
            age_priv_key = self._account.age_privkey

        try:
            trxs = [
                trx_decrypt(self._group.aes_key, age_priv_key, i) for i in encypted_trxs
            ]
            if senders:
                trxs = [i for i in trxs if i["Publisher"] in senders]
        except Exception as err:
            logger.warning("get_content error: %s", err)
            trxs = encypted_trxs
        return trxs

    def get_group_info(self):
        """get group info"""
        obj = {"GroupId": self.group_id}
        return super()._get_chaindata(obj, "group_info")

    def get_auth_type(self, trx_type: str):
        """get auth type of trx_type"""
        obj = {"GroupId": self.group_id, "TrxType": trx_type}
        return super()._get_chaindata(obj, "auth_type")

    def get_auth_allowlist(self):
        """get allowlist"""
        obj = {"GroupId": self.group_id}
        return super()._get_chaindata(obj, "auth_allowlist")

    def get_auth_denylist(self):
        """get denylist"""
        obj = {"GroupId": self.group_id}
        return super()._get_chaindata(obj, "auth_denylist")

    def get_appconfig_keylist(self):
        """get appconfig keylist"""
        obj = {"GroupId": self.group_id}
        return super()._get_chaindata(obj, "appconfig_listlist")

    def get_appconfig_key(self, key: str):
        """get appconfig key value by keyname"""
        obj = {"GroupId": self.group_id, "Key": key}
        return super()._get_chaindata(obj, "appconfig_item_bykey")

    def get_group_producer(self):
        """get group producers"""
        obj = {"GroupId": self.group_id}
        return super()._get_chaindata(obj, "group_producer")

    def get_announced_producer(self):
        """get announced producer"""
        obj = {"GroupId": self.group_id}
        return super()._get_chaindata(obj, "announced_producer")

    def get_announced_user(self, pubkey: str):
        """get announced user info by pubkey"""
        obj = {"GroupId": self.group_id, "SignPubkey": pubkey}
        return super()._get_chaindata(obj, "announced_user")
