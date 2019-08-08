#!/usr/bin/python

import yaml
from pprint import pprint
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse

with open('netmiko.yml', 'r') as file:
    devices=yaml.load(file)

cisco4 = devices.get('cisco4')
ssh = ConnectHandler(host=cisco4.get('host'), username=cisco4.get('username'), password=cisco4.get('password'), device_type='cisco_ios', session_log='ex6_cisco4_log.txt')
cisco4_conf = ssh.send_command('show run').splitlines()
#pprint(cisco4_conf)
#exit()

config = CiscoConfParse(cisco4_conf)
intf = config.find_objects_w_child(parentspec = r'^interface', childspec = r'^[\s]+ip address')
ipadd = config.find_objects_w_parents(parentspec = r'^interface', childspec = r'^[\s]+ip address')
table = list(zip([i.text for i in intf], [j.text for j in ipadd]))
for i in table:
    pprint('Interface Line: {0}'.format(i[0]))
    pprint('IP Address Line: {0}'.format(i[1]))
