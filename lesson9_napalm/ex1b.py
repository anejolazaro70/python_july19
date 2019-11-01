#!/usr/bin/env python

from my_devices import cisco3, arista1
from napalm import get_network_driver

def con_napalm(device):
    device_type = device.pop('device_type')
    driver = get_network_driver(device_type)
    return(driver(**device))

def main():
    print(con_napalm(cisco3))
    print(con_napalm(arista1))

if __name__ == '__main__':
    main()
