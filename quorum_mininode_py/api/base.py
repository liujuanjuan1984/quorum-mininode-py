import json
import logging
from urllib.parse import urlencode

from quorum_mininode_py.client._http import HttpRequest

logger = logging.getLogger(__name__)


class BaseAPI:
    """BaseAPI"""

    def __init__(self, client):
        self._client = client
        self._http = client.http
        self.group_id = client.group.group_id
        self._group = client.group
        self._account = client.account
        self._retry = 0

    def _get(self, endpoint: str, payload: dict = None):
        """api _get"""
        if self._retry >= 3:
            raise Exception("retry 3 times, check your network")
        try:
            resp = self._http.get(endpoint, payload)
        except Exception as err:
            logger.error("request failed: %s", err)
            chain_url = self._client.get_best_http(self._client.group.chain_urls)
            if chain_url is None:
                raise Exception("no available chain url") from err
            self._http = self._client.http = HttpRequest(
                chain_url["baseurl"] + "/api/v1", chain_url["jwt"]
            )
            self._retry += 1
            return self._get(endpoint, payload)
        self._retry = 0
        return resp

    def _post(self, endpoint: str, payload: dict = None):
        """api _post"""
        if self._retry >= 3:
            raise Exception("retry 3 times, check your network")
        try:
            resp = self._http.post(endpoint, payload)
        except Exception as err:
            logger.error("request failed: %s", err)
            chain_url = self._client.get_best_http(self._client.group.chain_urls)
            if chain_url is None:
                raise Exception("no available chain url") from err
            self._http = self._client.http = HttpRequest(
                chain_url["baseurl"] + "/api/v1", chain_url["jwt"]
            )
            self._retry += 1
            return self._post(endpoint, payload)
        self._retry = 0
        return resp

    def _get_trx(self, trx_id: str):
        return self._get(f"/trx/{self.group_id}/{trx_id}")

    def _get_content(self, payload: dict):
        for k, v in payload.items():
            if isinstance(v, bool):
                payload[k] = json.dumps(v)
        query_string = urlencode(payload, doseq=True)
        return self._get(f"/node/{self.group_id}/groupctn?{query_string}")

    def _post_content(self, payload: dict):
        return self._post(f"/node/{self.group_id}/trx", payload)

    def _get_group(self):
        return self._get(f"/node/{self.group_id}/info")

    def _get_encryptpubkeys(self):
        return self._get(f"/node/{self.group_id}/encryptpubkeys")

    def _get_auth_type(self, trx_type: str):
        return self._get(f"/node/{self.group_id}/auth/by/{trx_type}")

    def _get_alwlist(self):
        return self._get(f"/node/{self.group_id}/auth/alwlist")

    def _get_denylist(self):
        return self._get(f"/node/{self.group_id}/auth/denylist")

    def _get_appconfig_keylist(self):
        return self._get(f"/node/{self.group_id}/appconfig/keylist")

    def _get_appconfig_key(self, key: str):
        return self._get(f"/node/{self.group_id}/appconfig/by/{key}")

    def _get_producers(self):
        return self._get(f"/node/{self.group_id}/producers")

    def _get_announced_producer(self):
        return self._get(f"/node/{self.group_id}/announced/producer")

    def _get_announced_user(self):
        return self._get(f"/node/{self.group_id}/announced/user")

    def _post_announce(self, payload: dict):
        return self._post(f"/node/{self.group_id}/announce", payload)
