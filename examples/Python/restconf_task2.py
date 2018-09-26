import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

username = 'ignw'
password = 'ignw'
url = "https://10.0.05/restconf"
headers = {'content-type': 'application/yang-data+json',
           'accept': 'application/yang-data+json'}
endpoint = '/data/Cisco-IOS-XE-native:native/interface/'
data = {
'Cisco-IOS-XE-native:Loopback': {
    'name': 2,
    'description': 'RESTCONNFFFFF WHY IS IT  YELLING!',
    'ip': {
        'address': {
            'primary': {
                'address': '172.16.1.2',
                'mask': '255.255.255.255'
                }
            }
        }
    }
}
resp = requests.post(f'{url}/{endpoint}',
                     auth=(username, password), headers=headers,
                     verify=False, data=json.dumps(data))
print(resp.status_code)
print(resp.text)
