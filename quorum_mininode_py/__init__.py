import logging

from quorum_mininode_py.client import MiniNode, RumAccount, RumGroup
from quorum_mininode_py.crypto.account import (
    age_pvtkey_to_pubkey,
    create_age_keypair,
    create_private_key,
    private_key_to_pubkey,
    public_key_to_address,
)
from quorum_mininode_py.utils import decode_seed_url, update_seed_url

__version__ = "1.2.1"
__author__ = "liujuanjuan1984, zhangwm404"

# Set default logging handler to avoid "No handler found" warnings.
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

logger.info("Version: %s", __version__)
