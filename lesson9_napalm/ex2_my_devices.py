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

def open_napalm_connection(device):
    device_type = device.pop('device_type')
    driver = get_network_driver(device_type)
    return(driver(**device))

