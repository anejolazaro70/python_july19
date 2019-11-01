#!/usr/bin/env python

from my_devices import cisco3, arista1
from napalm import get_network_driver
from pprint import pprint
import requests 
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def con_napalm(device):
    device_type = device.pop('device_type')
    driver = get_network_driver(device_type)
    return(driver(**device))

def main():
    conns = list()
    devices = cisco3, arista1
    for dev in devices:
        conns.append(con_napalm(dev))
    print(conns)
    for con in conns:
        print(con)
        con.open()
        pprint(con.get_facts())
        con.close()

if __name__ == '__main__':
    main()
