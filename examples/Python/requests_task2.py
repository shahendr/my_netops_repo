import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = 'https://10.0.0.8/api/'
username = 'ignw'
password = 'ignw'

payload = '''
{
  "host": {
    "kind": "IPv4Address",
    "value": "8.8.8.8"
  },
  "kind": "object#NetworkObj",
  "name": "leGoogle",
  "objectId": "leGoogle"
}
'''

headers = {'Content-Type': 'application/json'}

resp = requests.post(f'{url}objects/networkobjects/leGoogle',
                     auth=(username,password), data=payload,
                     headers=headers, verify=False)

print(resp.status_code)
print(resp.text)
