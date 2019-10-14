import xmltodict
from pprint import pprint

def file_to_xml(filename):
    with open(filename) as file:
        xmldata = file.read().strip()
    return(xmltodict.parse(xmldata))

def main():
    file1 = file_to_xml('show_security_zones.xml')
    file2 = file_to_xml('show_security_zones_single_trust.xml')
    pprint(file1)
    pprint(file2)

if __name__ == '__main__':
    main()
