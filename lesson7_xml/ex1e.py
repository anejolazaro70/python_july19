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
# el root de un elemento esta identificado por la etiqueta del elemento
print(my_xml.tag)
print(len(my_xml.getchildren()))
print(my_xml.getchildren()[0].tag)
# nos posicionamos en el primer hijo del raiz
trust_zone = my_xml.getchildren()[0]
# dos formas de obtener la misma informacion
print(trust_zone.getchildren()[0].text)
print(trust_zone.find('zones-security-zonename').text)
