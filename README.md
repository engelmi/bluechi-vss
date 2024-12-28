# BlueChi to Kuksa bridge

```bash
# fetch proto files
wget -O proto/kuksa/val/v2/val.proto https://raw.githubusercontent.com/eclipse-kuksa/kuksa-databroker/refs/heads/main/proto/kuksa/val/v2/val.proto
wget -O proto/kuksa/val/v2/types.proto https://raw.githubusercontent.com/eclipse-kuksa/kuksa-databroker/refs/heads/main/proto/kuksa/val/v2/types.proto

# generate clients
python -m grpc_tools.protoc -Iproto/ --python_out=. --pyi_out=. --grpc_python_out=. proto/kuksa/val/v2/val.proto
python -m grpc_tools.protoc -Iproto/ --python_out=. --pyi_out=. --grpc_python_out=. proto/kuksa/val/v2/types.proto
```
