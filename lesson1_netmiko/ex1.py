from netmiko import ConnectHandler
from getpass import getpass

nxos1={"host": "nxos1.lasthop.io",
       "username": "pyclass",
       "password": "88newclass",
       "device_type": "cisco_nxos"}

ssh_con=ConnectHandler(**nxos1)
print(ssh_con.find_prompt())
