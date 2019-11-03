#|/usr/bin/env python

from my_devices import devices
from my_functions import ssh_command
from datetime import datetime, timedelta
import threading

def main():
    comando = 'show version'
    start_point = datetime.now()
    print('Inicio: {}'.format(start_point))
    for dev in devices:
        my_thread = threading.Thread(target=ssh_command, args=(dev, comando, ))
        print(my_thread)
        my_thread.start()
    main_thread = threading.currentThread()
    print(threading.enumerate())
    for hilo in threading.enumerate():
        if hilo != main_thread:
            hilo.join()
    end_point = datetime.now()
    print('Fin: {}'.format(end_point))
    print('Process duracion: {}'.format(end_point - start_point))

if __name__ == '__main__':
    main()
