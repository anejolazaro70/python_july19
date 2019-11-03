#|/usr/bin/env python

from my_devices import devices
from my_functions import ssh_command2
from datetime import datetime, timedelta
from concurrent.futures import ProcessPoolExecutor, as_completed

def main():
    start_point = datetime.now()
    print('Inicio: {}'.format(start_point))
    max_hilos = 5
    with ProcessPoolExecutor(max_hilos) as pool:
        comandos = []
        for dev in devices:
            if dev['device_type'] == 'juniper_junos':
                comandos.append("show arp")
            else:
                comandos.append('show ip arp')
        results = pool.map(ssh_command2, devices, comandos)
        for result in results:
            print(result)
    end_point = datetime.now()
    print('Fin: {}'.format(end_point))
    print('Process duracion: {}'.format(end_point - start_point))

if __name__ == '__main__':
    main()
