import logging
from urllib import parse

from quorum_mininode_py import utils
from quorum_mininode_py._requests import HttpRequest
from quorum_mininode_py.api import LightNodeAPI
from quorum_mininode_py.crypto import account as Account

logger = logging.getLogger(__name__)


from dataclasses import dataclass


@dataclass
class RumGroup:
    group_id: str = None
    aes_key: str = None
    encryption_type: str = None
    chainapi = None
    jwt = None

    def __init__(self, seedurl):

        info = utils.decode_seed_url(seedurl)
        url = parse.urlparse(info["url"])
        if not info["url"]:
            raise ValueError("Invalid seedurl.")
        jwt = parse.parse_qs(url.query)
        if jwt:
            jwt = jwt["jwt"][0]
        else:
            jwt = None
        self.group_id = info["group_id"]
        self.aes_key = bytes.fromhex(info["chiperkey"])
        self.encryption_type = info["encryption_type"]
        self.chainapi = f"{url.scheme}://{url.netloc}/api/v1"
        self.jwt = jwt


@dataclass
class RumAccount:
    pvtkey: str = None
    pubkey: str = None
    address: str = None
    age_pvtkey: str = None
    age_pubkey: str = None

    def __init__(self, pvtkey: str = None, age_pvtkey: str = None):
        self.pvtkey = pvtkey or Account.create_private_key()
        self.pubkey = Account.private_key_to_pubkey(self.pvtkey)
        self.address = Account.public_key_to_address(self.pubkey)

        if not age_pvtkey:
            self.age_pvtkey, self.age_pubkey = Account.create_age_keypair()
        else:
            self.age_pvtkey = age_pvtkey
            self.age_pubkey = Account.age_pvtkey_to_pubkey(age_pvtkey)


class MiniNode:
    """python for quorum lightnode, without datastore, one MiniNode client for one group"""

    def __init__(self, seedurl: str, pvtkey=None, age_pvtkey=None):
        self.account = RumAccount(pvtkey, age_pvtkey)
        self.group = RumGroup(seedurl)
        self.http = HttpRequest(api_base=self.group.chainapi, jwt_token=self.group.jwt)
        self.api = LightNodeAPI(self.http, self.group, self.account)
