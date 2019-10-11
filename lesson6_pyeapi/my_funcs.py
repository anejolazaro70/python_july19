import yaml

def function1(file):
    with open(file) as f:
        hosts = yaml.load(f)
    return(hosts)

def function2(output):
    arp_table = output[0]['result']['ipV4Neighbors']
    ip_table = [(entry.get('hwAddress'), entry.get('address')) for entry in arp_table]
    return(ip_table)

