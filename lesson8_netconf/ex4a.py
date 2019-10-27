#!/usr/bin/env python

from jnpr_devices import srx2
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from gather_routes import gather_routes
from print_output import print_output
from check_connected import check_connected

device = Device(**srx2)
device.open()
if check_connected(device):
    rtable = gather_routes(device)
    print_output(device, rtable, 'ROUTE_TABLE')
device.close()
