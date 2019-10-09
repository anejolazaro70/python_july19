#!/usr/bin/python

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(['./templates'])

vrfs_list = [{'vrf_name': 'blue',
        'rd_number': '100:1',
        'ipv4_enabled': True,
        'ipv6_enabled': False},
        {'vrf_name': 'jose',
         'rd_number': '100:2',
         'ipv4_enabled': True,
         'ipv6_enabled': True},
        {'vrf_name': 'red',
         'rd_number': '200:1',
         'ipv4_enabled': False,
         'ipv6_enabled': True}]

vrfs = {'vrfs_list': vrfs_list}

def main():
    template_file = 'ex4.j2'
    template = env.get_template(template_file)
    output = template.render(**vrfs)
    print(output)

main()
