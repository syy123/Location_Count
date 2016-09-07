# -*- coding: utf-8 -*-
"""
Created on Thu Aug 04 12:17:40 2016

@author: Administrator
"""

import threading
from random import randint
from Queue import Queue
from time import ctime,sleep
class MyThread(threading.Thread):
    def __init__(self,func, args, name=""):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func 
        self.args = args
    def getResult(self):
        return self.res
    def run(self):
        print 'starting', self.name, 'at:',ctime()
        self.res = apply(self.func, self.args)
        print self.name, 'finished at:',ctime()
def writeQ(queue):
    print 'producing object for Q ...',
    queue.put('xxx', 1)
    print "size now",queue.qsize()
def readQ(queue):
    val = queue.get(1)
    print 'consumed object from Q ... size now:',queue.qsize()
    
def writer(queue, nloops):
    for i in range(nloops):
        writeQ(queue)
        sleep(randint(1, 3))

def reader(queue, nloops):
    for i in range(nloops):
        readQ(queue)
        sleep(randint(2, 5))
        
funcs = [writer, reader]
nfuncs = range(len(funcs))

def main():
    nloops = randint(2,5)
    q = Queue(32)
    threads = []
    
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)
    for i in nfuncs:
        threads[i].start()
    for i in nfuncs:
        threads[i].join()
    print 'all done!'

if __name__ == '__main__':
    main()