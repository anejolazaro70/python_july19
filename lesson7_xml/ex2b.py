import xmltodict
from pprint import pprint

with open('show_security_zones.xml') as file:
    xmldata = file.read().strip()

my_xml = xmltodict.parse(xmldata)
pprint(my_xml)
my_xml = my_xml['zones-information']['zones-security']
i = 1
for zone in my_xml:
    print('Security Zone "#"{0}: {1}'.format(i, zone.get('zones-security-zonename')))
    i = i+1
