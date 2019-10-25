#!/usr/bin/python

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pprint
from getpass import getpass
from nxapi_plumbing import Device
from lxml import etree

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

nxos1 = Device(
    api_format = 'xml',
    host = 'nxos1.lasthop.io',
    username = 'pyclass',
    password = getpass(),
    transport = 'https',
    port = 8443,
    verify = False,
    )

commands = ['interface loopback 100', 'description LOOPBACK 100', 'interface loopback 199', 'description LOOPBACK 199']

output = nxos1.config_list(commands)
for out in output:
    pprint(etree.tostring(out).decode())
