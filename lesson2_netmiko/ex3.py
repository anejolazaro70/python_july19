#!/usr/bin/python
from datetime import datetime
from netmiko import ConnectHandler
from pprint import pprint

device={"host": "cisco4.lasthop.io",
       "username": "pyclass",
       "password": "88newclass",
       "device_type": "cisco_ios",
       "session_log": "cisco4_3.txt"}

ssh_con=ConnectHandler(**device)

t1=datetime.now()
output=ssh_con.send_command('show version', use_textfsm=True)
pprint(output)
output=ssh_con.send_command("show lldp neighbors", use_textfsm=True)
pprint(output)

print('\n\nINTERFACE DE VECINO: ', output[0]['neighbor_interface'])
t2=datetime.now()
t3=t2-t1

print("\nINICIO: ", t1)
print('\nFIN: ', t2)
print('\nDuracion ejecucion comando: ', t3)
ssh_con.disconnect()
