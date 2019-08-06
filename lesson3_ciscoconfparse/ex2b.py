#!/usr/bin/python

import yaml
from pprint import pprint

devices = [{'name': 'cisco3', 'hostname': 'cisco3.lasthop.io', 'username': 'pyclass', 'password': '88newclass'},
           {'name': 'cisco4', 'hostname': 'cisco4.lasthop.io', 'username': 'pyclass', 'password': '88newclass'},
           {'name': 'arista1', 'hostname': 'arista1.lasthop.io', 'username': 'pyclass', 'password': '88newclass'},
           {'name': 'arista2', 'hostname': 'arista2.lasthop.io', 'username': 'pyclass', 'password': '88newclass'}]

#pprint(devices)

with open('devices.yml', 'w') as file:
    yaml.dump(devices,file, default_flow_style=False)
print(file)
