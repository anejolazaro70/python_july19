#!/usr/bin/env python

import pytest
from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

arista1 = {
    "host": "arista1.lasthop.io",
    "device_type": "arista_eos",
    "username": "pyclass",
    "password": password,
    }

@pytest.fixture(scope="module")
def netmiko_conn():
    conn = ConnectHandler(**arista1)
    return conn

def test_netmiko_con(netmiko_conn):
    assert "arista1" in netmiko_conn.find_prompt()

def test_show_version(netmiko_conn):
    assert "4.20.10M" in netmiko_conn.send_command("show version")
