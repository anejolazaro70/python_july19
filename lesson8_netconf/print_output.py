#!/usr/bin/env python
from pprint import pprint

def print_output(device, table, descr):
    pprint('hostname: {}'.format(device.hostname))
    pprint('netconf port: {}'.format(device.port))
    pprint('user: {}'.format(device.user))
    pprint('***** {} *****'.format(descr))
    pprint(table)
