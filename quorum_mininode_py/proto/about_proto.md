
quorum.proto are merged from the .proto files from url:  https://github.com/rumsystem/quorum/blob/main/pkg/pb/chain.proto


```bash
cd quorum_mininode_py\proto
protoc  --python_out=. ./quorum.proto
```