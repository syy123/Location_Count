# -*- coding: utf-8 -*-
"""
Created on Thu Aug 04 15:10:13 2016

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

def fib(x):
    sleep(0.005)
    if x < 2:
        return 1
    return (fib(x-2)+fib(x-1))
def fac(x):
    sleep(0.1)
    if x < 2:
        return 1
    return (x * fac(x-1))
def sum1(x):
    sleep(0.2)
    if x < 2:
        return 1
    return (x + sum1(x-1))
    
funcs = [fib, fac, sum1]
n = 12

def main():
    nfuncs = range(len(funcs))
    
    print '***singel thread'
    for i in nfuncs:
        print 'starting',funcs[i].__name__,'at:',ctime()
        print funcs[i](n)
        print funcs[i].__name__,'finished at:',ctime
    
    print '***multiple thread'
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i],(n,),funcs[i].__name__)
        threads.append(t)
    for i in nfuncs:
        threads[i].start()
    for i in nfuncs:
        threads[i].join()
        print threads[i].getResult()
    print 'all done'

if __name__ == '__main__':
    main()
        