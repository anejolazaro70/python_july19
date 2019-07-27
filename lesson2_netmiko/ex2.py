#!/usr/bin/python
from datetime import datetime, timedelta
from netmiko import ConnectHandler

device={"host": "nxos2.lasthop.io",
       "username": "pyclass",
       "password": "88newclass",
       "device_type": "cisco_ios",
       "session_log": "nxos2_2.txt",
       "global_delay_factor": 2}

ssh_con=ConnectHandler(**device)

t1=datetime.now()
output=ssh_con.send_command("show lldp neighbors detail")
t2=datetime.now()
t3=t2-t1

print(output)
print("\nINICIO: ", t1)
print('\nFIN: ', t2)
print('\nDuracion ejecucion comando: ', t3)
ssh_con.disconnect()
