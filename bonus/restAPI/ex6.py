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

def restAPI_put(url, http_headers, datos):
    pprint(url)
    pprint(http_headers)
    pprint(datos)
    response = requests.put(url, headers=http_headers, data=json.dumps(datos), verify=False)
    return response

def restAPI_del(url, http_headers):
    response = requests.delete(url, headers=http_headers, verify=False)
    return response

def main():
    url = 'http://netbox.lasthop.io/api/ipam/ip-addresses/'
    token = os.environ['NETBOX_TOKEN']
    headers = {}
    headers['Content-Type'] = 'application/json; version=2.4;'
    headers['accept'] = 'application/json; version=2.4;'
    headers['Authorization'] = 'Token {}'.format(token)
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    new_url = 'https://netbox.lasthop.io/api/ipam/ip-addresses/73/'
    response = restAPI_get(new_url, headers)
    pprint(response.json())
    response = restAPI_del(new_url, headers)
    pprint(response.status_code)
    pprint(response.json())

if __name__ == '__main__':
    main()
