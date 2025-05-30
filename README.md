# Execution

before anythin start your llama.cpp server with embedding => e.g. 

```bash
llama-server -m /root/hf_models/embeddings/magicunicorn/mxbai-embed-large-v1/mxbai-embed-large-v1-q8_0.gguf -c 512 --port 8081
```

Notice the port 8081, this is not default port of llama.cpp. I use it because I run this embedding as a separate instance to have it always available for roo code extension.

then run the api server

```python
python api_server.py
```
