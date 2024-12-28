# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from kuksa.val.v2 import val_pb2 as kuksa_dot_val_dot_v2_dot_val__pb2

GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in kuksa/val/v2/val_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class VALStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetValue = channel.unary_unary(
                '/kuksa.val.v2.VAL/GetValue',
                request_serializer=kuksa_dot_val_dot_v2_dot_val__pb2.GetValueRequest.SerializeToString,
                response_deserializer=kuksa_dot_val_dot_v2_dot_val__pb2.GetValueResponse.FromString,
                _registered_method=True)
        self.GetValues = channel.unary_unary(
                '/kuksa.val.v2.VAL/GetValues',
                request_serializer=kuksa_dot_val_dot_v2_dot_val__pb2.GetValuesRequest.SerializeToString,
                response_deserializer=kuksa_dot_val_dot_v2_dot_val__pb2.GetValuesResponse.FromString,
                _registered_method=True)
        self.Subscribe = channel.unary_stream(
                '/kuksa.val.v2.VAL/Subscribe',
                request_serializer=kuksa_dot_val_dot_v2_dot_val__pb2.SubscribeRequest.SerializeToString,
                response_deserializer=kuksa_dot_val_dot_v2_dot_val__pb2.SubscribeResponse.FromString,
                _registered_method=True)
        self.SubscribeById = channel.unary_stream(
                '/kuksa.val.v2.VAL/SubscribeById',
                request_serializer=kuksa_dot_val_dot_v2_dot_val__pb2.SubscribeByIdRequest.SerializeToString,
                response_deserializer=kuksa_dot_val_dot_v2_dot_val__pb2.SubscribeByIdResponse.FromString,
                _registered_method=True)
        self.Actuate = channel.unary_unary(
                '/kuksa.val.v2.VAL/Actuate',
                request_serializer=kuksa_dot_val_dot_v2_dot_val__pb2.ActuateRequest.SerializeToString,
                response_deserializer=kuksa_dot_val_dot_v2_dot_val__pb2.ActuateResponse.FromString,
                _registered_method=True)
        self.BatchActuate = channel.unary_unary(
                '/kuksa.val.v2.VAL/BatchActuate',
                request_serializer=kuksa_dot_val_dot_v2_dot_val__pb2.BatchActuateRequest.SerializeToString,
                response_deserializer=kuksa_dot_val_dot_v2_dot_val__pb2.BatchActuateResponse.FromString,
                _registered_method=True)
        self.ListMetadata = channel.unary_unary(
                '/kuksa.val.v2.VAL/ListMetadata',
                request_serializer=kuksa_dot_val_dot_v2_dot_val__pb2.ListMetadataRequest.SerializeToString,
                response_deserializer=kuksa_dot_val_dot_v2_dot_val__pb2.ListMetadataResponse.FromString,
                _registered_method=True)
        self.PublishValue = channel.unary_unary(
                '/kuksa.val.v2.VAL/PublishValue',
                request_serializer=kuksa_dot_val_dot_v2_dot_val__pb2.PublishValueRequest.SerializeToString,
                response_deserializer=kuksa_dot_val_dot_v2_dot_val__pb2.PublishValueResponse.FromString,
                _registered_method=True)
        self.OpenProviderStream = channel.stream_stream(
                '/kuksa.val.v2.VAL/OpenProviderStream',
                request_serializer=kuksa_dot_val_dot_v2_dot_val__pb2.OpenProviderStreamRequest.SerializeToString,
                response_deserializer=kuksa_dot_val_dot_v2_dot_val__pb2.OpenProviderStreamResponse.FromString,
                _registered_method=True)
        self.GetServerInfo = channel.unary_unary(
                '/kuksa.val.v2.VAL/GetServerInfo',
                request_serializer=kuksa_dot_val_dot_v2_dot_val__pb2.GetServerInfoRequest.SerializeToString,
                response_deserializer=kuksa_dot_val_dot_v2_dot_val__pb2.GetServerInfoResponse.FromString,
                _registered_method=True)


class VALServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetValue(self, request, context):
        """Get the latest value of a signal
        If the signal exist but does not have a valid value
        a DataPoint where value is None shall be returned.

        Returns (GRPC error code):
        NOT_FOUND if the requested signal doesn't exist
        UNAUTHENTICATED if no credentials provided or credentials has expired
        PERMISSION_DENIED if access is denied
        INVALID_ARGUMENT if the request is empty or provided path is too long
        - MAX_REQUEST_PATH_LENGTH: usize = 1000;

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetValues(self, request, context):
        """Get the latest values of a set of signals.
        The returned list of data points has the same order as the list of the request.
        If a requested signal has no value a DataPoint where value is None will be returned.

        Returns (GRPC error code):
        NOT_FOUND if any of the requested signals doesn't exist.
        UNAUTHENTICATED if no credentials provided or credentials has expired
        PERMISSION_DENIED if access is denied for any of the requested signals.
        INVALID_ARGUMENT if the request is empty or provided path is too long
        - MAX_REQUEST_PATH_LENGTH: usize = 1000;

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Subscribe(self, request, context):
        """Subscribe to a set of signals using string path parameters
        Returns (GRPC error code):
        NOT_FOUND if any of the signals are non-existant.
        UNAUTHENTICATED if no credentials provided or credentials has expired
        PERMISSION_DENIED if access is denied for any of the signals.
        INVALID_ARGUMENT
        - if the request is empty or provided path is too long
        MAX_REQUEST_PATH_LENGTH: usize = 1000;
        - if buffer_size exceeds the maximum permitted
        MAX_BUFFER_SIZE: usize = 1000;

        When subscribing, Databroker shall immediately return the value for all
        subscribed entries.
        If a value isn't available when subscribing to a it, it should return None

        If a subscriber is slow to consume signals, messages will be buffered up
        to the specified buffer_size before the oldest messages are dropped.

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeById(self, request, context):
        """Subscribe to a set of signals using i32 id parameters
        Returns (GRPC error code):
        NOT_FOUND if any of the signals are non-existant.
        UNAUTHENTICATED if no credentials provided or credentials has expired
        PERMISSION_DENIED if access is denied for any of the signals.
        INVALID_ARGUMENT
        - if the request is empty or provided path is too long
        MAX_REQUEST_PATH_LENGTH: usize = 1000;
        - if buffer_size exceeds the maximum permitted
        MAX_BUFFER_SIZE: usize = 1000;

        When subscribing, Databroker shall immediately return the value for all
        subscribed entries.
        If a value isn't available when subscribing to a it, it should return None

        If a subscriber is slow to consume signals, messages will be buffered up
        to the specified buffer_size before the oldest messages are dropped.

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Actuate(self, request, context):
        """Actuate a single actuator

        Returns (GRPC error code):
        NOT_FOUND if the actuator does not exist.
        PERMISSION_DENIED if access is denied for the actuator.
        UNAUTHENTICATED if no credentials provided or credentials has expired
        UNAVAILABLE if there is no provider currently providing the actuator
        DATA_LOSS is there is a internal TransmissionFailure
        INVALID_ARGUMENT
        - if the provided path is not an actuator.
        - if the data type used in the request does not match
        the data type of the addressed signal
        - if the requested value is not accepted,
        e.g. if sending an unsupported enum value
        - if the provided value is out of the min/max range specified

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchActuate(self, request, context):
        """Actuate simultaneously multiple actuators.
        If any error occurs, the entire operation will be aborted
        and no single actuator value will be forwarded to the provider.

        Returns (GRPC error code):
        NOT_FOUND if any of the actuators are non-existant.
        PERMISSION_DENIED if access is denied for any of the actuators.
        UNAUTHENTICATED if no credentials provided or credentials has expired
        UNAVAILABLE if there is no provider currently providing an actuator
        DATA_LOSS is there is a internal TransmissionFailure
        INVALID_ARGUMENT
        - if any of the provided path is not an actuator.
        - if the data type used in the request does not match
        the data type of the addressed signal
        - if the requested value is not accepted,
        e.g. if sending an unsupported enum value
        - if any of the provided actuators values are out of the min/max range specified

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListMetadata(self, request, context):
        """List metadata of signals matching the request.

        Returns (GRPC error code):
        NOT_FOUND if the specified root branch does not exist.
        UNAUTHENTICATED if no credentials provided or credentials has expired
        INVALID_ARGUMENT if the provided path or wildcard is wrong.

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PublishValue(self, request, context):
        """Publish a signal value. Used for low frequency signals (e.g. attributes).

        Returns (GRPC error code):
        NOT_FOUND if any of the signals are non-existant.
        PERMISSION_DENIED
        - if access is denied for any of the signals.
        UNAUTHENTICATED if no credentials provided or credentials has expired
        INVALID_ARGUMENT
        - if the data type used in the request does not match
        the data type of the addressed signal
        - if the published value is not accepted,
        e.g. if sending an unsupported enum value
        - if the published value is out of the min/max range specified

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OpenProviderStream(self, request_iterator, context):
        """Open a stream used to provide actuation and/or publishing values using
        a streaming interface. Used to provide actuators and to enable high frequency
        updates of values.

        The open stream is used for request / response type communication between the
        provider and server (where the initiator of a request can vary).

        Errors:
        - Provider sends ProvideActuationRequest -> Databroker returns ProvideActuationResponse
        Returns (GRPC error code) and closes the stream call (strict case).
        NOT_FOUND if any of the signals are non-existant.
        PERMISSION_DENIED if access is denied for any of the signals.
        UNAUTHENTICATED if no credentials provided or credentials has expired
        ALREADY_EXISTS if a provider already claimed the ownership of an actuator

        - Provider sends PublishValuesRequest -> Databroker returns PublishValuesResponse upon error, and nothing upon success
        GRPC errors are returned as messages in the stream
        response with the signal id `map<int32, Error> status = 2;` (permissive case)
        NOT_FOUND if a signal is non-existant.
        PERMISSION_DENIED
        - if access is denied for a signal.
        INVALID_ARGUMENT
        - if the data type used in the request does not match
        the data type of the addressed signal
        - if the published value is not accepted,
        e.g. if sending an unsupported enum value
        - if the published value is out of the min/max range specified

        - Databroker sends BatchActuateStreamRequest -> Provider shall return a BatchActuateStreamResponse,
        for every signal requested to indicate if the request was accepted or not.
        It is up to the provider to decide if the stream shall be closed,
        as of today Databroker will not react on the received error message.

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetServerInfo(self, request, context):
        """Get server information
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VALServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetValue': grpc.unary_unary_rpc_method_handler(
                    servicer.GetValue,
                    request_deserializer=kuksa_dot_val_dot_v2_dot_val__pb2.GetValueRequest.FromString,
                    response_serializer=kuksa_dot_val_dot_v2_dot_val__pb2.GetValueResponse.SerializeToString,
            ),
            'GetValues': grpc.unary_unary_rpc_method_handler(
                    servicer.GetValues,
                    request_deserializer=kuksa_dot_val_dot_v2_dot_val__pb2.GetValuesRequest.FromString,
                    response_serializer=kuksa_dot_val_dot_v2_dot_val__pb2.GetValuesResponse.SerializeToString,
            ),
            'Subscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=kuksa_dot_val_dot_v2_dot_val__pb2.SubscribeRequest.FromString,
                    response_serializer=kuksa_dot_val_dot_v2_dot_val__pb2.SubscribeResponse.SerializeToString,
            ),
            'SubscribeById': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeById,
                    request_deserializer=kuksa_dot_val_dot_v2_dot_val__pb2.SubscribeByIdRequest.FromString,
                    response_serializer=kuksa_dot_val_dot_v2_dot_val__pb2.SubscribeByIdResponse.SerializeToString,
            ),
            'Actuate': grpc.unary_unary_rpc_method_handler(
                    servicer.Actuate,
                    request_deserializer=kuksa_dot_val_dot_v2_dot_val__pb2.ActuateRequest.FromString,
                    response_serializer=kuksa_dot_val_dot_v2_dot_val__pb2.ActuateResponse.SerializeToString,
            ),
            'BatchActuate': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchActuate,
                    request_deserializer=kuksa_dot_val_dot_v2_dot_val__pb2.BatchActuateRequest.FromString,
                    response_serializer=kuksa_dot_val_dot_v2_dot_val__pb2.BatchActuateResponse.SerializeToString,
            ),
            'ListMetadata': grpc.unary_unary_rpc_method_handler(
                    servicer.ListMetadata,
                    request_deserializer=kuksa_dot_val_dot_v2_dot_val__pb2.ListMetadataRequest.FromString,
                    response_serializer=kuksa_dot_val_dot_v2_dot_val__pb2.ListMetadataResponse.SerializeToString,
            ),
            'PublishValue': grpc.unary_unary_rpc_method_handler(
                    servicer.PublishValue,
                    request_deserializer=kuksa_dot_val_dot_v2_dot_val__pb2.PublishValueRequest.FromString,
                    response_serializer=kuksa_dot_val_dot_v2_dot_val__pb2.PublishValueResponse.SerializeToString,
            ),
            'OpenProviderStream': grpc.stream_stream_rpc_method_handler(
                    servicer.OpenProviderStream,
                    request_deserializer=kuksa_dot_val_dot_v2_dot_val__pb2.OpenProviderStreamRequest.FromString,
                    response_serializer=kuksa_dot_val_dot_v2_dot_val__pb2.OpenProviderStreamResponse.SerializeToString,
            ),
            'GetServerInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServerInfo,
                    request_deserializer=kuksa_dot_val_dot_v2_dot_val__pb2.GetServerInfoRequest.FromString,
                    response_serializer=kuksa_dot_val_dot_v2_dot_val__pb2.GetServerInfoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'kuksa.val.v2.VAL', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('kuksa.val.v2.VAL', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class VAL(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetValue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/kuksa.val.v2.VAL/GetValue',
            kuksa_dot_val_dot_v2_dot_val__pb2.GetValueRequest.SerializeToString,
            kuksa_dot_val_dot_v2_dot_val__pb2.GetValueResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetValues(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/kuksa.val.v2.VAL/GetValues',
            kuksa_dot_val_dot_v2_dot_val__pb2.GetValuesRequest.SerializeToString,
            kuksa_dot_val_dot_v2_dot_val__pb2.GetValuesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/kuksa.val.v2.VAL/Subscribe',
            kuksa_dot_val_dot_v2_dot_val__pb2.SubscribeRequest.SerializeToString,
            kuksa_dot_val_dot_v2_dot_val__pb2.SubscribeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SubscribeById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/kuksa.val.v2.VAL/SubscribeById',
            kuksa_dot_val_dot_v2_dot_val__pb2.SubscribeByIdRequest.SerializeToString,
            kuksa_dot_val_dot_v2_dot_val__pb2.SubscribeByIdResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Actuate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/kuksa.val.v2.VAL/Actuate',
            kuksa_dot_val_dot_v2_dot_val__pb2.ActuateRequest.SerializeToString,
            kuksa_dot_val_dot_v2_dot_val__pb2.ActuateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def BatchActuate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/kuksa.val.v2.VAL/BatchActuate',
            kuksa_dot_val_dot_v2_dot_val__pb2.BatchActuateRequest.SerializeToString,
            kuksa_dot_val_dot_v2_dot_val__pb2.BatchActuateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListMetadata(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/kuksa.val.v2.VAL/ListMetadata',
            kuksa_dot_val_dot_v2_dot_val__pb2.ListMetadataRequest.SerializeToString,
            kuksa_dot_val_dot_v2_dot_val__pb2.ListMetadataResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def PublishValue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/kuksa.val.v2.VAL/PublishValue',
            kuksa_dot_val_dot_v2_dot_val__pb2.PublishValueRequest.SerializeToString,
            kuksa_dot_val_dot_v2_dot_val__pb2.PublishValueResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def OpenProviderStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/kuksa.val.v2.VAL/OpenProviderStream',
            kuksa_dot_val_dot_v2_dot_val__pb2.OpenProviderStreamRequest.SerializeToString,
            kuksa_dot_val_dot_v2_dot_val__pb2.OpenProviderStreamResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetServerInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/kuksa.val.v2.VAL/GetServerInfo',
            kuksa_dot_val_dot_v2_dot_val__pb2.GetServerInfoRequest.SerializeToString,
            kuksa_dot_val_dot_v2_dot_val__pb2.GetServerInfoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
