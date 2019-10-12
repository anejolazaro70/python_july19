import yaml
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment


def function1(file):
    with open(file) as f:
        hosts = yaml.load(f)
    return(hosts)

def function2(output):
    table = list()
    if output[0].get('command') == 'show ip arp':
        arp_table = output[0]['result']['ipV4Neighbors']
        table = [(entry.get('hwAddress'), entry.get('address')) for entry in arp_table]
    elif output[0].get('command') == 'show ip route':
        vrf_default_iproute_table = output[0]['result']['vrfs']['default']['routes']
        for key,value in vrf_default_iproute_table.items():
            if value['routeType'] == 'static':
                entry = (key, value['routeType'], value['vias'][0]['nexthopAddr'])
            else:
                entry = (key, value['routeType'])
            table.append(entry)
    elif output[0].get('command') == 'show ip interface brief':
        table = output[0]['result']['output']
    return(table)

def function3(dict_cfg):
    env = Environment(undefined = StrictUndefined)
    env.loader = FileSystemLoader('./templates')
    template_file = 'intf.j2'
    template = env.get_template(template_file)
    return(template.render(**dict_cfg))
