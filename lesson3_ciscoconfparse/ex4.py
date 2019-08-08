#!/usr/bin/python

import json
from pprint import pprint

arp = dict()
table = dict()

with open('ex4_arp.json', 'r') as file:
    arp = json.load(file)

#pprint(arp)

new_arp = arp['ipV4Neighbors']
for e in new_arp:
    table[e.get('address')]=e.get('hwAddress')
print(table)

