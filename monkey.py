#-*-coding:utf8-*-
import threading,shutil,re
import os,sys,time,tarfile
from optparse import OptionParser

__author__ = 'Virtue'
	
def runMonkeyAll(SN):
    time.sleep(1)
    os.system("adb -s %s root" % SN)
    os.system("adb -s %s remount" % SN)
    time.sleep(1)
    os.system("adb -s %s shell rm -rf /sdcard/monkeytest/" % SN)
    os.system("adb -s %s shell mkdir /sdcard/monkeytest/" % SN)
    os.system('adb -s %s shell am broadcast -a android.intent.action.MEDIA_MOUNTED -d "file:///mnt/sdcard" ' % SN)
    os.system("adb -s %s push monkeyAll.sh /data/local/tmp/ " % SN)
    os.system("adb -s %s push whitelist.txt /sdcard/ " % SN)
    os.system("adb -s %s shell chmod 777  /data/local/tmp/monkeyAll.sh " % SN)
    os.system("adb -s %s shell input swipe 500 1000 500 50 100" % SN)
    os.system("adb -s %s shell input swipe 500 1000 500 50 100" % SN)
    os.system("adb -s %s shell input swipe 500 1000 500 50 100" % SN)
    os.system("adb -s %s shell sh /data/local/tmp/monkeyAll.sh" % SN)
    return True

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
        workers.append(threading.Thread(target=runMonkeyAll, args=(sn,)))

    for worker in workers:
        worker.start()

    for worker in workers:
        worker.join()

if __name__ == '__main__':
    print ('==================================================================')
    print ('                    START monkey                            ')
    print ('============START monkey==============START monkey=============================')
    batch_flash()
