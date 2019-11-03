#|/usr/bin/env python

from my_devices import devices, command_exe
from datetime import datetime, timedelta

def main():
    comando = 'show version'
    start_point = datetime()
    for dev in devices:
        command_exe(dev, comando)
    end_point = datetime()
    print('Process duracion: {}'.format(end_point - start_point))
