#!/usr/bin/python

from lxml import etree

my_xml = etree.parse('show_security_zones.xml')
print(my_xml)

with open('show_security_zones.xml') as file:
    my_xml = file.read()
    print(my_xml)

my_xml = etree.fromstring(my_xml)
print(my_xml)
print(type(my_xml))
print(my_xml.tag)
print(len(my_xml.getchildren()))
print(my_xml.getchildren()[0].tag)
