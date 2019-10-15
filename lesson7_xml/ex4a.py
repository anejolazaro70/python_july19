from lxml import etree
from pprint import pprint

def read_xml(filename):
    my_xml = etree.parse(filename)
    return(my_xml)

def main():
    my_xml = read_xml('show_security_zones.xml')
    zs =  my_xml.find('zones-security')
    pprint(zs.tag)
    pprint(zs.getchildren())
    for child in zs.getchildren():
        print(child.tag)


if __name__ == '__main__':
    main()
