#!/usr/bin/env python
from pprint import pprint

def print_output(device, table1, table2):
    pprint('hostname: {}'.format(device.hostname))
    pprint('netconf port: {}'.format(device.port))
    pprint('user: {}'.format(device.user))
    pprint('***** ARP_TABLE *****')
    pprint(table1)
    pprint('***** ROUTE_TABLE *****')
    pprint(table2)
