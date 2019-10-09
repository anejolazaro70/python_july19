#!/usr/bin/python

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from netmiko import ConnectHandler
from my_devices import nxos1, nxos2

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(['./templates'])

devices = [{'name': 'nxos1',
            'interface':'Ethernet1/1', 
            'ip_address':'10.1.100.1',
            'netmask':'/24',
            'local_as': 22,
            'peer_ip': '10.1.100.2'},
           {'name': 'nxos2',
            'interface':'Ethernet1/1',
            'ip_address':'10.1.100.2',
            'netmask': '/24',
            'local_as': 22,
            'peer_ip': '10.1.100.1'}]

connects = [nxos1, nxos2]


def wr_file(file,name):
    file_config = name + '.txt'
    with open(file_config,'w') as f:
        f.writelines(file)

def gen_config(equipos): 
    for device in equipos:
        template_file = 'ex2c.j2'
        template = env.get_template(template_file)
        output = template.render(**device)
        wr_file(output, device['name'])

def wr_config(equipos):
    for device in equipos:
        file_cfg = device['host'].split('.')[0] + '.txt'
        ssh_con = ConnectHandler(**device)
        ssh_con.send_config_from_file(config_file=file_cfg)
        ssh_con.exit_config_mode()
        ssh_con.disconnect()

def main():
    gen_config(devices)
    wr_config(connects)

if __name__ == '__main__':
    main()
