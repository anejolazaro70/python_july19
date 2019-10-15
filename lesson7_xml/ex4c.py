from lxml import etree
from pprint import pprint

def read_xml(filename):
    my_xml = etree.parse(filename)
    return(my_xml)

def main():
    my_xml = read_xml('show_security_zones.xml')
    zone_list =  my_xml.findall('.//zones-security')
    for zone in zone_list:
        zs_name = zone.find('zones-security-zonename')
        print(zs_name.text)


if __name__ == '__main__':
    main()
