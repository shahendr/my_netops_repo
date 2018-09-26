import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = 'https://10.0.0.8/api/'
username = 'ignw'
password = 'ignw'

resp = requests.get(f'{url}objects/networkobjects', auth=(username, password),
                    verify=False)
print(resp)
print(resp.status_code)
print(dir(resp))

resp = requests.get(f'{url}interfaces/physical', auth=(username, password),
                    verify=False)
resp_dict = json.loads(resp.text)
print(resp_dict)

ints_qty = resp_dict['rangeInfo']['total']
ints_names = []

for i in resp_dict['items']:
    ints_names.append(i['hardwareID'])

print(f'The ASAv has {ints_qty} interfaces. Named as follows: ')
print(ints_names)
