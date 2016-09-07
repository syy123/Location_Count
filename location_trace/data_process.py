# -*- coding: utf-8 -*-
"""
Created on Thu Aug 04 19:45:24 2016

@author: Administrator
"""
import numpy as np
import time
import struct
import threading
import wx
about_txt = u'''人数检测'''

class DataXferValidator(wx.PyValidator):
    def __init__(self, data, key):
        wx.PyValidator.__init__(self)
        self.data = data
        self.key = key
    def Clone(self):
        return DataXferValidator(self.data, self.key)
    def Validate(self, win):
        return True
    def TransferToWindow(self):
        textCtrl = self.GetWindow()
        textCtrl.SetValue(self.data.get(self.key, ""))
        return True
    
    def TransferFromWindow(self):
        textCtrl = self.GetWindow()
        self.data[self.key] = textCtrl.GetValue()
        return True

class MyDialog(wx.Dialog):
    def __init__(self, data):
        wx.Dialog.__init__(self, None, -1, "Validators:data transfer")
        about = wx.StaticText(self, -1, about_txt)
        #name_l = wx.StaticText(self, -1, "Name:")
        time_l = wx.StaticText(self, -1, u"训练时间:")
        person_l = wx.StaticText(self, -1, u"当前人数:")
        
        #self.name_t = wx.TextCtrl(self, validator = DataXferValidator(data, "name"))
        self.time_t = wx.TextCtrl(self, validator = DataXferValidator(data, u"time"))
        self.person_t = wx.TextCtrl(self, validator = DataXferValidator(data, u"currentPerson"))
        
        okay = wx.Button(self, wx.ID_OK)
        okay.SetDefault()
        cancel = wx.Button(self, wx.ID_CANCEL)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(about, 0, wx.ALL, 5)
        sizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.ALL, 5)
        
        fgs = wx.FlexGridSizer(3, 2, 5,5)
        #fgs.Add(name_l, 0, wx.ALIGN_RIGHT)
        #fgs.Add(self.name_t, 0, wx.EXPAND)
        fgs.Add(time_l, 0, wx.ALIGN_RIGHT)
        fgs.Add(self.time_t, 0, wx.EXPAND)
       
        fgs.Add(person_l, 0, wx.ALIGN_RIGHT)
        fgs.Add(self.person_t, 0, wx.EXPAND)
        
        fgs.AddGrowableCol(1)
        sizer.Add(fgs, 0, wx.EXPAND|wx.ALL, 5)
        
        btns = wx.StdDialogButtonSizer()
        btns.AddButton(okay)
        btns.AddButton(cancel)
        
        btns.Realize()
        sizer.Add(btns, 0, wx.EXPAND | wx.ALL, 5)
        
        self.SetSizer(sizer)
        sizer.Fit(self)
        
class  DataProcessThread(threading.Thread):         
    def __init__(self,func,args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
    def getResult(self):
        return self.res
    def run(self): 
        print 'starting',self.name,'at:',time.ctime()
        self.res = apply(self.func,self.args)
        print self.name,'finished at:',time.ctime()
def real_time_data_process(queue):    
    analyzeData1 = queue.get()   #如果队列为空且block为True，get()就使调用线程暂停，直至有项目可用。   
    (mode ,sequence ,frameLength ,singleMonitorPointSamples)=struct.unpack('!siii',analyzeData1[4:17])#包括帧的模式，帧时序，帧数据长度和单监测点的信息数量
    #print "ffff",mode,sequence,frameLength,singleMonitorPointSamples
    print u'人数检测：第%d秒的数据'%(sequence+1)
    singleMonitorPointSamples=singleMonitorPointSamples*180#180=3*(30+30):一个样点数据包括3个流，每一个流有30个实部和30个虚部
    MonitorPointNum=frameLength/(singleMonitorPointSamples*4+1)#1:每个监测点所占字节，singleMonitorPointSamples*4：每个监测点数据的字节数
    parameter="s%df"%singleMonitorPointSamples
    
    #!表示使用网络字节顺序解码，因为我们的数据是从网络中接收到的，在网络上传送的时候它是网络字节顺序的
    DataAllPoint=struct.unpack("!"+parameter*MonitorPointNum,analyzeData1[17:])#analyzeData1个字节转换为36000个float型数据,
    DataPoint=[]
    for i in range(MonitorPointNum):
       DataPoint.append(DataAllPoint[singleMonitorPointSamples*i+i+1:singleMonitorPointSamples*(i+1)+i+1])
    #[(9000),(9000),(9000),(9000)]
    #print "DataPoint",len(DataPoint),len(DataPoint[0]),len(DataPoint[1]),len(DataPoint[2]),len(DataPoint[3]),DataAllPoint[0],DataAllPoint[9001],DataAllPoint[18002],DataAllPoint[27003]   
    AllMonitorPointListLineAmplitude=[]#所有监测点每个样点的幅值
    MonitorPointListFlowAmplitude=[]#每一个流的幅值
    for i in range(len(DataPoint)):
       MonitorPointListLineAmplitude=[]#每个样点有三个流，每一个样点的幅值
       for j in range(len(DataPoint[i])/60):#每一个流包含30个实部和30个虚部，len(DataPoint[i])/60表示流的个数
          for k in range(30):
             MonitorPointListFlowAmplitude.append(round(((float(DataPoint[i][k+j*60]))**2+(float(DataPoint[i][j*60+k+30]))**2)**0.5,4))#计算每一个流的幅值
          if((j+1)%3==0):
             MonitorPointListLineAmplitude.append(MonitorPointListFlowAmplitude)#MonitorPointListLineAmplitude表示每一条数据的幅值
             MonitorPointListFlowAmplitude=[]#每一个流的幅值 ，3个流组成一条数据                                                                  
       AllMonitorPointListLineAmplitude.append(MonitorPointListLineAmplitude)                                                                          
    #print "AllMonitorPointListLineAmplitude",len(AllMonitorPointListLineAmplitude),len(AllMonitorPointListLineAmplitude[0]),len(AllMonitorPointListLineAmplitude[0][0])
    #  Flow=[90]   Line =[[90],[90],[90]...[90]] 50个   AllLine = [[line],[line],[line],[line]] 
       
    for i in range(1,len(AllMonitorPointListLineAmplitude)):
       for j in range(len(AllMonitorPointListLineAmplitude[i])):  #50
          AllMonitorPointListLineAmplitude[0][j]=AllMonitorPointListLineAmplitude[0][j]+AllMonitorPointListLineAmplitude[i][j]#四个监测点样点数合并成一个向量
    ReceiveDataMerge=[]
    for i in range(len(AllMonitorPointListLineAmplitude[0])):
       #print len(ReceiveDataListPoint[0][i])
       ReceiveDataMerge.append(AllMonitorPointListLineAmplitude[0][i])
    #print "长度",len(ReceiveDataMerge),len(ReceiveDataMerge[0])   ##长度 50 360
    #ReceiveDataMerge = [[360],[360],[360]...[360]]  50个
    Var = np.var(ReceiveDataMerge, axis=0)
    Var = Var.tolist()
    return Var  #array[1*360]
