#!/usr/bin/env python

from jnpr.junos import Device
from jnpr_devices import srx2
from check_connected import check_connected
from gather_arp_table import gather_arp_table
from gather_routes import gather_routes
from print_output import print_output

device = Device(**srx2)
device.open()

if check_connected:
    print('NETCONF connection opened for: {}'.format(srx2.get('host')))
    arp_t = gather_arp_table(device)
    route_t = gather_routes(device)
    print_output(device, arp_t, route_t)
else:
    pprint('**** WARNING!!! CONNECTION NOT OPENED!!! ****')

device.close()
print('NETCONF connection closed for: {}'.format(srx2.get('host')))
