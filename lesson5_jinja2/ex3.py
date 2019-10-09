#!/usr/bin/python

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(['./templates'])

vrfs = {'vrf_name': 'blue', 
        'rd_number': '100:1',
        'ipv4_enabled': True,
        'ipv6_enabled': True}

def main():
    template_file = 'ex3.j2'
    template = env.get_template(template_file)
    output = template.render(**vrfs)
    print(output)

main()
