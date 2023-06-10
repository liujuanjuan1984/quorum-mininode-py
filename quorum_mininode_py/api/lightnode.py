import logging

from quorum_mininode_py.api.base import BaseAPI
from quorum_mininode_py.crypto.account import check_pvtkey
from quorum_mininode_py.crypto.trx import get_announce_param, trx_decrypt, trx_encrypt

logger = logging.getLogger(__name__)


class LightNodeAPI(BaseAPI):
    """the light node api for quorum"""

    def post_content(
        self,
        data: dict,
        trx_id: str = None,
    ):
        """post content to group"""
        trx = trx_encrypt(
            self.group_id,
            self._group.aes_key,
            data,
            check_pvtkey(self._account.pvtkey),
            trx_id,
        )
        return super()._post_content(trx)

    def get_trx(self, trx_id: str):
        """get encrpyted trx"""
        return super()._get_trx(trx_id)

    def trx(self, trx_id: str):
        """get decrypted trx"""
        return trx_decrypt(self._group.aes_key, self.get_trx(trx_id))

    def get_content(
        self,
        start_trx: str = None,
        num: int = 20,
        reverse: bool = False,
        include_start_trx: bool = False,
        senders: list = None,
    ):
        """get content"""
        params = {
            "reverse": reverse,
            "num": num,
        }
        if start_trx:
            params["start_trx"] = start_trx
            params["include_start_trx"] = include_start_trx
        if senders:
            params["senders"] = senders

        encypted_trxs = super()._get_content(params)
        trxs = []
        for trx in encypted_trxs:
            try:
                trx = trx_decrypt(self._group.aes_key, trx)
            except Exception as err:
                logger.error(err)
            trxs.append(trx)
        return trxs

    def get_group_info(self):
        """get group info"""
        return super()._get_group()

    def get_encryptpubkeys(self):
        """get encrypt pubkeys"""
        return super()._get_encryptpubkeys()

    def get_auth_type(self, trx_type: str):
        """get auth type of trx_type"""
        trx_type = trx_type.upper()
        if trx_type not in ["POST", "ANNOUNCE", "REQ_BLOCK"]:
            raise ValueError("trx_type must be one of [POST ANNOUNCE REQ_BLOCK]")
        return super()._get_auth_type(trx_type)

    def get_auth_allowlist(self):
        """get allowlist"""
        return super()._get_alwlist()

    def get_auth_denylist(self):
        """get denylist"""
        return super()._get_denylist()

    def get_appconfig_keylist(self):
        """get appconfig keylist"""
        return super()._get_appconfig_keylist()

    def get_appconfig_key(self, key: str):
        """get appconfig key value by keyname"""
        return super()._get_appconfig_key(key)

    def get_producers(self):
        """get group producers"""
        return super()._get_producers()

    def get_announced_producer(self):
        """get announced producer"""
        return super()._get_announced_producer()

    def get_announced_user(self):
        """get announced user"""
        return super()._get_announced_user()

    def announce(self, action: str, _type: str, memo: str = None):
        """post annonce to group
        action: str, one of [add, remove]
        _type: str, one of [user, producer]
        """
        # only announce self as user will be success
        payload = get_announce_param(
            self._account.age_pubkey,
            check_pvtkey(self._account.pvtkey),
            self.group_id,
            action,
            _type,
            memo or f"annonce as {_type}",
        )
        return super()._post_announce(payload)

    def announce_as_user(self):
        """announce as user"""
        return self.announce("add", "user")

    def announce_as_producer(self):
        """announce as producer"""
        # lightnote can not announce as producer, return http 400
        return self.announce("add", "producer")

    def get_encrypt_pubkeys(self):
        """get age pubkeys of private group"""
        return super()._get_encryptpubkeys().get("keys")
