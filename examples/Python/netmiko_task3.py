import sys
import time
from netmiko import ConnectHandler


cisco_cloud_router = {'device_type': 'cisco_ios',
                      'ip': '10.0.0.5',
                      'username': 'ignw',
                      'password': 'ignw'}

connection = ConnectHandler(**cisco_cloud_router)

commands = ['interface loopback1',
            'description IGNW was here!',
            'ip address 8.8.4.4 255.255.255.255',
            'no shut']

connection.config_mode()

connection.send_config_set(commands)
time.sleep(2)

show_output = connection.send_command('show ip int loopback1 | i Loopback1')
if show_output.count('up') == 2:
    print('It looks like loopback1 is "up/up"! Way to go!')
else:
    print('Something went wrong... let\'s get outa here before we break something!')
    sys.exit()

print('Moving on to GigabitEthernet2...')
commands = ['interface GigabitEthernet2',
            'description This goes to the ASAv',
            'ip address 203.0.113.1 255.255.255.192',
            'no shut']

connection.send_config_set(commands)
time.sleep(2)

show_output = connection.send_command('show ip int GigabitEthernet2 | i GigabitEthernet2')
if show_output.count('up') == 2:
    print('It looks like GigabitEthernet2 is "up/up"! Keep going!')
else:
    print('Something went wrong... let\'s get outa here before we break something!')
    sys.exit()

print('Moving on to static routing...')

commands = ['ip route 10.255.255.2 255.255.255.255 203.0.113.2']

connection.send_config_set(commands)
time.sleep(2)

show_output = connection.send_command('show ip route 10.255.255.2')
if 'Network not in table' in show_output:
    print('Something went wrong... let\'s get outa here before we break something!')
    sys.exit()
else:
    print('It looks like the route made it into the table!')

connection.send_command('wr')


print('Moving on to ASA interfaces!')

asav = {'device_type': 'cisco_asa',
        'ip': '10.0.0.8',
        'username': 'ignw',
        'password': 'ignw',
        'secret': 'ignw'}
connection = ConnectHandler(**asav)

print('Starting on GigabitEthernet0/0...')

commands = ['interface GigabitEthernet0/0',
            'description Connected to CSR',
            'nameif outside',
            'security-level 0',
            'ip address 203.0.113.2 255.255.255.192',
            'no shut']

connection.send_config_set(commands)

print('Starting on GigabitEthernet0/1...')

commands = ['interface GigabitEthernet0/1',
            'description Connected to NX-OSv',
            'nameif inside',
            'security-level 100',
            'ip address 10.255.255.1 255.255.255.240',
            'no shut']

connection.send_config_set(commands)
time.sleep(2)

show_output = connection.send_command('show int ip brief | i GigabitEthernet0/0')
if show_output.count('up') == 2:
    print('It looks like GigabitEthernet0/0 is "up/up"!')
else:
    print('Something went wrong... let\'s get outa here before we break something!')
    sys.exit()
show_output = connection.send_command('show int ip brief | i GigabitEthernet0/1')
if show_output.count('up') == 2:
    print('It looks like GigabitEthernet0/1 is "up/up"!')
else:
    print('Something went wrong... let\'s get outa here before we break something!')
    sys.exit()

print('Moving on to static routing...')

commands = ['route outside 8.8.4.4 255.255.255.255 203.0.113.1']

connection.send_config_set(commands)
time.sleep(2)

show_output = connection.send_command('show route 8.8.4.4')
if 'Network not in table' in show_output:
    print('Something went wrong... let\'s get outa here before we break something!')
    sys.exit()
else:
    print('It looks like the route made it into the table!')

print('Moving on to access-list configuration...')

commands = ['access-list outside_in extended permit icmp any any',
            'access-group outside_in in interface outside']

connection.send_config_set(commands)
connection.send_command('wr')

print('Moving on to NXOSv Port')

nxosv = {'device_type': 'cisco_nxos',
         'ip': '10.0.0.6',
         'username': 'ignw',
         'password': 'ignw'}
connection = ConnectHandler(**nxosv)

commands = ['feature interface-vlan',
            'vlan 1000',
            'interface vlan1000',
            'description To ASAv',
            'ip address 10.255.255.2 255.255.255.240',
            'no shut',
            'interface Ethernet1/2',
            'switchport',
            'no shut',
            'switchport mode trunk',
            'switchport trunk native vlan 1000',
            'no shut']

connection.send_config_set(commands)
time.sleep(2)

show_output = connection.send_command('show ip int Vlan1000 | i Vlan1000')
if show_output.count('up') == 3:
    print('It looks like Vlan1000 is "up/up"! Way to go!')
else:
    print('Something went wrong... let\'s get outa here before we break something!')
    sys.exit()
show_output = connection.send_command('show int statu | i Eth1/2')
if show_output.count('connected') == 1:
    print('It looks like Eth1/2 is "up/up"! Way to go!')
else:
    print('Something went wrong... let\'s get outa here before we break something!')
    sys.exit()

print('Testing connectivity from CSR')

connection = ConnectHandler(**cisco_cloud_router)
show_output = connection.send_command('ping 10.255.255.2 source 8.8.4.4')
print(show_output)
