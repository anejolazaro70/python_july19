#!/usr/bin/python
from datetime import datetime
from netmiko import ConnectHandler
from pprint import pprint
from getpass import getpass

password=getpass()

device={"host": "cisco4.lasthop.io",
       "username": "pyclass",
       "password": password,
       'secret': password,
       "device_type": "cisco_ios",
       "session_log": "cisco4_6b.txt"}

t1=datetime.now()
ssh_con=ConnectHandler(**device)
ssh_con.config_mode()
prompt=ssh_con.find_prompt()
print(prompt)
ssh_con.disconnect()

t2=datetime.now()
t3=t2-t1

print("\nINICIO: ", t1)
print('\nFIN: ', t2)
print('\nDuracion ejecucion comando: ', t3)
