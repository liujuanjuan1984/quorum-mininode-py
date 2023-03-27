import logging

from quorum_mininode_py.client._http import HttpRequest
from quorum_mininode_py.crypto import trx as crypto

logger = logging.getLogger(__name__)


class BaseAPI:
    """BaseAPI"""

    def __init__(self, http: HttpRequest, group, account):
        self._http = http
        self.group_id = group.group_id
        self._group = group
        self._account = account

    def _get(self, endpoint: str, payload: dict = None):
        """api _get"""
        return self._http.get(endpoint, payload)

    def _post(self, endpoint: str, payload: dict = None):
        """api _post"""
        return self._http.post(endpoint, payload)

    def _get_trx(self, trx_id: str):
        return self._get(f"/trx/{self.group_id}/{trx_id}")

    def _get_content(self, payload: dict):
        return self._post(f"/node/groupctn/{self.group_id}", payload)

    def _post_content(self, payload: dict):
        return self._post(f"/node/trx/{self.group_id}", payload)

    def _get_chaindata(self, obj: dict, req_type: str):
        """base api of get chaindata"""
        payload = {
            "Req": crypto.pack_obj(obj, self._group.aes_key),
            "ReqType": req_type,
        }
        return self._post(f"/node/getchaindata/{self.group_id}", payload)
