#|/usr/bin/env python

from my_devices import devices, ssh_command
from datetime import datetime, timedelta

def main():
    comando = 'show version'
    start_point = datetime.now()
    print('Inicio: {}'.format(start_point))
    for dev in devices:
        ssh_command(dev, comando)
    end_point = datetime.now()
    print('Fin: {}'.format(end_point))
    print('Process duracion: {}'.format(end_point - start_point))

if __name__ == '__main__':
    main()
