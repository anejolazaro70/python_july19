#!/usr/bin/env python

from __future__ import print_function, unicode_literals
from jnpr.junos import Device
from jnpr_devices import srx2
from check_connected import check_connected
from pprint import pprint
from lxml import etree

device = Device(**srx2)
device.open()

if check_connected(device):
    print('NETCONF session openned to {}'.format(device.hostname))
    xml_out = device.rpc.get_interface_information(interface_name='fe-0/0/7', terse=True, normalize=True)
    pprint(xml_out.find('.//name').text)
    xml_out = etree.tostring(xml_out, encoding='unicode', pretty_print=True)
    pprint(xml_out)
print('Closing NETCONF session to {}'.format(device.hostname))
device.close()

