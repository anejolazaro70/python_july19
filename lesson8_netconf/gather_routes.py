#!/usr/bin/env python
from jnpr.junos.op.routes import RouteTable

def gather_routes(device):
    route_table = RouteTable(device)
    route_entries = route_table.get()
    return(route_entries.items())
    #return(route_table)
