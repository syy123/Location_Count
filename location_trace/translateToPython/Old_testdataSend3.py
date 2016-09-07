# -*- coding: cp936 -*-
from read_bf_buffer import *
from get_scaled_csi import *
import struct
from socket import *
import numpy as np
import time
import threading

##########################################################
################      ������ģ��       #####################
##########################################################

#------------------------------------dataSend FUNC-----------------------------------------------
def dataSend(countInt,bufList,bufListCopy):
    begin = time.clock()        
    Array1 = []
    Array2 = []
    Array3 = []
    ArrayList = []
    ArrayList.append(Array1)
    ArrayList.append(Array2)
    ArrayList.append(Array3)  # 3������
    if (len(bufList[0])>=43000) and (len(bufList[1])>=43000) and (len(bufList[2])>=43000):
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
        sendstr = sendstr + '\x30'    # mode 
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
        tcpClient.send(sendstr)
       # print len(sendstr)
        countInt += 1  #ʱ���1

        end = time.clock()
        print "����ͷ������ݻ���:",end-begin,"\n"
        global timer
        timer = threading.Timer(1-(end-begin),dataSend,(countInt,bufList,bufListCopy))
        timer.start()
        
    else:           ###�����ڲ��ԣ�ѭ��####
        bufList = list(bufListCopy)
        dataSend(countInt,bufList,bufListCopy)
    
#--------------------------------���ջ���--------------------------------------------------
    
HOST ='localhost'
PORT = 10001
ADDR = (HOST,PORT)
BUFSIZE = 1024*1024*5
tcpClient = socket(AF_INET,SOCK_STREAM)
tcpClient.connect(ADDR)
print "���ӳɹ�"

buf1 =''
buf2 =''
buf3 =''
bufList = [buf1,buf2,buf3]
#-------------------------ģ����յ���buf��ʵ���Ǳ����ļ������ݣ�------------------------------
with open(r"F:\U��\matlabCode624\location and trace\2016-5-7-16\Test_data\point0_00_00\CSI00_00.dat","rb") as file:
    while True:
        bytex = file.readline()
        if  bytex:
            bufList[0] +=  bytex
            #print bytex.encode('string-escape')
        else:
            break
        
with open(r"F:\U��\matlabCode624\location and trace\2016-5-7-16\Test_data\point1_10_00\CSI00_00.dat","rb") as file:
    while True:
        bytex = file.readline()
        if  bytex:
            bufList[1] +=  bytex
            #print bytex.encode('string-escape')
        else:
            break

with open(r"F:\U��\matlabCode624\location and trace\2016-5-7-16\Test_data\point2_10_06\CSI00_00.dat","rb") as file:
    while True:
        bytex = file.readline()
        if  bytex:
            bufList[2] +=  bytex
            #print bytex.encode('string-escape')
        else:
            break
bufListCopy = list(bufList)  # ����
#-----------------------------------------------------------------------------------------
        
countInt = 0  #ʱ�� ��ȫ�ֱ���
timer = threading.Timer(1,dataSend,(countInt,bufList,bufListCopy))
timer.start()













