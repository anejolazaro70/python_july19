def test_prompt(netmiko_conn):
    assert "arista1" in netmiko_conn.find_prompt()

def test_show_version(netmiko_conn):
    assert "4.20.10M" in netmiko_conn.send_command("show version")
