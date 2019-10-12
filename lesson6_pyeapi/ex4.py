import pyeapi
from getpass import getpass
from my_funcs import function1, function2, function3
from pprint import pprint

def main():
    hosts = function1('ex4.yml')
    for host in hosts:
        cfg = function3(host.get('data'))
        print("Connecting to...", host.get('host'))
        connection = pyeapi.client.connect(**host, password=getpass())
        device = pyeapi.client.Node(connection)
        device.api('ipinterfaces').delete(host.get('data')['intf_name'])
        device.api('ipinterfaces').create(host.get('data')['intf_name'])
        device.api('ipinterfaces').set_address(host.get('data')['intf_name'], value = host.get('data')['intf_ip']+'/'+str(host.get('data')['intf_mask']))
        intf_ip = device.enable('show ip interface brief')
        output = function2(intf_ip)
        pprint(output)

if __name__ == '__main__':
    main()
