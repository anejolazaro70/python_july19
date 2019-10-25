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

commands = ['show interface Ethernet1/1']

output = nxos1.show('show interface Ethernet1/1')
my_xml = etree.tostring(output).decode()
my_xml = etree.fromstring(my_xml)
mtu = my_xml.find('.//eth_mtu').text
state = my_xml.find('.//state').text
intf = my_xml.find('.//interface').text 
#output = output.get('TABLE_interface').get('ROW_interface')
pprint('Interface: {0}; State: {1}; MTU: {2}'.format(intf, state, mtu))

