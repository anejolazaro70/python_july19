#!/usr/bin/env python

import requests
import os
from urllib3.exceptions import InsecureRequestWarning
from pprint import pprint
import json

def restAPI_get(url, http_headers):
    response = requests.get(url, headers=http_headers, verify=False)
    return response

def restAPI_post(url, http_headers, datos):
    response = requests.post(url, headers=http_headers, data=json.dumps(datos), verify=False)
    return response

def main():
    url = 'http://netbox.lasthop.io/api/ipam/ip-addresses/'
    token = os.environ['NETBOX_TOKEN']
    headers = {}
    headers['Content-Type'] = 'application/json; version=2.4;'
    headers['accept'] = 'application/json; version=2.4;'
    headers['Authorization'] = 'Token {}'.format(token)
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    data = {'address': '192.0.2.134/32'}
    response = restAPI_post(url, headers, data)
    pprint('Status code: {}'.format(response.status_code))
    pprint('Elapsed time: {}'.format(response.elapsed))
    addresses = response.json()['results']
    for address in addresses: 
        if address['address'] == '192.0.2.133/32':
            id = address['id']    
    print(id)
    new_url = 'https://netbox.lasthop.io/api/ipam/ip-addresses/' + str(id) + '/'
    response = restAPI_get(new_url, headers)
    pprint(response.json())
    """
    if response.status_code == 200:
        addresses = response.json()['results']
        for address in addresses:
            print('-'*60)
            print('Address: {}'.format(address['address']))
            print('Created: {}'.format(address['created']))
            print('-'*60)
    else:
        print('REST API operation status code: {}'.format(response.status_code))
        print('Fallo en operacion REST-API')
    """

if __name__ == '__main__':
    main()
