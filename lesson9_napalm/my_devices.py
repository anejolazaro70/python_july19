#!/usr/bin/env python

from getpass import getpass

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

