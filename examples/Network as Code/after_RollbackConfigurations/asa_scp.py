#!/usr/bin/python3
"""Script to upgrade a Cisco ASA."""
import sys
from netmiko import ConnectHandler, FileTransfer


ASA_IP = sys.argv[1]
ASA_USER = sys.argv[2]
ASA_PASSWORD = sys.argv[3]
ASA_ENABLE = sys.argv[4]
BACKUP_FILE = sys.argv[5]


def asa_scp_handler(ssh_conn, cmd='ssh scopy enable', mode='enable'):
    """Enable/disable SCP on Cisco ASA."""
    if mode == 'disable':
        cmd = 'no ' + cmd
    return ssh_conn.send_config_set([cmd])


def main():
    net_device = {
        'device_type': 'cisco_asa',
        'ip': ASA_IP,
        'username': ASA_USER,
        'password': ASA_USER,
        'secret': ASA_ENABLE,
        'port': 22,
    }

    ssh_conn = ConnectHandler(**net_device)

    dest_file_system = 'disk0:'
    source_file = BACKUP_FILE
    dest_file = 'backup.cfg'

    with FileTransfer(ssh_conn, source_file=source_file, dest_file=dest_file,
                      file_system=dest_file_system) as scp_transfer:

        if scp_transfer.check_file_exists():
            ssh_conn.send_command(f'delete /noconfirm {dest_file_system}:/{dest_file}')

        if not scp_transfer.verify_space_available():
            raise ValueError("Insufficient space available on remote device")

        asa_scp_handler(ssh_conn, mode='enable')

        scp_transfer.transfer_file()

        asa_scp_handler(ssh_conn, mode='disable')

        if not scp_transfer.verify_file():
            raise ValueError("MD5 failure between source and destination files")


if __name__ == "__main__":
    main()

