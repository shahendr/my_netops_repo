import sys
import requests

key = 'NzViNjdjMzctMDZkOC00Yzg3LWE2ODUtMmM3NzI2MWM0YmU0MWY0YjQxYjAtZmY3'
headers = {'authorization': f'Bearer {key}'}
url = 'https://api.ciscospark.com/v1/'

r = requests.get(f'{url}rooms', headers=headers)
# print(r.status_code)
# print(r.text)

room_id = ''

for room in r.json()['items']:
    if room['title'] == 'IGNW-NetOps':
        room_id = room['id']

if room_id == '':
    print('Uhoh, room doesn\'t exist :(')
    sys.exit()

# print(room_id)

data = {
    'roomId': room_id,
    'text': 'Hey, is this thing on?'
}
r = requests.post(f'{url}messages', headers=headers, data=data)
print(r.status_code)
print(r.text)
