from netmiko import ConnectHandler
from getpass import getpass

nxos1={"host": "nxos1.lasthop.io",
       "username": "pyclass",
       "password": "88newclass",
       "device_type": "cisco_nxos"}
nxos2={"host": "nxos2.lasthop.io",
       "username": "pyclass",
       "password": "88newclass",
       "device_type": "cisco_nxos"}

hosts=[nxos1, nxos2]

for h in hosts:
    ssh_con=ConnectHandler(**h)
    print(ssh_con.find_prompt())
