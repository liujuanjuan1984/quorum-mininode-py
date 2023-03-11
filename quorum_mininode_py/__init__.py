import logging

from quorum_mininode_py.client import MiniNode

__version__ = "1.0.0"
__author__ = "liujuanjuan1984"

# Set default logging handler to avoid "No handler found" warnings.
logging.getLogger(__name__).addHandler(logging.NullHandler())
