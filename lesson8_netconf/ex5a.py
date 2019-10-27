#!/usr/bin/env python

from jnpr.junos import Device
from jnpr_devices import srx2
from check_connected import check_connected
from pprint import pprint
from lxml import etree

device = Device(**srx2)
device.open()

if check_connected(device):
    print('NETCONF session openned to {}'.format(device.hostname))
    xml_out = device.rpc.get_software_information()
    pprint(etree.tostring(xml_out).decode())
print('Closing NETCONF session to {}'.format(device.hostname))
device.close()

