#!/usr/bin/python
from datetime import datetime
from netmiko import ConnectHandler
from pprint import pprint
from getpass import getpass

device={"host": "cisco3",
       "username": "user",
       "password": getpass(),
       "device_type": "cisco_ios",
       "session_log": "cisco3_4.txt",
       "fast_cli": True}

comandos=['ip name-server 1.1.1.1', 'ip name-server 1.0.0.1', 'ip domain-lookup']

ssh_con=ConnectHandler(**device)

t1=datetime.now()
output=ssh_con.send_config_set(comandos)
pprint(output)

t2=datetime.now()
t3=t2-t1

print("\nINICIO: ", t1)
print('\nFIN: ', t2)
print('\nDuracion ejecucion comando: ', t3)
ssh_con.disconnect()
