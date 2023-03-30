# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: quorum.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0cquorum.proto\x12\tquorum.pb"=\n\x07Package\x12$\n\x04type\x18\x01 \x01(\x0e\x32\x16.quorum.pb.PackageType\x12\x0c\n\x04\x44\x61ta\x18\x02 \x01(\x0c"\x88\x02\n\x03Trx\x12\r\n\x05TrxId\x18\x01 \x01(\t\x12 \n\x04Type\x18\x02 \x01(\x0e\x32\x12.quorum.pb.TrxType\x12\x0f\n\x07GroupId\x18\x03 \x01(\t\x12\x0c\n\x04\x44\x61ta\x18\x04 \x01(\x0c\x12\x11\n\tTimeStamp\x18\x05 \x01(\x03\x12\x0f\n\x07Version\x18\x06 \x01(\t\x12\x0f\n\x07\x45xpired\x18\x07 \x01(\x03\x12\x13\n\x0bResendCount\x18\x08 \x01(\x03\x12\r\n\x05Nonce\x18\t \x01(\x03\x12\x14\n\x0cSenderPubkey\x18\n \x01(\t\x12\x12\n\nSenderSign\x18\x0b \x01(\x0c\x12.\n\x0bStorageType\x18\x0c \x01(\x0e\x32\x19.quorum.pb.TrxStroageType"\xca\x01\n\x05\x42lock\x12\x0f\n\x07GroupId\x18\x01 \x01(\t\x12\x0f\n\x07\x42lockId\x18\x02 \x01(\x04\x12\r\n\x05\x45poch\x18\x03 \x01(\x04\x12\x10\n\x08PrevHash\x18\x04 \x01(\x0c\x12\x16\n\x0eProducerPubkey\x18\x05 \x01(\t\x12\x1c\n\x04Trxs\x18\x06 \x03(\x0b\x32\x0e.quorum.pb.Trx\x12\x0c\n\x04Sudo\x18\x07 \x01(\x08\x12\x11\n\tTimeStamp\x18\x08 \x01(\x03\x12\x11\n\tBlockHash\x18\t \x01(\x0c\x12\x14\n\x0cProducerSign\x18\n \x01(\x0c"X\n\x08ReqBlock\x12\x0f\n\x07GroupId\x18\x01 \x01(\t\x12\x11\n\tFromBlock\x18\x02 \x01(\x04\x12\x15\n\rBlksRequested\x18\x03 \x01(\x05\x12\x11\n\tReqPubkey\x18\x04 \x01(\t"0\n\x0c\x42locksBundle\x12 \n\x06\x42locks\x18\x01 \x03(\x0b\x32\x10.quorum.pb.Block"\xe2\x01\n\x0cReqBlockResp\x12\x0f\n\x07GroupId\x18\x01 \x01(\t\x12\x17\n\x0fRequesterPubkey\x18\x02 \x01(\t\x12\x16\n\x0eProviderPubkey\x18\x03 \x01(\t\x12\'\n\x06Result\x18\x04 \x01(\x0e\x32\x17.quorum.pb.ReqBlkResult\x12\x11\n\tFromBlock\x18\x05 \x01(\x04\x12\x15\n\rBlksRequested\x18\x06 \x01(\x05\x12\x14\n\x0c\x42lksProvided\x18\x07 \x01(\x05\x12\'\n\x06\x42locks\x18\x08 \x01(\x0b\x32\x17.quorum.pb.BlocksBundle"S\n\x08PostItem\x12\r\n\x05TrxId\x18\x01 \x01(\t\x12\x14\n\x0cSenderPubkey\x18\x02 \x01(\t\x12\x0f\n\x07\x43ontent\x18\x03 \x01(\x0c\x12\x11\n\tTimeStamp\x18\x04 \x01(\x03"\xc9\x01\n\x0cProducerItem\x12\x0f\n\x07GroupId\x18\x01 \x01(\t\x12\x16\n\x0eProducerPubkey\x18\x02 \x01(\t\x12\x18\n\x10GroupOwnerPubkey\x18\x03 \x01(\t\x12\x16\n\x0eGroupOwnerSign\x18\x04 \x01(\t\x12%\n\x06\x41\x63tion\x18\x05 \x01(\x0e\x32\x15.quorum.pb.ActionType\x12\x16\n\x0eWithnessBlocks\x18\x06 \x01(\x03\x12\x11\n\tTimeStamp\x18\x07 \x01(\x03\x12\x0c\n\x04Memo\x18\x08 \x01(\t"C\n\x15\x42\x46TProducerBundleItem\x12*\n\tProducers\x18\x01 \x03(\x0b\x32\x17.quorum.pb.ProducerItem"\xc0\x01\n\x08UserItem\x12\x0f\n\x07GroupId\x18\x01 \x01(\t\x12\x12\n\nUserPubkey\x18\x02 \x01(\t\x12\x15\n\rEncryptPubkey\x18\x03 \x01(\t\x12\x18\n\x10GroupOwnerPubkey\x18\x04 \x01(\t\x12\x16\n\x0eGroupOwnerSign\x18\x05 \x01(\t\x12\x11\n\tTimeStamp\x18\x06 \x01(\x03\x12%\n\x06\x41\x63tion\x18\x07 \x01(\x0e\x32\x15.quorum.pb.ActionType\x12\x0c\n\x04Memo\x18\x08 \x01(\t"\xaa\x02\n\x0c\x41nnounceItem\x12\x0f\n\x07GroupId\x18\x01 \x01(\t\x12\x12\n\nSignPubkey\x18\x02 \x01(\t\x12\x15\n\rEncryptPubkey\x18\x03 \x01(\t\x12\x1a\n\x12\x41nnouncerSignature\x18\x04 \x01(\t\x12%\n\x04Type\x18\x05 \x01(\x0e\x32\x17.quorum.pb.AnnounceType\x12\x13\n\x0bOwnerPubkey\x18\x06 \x01(\t\x12\x16\n\x0eOwnerSignature\x18\x07 \x01(\t\x12&\n\x06Result\x18\x08 \x01(\x0e\x32\x16.quorum.pb.ApproveType\x12\x11\n\tTimeStamp\x18\t \x01(\x03\x12%\n\x06\x41\x63tion\x18\n \x01(\x0e\x32\x15.quorum.pb.ActionType\x12\x0c\n\x04Memo\x18\x0b \x01(\t"\xbc\x02\n\tGroupItem\x12\x0f\n\x07GroupId\x18\x01 \x01(\t\x12\x11\n\tGroupName\x18\x02 \x01(\t\x12\x13\n\x0bOwnerPubKey\x18\x03 \x01(\t\x12\x16\n\x0eUserSignPubkey\x18\x04 \x01(\t\x12\x19\n\x11UserEncryptPubkey\x18\x05 \x01(\t\x12\x12\n\nLastUpdate\x18\x06 \x01(\x03\x12&\n\x0cGenesisBlock\x18\x07 \x01(\x0b\x32\x10.quorum.pb.Block\x12\x30\n\x0b\x45ncryptType\x18\x08 \x01(\x0e\x32\x1b.quorum.pb.GroupEncryptType\x12\x32\n\x0c\x43onsenseType\x18\t \x01(\x0e\x32\x1c.quorum.pb.GroupConsenseType\x12\x11\n\tCipherKey\x18\n \x01(\t\x12\x0e\n\x06\x41ppKey\x18\x0b \x01(\t"\xa8\x01\n\x0f\x43hainConfigItem\x12\x0f\n\x07GroupId\x18\x01 \x01(\t\x12(\n\x04Type\x18\x02 \x01(\x0e\x32\x1a.quorum.pb.ChainConfigType\x12\x0c\n\x04\x44\x61ta\x18\x03 \x01(\x0c\x12\x13\n\x0bOwnerPubkey\x18\x04 \x01(\t\x12\x16\n\x0eOwnerSignature\x18\x05 \x01(\t\x12\x11\n\tTimeStamp\x18\x06 \x01(\x03\x12\x0c\n\x04Memo\x18\x07 \x01(\t"s\n\x18\x43hainSendTrxRuleListItem\x12%\n\x06\x41\x63tion\x18\x01 \x01(\x0e\x32\x15.quorum.pb.ActionType\x12\x0e\n\x06Pubkey\x18\x03 \x01(\t\x12 \n\x04Type\x18\x04 \x03(\x0e\x32\x12.quorum.pb.TrxType"\\\n\x12SetTrxAuthModeItem\x12 \n\x04Type\x18\x01 \x01(\x0e\x32\x12.quorum.pb.TrxType\x12$\n\x04Mode\x18\x02 \x01(\x0e\x32\x16.quorum.pb.TrxAuthMode"\xd5\x01\n\rAppConfigItem\x12\x0f\n\x07GroupId\x18\x01 \x01(\t\x12%\n\x06\x41\x63tion\x18\x02 \x01(\x0e\x32\x15.quorum.pb.ActionType\x12\x0c\n\x04Name\x18\x03 \x01(\t\x12&\n\x04Type\x18\x04 \x01(\x0e\x32\x18.quorum.pb.AppConfigType\x12\r\n\x05Value\x18\x05 \x01(\t\x12\x13\n\x0bOwnerPubkey\x18\x06 \x01(\t\x12\x11\n\tOwnerSign\x18\x07 \x01(\t\x12\x0c\n\x04Memo\x18\x08 \x01(\t\x12\x11\n\tTimeStamp\x18\t \x01(\x03"\xd1\x01\n\tGroupSeed\x12&\n\x0cGenesisBlock\x18\x01 \x01(\x0b\x32\x10.quorum.pb.Block\x12\x0f\n\x07GroupId\x18\x02 \x01(\t\x12\x11\n\tGroupName\x18\x03 \x01(\t\x12\x13\n\x0bOwnerPubkey\x18\x04 \x01(\t\x12\x15\n\rConsensusType\x18\x05 \x01(\t\x12\x16\n\x0e\x45ncryptionType\x18\x06 \x01(\t\x12\x11\n\tCipherKey\x18\x07 \x01(\t\x12\x0e\n\x06\x41ppKey\x18\x08 \x01(\t\x12\x11\n\tSignature\x18\t \x01(\t"\x83\x01\n\x10NodeSDKGroupItem\x12#\n\x05Group\x18\x01 \x01(\x0b\x32\x14.quorum.pb.GroupItem\x12\x14\n\x0c\x45ncryptAlias\x18\x02 \x01(\t\x12\x11\n\tSignAlias\x18\x03 \x01(\t\x12\x0e\n\x06\x41piUrl\x18\x04 \x03(\t\x12\x11\n\tGroupSeed\x18\x05 \x01(\t"+\n\x0bHBTrxBundle\x12\x1c\n\x04Trxs\x18\x01 \x03(\x0b\x32\x0e.quorum.pb.Trx"j\n\x07HBMsgv1\x12\r\n\x05MsgId\x18\x01 \x01(\t\x12\r\n\x05\x45poch\x18\x02 \x01(\x04\x12\x30\n\x0bPayloadType\x18\x03 \x01(\x0e\x32\x1b.quorum.pb.HBMsgPayloadType\x12\x0f\n\x07Payload\x18\x04 \x01(\x0c">\n\x06RBCMsg\x12#\n\x04Type\x18\x01 \x01(\x0e\x32\x15.quorum.pb.RBCMsgType\x12\x0f\n\x07Payload\x18\x02 \x01(\x0c"\xad\x01\n\x0bInitPropose\x12\x10\n\x08RootHash\x18\x01 \x01(\x0c\x12\r\n\x05Proof\x18\x02 \x03(\x0c\x12\r\n\x05Index\x18\x03 \x01(\x03\x12\x0e\n\x06Leaves\x18\x04 \x01(\x03\x12\x18\n\x10OriginalDataSize\x18\x05 \x01(\x03\x12\x16\n\x0eRecvNodePubkey\x18\x06 \x01(\t\x12\x16\n\x0eProposerPubkey\x18\x07 \x01(\t\x12\x14\n\x0cProposerSign\x18\x08 \x01(\x0c"\xb6\x01\n\x04\x45\x63ho\x12\x10\n\x08RootHash\x18\x01 \x01(\x0c\x12\r\n\x05Proof\x18\x02 \x03(\x0c\x12\r\n\x05Index\x18\x03 \x01(\x03\x12\x0e\n\x06Leaves\x18\x04 \x01(\x03\x12\x18\n\x10OriginalDataSize\x18\x05 \x01(\x03\x12\x1e\n\x16OriginalProposerPubkey\x18\x06 \x01(\t\x12\x1a\n\x12\x45\x63hoProviderPubkey\x18\x07 \x01(\t\x12\x18\n\x10\x45\x63hoProviderSign\x18\x08 \x01(\x0c"q\n\x05Ready\x12\x10\n\x08RootHash\x18\x01 \x01(\x0c\x12\x1e\n\x16OriginalProposerPubkey\x18\x02 \x01(\t\x12\x1b\n\x13ReadyProviderPubkey\x18\x03 \x01(\t\x12\x19\n\x11ReadyProviderSign\x18\x04 \x01(\x0c">\n\x06\x42\x42\x41Msg\x12#\n\x04Type\x18\x01 \x01(\x0e\x32\x15.quorum.pb.BBAMsgType\x12\x0f\n\x07Payload\x18\x02 \x01(\x0c"N\n\x04\x42val\x12\x12\n\nProposerId\x18\x01 \x01(\t\x12\x14\n\x0cSenderPubkey\x18\x02 \x01(\t\x12\r\n\x05\x45poch\x18\x03 \x01(\x03\x12\r\n\x05Value\x18\x04 \x01(\x08"M\n\x03\x41ux\x12\x12\n\nProposerId\x18\x01 \x01(\t\x12\x14\n\x0cSenderPubkey\x18\x02 \x01(\t\x12\r\n\x05\x45poch\x18\x03 \x01(\x04\x12\r\n\x05Value\x18\x04 \x01(\x08"E\n\x08PSyncMsg\x12(\n\x07MsgType\x18\x01 \x01(\x0e\x32\x17.quorum.pb.PSyncMsgType\x12\x0f\n\x07Payload\x18\x02 \x01(\x0c"i\n\x08PSyncReq\x12\x0f\n\x07GroupId\x18\x01 \x01(\t\x12\x11\n\tSessionId\x18\x02 \x01(\t\x12\x14\n\x0cSenderPubkey\x18\x03 \x01(\t\x12\x0f\n\x07MyEpoch\x18\x04 \x01(\x04\x12\x12\n\nSenderSign\x18\x05 \x01(\x0c"\xcd\x01\n\tPSyncResp\x12\x0f\n\x07GroupId\x18\x01 \x01(\t\x12\x11\n\tSessionId\x18\x02 \x01(\t\x12\x14\n\x0cSenderPubkey\x18\x03 \x01(\t\x12\x12\n\nMyCurEpoch\x18\x04 \x01(\x04\x12\x37\n\x11MyCurProducerList\x18\x05 \x01(\x0b\x32\x1c.quorum.pb.PSyncProducerItem\x12%\n\rProducerProof\x18\x06 \x01(\x0b\x32\x0e.quorum.pb.Trx\x12\x12\n\nSenderSign\x18\x07 \x01(\x0c"&\n\x11PSyncProducerItem\x12\x11\n\tProducers\x18\x01 \x03(\t"\x92\x03\n\x0bGroupItemV0\x12\x0f\n\x07GroupId\x18\x01 \x01(\t\x12\x11\n\tGroupName\x18\x02 \x01(\t\x12\x13\n\x0bOwnerPubKey\x18\x03 \x01(\t\x12\x16\n\x0eUserSignPubkey\x18\x04 \x01(\t\x12\x19\n\x11UserEncryptPubkey\x18\x05 \x01(\t\x12#\n\x08UserRole\x18\x06 \x01(\x0e\x32\x11.quorum.pb.RoleV0\x12\x12\n\nLastUpdate\x18\x07 \x01(\x03\x12\x15\n\rHighestHeight\x18\x08 \x01(\x03\x12\x16\n\x0eHighestBlockId\x18\t \x01(\t\x12&\n\x0cGenesisBlock\x18\n \x01(\x0b\x32\x10.quorum.pb.Block\x12\x30\n\x0b\x45ncryptType\x18\x0b \x01(\x0e\x32\x1b.quorum.pb.GroupEncryptType\x12\x32\n\x0c\x43onsenseType\x18\x0c \x01(\x0e\x32\x1c.quorum.pb.GroupConsenseType\x12\x11\n\tCipherKey\x18\r \x01(\t\x12\x0e\n\x06\x41ppKey\x18\x0e \x01(\t*5\n\x0bPackageType\x12\x07\n\x03TRX\x10\x00\x12\t\n\x05\x42LOCK\x10\x01\x12\x07\n\x03HBB\x10\x02\x12\t\n\x05PSYNC\x10\x03*,\n\x0c\x41nnounceType\x12\x0b\n\x07\x41S_USER\x10\x00\x12\x0f\n\x0b\x41S_PRODUCER\x10\x01*8\n\x0b\x41pproveType\x12\r\n\tANNOUNCED\x10\x00\x12\x0c\n\x08\x41PPROVED\x10\x01\x12\x0c\n\x08REJECTED\x10\x02*!\n\nActionType\x12\x07\n\x03\x41\x44\x44\x10\x00\x12\n\n\x06REMOVE\x10\x01*&\n\x0eTrxStroageType\x12\t\n\x05\x43HAIN\x10\x00\x12\t\n\x05\x43\x41\x43HE\x10\x01*~\n\x07TrxType\x12\x08\n\x04POST\x10\x00\x12\x0c\n\x08\x41NNOUNCE\x10\x01\x12\x0c\n\x08PRODUCER\x10\x02\x12\x08\n\x04USER\x10\x03\x12\r\n\tREQ_BLOCK\x10\x04\x12\x12\n\x0eREQ_BLOCK_RESP\x10\x05\x12\x10\n\x0c\x43HAIN_CONFIG\x10\x06\x12\x0e\n\nAPP_CONFIG\x10\x07*P\n\x0cReqBlkResult\x12\x11\n\rBLOCK_IN_RESP\x10\x00\x12\x18\n\x14\x42LOCK_IN_RESP_ON_TOP\x10\x01\x12\x13\n\x0f\x42LOCK_NOT_FOUND\x10\x02*+\n\x10GroupEncryptType\x12\n\n\x06PUBLIC\x10\x00\x12\x0b\n\x07PRIVATE\x10\x01*%\n\x11GroupConsenseType\x12\x07\n\x03POA\x10\x00\x12\x07\n\x03POS\x10\x01*,\n\x06RoleV0\x12\x12\n\x0eGROUP_PRODUCER\x10\x00\x12\x0e\n\nGROUP_USER\x10\x01*L\n\x0f\x43hainConfigType\x12\x15\n\x11SET_TRX_AUTH_MODE\x10\x00\x12\x10\n\x0cUPD_DNY_LIST\x10\x01\x12\x10\n\x0cUPD_ALW_LIST\x10\x02*7\n\x0bTrxAuthMode\x12\x13\n\x0f\x46OLLOW_ALW_LIST\x10\x00\x12\x13\n\x0f\x46OLLOW_DNY_LIST\x10\x01*-\n\x0c\x41uthListType\x12\x0e\n\nALLOW_LIST\x10\x00\x12\r\n\tDENY_LIST\x10\x01*.\n\rAppConfigType\x12\x07\n\x03INT\x10\x00\x12\x08\n\x04\x42OOL\x10\x01\x12\n\n\x06STRING\x10\x02*$\n\x10HBMsgPayloadType\x12\x07\n\x03RBC\x10\x00\x12\x07\n\x03\x42\x42\x41\x10\x01*3\n\nRBCMsgType\x12\x10\n\x0cINIT_PROPOSE\x10\x00\x12\x08\n\x04\x45\x43HO\x10\x01\x12\t\n\x05READY\x10\x02*\x1f\n\nBBAMsgType\x12\x08\n\x04\x42VAL\x10\x00\x12\x07\n\x03\x41UX\x10\x01*-\n\x0cPSyncMsgType\x12\r\n\tPSYNC_REQ\x10\x00\x12\x0e\n\nPSYNC_RESP\x10\x01\x42$Z"github.com/rumsystem/quorum/pkg/pbb\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "quorum_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z"github.com/rumsystem/quorum/pkg/pb'
    _PACKAGETYPE._serialized_start = 4795
    _PACKAGETYPE._serialized_end = 4848
    _ANNOUNCETYPE._serialized_start = 4850
    _ANNOUNCETYPE._serialized_end = 4894
    _APPROVETYPE._serialized_start = 4896
    _APPROVETYPE._serialized_end = 4952
    _ACTIONTYPE._serialized_start = 4954
    _ACTIONTYPE._serialized_end = 4987
    _TRXSTROAGETYPE._serialized_start = 4989
    _TRXSTROAGETYPE._serialized_end = 5027
    _TRXTYPE._serialized_start = 5029
    _TRXTYPE._serialized_end = 5155
    _REQBLKRESULT._serialized_start = 5157
    _REQBLKRESULT._serialized_end = 5237
    _GROUPENCRYPTTYPE._serialized_start = 5239
    _GROUPENCRYPTTYPE._serialized_end = 5282
    _GROUPCONSENSETYPE._serialized_start = 5284
    _GROUPCONSENSETYPE._serialized_end = 5321
    _ROLEV0._serialized_start = 5323
    _ROLEV0._serialized_end = 5367
    _CHAINCONFIGTYPE._serialized_start = 5369
    _CHAINCONFIGTYPE._serialized_end = 5445
    _TRXAUTHMODE._serialized_start = 5447
    _TRXAUTHMODE._serialized_end = 5502
    _AUTHLISTTYPE._serialized_start = 5504
    _AUTHLISTTYPE._serialized_end = 5549
    _APPCONFIGTYPE._serialized_start = 5551
    _APPCONFIGTYPE._serialized_end = 5597
    _HBMSGPAYLOADTYPE._serialized_start = 5599
    _HBMSGPAYLOADTYPE._serialized_end = 5635
    _RBCMSGTYPE._serialized_start = 5637
    _RBCMSGTYPE._serialized_end = 5688
    _BBAMSGTYPE._serialized_start = 5690
    _BBAMSGTYPE._serialized_end = 5721
    _PSYNCMSGTYPE._serialized_start = 5723
    _PSYNCMSGTYPE._serialized_end = 5768
    _PACKAGE._serialized_start = 27
    _PACKAGE._serialized_end = 88
    _TRX._serialized_start = 91
    _TRX._serialized_end = 355
    _BLOCK._serialized_start = 358
    _BLOCK._serialized_end = 560
    _REQBLOCK._serialized_start = 562
    _REQBLOCK._serialized_end = 650
    _BLOCKSBUNDLE._serialized_start = 652
    _BLOCKSBUNDLE._serialized_end = 700
    _REQBLOCKRESP._serialized_start = 703
    _REQBLOCKRESP._serialized_end = 929
    _POSTITEM._serialized_start = 931
    _POSTITEM._serialized_end = 1014
    _PRODUCERITEM._serialized_start = 1017
    _PRODUCERITEM._serialized_end = 1218
    _BFTPRODUCERBUNDLEITEM._serialized_start = 1220
    _BFTPRODUCERBUNDLEITEM._serialized_end = 1287
    _USERITEM._serialized_start = 1290
    _USERITEM._serialized_end = 1482
    _ANNOUNCEITEM._serialized_start = 1485
    _ANNOUNCEITEM._serialized_end = 1783
    _GROUPITEM._serialized_start = 1786
    _GROUPITEM._serialized_end = 2102
    _CHAINCONFIGITEM._serialized_start = 2105
    _CHAINCONFIGITEM._serialized_end = 2273
    _CHAINSENDTRXRULELISTITEM._serialized_start = 2275
    _CHAINSENDTRXRULELISTITEM._serialized_end = 2390
    _SETTRXAUTHMODEITEM._serialized_start = 2392
    _SETTRXAUTHMODEITEM._serialized_end = 2484
    _APPCONFIGITEM._serialized_start = 2487
    _APPCONFIGITEM._serialized_end = 2700
    _GROUPSEED._serialized_start = 2703
    _GROUPSEED._serialized_end = 2912
    _NODESDKGROUPITEM._serialized_start = 2915
    _NODESDKGROUPITEM._serialized_end = 3046
    _HBTRXBUNDLE._serialized_start = 3048
    _HBTRXBUNDLE._serialized_end = 3091
    _HBMSGV1._serialized_start = 3093
    _HBMSGV1._serialized_end = 3199
    _RBCMSG._serialized_start = 3201
    _RBCMSG._serialized_end = 3263
    _INITPROPOSE._serialized_start = 3266
    _INITPROPOSE._serialized_end = 3439
    _ECHO._serialized_start = 3442
    _ECHO._serialized_end = 3624
    _READY._serialized_start = 3626
    _READY._serialized_end = 3739
    _BBAMSG._serialized_start = 3741
    _BBAMSG._serialized_end = 3803
    _BVAL._serialized_start = 3805
    _BVAL._serialized_end = 3883
    _AUX._serialized_start = 3885
    _AUX._serialized_end = 3962
    _PSYNCMSG._serialized_start = 3964
    _PSYNCMSG._serialized_end = 4033
    _PSYNCREQ._serialized_start = 4035
    _PSYNCREQ._serialized_end = 4140
    _PSYNCRESP._serialized_start = 4143
    _PSYNCRESP._serialized_end = 4348
    _PSYNCPRODUCERITEM._serialized_start = 4350
    _PSYNCPRODUCERITEM._serialized_end = 4388
    _GROUPITEMV0._serialized_start = 4391
    _GROUPITEMV0._serialized_end = 4793
# @@protoc_insertion_point(module_scope)
