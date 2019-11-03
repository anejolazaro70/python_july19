#!/usr/bin/env python

from getpass import getpass
from sys import exit

password = getpass()

cisco3 = dict(
    host= 'cisco3.lasthop.io',
    username= 'pyclass',
    password= password,
    device_type= 'cisco_ios',
)

arista1 = dict(
    host= 'arista1.lasthop.io',
    username= 'pyclass',
    password= password,
    global_delay_factor= 4,
    device_type= 'arista_eos',
)

arista2 = dict(
    host= 'arista2.lasthop.io',
    username= 'pyclass',
    password= password,
    global_delay_factor= 4,
    device_type= 'arista_eos',
)

srx2 = dict(
    host= 'srx2.lasthop.io',
    username= 'pyclass',
    password= password,
    device_type= 'juniper_junos'
)

devices = cisco3, arista1, arista2, srx2
