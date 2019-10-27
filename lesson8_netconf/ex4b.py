#!/usr/bin/env python

from jnpr_devices import srx2
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from gather_routes import gather_routes
from print_output import print_output
from check_connected import check_connected
from compare_lists import compare_lists

device = Device(**srx2)
device.open()
if check_connected(device):
    rtable_b = gather_routes(device)
    cfg = Config(device)
    cfg.lock()
    cfg.load(path='routes.conf', format='text', merge=True)
    print(cfg.diff())
    cfg.commit()
    rtable_a = gather_routes(device)
    print_output(device, rtable_a, 'ROUTE_TABLE')
cfg.unlock()
device.close()
