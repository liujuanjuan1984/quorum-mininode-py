# QuoRum LightNode Python SDK

Python SDK for Quorum LightNode, Without local storage.

Another better choice is [quorum-lightnode-py](https://github.com/zhangwm404/quorum-lightnode-py), with local storage.

More about QuoRum:

- https://rumsystem.net/
- https://github.com/rumsystem/quorum

### Install

```sh
pip install quorum_mininode_py
```

### Usage

```python3
from quorum_mininode_py import MiniNode

seed_url = 'rum://seed?v=1&e=0&n=0&c=apzmbMVtMy6J0sQKwhF...2MwHjpA2E'
pvtkey = "0xd4e9ddc19ec5b...d8c"

bot = MiniNode(seed_url,pvtkey)

# post content to rum group chain
data = {
    "type": "Create",
    "object": {
        "type": "Note",
        "content": "Hello world! Hello quorum!",
        "id": "a1d92233-3801-4295-a3cd-0e594385acc6",
    },
}

resp = bot.api.post_content(data)
print(resp)

# like a post
data = {
    "type": "Like",
    "object": {"type": "Note", "id": "a1d92233-3801-4295-a3cd-0e594385acc6"},
}

resp = bot.api.post_content(data)
print(resp)

# get content from rum group chain
trxs = bot.api.get_content(num=2, reverse=True)
print(trxs)


```

### Source

- quorum fullnode sdk for python: https://github.com/liujuanjuan1984/quorum-fullnode-py 
- quorum mininode sdk for python: https://github.com/liujuanjuan1984/quorum-mininode-py 
- quorum lightnode sdk for python: https://github.com/zhangwm404/quorum-lightnode-py 
- quorum data module for python: https://github.com/liujuanjuan1984/quorum-data-py

- quorum fullnode sdk for nodejs: https://github.com/okdaodine/rum-fullnode-sdk 
- quorum lightnode sdk for nodejs: https://github.com/okdaodine/rum-sdk-nodejs

- and more.. https://github.com/okdaodine/awesome-quorum

### License

This work is released under the `GPL3.0` license. A copy of the license is provided in the [LICENSE](https://github.com/liujuanjuan1984/quorum_mininode_py/blob/master/LICENSE) file.