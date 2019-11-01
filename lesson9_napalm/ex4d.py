#!/usr/bin/env python

from ex2_my_devices import cisco3, arista1, nxos1, open_napalm_connection, create_backup, create_checkpoint
from pprint import pprint

import requests 
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def main():
    device = open_napalm_connection(nxos1)
    device.open()
    create_checkpoint(device)
    device.load_replace_candidate(filename='ex4c_nxos1.cfg')
    pprint(device.compare_config())
    device.discard_config()
    pprint(device.compare_config())

if __name__ == '__main__':
    main()
