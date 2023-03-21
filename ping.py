#!/usr/bin/python
import subprocess
import sys
import time
import datetime

ping_path = '/bin/ping'

if len(sys.argv) != 5:
    print('usage: hostname timeout interval count')

if len(sys.argv) == 5:
    host = sys.argv[1]
    timeout = float(sys.argv[2])
    interval = float(sys.argv[3])
    count = int(sys.argv[4])
    success = 0
    failed = 0
    sys.stdout.write(f'Sending {count} Ping Packets to {host}\n')
    start = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
    for i in range(count):
        res = subprocess.run([ping_path, host, '-c 1', f'-W {timeout}'], stdout=subprocess.PIPE)
        ping_res = res.stdout.decode('utf-8')
        if '100% packet loss' in ping_res:
            sys.stdout.write('!')
            failed += 1
        else:
            sys.stdout.write('.')
            success += 1
        sys.stdout.flush()
        time.sleep(interval)
    stop = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
    diff = datetime.datetime.strptime(stop,"%m/%d/%Y %H:%M:%S") - datetime.datetime.strptime(start,"%m/%d/%Y %H:%M:%S")
    print('\n\033[1mSuccess = {}% | Loss = {}%'.format(success * 100 / count, failed * 100 / count))
    print('Send packets: {}\nLoss packets: {}\033[0m'.format(success, failed))
    print('{} - {} ({})'.format(start, stop, diff))
