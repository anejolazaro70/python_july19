#!/usr/bin/python

import textfsm

keys = ["PORT_NAME", "STATUS", "VLAN", "DUPLEX", "SPEED", "PORT_TYPE"]

tpl_file = "ex2.tpl"
tpl = open(tpl_file)

with open("ex1.txt") as file:
    raw_data = file.read()
print(raw_data)
#print(type(raw_data))

re_table = textfsm.TextFSM(tpl)
#print(re_table)
#print(type(re_table))

data = re_table.ParseText(raw_data)
#print(data)
#print(type(data))


data_formated = [dict(zip(keys,i)) for i in data]
print(data_formated)
