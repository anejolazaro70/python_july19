#!/usr/bin/python

import yaml
from pprint import pprint

devices = [{'name': 'cisco3', 'hostname': 'cisco3', 'username': 'user', 'password': 'pass'},
           {'name': 'cisco4', 'hostname': 'cisco4', 'username': 'user', 'password': 'pass'},
           {'name': 'arista1', 'hostname': 'arista1', 'username': 'user', 'password': 'pass'},
           {'name': 'arista2', 'hostname': 'arista2', 'username': 'user', 'password': 'pass'}]

#pprint(devices)

with open('devices.yml', 'w') as file:
    yaml.dump(devices,file, default_flow_style=False)
print(file)
