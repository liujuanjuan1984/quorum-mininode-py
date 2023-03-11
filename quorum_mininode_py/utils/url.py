import base64
import json
import logging
import uuid
from typing import Dict, Optional
from urllib import parse

logger = logging.getLogger(__name__)


def join_url(
    base: Optional[str] = None,
    endpoint: Optional[str] = None,
    is_quote: bool = False,
    **query_params,
) -> str:
    """pack base and endpoint to url"""
    # url = parse.urljoin(base, endpoint) if base else endpoint
    url = ""
    if base:
        url = base
    if endpoint:
        url += endpoint

    if query_params:
        for key, value in query_params.items():
            if isinstance(value, bool):
                query_params[key] = json.dumps(value)
        query_ = parse.urlencode(query_params)
        if is_quote:
            query_ = parse.quote(query_, safe="?&/")
        return "?".join([url, query_])
    return url


def _decode_b64_urlsafe(b64str: str) -> bytes:
    # 对 base64 字符串检查长度，并补位，转换为字节
    num = (4 - len(b64str) % 4) % 4
    b64byte = b64str.encode() + b"=" * num
    b64byte = base64.urlsafe_b64decode(b64byte)
    return b64byte


def _decode_uuid(b64str: str) -> str:
    b64byte = _decode_b64_urlsafe(b64str)
    b64uuid = uuid.UUID(bytes=b64byte)
    return str(b64uuid)


def _decode_timestamp(b64str: str) -> int:
    b64byte = _decode_b64_urlsafe(b64str)
    bigint = int.from_bytes(b64byte, "big")
    return bigint


def _decode_cipher_key(b64str: str):
    b64byte = _decode_b64_urlsafe(b64str)
    return b64byte.hex()


def _decode_pubkey(b64str: str) -> str:
    b64byte = _decode_b64_urlsafe(b64str)
    pubkey = base64.standard_b64encode(b64byte).decode()
    return pubkey


def parse_chain_url(url: str):
    u = urlparse(url)
    baseurl = f"{u.scheme}://{u.hostname}:{u.port}"
    query = parse_qs(u.query)
    jwt = _get_value_from_query(query, "jwt")
    return ChainURL(baseurl=baseurl, jwt=jwt)


def decode_seed_url(seedurl: str) -> Dict:
    """
    seedurl (str):
    the seed url of rum group which shared by rum fullnode,
    with host:post?jwt=xxx to connect
    """

    if not isinstance(seedurl, str):
        raise TypeError("seedurl must be string type.")

    if not seedurl.startswith("rum://seed?"):
        raise ValueError(
            "invalid seedurl, must start with rum://seed?, shared by rum fullnode."
        )

    # 由于 Python 的实现中，每个 key 的 value 都是 列表，所以做了下述处理
    # TODO: 如果 u 参数的值有多个，该方法需升级
    query_dict = {}
    _q = parse.urlparse(seedurl).query
    for key, value in parse.parse_qs(_q).items():
        if len(value) == 1:
            query_dict[key] = value[0]
        else:
            raise ValueError(f"key:{key}, value:{value}, is not 1:1, please check.")

    encryption_type = "public" if query_dict.get("e") == "0" else "private"

    """ 
    chain_urls = []
    urls = list(set(query_dict.get("u").split("|")))
    for url in urls:
        item = parse_chain_url(url)
        chain_urls.append(item)
    """

    info = {
        "group_id": _decode_uuid(query_dict.get("g")),
        "group_name": query_dict.get("a"),
        "app_key": query_dict.get("y"),
        "owner": _decode_pubkey(query_dict.get("k")),
        "chiperkey": _decode_cipher_key(query_dict.get("c")),
        "encryption_type": encryption_type,
        "url": query_dict.get("u"),
        "timestamp": _decode_timestamp(query_dict.get("t")),
        # "chain_urls": chain_urls,
    }
    try:
        info["genesis_block_id"] = _decode_uuid(query_dict.get("b"))
    except Exception as err:
        logger.info(err)
    return info
