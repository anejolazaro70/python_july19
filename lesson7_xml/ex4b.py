from lxml import etree
from pprint import pprint

def read_xml(filename):
    my_xml = etree.parse(filename)
    return(my_xml)

def main():
    my_xml = read_xml('show_security_zones.xml')
    zs =  my_xml.find('.//zones-security-zonename')
    pprint(zs.text)

if __name__ == '__main__':
    main()
