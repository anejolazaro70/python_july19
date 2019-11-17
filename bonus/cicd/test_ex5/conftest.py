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
def netmiko_conn(request):
    conn = ConnectHandler(**arista1)
    def fin():
        conn.disconnect()
    request.addfinalizer(fin)
    return conn
