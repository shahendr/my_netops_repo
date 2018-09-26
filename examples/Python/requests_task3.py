import json
import ipaddress
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = 'https://10.0.0.8/api/'
username = 'ignw'
password = 'ignw'
headers = {'Content-Type': 'application/json'}

resp = requests.get(f'{url}interfaces/physical', auth=(username, password),
                    verify=False)
resp_dict = json.loads(resp.text)

netobj_dict = {}

for i in resp_dict['items']:
    if i['name'] != '':
        netobj_dict[i['name']] = []
        netobj_dict[i['name']].append(i['ipAddress']['ip']['value'])
        netobj_dict[i['name']].append(i['ipAddress']['netMask']['value'])
    else:
        pass

for k in netobj_dict:
    network = ipaddress.ip_network(f'{netobj_dict[k][0]}/{netobj_dict[k][1]}', strict=False)
    payload = f'''
{{
  "host": {{
    "kind": "IPv4Network",
    "value": "{network}"
  }},
  "kind": "object#NetworkObj",
  "name": "{k}"
}}
'''
    resp = requests.post(f'{url}objects/networkobjects/{k}',
                         auth=(username, password), data=payload,
                         headers=headers, verify=False)
    print(resp.status_code)
