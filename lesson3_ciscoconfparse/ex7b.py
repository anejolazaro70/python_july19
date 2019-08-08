#!/usr/bin/python

from ciscoconfparse import CiscoConfParse
import re

with open('ex7_bgp_conf.txt', 'r') as file:
    conf = file.readlines()

bgp_conf = [i.rstrip() for i in conf]
config = CiscoConfParse(bgp_conf)
neighbor = config.find_objects_w_child(parentspec = r'^[\s]+neighbor', childspec = r'^[\s]+remote-as')
remote_as = config.find_objects_w_parents(parentspec = r'^[\s]+neighbor', childspec = r'^[\s]+remote-as')

new_nb = [i.text for i in neighbor]
new_as = [i.text for i in remote_as]

ip = re.compile(r'[0-9]+\.[0-9]+\.+[0-9]+\.[0-9]+')
ra = re.compile(r'[0-9]+')

table = list(zip([ip.search(i).group(0) for i in new_nb], [ra.search(j).group(0) for j in new_as]))

print(table)
