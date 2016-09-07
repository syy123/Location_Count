# -*- coding: utf-8 -*-
"""
Created on Wed Aug 03 11:35:31 2016

@author: Administrator
"""

import wx
from socket import *
import time
import threading
import struct
import numpy as np
import sys
from Queue import Queue 
path='E:\Located\libsvm-3.21\python'
#path='E:\Located\GuanTao\matlab-four\libsvm-master\python'
sys.path.append(path)
from data_process import *
from svmutil import *
class NewFrame(wx.Frame): 
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "frame", size = (1200, 800))
        panel = wx.Panel(self,-1)
        self.label1 = wx.StaticText(panel,-1,u"人数",size=(50,20),pos=(20,20))
        self.number = wx.TextCtrl(panel, -1,size=(100,20),pos=(50,20))
        self.label2 = wx.StaticText(panel, -1, u'训练时间', size=(50,20),pos=(160,20))
        self.time = wx.TextCtrl(panel, -1, size = (100, 20), pos = (220, 20))
        self.button0 = wx.Button(panel, -1, u"启动",size=(70,20),pos=(20,50))
        self.Bind(wx.EVT_BUTTON,self.OnClick, self.button0)
        
        self.button1 = wx.Button(panel, -1, u" 关闭",size=(70,20),pos=(100,50))
        self.Bind(wx.EVT_BUTTON,self.offClick, self.button1)
        
        self.button2 = wx.Button(panel, -1, u"训练",size=(70,20),pos=(20,80))
        self.Bind(wx.EVT_BUTTON,self.OnClick1, self.button2)
        self.button3 = wx.Button(panel, -1, u"测试",size=(70,20),pos=(100,80))
        self.Bind(wx.EVT_BUTTON,self.OnClick2, self.button3)
        self.DisplayText=wx.TextCtrl(panel,-1,"",size=(1080,750),pos=(20,110),style=wx.TE_MULTILINE)
        self.testdata=[]
        self.testlabel=[]
    #global analyzeDataAndAlgorithm
    def offClick(self, event):
        self.DisplayText.AppendText(u'\t训练完毕！\n')
        model = svm_train(self.testlabel, self.testdata, '-t 2 -c 3.5 -g 0.000015 -e 0.000001')
        svm_save_model('sixperson_model.txt',model)
        self.DisplayText.AppendText(u'\t训练模型生成！\n')
        #self.Destroy()
    def OnClick2(self, event):
        global BEGINTRAIN
        BEGINTRAIN = True  
        global CONNECTSTATE
        self.DisplayText.AppendText(u'下载训练模型,进行人数检测...\n')         
        svm_model = svm_load_model('sixperson_model.txt')
        def real_time_predict(queue):
            xlabel = 0
            predict_data = real_time_data_process(queue)
            [p_label, acc, div] = svm_predict([xlabel],[predict_data],svm_model)
            disp = str(time.ctime())+'  '+ u'人数为: ' + str(p_label)
            self.DisplayText.AppendText(str(disp))
        predict_thread = DataProcessThread(real_time_predict,(queue,),'predict')
        predict_thread.start()
        print u'人数检测线程开启'
        
    def OnClick1(self, event):
        global BEGINTRAIN
        BEGINTRAIN = True  
        global CONNECTSTATE
        ############  孙园园写的 #######################   
        def showText():
              time.sleep(train_time)
              show1 = 'len(self.testlabel)='+str(len(self.testlabel))+','+'len(self.testdata)='+str(len(self.testdata))+','+'len(self.testdata[0]=)'+str(len(self.testdata[0]))+'\n'
              self.DisplayText.AppendText(str(show1)) 
              self.DisplayText.AppendText(u'当前人数:%d 训练完毕，请重新输入人数...\n'%currentPerson)
              global BEGINTRAIN
              BEGINTRAIN = False
                                 
        if CONNECTSTATE:
           dialog = wx.TextEntryDialog(None, "what kind of text would you like to enter?","TextEntry","Default Value",
                                style=wx.OK|wx.CANCEL)
           if dialog.ShowModal() == wx.ID_OK:
                 print "you enterd: %s" %dialog.GetValue()
           train_time = int(self.time.GetValue())
           currentPerson = int(self.number.GetValue())                   
           def analyze_data(train_queue, train_time):
               for i in range(train_time):
                   var = real_time_data_process(train_queue)
                   #print u"孙圆圆的testdata"
                   self.testdata.append(var)
                   self.testlabel.append(currentPerson)   
           
           DataProThread = DataProcessThread(analyze_data,(train_queue,train_time),'analyze')     
           showthread = threading.Thread(target = showText)
           DataProThread.start()
           self.DisplayText.AppendText(u'当前人数:%d 开始训练...\n'%currentPerson)
           showthread.start()
     
            
    BEGINTRAIN = False   
    def OnClick(self, event):
        #Flag = True
        global BEGINTRAIN
        BEGINTRAIN = False
        class ReceiveData(threading.Thread):
            
            def __init__(self,t_name,train_queue):
                threading.Thread.__init__(self,name=t_name)
                self.dataqueue=train_queue
            def run(self):
                print u'数据接收线程运行时间:',time.ctime()
                global client
                data1=''
                global BEGINTRAIN
                while True:           
                    recvdata = client.recv(BUFSIZ)
                    data1=data1+recvdata               
                    if len(data1)>17:
                        if '\xff\xff\xff\xff' in data1[:4]:
                           if (int(struct.unpack("!i",data1[9:13])[0])==len(data1[17:])):  #数据域部分长度144004
                               #print 'len data1:',len(data1)
                               global BEGINTRAIN
                              # print "BEGINTRAIN:",BEGINTRAIN
                               if BEGINTRAIN:
                                   self.dataqueue.put(data1) 
                                   print u'队列长度：',self.dataqueue.qsize()   
                               data1=''
        
        def realtime_accept():           
            global client
            info = u'等待连接，端口号是'+str(PORT)+'\n'
            self.DisplayText.AppendText(str(info))
            print info
            client,addr = server.accept()
            global CONNECTSTATE
            CONNECTSTATE = True
            self.DisplayText.AppendText(u'连接成功,正在接收数据...\n')
            receiveData = ReceiveData('rev',train_queue)   ##线程类
            #analyzeDataAndAlgorithm = AnalyzeDataAndAlgorithm('send',queue)  ##线程类
            receiveData.start()
            #analyzeDataAndAlgorithm.start()                       
        try:        
            HOST = ''
            global PORT
            PORT = 10001
            ADDR =(HOST,PORT) 
            BUFSIZ = 1024*1024*5    
            server = socket(AF_INET,SOCK_STREAM)
            server.bind(ADDR) 
            server.listen(1)
            global train_queue
            train_queue=Queue()
            global CONNECTSTATE
            CONNECTSTATE = False

            t0 = threading.Thread(target=realtime_accept) 
            t0.start()
        except:
            self.DisplayText.AppendText("bind error...")
           
        
        
class MyApp(wx.App):
    def OnInit(self):
        frame= NewFrame(None)
        frame.Show(True)
        return True

def mainFunc():
    app = MyApp(0)
    app.MainLoop()

if __name__=='__main__':
    mainFunc()