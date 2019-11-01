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

if __name__ == '__main__':
    main()
