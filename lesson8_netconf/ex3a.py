#!/usr/bin/env python

from jnpr_devices import srx2
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from check_connected import check_connected

device = Device(**srx2)
device.open()
if check_connected:
    print('NETCONF session OPENNED to {} from USER {}'.format(device.hostname, device.user))
    cfg = Config(device)
    cfg.lock()
    #cfg.lock()
    try:
        cfg.lock()
    except 'LockError':
        print('Session locked yet')
        pass
#cfg.unlock()
#device.close()
