import pyeapi
from pprint import pprint
from getpass import getpass

hosts = [{'host': 'arista3.lasthop.io',
         'username': 'pyclass',
         'password': getpass(),
         'port': '443',
         'transport': 'https'},
         {'host': 'arista4.lasthop.io',
         'username': 'pyclass',
         'password': getpass(),
         'port': '443',
         'transport': 'https'}]

all_table = list()

for host in hosts:
    connection = pyeapi.client.connect(**host)
    device = pyeapi.client.Node(connection)
    output = device.enable(["show ip arp"])
    arp_table = output[0]['result']['ipV4Neighbors']
    ip_arp = [(entry.get('hwAddress'), entry.get('address')) for entry in arp_table]
    #print(type(all_table))
    all_table.append({host.get('host').split('.')[0]:ip_arp})
    #print(all_table)

pprint(all_table)
