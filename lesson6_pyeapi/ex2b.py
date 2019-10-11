import pyeapi
from getpass import getpass
from my_funcs import function1, function2
from pprint import pprint

def main():
    all_table = list()
    hosts = function1('ex2b.yml')
    for host in hosts:
        print("Connecting to...", host.get('host'))
        connection = pyeapi.client.connect(**host, password=getpass())
        device = pyeapi.client.Node(connection)
        output = device.enable(['show ip arp'])
        ip_table = function2(output)
        entry = (host.get('host').split('.')[0], ip_table)
        all_table.append(entry)
    pprint(all_table)

if __name__ == '__main__':
    main()
