import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

username = 'ignw'
password = 'ignw'
url = "https://10.0.0.5/restconf"
headers = {'content-type': 'application/yang-data+json',
           'accept': 'application/yang-data+json'}

resp = requests.get(url, auth=(username, password), headers=headers,
                    verify=False)
print(resp.status_code)
print(resp.text)

resp = requests.get(f'{url}/data/Cisco-IOS-XE-native:native?content=config',
                    auth=(username, password), headers=headers,
                    verify=False)
print(resp.status_code)
print(resp.text)

resp = requests.get(f'{url}/data/Cisco-IOS-XE-native:native/interface/Loopback',
                 auth=(username, password), headers=headers,
                 verify=False)
print(resp.status_code)
print(resp.text)
