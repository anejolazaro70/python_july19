#!/usr/bin/env python

from ex2_my_devices import cisco3, arista1, open_napalm_connection

import requests 
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def main():
    conns = list()
    devices = cisco3, arista1
    for dev in devices:
        conns.append(open_napalm_connection(dev))
    print(conns)

if __name__ == '__main__':
    main()
