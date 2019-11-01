#!/usr/bin/env python

from ex2_my_devices import cisco3, arista1, open_napalm_connection, create_backup
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
        if con.hostname == cisco3.get('hostname'):
            config = 'cisco3.lasthop.io-loopbacks'
        elif con.hostname == arista1.get('hostname'):
            config = 'arista1.lasthop.io-loopbacks'
        print(config)
        con.open()
        con.load_merge_candidate(filename=config)
        pprint(con.compare_config())
        con.commit_config()
        pprint(con.compare_config())
        con.close()

if __name__ == '__main__':
    main()
