import xmltodict
from pprint import pprint

with open('show_security_zones.xml') as file:
    xmldata = file.read().strip()

my_xml = xmltodict.parse(xmldata)
pprint(my_xml)
pprint(type(my_xml))
