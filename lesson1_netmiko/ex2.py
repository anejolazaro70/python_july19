from netmiko import ConnectHandler
from getpass import getpass

nxos1={"host": "nxos1",
       "username": "user",
       "password": getpass(),
       "device_type": "cisco_nxos"}
nxos2={"host": "nxos2",
       "username": "user",
       "password": getpass(),
       "device_type": "cisco_nxos"}

hosts=[nxos1, nxos2]

for h in hosts:
    ssh_con=ConnectHandler(**h)
    print(ssh_con.find_prompt())
