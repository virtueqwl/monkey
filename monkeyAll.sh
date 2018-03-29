#!/usr/bin/env bash
echo "start monkey"
echo "get log"
logcat -d -v threadtime > /sdcard/monkeytest/logcat.txt &
monkey --pkg-whitelist-file /sdcard/whitelist.txt   -s $RANDOM --throttle 300 --ignore-crashes --ignore-timeouts --ignore-native-crashes -v -v -v 100000 2>/sdcard/monkeytest/error.txt 1>/sdcard/monkeytest/info.txt
echo "end monkey"
logcat -d -b radio -v threadtime > /sdcard/monkeytest/radio.txt
logcat -d -b events -v threadtime > /sdcard/monkeytest/events.txt
logcat -d -b system -v threadtime > /sdcard/monkeytest/system.txt
getprop > /sdcard/monkeytest/props.txt
env > /sdcard/monkeytest/env.txt
dmesg > /sdcard/monkeytest/dmesg.txt
cat /proc/last_kmsg > /sdcard/monkeytest/last_kmsg.txt
cat /sys/fs/pstore/console-ramoops > /sdcard/monkeytest/console-ramoops
ps > /sdcard/monkeytest/ps.txt
ps -t > /sdcard/monkeytest/ps_t.txt
top -n 1 -t > /sdcard/monkeytest/top_t.txt
tinymix > /sdcard/monkeytest/tinymix.txt
cat /proc/cmdline > /sdcard/monkeytest/cmdline.txt
ls -lR /data  > /sdcard/monkeytest/userdata_check.txt   
echo 1 > /proc/sys/kernel/sysrq
echo w > /proc/sysrq-trigger
dmesg > /sdcard/monkeytest/dmesg_sysrq_blocked_tasks.txt
dumpsys power> /sdcard/monkeytest/power.txt
dmesg > /sdcard/monkeytest/dmesg_sysrq.txt
echo "getting screenshot ..." 
screencap -p   /sdcard/monkeytest/screenshot.png
echo "getting bugreport ... "
bugreport > /sdcard/monkeytest/bugreport.txt
echo "getting dropbox,anr,tombstones,logd...."
cp -fr /data/system/dropbox /sdcard/monkeytest/dropbox
cp -fr /data/anr /sdcard/monkeytest/anr
cp -fr /data/tombstones /sdcard/monkeytest/tombstones
cp -fr /data/misc/logd /sdcard/monkeytest/logd
cp -fr /data/zslogs  /sdcard/monkeytest/zslogs
cp -fr /data/cplc_info /sdcard/monkeytest/cplc
cp -fr /sdcard/logs /sdcard/monkeytest/offlinelogs
cp -fr /sdcard/tcpdump /sdcard/monkeytest/tcpdump
echo "doooooooooone\n"
exit
