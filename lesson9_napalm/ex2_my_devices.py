#!/usr/bin/env python

from getpass import getpass
from napalm import get_network_driver

password = getpass()

cisco3 = dict(
    hostname='cisco3.lasthop.io',
    device_type='ios',
    username='pyclass',
    password=password,
    optional_args={},
)

arista1 = {
    'hostname': 'arista1.lasthop.io',
    'device_type': 'eos',
    'username': 'pyclass',
    'password': password,
    'optional_args': {'port': 443}
}

nxos1 = dict(
    hostname='nxos1.lasthop.io',
    device_type='nxos',
    username='pyclass',
    password=password,
    optional_args={'port': 8443},
)


def open_napalm_connection(device):
    device_type = device.pop('device_type')
    driver = get_network_driver(device_type)
    return(driver(**device))

def create_backup(nplm_obj):
    config = nplm_obj.get_config()
    running = config.get('running')
    filename = nplm_obj.hostname
    print(filename)
    with open(nplm_obj.hostname.split('.')[0], 'w') as file:
        file.write(running)

def create_checkpoint(nplm_obj):
    chkp = nplm_obj._get_checkpoint_file()
    filename = nplm_obj.hostname.split('.')[0] + '.ckp'
    with open(filename, 'w') as file:
        file.write(chkp)
