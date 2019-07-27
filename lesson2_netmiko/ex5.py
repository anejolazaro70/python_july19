#!/usr/bin/python
from datetime import datetime
from netmiko import ConnectHandler
from pprint import pprint

nxos1={"host": "nxos1.lasthop.io",
       "username": "pyclass",
       "password": "88newclass",
       "device_type": "cisco_nxos",
       "session_log": "nxos1_5.txt",
       "fast_cli": True}

nxos2={"host": "nxos2.lasthop.io",
       'username': 'pyclass',
       'password': '88newclass',
       'device_type': 'cisco_nxos',
       'session_log': 'nxos2_5.txt',
       'fast_cli': True}

device=[nxos1, nxos2]

t0=datetime.now()

for d in device:
    t1=datetime.now()
    ssh_con=ConnectHandler(**d)
    ssh_con.send_config_from_file('ex5_commands.txt')
    ssh_con.save_config()
    ssh_con.disconnect()
    t2=datetime.now()
    t3=t2-t1
    print("\nINICIO: ", t1)
    print('\nFIN: ', t2)
    print('\nDuracion ejecucion comando: ', t3)

tf=datetime.now()
print('\nDuracion configuracion equipos: ', tf-t0)
