import pyeapi
from pprint import pprint
from getpass import getpass

hosts = {'host': 'arista3.lasthop.io',
         'username': 'pyclass',
         'password': getpass(),
         'port': '443',
         'transport': 'https'}

connection = pyeapi.client.connect(**hosts)

device = pyeapi.client.Node(connection)
output = device.enable(["show ip arp"])
arp_table = output[0]['result']['ipV4Neighbors']

ip_arp = [(entry.get('hwAddress'), entry.get('address')) for entry in arp_table]

pprint(ip_arp)
