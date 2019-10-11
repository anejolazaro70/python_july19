import yaml
import pyeapi
from getpass import getpass

with open('ex2a.yml') as f:
    hosts = yaml.load(f)
#    print(hosts)

print(hosts)

for host in hosts:
    connection = pyeapi.client.connect(**host, password=getpass())
    device = pyeapi.client.Node(connection)
    output = device.enable(['show ip arp'])
    arp_table = output[0]['result']['ipV4Neighbors']
    ip_table = [(entry.get('hwAddress'), entry.get('address')) for entry in arp_table]

print(ip_table)
