import logging
from dataclasses import dataclass

from quorum_mininode_py.api import LightNodeAPI
from quorum_mininode_py.client._http import HttpRequest
from quorum_mininode_py.crypto import account as eth_acc
from quorum_mininode_py.crypto import age as age_acc
from quorum_mininode_py.utils.url import decode_seed_url

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
        try:
            info = decode_seed_url(seed_url)
        except KeyError as err:
            raise ValueError(f"invalid seed_url: {err}") from err
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

    def __init__(self, pvtkey: str = None, age_pvtkey: str = None):
        self.pvtkey = pvtkey or eth_acc.create_pvtkey()
        self.pubkey = eth_acc.pvtkey_to_pubkey(self.pvtkey)
        self.address = eth_acc.pubkey_to_address(self.pubkey)

        if age_pvtkey:
            self.age_pvtkey = age_pvtkey
            self.age_pubkey = age_acc.age_pvtkey_to_pubkey(age_pvtkey)
        else:
            self.age_pvtkey, self.age_pubkey = age_acc.create_age_keypair()


class MiniNode:
    """python for quorum lightnode, without datastore, one MiniNode client for one group"""

    def __init__(self, seed_url: str, pvtkey=None, age_pvtkey=None):
        self.group = RumGroup(seed_url)
        self.http = HttpRequest(chain_urls=self.group.chain_urls or [])
        self.account = RumAccount(pvtkey, age_pvtkey)
        self.api = LightNodeAPI(self)

    def change_account(self, pvtkey, age_pvtkey=None):
        age_pvtkey = age_pvtkey or self.account.age_pvtkey
        if pvtkey != self.account.pvtkey or age_pvtkey != self.account.age_pvtkey:
            self.account = RumAccount(pvtkey, age_pvtkey)
            self.api = LightNodeAPI(self)
