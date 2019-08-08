#!/usr/bin/python

import yaml
from pprint import pprint
from netmiko import ConnectHandler

with open('netmiko.yml', 'r') as file:
    devices=yaml.load(file)

cisco3 = devices.get('cisco3')
ssh = ConnectHandler(host=cisco3.get('host'), username=cisco3.get('username'), password=cisco3.get('password'), device_type='cisco_ios', session_log='cisco3_log.txt')
pprint(ssh.find_prompt())
