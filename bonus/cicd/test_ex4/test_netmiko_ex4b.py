#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

arista1 = {
    "host": "arista1.lasthop.io",
    "device_type": "arista_eos",
    "username": "pyclass",
    "password": getpass(),
    }

def netmiko_conn(**kwargs):
    conn = ConnectHandler(**kwargs)
    return conn

def test_netmiko_conn(**kwargs):
    conn = netmiko_conn(**arista1)
    assert "arista1" in conn.find_prompt()
