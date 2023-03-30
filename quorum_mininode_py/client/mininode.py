import logging
from dataclasses import dataclass

import requests

from quorum_mininode_py import utils
from quorum_mininode_py.api import LightNodeAPI
from quorum_mininode_py.client._http import HttpRequest
from quorum_mininode_py.crypto import account as Account

logger = logging.getLogger(__name__)


@dataclass
class RumGroup:
    seed: dict = None
    seed_url: str = None
    group_id: str = None
    aes_key: str = None
    encryption_type: str = None
    chain_urls: list = None

    def __init__(self, seed_url: str):
        info = utils.decode_seed_url(seed_url)
        seed = info["seed"]
        self.seed = seed
        self.seed_url = seed_url
        self.group_id = seed["group_id"]
        self.aes_key = bytes.fromhex(seed["cipher_key"])
        self.encryption_type = seed["encryption_type"]
        self.chain_urls = info["chain_urls"]


@dataclass
class RumAccount:
    pvtkey: str = None
    pubkey: str = None
    address: str = None
    age_pvtkey: str = None
    age_pubkey: str = None

    def __init__(
        self, pvtkey: str = None, age_pvtkey: str = None, encryption_type: str = None
    ):
        self.pvtkey = pvtkey or Account.create_private_key()
        self.pubkey = Account.private_key_to_pubkey(self.pvtkey)
        self.address = Account.public_key_to_address(self.pubkey)

        if age_pvtkey:
            self.age_pvtkey = age_pvtkey
            self.age_pubkey = Account.age_pvtkey_to_pubkey(age_pvtkey)
        elif (encryption_type or "").upper() == "PRIVATE":
            self.age_pvtkey, self.age_pubkey = Account.create_age_keypair()
        else:
            self.age_pvtkey = None
            self.age_pubkey = None


class MiniNode:
    """python for quorum lightnode, without datastore, one MiniNode client for one group"""

    def __init__(self, seed_url: str, pvtkey=None, age_pvtkey=None):
        self.group = RumGroup(seed_url)
        self.account = RumAccount(pvtkey, age_pvtkey, self.group.encryption_type)

        chain_url = self.get_best_http(self.group.chain_urls)
        http = HttpRequest(chain_url["baseurl"] + "/api/v1", chain_url["jwt"])
        self.api = LightNodeAPI(http, self.group, self.account)

    def get_best_http(self, chain_urls):
        headers = {"Content-Type": "application/json"}
        best = None
        for chain_url in chain_urls:
            jwt = chain_url["jwt"]
            headers.update({"Authorization": f"Bearer {jwt}"})
            url = chain_url["baseurl"] + f"/api/v1/node/{self.group.group_id}/info"
            try:
                response = requests.get(url, headers=headers, timeout=5)
                if response.status_code == 200:
                    best = chain_url
                    break
            except Exception as e:
                logger.warning("get_best_http error: %s", e)
        return best
