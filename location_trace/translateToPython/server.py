# -*- coding: cp936 -*-
from socket import *
import struct
import threading

HOST = ''
PORT = 10010
ADDR = (HOST,PORT)
BUFSIZ = 1024*1024*5
server = socket(AF_INET,SOCK_STREAM)
server.bind(ADDR)
server.listen(5)
print "�ȴ�����..\n"

def process(client,addr):
    data1 = ''
    while True:           
        recvdata = client.recv(BUFSIZ)
        print recvdata[:17].encode('string-escape')
        if recvdata:
            data1=data1+recvdata
            print struct.unpack("!5s3i",recvdata[:17])
            print len(data1)
        else:
            client.close()
            print "�߳̽���"
            break

while True:
    client,addr = server.accept()
    print "���ӳɹ�..\n"
    t = threading.Thread(target = process,args = (client,addr))
    t.start()

            
