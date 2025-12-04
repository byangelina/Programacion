#pip install requests

import json
import requests

url = f"https://mindicador.cl/api"
res = requests.get(url)
data = json.loads(res.text.encode("utf-8"))
dataJSON = json.dumps(data, indent=2)
print(dataJSON)
print("UTM -> " , data["utm"]["fecha"])
print("UTM valor -> " , data["utm"]["valor"])
