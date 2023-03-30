import base64
import hashlib
import uuid
from urllib.parse import parse_qs, unquote, urlencode, urlparse

from google.protobuf import json_format

from quorum_mininode_py.proto import pbQuorum


def urlsafe_b64decode(b64str: str) -> bytes:
    num = (4 - len(b64str) % 4) % 4
    b64byte = b64str.encode() + b"=" * num
    b64byte = base64.urlsafe_b64decode(b64byte)
    return b64byte


def _get_value_from_query(query: dict, key: str) -> str:
    val = query.get(key)
    if not val:
        raise KeyError(f"can not find key: {key} or value is empty")
    if not isinstance(val, list):
        raise ValueError("value is not a list")
    return val[0]


def extract_uuid_from_query(query: dict, key: str) -> str:
    val = _get_value_from_query(query, key)
    b = urlsafe_b64decode(val)
    return str(uuid.UUID(bytes=b))


def extra_timestamp_from_query(query: dict, key: str) -> int:
    val = _get_value_from_query(query, key)
    t = urlsafe_b64decode(val)
    timestamp = int.from_bytes(t, byteorder="big")
    return timestamp


def hash_block(block: pbQuorum.Block) -> bytes:  # pylint: disable=no-member
    new_block = pbQuorum.Block()  # pylint: disable=no-member
    new_block.CopyFrom(block)
    new_block.BlockHash = b""
    new_block.ProducerSign = b""
    new_block_bytes = new_block.SerializeToString()
    return hashlib.sha256(new_block_bytes).digest()


def parse_chain_url(url: str):
    u = urlparse(url)
    baseurl = f"{u.scheme}://{u.hostname}:{u.port}"
    query = parse_qs(u.query)
    jwt = _get_value_from_query(query, "jwt")
    return dict(baseurl=baseurl, jwt=jwt)


def decode_seed_url(seed_url: str):
    """
    seed_url (str):
    the seed url of rum group which shared by rum fullnode,
    with host:post?jwt=xxx to connect
    """

    if not isinstance(seed_url, str):
        raise TypeError("seed_url must be string type.")

    if not seed_url.startswith("rum://seed?v=1"):
        raise ValueError("seed_url must start with rum://seed?")

    parsed = urlparse(seed_url)
    query = parse_qs(parsed.query)

    group_id = extract_uuid_from_query(query, "g")
    genesis_block = pbQuorum.Block(  # pylint: disable=no-member
        Epoch=0,
        GroupId=group_id,
        PrevHash=None,
        Trxs=None,
    )
    genesis_block.BlockHash = hash_block(genesis_block)
    genesis_block.ProducerPubkey = _get_value_from_query(query, "k")
    genesis_block.TimeStamp = extra_timestamp_from_query(query, "t")
    genesis_block.BlockHash = hash_block(genesis_block)
    genesis_block.ProducerSign = urlsafe_b64decode(_get_value_from_query(query, "s"))

    consensus_type = "pos" if _get_value_from_query(query, "n") == "1" else "poa"
    encryption_type = (
        "public" if _get_value_from_query(query, "e") == "0" else "private"
    )
    seed = dict(
        genesis_block=genesis_block,
        group_id=group_id,
        group_name=_get_value_from_query(query, "a"),
        consensus_type=consensus_type,
        encryption_type=encryption_type,
        cipher_key=urlsafe_b64decode(_get_value_from_query(query, "c")).hex(),
        owner_pubkey=genesis_block.ProducerPubkey,
        signature=genesis_block.ProducerSign.hex(),
        app_key=unquote(_get_value_from_query(query, "y")),
    )

    chain_urls = []
    urls = list(set(_get_value_from_query(query, "u").split("|")))
    for url in urls:
        item = parse_chain_url(url)
        chain_urls.append(item)

    seed["genesis_block"] = json_format.MessageToDict(seed["genesis_block"])

    # get clean seed_url without chain_url
    query["u"] = [""]
    new_query_str = urlencode(query, doseq=True)
    updated_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}?{new_query_str}"

    return dict(seed=seed, chain_urls=chain_urls, seed_url=updated_url)


def update_seed_url(seed_url: str, *chain_urls: list):
    """
    seed_url (str):
    the seed url of rum group which shared by rum fullnode,
    with host:post?jwt=xxx to connect
    chain_urls (list):
    the chain urls of rum group which shared by rum fullnode,
    with host:post?jwt=xxx to connect
    """
    decoded = decode_seed_url(seed_url)
    for chain_url in chain_urls:
        if chain_url not in decoded["chain_urls"]:
            decoded["chain_urls"].append(chain_url)

    chain_url_str = ""
    for url in decoded["chain_urls"]:
        chain_url_str += f"{url['baseurl']}?jwt={url['jwt']}|"
    if chain_url_str.endswith("|"):
        chain_url_str = chain_url_str[:-1]
    updated_url = decoded["seed_url"] + "&u=" + chain_url_str
    return updated_url
