# -*- coding: cp936 -*-
from read_bf_buffer import *
from get_scaled_csi import *
import struct
from socket import *
import numpy as np
import time
import threading

#------------------------------------dataSend FUNC-----------------------------------------------
def dataSend(countInt,bufList):
    begin = time.clock()        
    Array1 = []
    Array2 = []
    Array3 = []
    ArrayList = []
    ArrayList.append(Array1)
    ArrayList.append(Array2)
    ArrayList.append(Array3)  # 3������

    if (len(bufList[0])>=43000) and (len(bufList[0])>=43000) and (len(bufList[0])>=43000):  #�ж��ǻ����Ƿ�200����
        for index in range(len(ArrayList)):
            csi_trace = read_bf_buffer(bufList[index][:43000])  # ����һ������p���ṹ����б����������200�����ݰ���215B*200��    
            bufList[index] = bufList[index][43000:]  # ����Щ����ɾ��       
            p = len(csi_trace)
            for i in range(p/4+1):
                csi_entry = csi_trace[i*4]   # ��4*i���ṹ�壨�ֵ䣩
                csi = get_scaled_csi(csi_entry)  # 3*30 complex
                rel = np.real(csi)  # 3*30 double    
                ima = np.imag(csi)  # 3*30 double 
                x,y = np.shape(csi) # x=3 y=30
                X = 0
                sendArray = []
                while X < x:       
                    relList = rel[X].tolist()
                    imaList = ima[X].tolist()
                    sendArray = sendArray + relList + imaList  # 30��ʵ����30���鲿
                    X = X + 1
                ArrayList[index].extend(sendArray)  # 50����¼����
        ArrayLength = (len(Array1)*4+1)*len(ArrayList)   
        #------------------------------��֡�ͷ���---------------------------------------------
        sendstr = '\xff\xff\xff\xff'  # ֡ͷ
        sendstr = sendstr + '\x30'    # mode = 0
        sendstr = sendstr + struct.pack('!i',countInt)  # ��ʾ�ڼ������ݣ�ʱ��
        sendstr = sendstr + struct.pack('!i',ArrayLength)  # �����򳤶�
        sendstr = sendstr + struct.pack('!i',50)  # ÿ�������¼����
        
        sendstr = sendstr + '\x31'
        for num in Array1:
            sendstr = sendstr + struct.pack("!f",num)  # ����1����
        sendstr = sendstr + '\x32'
        for num in Array2:
            sendstr = sendstr + struct.pack("!f",num)  # ����2����
        sendstr = sendstr + '\x33'
        for num in Array3:
            sendstr = sendstr + struct.pack("!f",num)  # ����3����
            
        global clientList
        for each in clientList:
            try:
                each.send(sendstr)
            except:
                clientList.remove(each)
                print "�ͻ��˳�����..."
                each.close()
                
        countInt += 1  #ʱ���1
        
        end = time.clock()
        print "����ͷ������ݻ���:",end-begin,"\n"
        global timer  #û��global��䣬�ǲ�����Ϊ�����ں�����ı�����ֵ�ġ�
        timer = threading.Timer(1-(end-begin),dataSend,(countInt,bufList,bufListCopy))
        timer.start()
    else:
        timer = threading.Timer(1,dataSend,(countInt,bufList))
        timer.start()
               
#--------------------------------�������ݰ�--------------------------------------------------
Server_Port = 10003
Server_HOST1 = '192.168.1.101'  # ����1
Server_HOST2 = '192.168.1.102'  # ����2
Server_HOST3 = '192.168.1.107'  # ����3
APServer_HOST = '192.168.1.104'  # AP
Server_ADDR1 = (Server_HOST1,Server_Port)
Server_ADDR2 = (Server_HOST2,Server_Port)
Server_ADDR3 = (Server_HOST3,Server_Port)
APServe_ADDR = (APServer_HOST,Server_Port)
client1 = socket(AF_INET,SOCK_STREAM)
client2 = socket(AF_INET,SOCK_STREAM)
client3 = socket(AF_INET,SOCK_STREAM)
client4 = socket(AF_INET,SOCK_STREAM)
client1.connect(Server_ADDR1)
print "client1 connect to server successfully"
client2.connect(Server_ADDR2)
print "client2 connect to server successfully"
client3.connect(Server_ADDR3)
print "client3 connect to server successfully"
client4.connect(APServe_ADDR)
print "AP client connect to server successfully"     ###��Ϊ�ͻ��ˣ���Щ�׽������ڽ���4�����㷢����������


#-----------------------------stop���� ʹ����������------------------------------------
def stop():
    client1.write('Q')
    time.sleep(1)
    client2.write('Q')
    time.sleep(1)
    client3.write('Q')
    time.sleep(1)
    client4.write('Quit')
    client1.close()
    client2.close()
    client3.close()
    client4.close()
    global timer
    timer.cancel()
#------------------------------------------------------------------------------------------
buf1 =''
buf2 =''
buf3 =''
bufList = [buf1,buf2,buf3]
#-----------------------------------����buffer------------------------------------------
def readBuf(_socket,_buf):
    while True:
        recvdata = _socket.recv()
        if recvdata:
            _buf += recvdata
        elif  not recvdata:
            _socket.close()
            break
t0 = threading.Thread(target=readBuf,args=(client1,bufList[0]))
t1 = threading.Thread(target=readBuf,args=(client2,bufList[1]))
t2 = threading.Thread(target=readBuf,args=(client3,bufList[2]))
t0.start()
t1.start()
t2.start()

#-----------------------------------������------------------------------------------

HOST =''   ## ����ͬʱ���������������ڷ��ʹ����������
PORT = 10012
ADDR = (HOST,PORT)
BUFSIZE = 1024*1024*5
server = socket(AF_INET,SOCK_STREAM)
server.bind(ADDR)
server.listen(5)
clientList = []
def acceptFunc():
    while True:
        print "�ȴ�����:"
        client,addr = server.accept()
        clientList.append(client)
        print "���ӳɹ�",addr
th = threading.Thread(target = acceptFunc)
th.start()
#-----------------------------------ִ��--------------------------------------------------------        

countInt = 0  #ʱ�� ��ȫ�ֱ���
timer = threading.Timer(1,dataSend,(countInt,bufList))
timer.start()













