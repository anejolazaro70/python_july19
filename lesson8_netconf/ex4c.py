#!/usr/bin/env python

from jnpr_devices import srx2
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from gather_routes import gather_routes
from print_output import print_output
from check_connected import check_connected
from compare_lists import compare_lists
from pprint import pprint
from clean_rtable import clean_rtable

device = Device(**srx2)
device.open()
if check_connected(device):
    rtable_b = gather_routes(device)
    #print_output(device, rtable_b, 'ROUTE_TABLE')
    cfg = Config(device)
    cfg.lock()
    cfg.load(path='routes.conf', format='text', merge=True)
    print(cfg.diff())
    cfg.commit()
    rtable_a = gather_routes(device)
    rtable_b = clean_rtable(rtable_b)
    rtable_a = clean_rtable(rtable_a)
    #print_output(device, rtable_a, 'ROUTE_TABLE')
    routes_added = compare_lists(rtable_b, rtable_a)
    print('******* ROUTES_ADDED *******')
    pprint(routes_added)
cfg.unlock()
device.close()
