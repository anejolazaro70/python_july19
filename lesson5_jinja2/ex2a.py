#!/usr/bin/python

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(['./templates'])

# nxos1 = {'interface': 'Ethernet1/1', 'ip_address': '10.1.100.1', 'netmask': '/24'}
# nxos2 = {'interface': 'Ethernet1/1', 'ip_address': '10.1.100.2', 'netmask': '/24'}


devices = [{'name': 'nxos1',
            'interface':'Ethernet1/1', 
            'ip_address':'10.1.100.1',
            'netmask':'/24'},
           {'name': 'nxos2',
            'interface':'Ethernet1/1',
            'ip_address':'10.1.100.2',
            'netmask': '/24'}]

for device in devices:
    template_file = 'ex2a.j2'
    template = env.get_template(template_file)
    output = template.render(**device)
    print(output)
    print("")

