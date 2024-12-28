# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: kuksa/val/v2/val.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'kuksa/val/v2/val.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kuksa.val.v2 import types_pb2 as kuksa_dot_val_dot_v2_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16kuksa/val/v2/val.proto\x12\x0ckuksa.val.v2\x1a\x18kuksa/val/v2/types.proto\"<\n\x0fGetValueRequest\x12)\n\tsignal_id\x18\x01 \x01(\x0b\x32\x16.kuksa.val.v2.SignalID\"?\n\x10GetValueResponse\x12+\n\ndata_point\x18\x01 \x01(\x0b\x32\x17.kuksa.val.v2.Datapoint\">\n\x10GetValuesRequest\x12*\n\nsignal_ids\x18\x01 \x03(\x0b\x32\x16.kuksa.val.v2.SignalID\"A\n\x11GetValuesResponse\x12,\n\x0b\x64\x61ta_points\x18\x01 \x03(\x0b\x32\x17.kuksa.val.v2.Datapoint\"=\n\x10SubscribeRequest\x12\x14\n\x0csignal_paths\x18\x01 \x03(\t\x12\x13\n\x0b\x62uffer_size\x18\x02 \x01(\r\"\x9b\x01\n\x11SubscribeResponse\x12=\n\x07\x65ntries\x18\x01 \x03(\x0b\x32,.kuksa.val.v2.SubscribeResponse.EntriesEntry\x1aG\n\x0c\x45ntriesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.kuksa.val.v2.Datapoint:\x02\x38\x01\"?\n\x14SubscribeByIdRequest\x12\x12\n\nsignal_ids\x18\x01 \x03(\x05\x12\x13\n\x0b\x62uffer_size\x18\x02 \x01(\r\"\xa3\x01\n\x15SubscribeByIdResponse\x12\x41\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x30.kuksa.val.v2.SubscribeByIdResponse.EntriesEntry\x1aG\n\x0c\x45ntriesEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.kuksa.val.v2.Datapoint:\x02\x38\x01\"_\n\x0e\x41\x63tuateRequest\x12)\n\tsignal_id\x18\x01 \x01(\x0b\x32\x16.kuksa.val.v2.SignalID\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.kuksa.val.v2.Value\"\x11\n\x0f\x41\x63tuateResponse\"M\n\x13\x42\x61tchActuateRequest\x12\x36\n\x10\x61\x63tuate_requests\x18\x01 \x03(\x0b\x32\x1c.kuksa.val.v2.ActuateRequest\"\x16\n\x14\x42\x61tchActuateResponse\"3\n\x13ListMetadataRequest\x12\x0c\n\x04root\x18\x01 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x02 \x01(\t\"@\n\x14ListMetadataResponse\x12(\n\x08metadata\x18\x01 \x03(\x0b\x32\x16.kuksa.val.v2.Metadata\"m\n\x13PublishValueRequest\x12)\n\tsignal_id\x18\x01 \x01(\x0b\x32\x16.kuksa.val.v2.SignalID\x12+\n\ndata_point\x18\x02 \x01(\x0b\x32\x17.kuksa.val.v2.Datapoint\"\x16\n\x14PublishValueResponse\"\xbf\x01\n\x14PublishValuesRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\x05\x12G\n\x0b\x64\x61ta_points\x18\x02 \x03(\x0b\x32\x32.kuksa.val.v2.PublishValuesRequest.DataPointsEntry\x1aJ\n\x0f\x44\x61taPointsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.kuksa.val.v2.Datapoint:\x02\x38\x01\"\xb0\x01\n\x15PublishValuesResponse\x12\x12\n\nrequest_id\x18\x01 \x01(\x05\x12?\n\x06status\x18\x02 \x03(\x0b\x32/.kuksa.val.v2.PublishValuesResponse.StatusEntry\x1a\x42\n\x0bStatusEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.kuksa.val.v2.Error:\x02\x38\x01\"O\n\x17ProvideActuationRequest\x12\x34\n\x14\x61\x63tuator_identifiers\x18\x01 \x03(\x0b\x32\x16.kuksa.val.v2.SignalID\"\x1a\n\x18ProvideActuationResponse\"S\n\x19\x42\x61tchActuateStreamRequest\x12\x36\n\x10\x61\x63tuate_requests\x18\x01 \x03(\x0b\x32\x1c.kuksa.val.v2.ActuateRequest\"k\n\x1a\x42\x61tchActuateStreamResponse\x12)\n\tsignal_id\x18\x01 \x01(\x0b\x32\x16.kuksa.val.v2.SignalID\x12\"\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x13.kuksa.val.v2.Error\"\x8a\x02\n\x19OpenProviderStreamRequest\x12J\n\x19provide_actuation_request\x18\x01 \x01(\x0b\x32%.kuksa.val.v2.ProvideActuationRequestH\x00\x12\x44\n\x16publish_values_request\x18\x02 \x01(\x0b\x32\".kuksa.val.v2.PublishValuesRequestH\x00\x12Q\n\x1d\x62\x61tch_actuate_stream_response\x18\x03 \x01(\x0b\x32(.kuksa.val.v2.BatchActuateStreamResponseH\x00\x42\x08\n\x06\x61\x63tion\"\x8d\x02\n\x1aOpenProviderStreamResponse\x12L\n\x1aprovide_actuation_response\x18\x01 \x01(\x0b\x32&.kuksa.val.v2.ProvideActuationResponseH\x00\x12\x46\n\x17publish_values_response\x18\x02 \x01(\x0b\x32#.kuksa.val.v2.PublishValuesResponseH\x00\x12O\n\x1c\x62\x61tch_actuate_stream_request\x18\x03 \x01(\x0b\x32\'.kuksa.val.v2.BatchActuateStreamRequestH\x00\x42\x08\n\x06\x61\x63tion\"\x16\n\x14GetServerInfoRequest\"K\n\x15GetServerInfoResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x13\n\x0b\x63ommit_hash\x18\x03 \x01(\t2\xde\x06\n\x03VAL\x12I\n\x08GetValue\x12\x1d.kuksa.val.v2.GetValueRequest\x1a\x1e.kuksa.val.v2.GetValueResponse\x12L\n\tGetValues\x12\x1e.kuksa.val.v2.GetValuesRequest\x1a\x1f.kuksa.val.v2.GetValuesResponse\x12N\n\tSubscribe\x12\x1e.kuksa.val.v2.SubscribeRequest\x1a\x1f.kuksa.val.v2.SubscribeResponse0\x01\x12Z\n\rSubscribeById\x12\".kuksa.val.v2.SubscribeByIdRequest\x1a#.kuksa.val.v2.SubscribeByIdResponse0\x01\x12\x46\n\x07\x41\x63tuate\x12\x1c.kuksa.val.v2.ActuateRequest\x1a\x1d.kuksa.val.v2.ActuateResponse\x12U\n\x0c\x42\x61tchActuate\x12!.kuksa.val.v2.BatchActuateRequest\x1a\".kuksa.val.v2.BatchActuateResponse\x12U\n\x0cListMetadata\x12!.kuksa.val.v2.ListMetadataRequest\x1a\".kuksa.val.v2.ListMetadataResponse\x12U\n\x0cPublishValue\x12!.kuksa.val.v2.PublishValueRequest\x1a\".kuksa.val.v2.PublishValueResponse\x12k\n\x12OpenProviderStream\x12\'.kuksa.val.v2.OpenProviderStreamRequest\x1a(.kuksa.val.v2.OpenProviderStreamResponse(\x01\x30\x01\x12X\n\rGetServerInfo\x12\".kuksa.val.v2.GetServerInfoRequest\x1a#.kuksa.val.v2.GetServerInfoResponseB\x0eZ\x0ckuksa/val/v2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kuksa.val.v2.val_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\014kuksa/val/v2'
  _globals['_SUBSCRIBERESPONSE_ENTRIESENTRY']._loaded_options = None
  _globals['_SUBSCRIBERESPONSE_ENTRIESENTRY']._serialized_options = b'8\001'
  _globals['_SUBSCRIBEBYIDRESPONSE_ENTRIESENTRY']._loaded_options = None
  _globals['_SUBSCRIBEBYIDRESPONSE_ENTRIESENTRY']._serialized_options = b'8\001'
  _globals['_PUBLISHVALUESREQUEST_DATAPOINTSENTRY']._loaded_options = None
  _globals['_PUBLISHVALUESREQUEST_DATAPOINTSENTRY']._serialized_options = b'8\001'
  _globals['_PUBLISHVALUESRESPONSE_STATUSENTRY']._loaded_options = None
  _globals['_PUBLISHVALUESRESPONSE_STATUSENTRY']._serialized_options = b'8\001'
  _globals['_GETVALUEREQUEST']._serialized_start=66
  _globals['_GETVALUEREQUEST']._serialized_end=126
  _globals['_GETVALUERESPONSE']._serialized_start=128
  _globals['_GETVALUERESPONSE']._serialized_end=191
  _globals['_GETVALUESREQUEST']._serialized_start=193
  _globals['_GETVALUESREQUEST']._serialized_end=255
  _globals['_GETVALUESRESPONSE']._serialized_start=257
  _globals['_GETVALUESRESPONSE']._serialized_end=322
  _globals['_SUBSCRIBEREQUEST']._serialized_start=324
  _globals['_SUBSCRIBEREQUEST']._serialized_end=385
  _globals['_SUBSCRIBERESPONSE']._serialized_start=388
  _globals['_SUBSCRIBERESPONSE']._serialized_end=543
  _globals['_SUBSCRIBERESPONSE_ENTRIESENTRY']._serialized_start=472
  _globals['_SUBSCRIBERESPONSE_ENTRIESENTRY']._serialized_end=543
  _globals['_SUBSCRIBEBYIDREQUEST']._serialized_start=545
  _globals['_SUBSCRIBEBYIDREQUEST']._serialized_end=608
  _globals['_SUBSCRIBEBYIDRESPONSE']._serialized_start=611
  _globals['_SUBSCRIBEBYIDRESPONSE']._serialized_end=774
  _globals['_SUBSCRIBEBYIDRESPONSE_ENTRIESENTRY']._serialized_start=703
  _globals['_SUBSCRIBEBYIDRESPONSE_ENTRIESENTRY']._serialized_end=774
  _globals['_ACTUATEREQUEST']._serialized_start=776
  _globals['_ACTUATEREQUEST']._serialized_end=871
  _globals['_ACTUATERESPONSE']._serialized_start=873
  _globals['_ACTUATERESPONSE']._serialized_end=890
  _globals['_BATCHACTUATEREQUEST']._serialized_start=892
  _globals['_BATCHACTUATEREQUEST']._serialized_end=969
  _globals['_BATCHACTUATERESPONSE']._serialized_start=971
  _globals['_BATCHACTUATERESPONSE']._serialized_end=993
  _globals['_LISTMETADATAREQUEST']._serialized_start=995
  _globals['_LISTMETADATAREQUEST']._serialized_end=1046
  _globals['_LISTMETADATARESPONSE']._serialized_start=1048
  _globals['_LISTMETADATARESPONSE']._serialized_end=1112
  _globals['_PUBLISHVALUEREQUEST']._serialized_start=1114
  _globals['_PUBLISHVALUEREQUEST']._serialized_end=1223
  _globals['_PUBLISHVALUERESPONSE']._serialized_start=1225
  _globals['_PUBLISHVALUERESPONSE']._serialized_end=1247
  _globals['_PUBLISHVALUESREQUEST']._serialized_start=1250
  _globals['_PUBLISHVALUESREQUEST']._serialized_end=1441
  _globals['_PUBLISHVALUESREQUEST_DATAPOINTSENTRY']._serialized_start=1367
  _globals['_PUBLISHVALUESREQUEST_DATAPOINTSENTRY']._serialized_end=1441
  _globals['_PUBLISHVALUESRESPONSE']._serialized_start=1444
  _globals['_PUBLISHVALUESRESPONSE']._serialized_end=1620
  _globals['_PUBLISHVALUESRESPONSE_STATUSENTRY']._serialized_start=1554
  _globals['_PUBLISHVALUESRESPONSE_STATUSENTRY']._serialized_end=1620
  _globals['_PROVIDEACTUATIONREQUEST']._serialized_start=1622
  _globals['_PROVIDEACTUATIONREQUEST']._serialized_end=1701
  _globals['_PROVIDEACTUATIONRESPONSE']._serialized_start=1703
  _globals['_PROVIDEACTUATIONRESPONSE']._serialized_end=1729
  _globals['_BATCHACTUATESTREAMREQUEST']._serialized_start=1731
  _globals['_BATCHACTUATESTREAMREQUEST']._serialized_end=1814
  _globals['_BATCHACTUATESTREAMRESPONSE']._serialized_start=1816
  _globals['_BATCHACTUATESTREAMRESPONSE']._serialized_end=1923
  _globals['_OPENPROVIDERSTREAMREQUEST']._serialized_start=1926
  _globals['_OPENPROVIDERSTREAMREQUEST']._serialized_end=2192
  _globals['_OPENPROVIDERSTREAMRESPONSE']._serialized_start=2195
  _globals['_OPENPROVIDERSTREAMRESPONSE']._serialized_end=2464
  _globals['_GETSERVERINFOREQUEST']._serialized_start=2466
  _globals['_GETSERVERINFOREQUEST']._serialized_end=2488
  _globals['_GETSERVERINFORESPONSE']._serialized_start=2490
  _globals['_GETSERVERINFORESPONSE']._serialized_end=2565
  _globals['_VAL']._serialized_start=2568
  _globals['_VAL']._serialized_end=3430
# @@protoc_insertion_point(module_scope)
