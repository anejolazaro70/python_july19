#!/usr/bin/env python

import requests
import os
from urllib3.exceptions import InsecureRequestWarning
from pprint import pprint

def restAPI_get(url, http_headers):
    response = requests.get(url, headers=http_headers, verify=False)
    return response

def main():
    url = 'http://netbox.lasthop.io/api/dcim/devices/'
    token = os.environ['NETBOX_TOKEN']
    headers = {'accept': 'application/json; version=2.4;'}
    headers['Authorization'] = 'Token {}'.format(token)
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    response = restAPI_get(url, headers)
    devices = response.json()['results']
    for element in devices:
        print('-'*60)
        pprint(element['display_name'])
        print('-'*10)
        print('Location: {}'.format(element['site']['name']))
        print('Vendor: {}'.format(element['device_type']['manufacturer']['name']))
        print('Status: {}'.format(element['status']['label']))
        print('-'*60)
        print('\n'*2)

if __name__ == '__main__':
    main()
