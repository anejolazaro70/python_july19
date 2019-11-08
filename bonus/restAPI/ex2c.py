import requests
from urllib3.exceptions import InsecureRequestWarning
from pprint import pprint


def url_get(url, http_headers):
    response = requests.get(url, headers=http_headers, verify=False)
    return response

def main():
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    url= 'https://netbox.lasthop.io/api/dcim/'
    http_headers = {}
    http_headers['Accept'] = 'application/json; version=2.4;'
    response = url_get(url, http_headers)
    pprint('HTTP status code {}'.format(response.status_code))
    pprint(response.json())
    pprint(response.headers)

if __name__ == '__main__':
    main()
