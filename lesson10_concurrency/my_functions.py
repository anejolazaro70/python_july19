#!/usr/bin/env python

from netmiko import ConnectHandler

def ssh_command(device, command):
    print('SSH connect to {}'.format(device.get('host')))
    try:
        ssh_con = ConnectHandler(**device)
    except:
        print('NETMIKO SSH CONNECTION FAILURE')
        exit()
    print('{} {}'.format(command, device.get('host')))
    output = ssh_con.send_command(command)
    print(output)
    ssh_con.disconnect()

def ssh_command2(device, command):
    try:
        ssh_con = ConnectHandler(**device)
    except:
        print('NETMIKO SSH CONNECTION FAILURE')
        exit()
    output = ssh_con.send_command(command)
    ssh_con.disconnect()
    return(output)

