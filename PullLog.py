#coding=utf8
import threading
import sys

__author__ = 'Virtue'

import time,os

def pulllog(SN):
    if os.path.exists("monkeyResult"):
        pass
    else:
        os.makedirs("monkeyResult")
    print "start pull log"
    os.system("adb -s %s pull /sdcard/monkeytest monkeyResult\\%s\\" % (SN,SN))
    print "end pull log"
    time.sleep(10)


def search_sn():
    command = 'adb devices'
    os.system(command)
    output = os.popen(command).read()
    if 'List of devices attached' in output:
        deviceslist = [device.split('\t')[0] for device in output.split('\n')[1:] if device != '']

        if len(deviceslist)>0:
            print deviceslist
            return deviceslist
        else:
            print 'no devices found, script exit'
            return False
            sys.exit()
    else:
        print ('adb status error, script exit')
        return False
        sys.exit(1)

def batch_flash():
    workers = []
    sn_list = search_sn()
    for sn in sn_list:
        workers.append(threading.Thread(target=pulllog, args=(sn,)))

    for worker in workers:
        worker.start()

    for worker in workers:
        worker.join()

if __name__ == '__main__':
    print '=================================================================='
    print '                    START BATCH FLASH                             '
    print '=================================================================='

    batch_flash()



