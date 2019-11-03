#|/usr/bin/env python

from my_devices import devices
from my_functions import ssh_command
from datetime import datetime, timedelta
import threading

def main():
    hilos = []
    comando = 'show version'
    start_point = datetime.now()
    print('Inicio: {}'.format(start_point))
    for dev in devices:
        my_thread = threading.Thread(target=ssh_command, args=(dev, comando, ))
        hilos.append(my_thread)
        my_thread.start()
    for hilo in hilos:
        hilo.join()
    end_point = datetime.now()
    print('Fin: {}'.format(end_point))
    print('Process duracion: {}'.format(end_point - start_point))

if __name__ == '__main__':
    main()
