# -*- coding: cp936 -*-
import threading
import time

def printMessage():
    j = 0
    while j< 10:
        print "Exit"
        time.sleep(1)
        j = j+1
        
##def inputthread():
##    strings = raw_input("请输入:")
##    if(strings == "Stop"):
##        printMessage()

class runClass(threading.Thread):
    def __init__(self,t_name):
        threading.Thread.__init__(self,name=t_name)        
    def run(self):
        i = 0
        while i< 1000:
            print"运行中"
            time.sleep(1)


xxx = "asdas"
bbb = "abbbbbsdasd"
def stop():
    print bbb
    xxx = xxx +bbb
    print xxx
    
#t1 = threading.Thread(target = inputthread)
t2 = runClass('test')
#t1.start()
t2.start()
