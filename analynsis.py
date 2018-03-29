#coding=utf-8
import threading
import sys
import time,os
import re, csv
from write_excel import write_excel as wrex


def analysis():
    contents = []
    filelist=os.listdir("./monkeyResult")
    for erraddress in filelist:
        listfile1=os.listdir("./monkeyResult/"+erraddress+"/")
        for lili in listfile1:
            fl2 = []
            matchObi = re.match( r'error.*', lili)
            if matchObi:
               fl2.append(matchObi.group())
            for mon in fl2:
                arr_err1 = []
                milk = open("./monkeyResult/"+erraddress+"/"+mon,"r") 
                meat = milk.readlines()
                for infoo in meat:
                    matchObk = re.match( r'\/\/\s(CRASH\:\s\S*)', infoo)              #crash
                    if matchObk:
                        arr_err1.append(matchObk.group(1))
                    matchObm = re.match( r'\/\/\sShort\sMsg\:\s(Native\scrash)', infoo) #Native crash
                    if matchObm:
                        print (matchObm.group(1))
                        arr_err1[-1] = arr_err1[-1].replace('CRASH','Native crash')
                for infoo in meat:
                    matchObl = re.match( r'ANR\sin\s\S*', infoo)                        #ANR
                    if matchObl:
                        arr_err1.append(matchObl.group())
                        arr_err1[-1] = arr_err1[-1].replace(' in',':')
                mysets = sorted(set(arr_err1))
                for item in mysets:
                    tt=arr_err1.count(item)
                    tem='%d' %tt
                    cont = [erraddress,item,tem]
                    contents.append(cont) 
                milk.close()
         				
    wrex(contents)
    #send_email(contents,"path")
def main():
    os.system("pause")
    analysis()

if __name__ == '__main__':
    print ('==================================================================')
    print ('                    analysis                            ')
    print ('==================================================================')
    main()
