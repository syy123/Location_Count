# -*- coding: cp936 -*-
from read_bf_buffer import *
from get_scaled_csi import *
import struct
from socket import *
import numpy as np
import time
import threading

##########################################################
################      仅用于模拟       #####################
##########################################################

#------------------------------------dataSend FUNC-----------------------------------------------
def dataSend(countInt,bufList):
    begin = time.clock()        
    Array1 = []
    Array2 = []
    Array3 = []
    ArrayList = []
    ArrayList.append(Array1)
    ArrayList.append(Array2)
    ArrayList.append(Array3)  # 3个监测点
    if (len(bufList[0])>=43000) and (len(bufList[1])>=43000) and (len(bufList[2])>=43000):
        for index in range(len(ArrayList)):
            csi_trace = read_bf_buffer(bufList[index][:43000])  # 返回一个包含p个结构体的列表，输入参数是200个数据包（215B*200）    
            bufList[index] = bufList[index][43000:]  # 将这些数据删掉      
            p = len(csi_trace)
            for i in range(p/4+1):
                csi_entry = csi_trace[i*4]   # 第4*i个结构体（字典）
                csi = get_scaled_csi(csi_entry)  # 3*30 complex
                rel = np.real(csi)  # 3*30 double    
                ima = np.imag(csi)  # 3*30 double 
                x,y = np.shape(csi) # x=3 y=30
                X = 0
                sendArray = []
                while X < x:       
                    relList = rel[X].tolist()
                    imaList = ima[X].tolist()
                    sendArray = sendArray + relList + imaList  # 30个实部，30个虚部
                    X = X + 1
                ArrayList[index].extend(sendArray)  # 50条记录串联
        ArrayLength = (len(Array1)*4+1)*len(ArrayList)   
        #------------------------------组帧和发送---------------------------------------------
        sendstr = '\xff\xff\xff\xff'  # 帧头
        sendstr = sendstr + '\x30'    # mode 
        sendstr = sendstr + struct.pack('!i',countInt)  # 表示第几次数据（时序）
        sendstr = sendstr + struct.pack('!i',ArrayLength)  # 数据域长度
        sendstr = sendstr + struct.pack('!i',50)  # 每个监测点记录数量
        
        sendstr = sendstr + '\x31'
        for num in Array1:
            sendstr = sendstr + struct.pack("!f",num)  # 监测点1数据
        sendstr = sendstr + '\x32'
        for num in Array2:
            sendstr = sendstr + struct.pack("!f",num)  # 监测点2数据
        sendstr = sendstr + '\x33'
        for num in Array3:
            sendstr = sendstr + struct.pack("!f",num)  # 监测点3数据

        global clientList
        for each in clientList:  ## 向所有连接的客户发送帧
            try:
                each.send(sendstr)
            except:
                clientList.remove(each)  ## 客户端关闭，从列表中删除
                print "客户退出服务..."
                each.close()
       
        countInt += 1  #时序加1

        end = time.clock()
        print "处理和发送数据花费:",end-begin,"客户数量是:",len(clientList)
        global timer
        timer = threading.Timer(1-(end-begin),dataSend,(countInt,bufList))
        timer.start()
        
    else:           ###仅用于测试，循环####
        bufList = list(bufListCopy)       
        timer = threading.Timer(1,dataSend,(countInt,bufList))
        timer.start()
    
#-------------------------模拟接收到的buf（实际是本地文件中内容）------------------------------
buf1 =''
buf2 =''
buf3 =''
bufList = [buf1,buf2,buf3]

with open(r"..\2016-5-7-16\Test_data\point0_00_00\CSI00_00.dat","rb") as file:
    while True:
        bytex = file.readline()
        if  bytex:
            bufList[0] +=  bytex
            #print bytex.encode('string-escape')
        else:
            break
        
with open(r"..\2016-5-7-16\Test_data\point1_10_00\CSI00_00.dat","rb") as file:
    while True:
        bytex = file.readline()
        if  bytex:
            bufList[1] +=  bytex
            #print bytex.encode('string-escape')
        else:
            break

with open(r"..\2016-5-7-16\Test_data\point2_10_06\CSI00_00.dat","rb") as file:
    while True:
        bytex = file.readline()
        if  bytex:
            bufList[2] +=  bytex
            #print bytex.encode('string-escape')
        else:
            break
bufListCopy = list(bufList)  # 复制

#--------------------------------创建服务器--------------------------------------------------
    
HOST =''  ## 本机同时建立服务器，用于发送处理过的数据
PORT = 10006
ADDR = (HOST,PORT)
BUFSIZE = 1024*1024*5
server = socket(AF_INET,SOCK_STREAM)
server.bind(ADDR)
server.listen(5)
clientList = []  ##将连接到的客户套接字加入列表
def acceptFunc():
    while True:
        print "等待连接:"
        client,addr = server.accept()
        clientList.append(client)
        print "连接成功",addr
th = threading.Thread(target = acceptFunc)
th.start()
#-----------------------------------------------------------------------------------------
        
countInt = 0  #时序 ，全局变量
timer = threading.Timer(1,dataSend,(countInt,bufList))
timer.start()













