from quorum_mininode_py import MiniNode

seed = "rum://seed?v=1&e=0&n=0&c=KNda...jL61aXaZyE"
pvtkey = "0x16c1c86...d337"
bot = MiniNode(seed, pvtkey)

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
