import napalm

username = 'ignw'
password = 'ignw'
device_ip = '10.0.0.5'

napalm_driver = napalm.get_network_driver('ios')
device = napalm_driver(hostname=device_ip,
                       username=username,
                       password=password)

device.open()
device.load_merge_candidate(filename='../my_network_as_code/acme-sea-rtr1')
print(device.compare_config())

device.close()
