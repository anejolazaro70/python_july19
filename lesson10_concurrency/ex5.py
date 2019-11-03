#|/usr/bin/env python

from my_devices import devices
from my_functions import ssh_command2
from datetime import datetime, timedelta
from concurrent.futures import ProcessPoolExecutor, as_completed

def main():
    start_point = datetime.now()
    print('Inicio: {}'.format(start_point))
    hilos = []
    comando = 'show version'
    max_hilos = 5
    with ProcessPoolExecutor(max_hilos) as pool:
        for dev in devices:
            hilos.append(pool.submit(ssh_command2, dev, comando))
        for hilo in as_completed(hilos):
            print(hilo.result())
    end_point = datetime.now()
    print('Fin: {}'.format(end_point))
    print('Process duracion: {}'.format(end_point - start_point))

if __name__ == '__main__':
    main()
