import pexpect
import re

username = 'ignw'
password = 'ignw'
device_ip = '10.0.0.5'

connection = pexpect.spawn(f'ssh {username}@{device_ip}')
print(connection)
print(type(connection))

connection.expect('Password:')
connection.sendline(password)

print(connection.before)
print(connection.after)

connection.expect('ignw-csr#')
print(connection.before)
print(connection.after)

hostname = connection.after[:-1]
print(hostname)

connection.sendline('show run interface g1')
connection.expect('ignw-csr#')
interface_output = connection.before
print(interface_output)

print(type(interface_output))
split_output = interface_output.decode().split('\r\n')
print(split_output)


interface_description = 'N/A'

for line in split_output:
    if line.startswith('interface'):
        interface_name = line[10:]
    elif line.startswith(' ip address'):
        interface_ip_address = line[12:]
    elif line.startswith(' description'):
        interface_description = line[12:]

print(f'Interface: {interface_name}, Description: {interface_description},'
      f'IP: {interface_ip_address}')



interface_name = re.findall(rb'interface.[A-Z, a-z]*?Ethernet[^\r]*', interface_output)
interface_description = re.findall(rb'description[^\r]*', interface_output)
if not interface_description:
    interface_description.append(b'            N/A')
interface_ip_address = re.findall(rb'ip address.[0-255]{0,3}.[0-255]{0,3}.[0-255]{0,3}.[0-255]{0,3}.[0-255]{0,3}.[0-255]{0,3}.[0-255]{0,3}.[0-255]{0,3}.[0-255]{0,3}', interface_output)
print(f'Interface: {interface_name[0].decode()[10:]}, Description: {interface_description[0].decode()[12:]}, IP: {interface_ip_address[0].decode()[11:]}')
