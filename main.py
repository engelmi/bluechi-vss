import datetime
import grpc

from kuksa.val.v2.types_pb2 import SignalID, Datapoint, Value
from kuksa.val.v2.val_pb2 import GetValueRequest, PublishValueRequest
from kuksa.val.v2.val_pb2_grpc import VALStub

with grpc.insecure_channel("0.0.0.0:55555") as channel:
    stub = VALStub(channel)
    response = stub.GetValue(GetValueRequest(
        signal_id=SignalID(path="Vehicle.Speed")))
    print(response)
    stub.PublishValue(PublishValueRequest(
        signal_id=SignalID(path="Vehicle.Speed"),
        data_point=Datapoint(
            timestamp=datetime.datetime.now(), value=Value(float=99.0)),
    ))
