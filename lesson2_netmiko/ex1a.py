#!/usr/bin/python
import time
from netmiko import ConnectHandler
from getpass import getpass

cisco4={"host": "cisco4",
       "username": "user",
       "password": getpass(),
       "device_type": "cisco_ios",
       "session_log": "cisco4_1a_ping.txt"}

ssh_con=ConnectHandler(**cisco4)

ssh_con.send_command_timing("ping")
ssh_con.send_command_timing('\n')
ssh_con.send_command_timing("8.8.8.8")
ssh_con.send_command_timing('\n')
ssh_con.send_command_timing('\n')
ssh_con.send_command_timing('\n')
ssh_con.send_command_timing('\n')
ssh_con.send_command_timing('\n')

ssh_con.disconnect()
