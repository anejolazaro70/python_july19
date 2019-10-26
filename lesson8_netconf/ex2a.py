#!/usr/bin/env python

from jnpr.junos import Device
from jnpr_devices import srx2
from pprint import pprint

device = Device(**srx2)
device.open()

pprint(device.facts.get('hostname'))
