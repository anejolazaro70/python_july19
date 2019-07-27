#!/usr/bin/python
import time
from netmiko import ConnectHandler

cisco4={"host": "cisco4.lasthop.io",
       "username": "pyclass",
       "password": "88newclass",
       "device_type": "cisco_ios",
       "session_log": "cisco4_1b_ping.txt"}

ssh_con=ConnectHandler(**cisco4)

ssh_con.send_command("ping", expect_string=r'\:')
ssh_con.send_command('\n', expect_string=r'address\:')
ssh_con.send_command("8.8.8.8", expect_string=r'\:')
ssh_con.send_command('\n', expect_string=r'\n')
ssh_con.send_command('\n', expect_string=r'\n')
ssh_con.send_command('\n', expect_string=r'\n')
ssh_con.send_command('\n', expect_string=r'\n')

ssh_con.disconnect()
