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

from quorum_data_py import FeedData as feed
from quorum_mininode_py import MiniNode

seed_url = 'rum://seed?v=1&e=0&n=0&c=apzmbMVtMy6J0sQKwhF...2MwHjpA2E'
pvtkey = "0xd4e9ddc19ec5b...d8c"
agepvtkey = 'AGE-SECRET-KEY-15RSH3AXCVY...NSLWJZAP'

bot = MiniNode(seed_url,pvtkey,agepvtkey)

# post content to rum group chain
data = feed.new_post(content="hello world!")
resp = bot.api.post_content(data)

# get content from rum group chain
trxs = bot.api.get_content(num=3, reverse=True)

```

### Source

- quorum fullnode sdk for python: https://github.com/liujuanjuan1984/quorum-fullnode-py 
- quorum lightnode sdk for python: https://github.com/zhangwm404/quorum-lightnode-py 
- quorum data module for python: https://github.com/liujuanjuan1984/quorum-data-py

- quorum fullnode sdk for nodejs: https://github.com/okdaodine/rum-fullnode-sdk 
- quorum lightnode sdk for nodejs: https://github.com/okdaodine/rum-sdk-nodejs

- and more.. https://github.com/okdaodine/awesome-quorum

### License

This work is released under the `GPL3.0` license. A copy of the license is provided in the [LICENSE](https://github.com/liujuanjuan1984/quorum_mininode_py/blob/master/LICENSE) file.