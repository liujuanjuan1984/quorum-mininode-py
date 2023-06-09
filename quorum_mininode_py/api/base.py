import json
import logging
from urllib.parse import urlencode

logger = logging.getLogger(__name__)


class BaseAPI:
    """BaseAPI"""

    def __init__(self, client):
        self._http = client.http
        self.group_id = client.group.group_id
        self._group = client.group
        self._account = client.account

    def _get(self, endpoint: str, payload: dict = None):
        """api _get"""
        return self._http.get(endpoint, payload)

    def _post(self, endpoint: str, payload: dict = None):
        """api _post"""
        return self._http.post(endpoint, payload)

    def _get_trx(self, trx_id: str):
        return self._get(f"/api/v1/trx/{self.group_id}/{trx_id}")

    def _get_content(self, payload: dict):
        for k, v in payload.items():
            if isinstance(v, bool):
                payload[k] = json.dumps(v)
        query_string = urlencode(payload, doseq=True)
        return self._get(f"/api/v1/node/{self.group_id}/groupctn?{query_string}")

    def _post_content(self, payload: dict):
        return self._post(f"/api/v1/node/{self.group_id}/trx", payload)

    def _get_group(self):
        return self._get(f"/api/v1/node/{self.group_id}/info")

    def _get_encryptpubkeys(self):
        return self._get(f"/api/v1/node/{self.group_id}/encryptpubkeys")

    def _get_auth_type(self, trx_type: str):
        return self._get(f"/api/v1/node/{self.group_id}/auth/by/{trx_type}")

    def _get_alwlist(self):
        return self._get(f"/api/v1/node/{self.group_id}/auth/alwlist")

    def _get_denylist(self):
        return self._get(f"/api/v1/node/{self.group_id}/auth/denylist")

    def _get_appconfig_keylist(self):
        return self._get(f"/api/v1/node/{self.group_id}/appconfig/keylist")

    def _get_appconfig_key(self, key: str):
        return self._get(f"/api/v1/node/{self.group_id}/appconfig/by/{key}")

    def _get_producers(self):
        return self._get(f"/api/v1/node/{self.group_id}/producers")

    def _get_announced_producer(self):
        return self._get(f"/api/v1/node/{self.group_id}/announced/producer")

    def _get_announced_user(self):
        return self._get(f"/api/v1/node/{self.group_id}/announced/user")

    def _post_announce(self, payload: dict):
        return self._post(f"/api/v1/node/{self.group_id}/announce", payload)

    def _get_encrypt_pubkeys(self):
        """get the age pubkeys of private group"""
        return self._get(f"/api/v1/node/getencryptpubkeys/{self.group_id}")
