#!/usr/bin/python
import json
from pprint import pprint

ipv4_list=[]
ipv6_list=[]

with open('ex3_nxos.json', 'r') as file:
    nxos_dev = json.load(file)

for v in nxos_dev.values():
    if v.get('ipv4'):
        ipv4_list.append(v['ipv4'])
    if v.get('ipv6'):
        ipv6_list.append(v['ipv6'])
pprint(ipv4_list)
pprint(ipv6_list)

