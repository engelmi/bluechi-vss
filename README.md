# BlueChi to Kuksa bridge

```bash
# generate clients
python -m grpc_tools.protoc -Isubmodule/kuksa/proto/ --python_out=./bluechi2kuksa/ --pyi_out=./bluechi2kuksa/ --grpc_python_out=./bluechi2kuksa/ submodule/kuksa/proto/kuksa/val/v2/val.proto
python -m grpc_tools.protoc -Isubmodule/kuksa/proto/ --python_out=./bluechi2kuksa/ --pyi_out=./bluechi2kuksa/ --grpc_python_out=./bluechi2kuksa/ submodule/kuksa/proto/kuksa/val/v2/types.proto

# generate vss with BlueChi model
vspec export json --vspec spec/bluechi.vspec -o spec/bluechi.json

# build kuksa-databroker with latest vss.json
podman build -f container/kuksa-databroker -t kuksa-databroker-with-bluechi .
```
