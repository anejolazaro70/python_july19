#!/usr/bin/python

from lxml import etree
from pprint import pprint

def read_xml(filename):
    my_xml = etree.parse(filename)
    return(my_xml)

def read_xml_text(filename):
    with open(filename, 'rb') as file:
       my_xml = file.read().strip()
    my_xml = etree.fromstring(my_xml)
    return(my_xml)

def main():
    my_xml = read_xml_text('show_version.xml')
    pprint(my_xml.nsmap)

if __name__ == '__main__':
    main()
