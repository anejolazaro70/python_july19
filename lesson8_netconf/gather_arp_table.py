#!/usr/bin/env python
from jnpr.junos.op.arp import ArpTable

def gather_arp_table(device):
    arp_table = ArpTable(device)
    arp_entries = arp_table.get()
    return(arp_entries.items())
    #return(arp_table)
