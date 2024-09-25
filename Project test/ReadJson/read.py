import json
import base64
# 讀取 JSON 數據
with open('data.json', 'r') as f:
    data = json.load(f)

#print(json.loads('{"data": "dsadas"}')['data'])

# print data
newdata = json.loads(data[0]['data'][0])['data']

decode_bytes = base64.b64decode(newdata)

#print(decode_bytes)
with open('output.png', 'wb') as f:
    f.write(decode_bytes)
