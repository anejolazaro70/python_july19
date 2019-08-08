from netmiko import ConnectHandler
from getpass import getpass

nxos1={"host": "nxos1",
       "username": "user",
       "password": getpass(),
       "device_type": "cisco_nxos",
       "session_log": "nxos1_ver.txt"}
nxos2={"host": "nxos2",
       "username": "user",
       "password": getpass(),
       "device_type": "cisco_nxos",
       "session_log": "nxos2_ver.txt"}

hosts=[nxos1, nxos2]

for h in hosts:
    ssh_con=ConnectHandler(**h)
    ssh_con.send_command("show version")
