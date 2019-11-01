#!/usr/bin/env python

from ex2_my_devices import cisco3, arista1, open_napalm_connection
from pprint import pprint

import requests 
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def main():
    conns = list()
    devices = cisco3, arista1
    for dev in devices:
        conns.append(open_napalm_connection(dev))
    print(conns)
    for con in conns:
        con.open()
        try:
            pprint(con.get_ntp_peers())
        except NotImplementedError:
            print('NTP not configured')

if __name__ == '__main__':
    main()
