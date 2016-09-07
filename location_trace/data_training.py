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
      
#class trainingDialog(wx.Dialog):
#   def __init__(self):
#      wx.Dialog.__init__(self,None,-1,u'参数选择 ：')
#      
#      about = wx.StaticText(self, -1, u"定位检测")     
#      time = wx.StaticText(self, -1, u"训练时间:")
#      positionST = wx.StaticText(self,-1,u'指纹点坐标：',style = wx.ALIGN_LEFT)
#
#      okay = wx.Button(self, wx.ID_OK)
#      okay.SetDefault()
#      cancel = wx.Button(self, wx.ID_CANCEL)
#      
#      self.time_t = wx.TextCtrl(self,-1)
###      positionList = ['(00,00)','(02,00)','(04,00)','(06,00)','(08,00)',
###                     '(10,00)','(00,02)','(02,02)','(04,02)','(06,02)',
###                     '(08,02)','(10,02)','(00,04)','(02,04)','(04,04)',
###                     '(06,04)','(08,04)','(10,04)','(00,06)','(02,06)',
###                     '(04,06)','(06,06)','(08,06)','(10,06)']      
#      self.position_t = wx.TextCtrl(self,-1)
#
#      sizer = wx.BoxSizer(wx.VERTICAL)
#      sizer.Add(about, 0, wx.ALL, 5)
#      sizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.ALL, 5)
#     
#      fgs = wx.FlexGridSizer(3, 2, 5,5)
#      #fgs.Add(name_l, 0, wx.ALIGN_RIGHT)
#      #fgs.Add(self.name_t, 0, wx.EXPAND)
#      fgs.Add(time, 0, wx.ALIGN_RIGHT)
#      fgs.Add(self.time_t, 0, wx.EXPAND)
#    
#      fgs.Add(positionST, 0, wx.ALIGN_RIGHT)
#      fgs.Add(self.position_t, 0, wx.EXPAND)
#     
#      fgs.AddGrowableCol(1)
#      sizer.Add(fgs, 0, wx.EXPAND|wx.ALL, 5)
#      btns = wx.StdDialogButtonSizer()
#      btns.AddButton(okay)
#      btns.AddButton(cancel)
#      btns.Realize()
#      sizer.Add(btns, 0, wx.EXPAND | wx.ALL, 5)
#        
#      self.SetSizer(sizer)
#      sizer.Fit(self)
class trainingDialog(wx.Dialog):
    def __init__(self, data):
        wx.Dialog.__init__(self, None, -1, "Validators:data transfer")
        about = wx.StaticText(self, -1, u"定位训练")
        #name_l = wx.StaticText(self, -1, "Name:")
        time_l = wx.StaticText(self, -1, u"训练时间:")
        position_l = wx.StaticText(self, -1, u"指纹点坐标:")
        
        #self.name_t = wx.TextCtrl(self, validator = DataXferValidator(data, "name"))
        self.time_t = wx.TextCtrl(self, validator = DataXferValidator(data, u"time"))
        self.position_t = wx.TextCtrl(self, validator = DataXferValidator(data, u"position"))
        
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
       
        fgs.Add(position_l, 0, wx.ALIGN_RIGHT)
        fgs.Add(self.position_t, 0, wx.EXPAND)
        
        fgs.AddGrowableCol(1)
        sizer.Add(fgs, 0, wx.EXPAND|wx.ALL, 5)
        
        btns = wx.StdDialogButtonSizer()
        btns.AddButton(okay)
        btns.AddButton(cancel)
        
        btns.Realize()
        sizer.Add(btns, 0, wx.EXPAND | wx.ALL, 5)
        
        self.SetSizer(sizer)
        sizer.Fit(self)
over = False
def real_time_data_Training(dirName,train_point,train_queue,train_time):
   global over
   over = False
   point0Name = dirName+'\\point0_00_00'
   point1Name = dirName+'\\point1_10_00'
   point2Name = dirName+'\\point2_10_06'
   point3Name = dirName+'\\point3_00_06'
   dirList=[point0Name,point1Name,point2Name,point3Name]
   count = 0  #第0秒
   print time.ctime(),u":开始训练"
   while count < train_time:
        analyzeData1 = train_queue.get()   #如果队列为空且block为True，get()就使调用线程暂停，直至有项目可用。   
        #print "有数据" 
        (mode ,sequence ,frameLength ,singleMonitorPointSamples)=struct.unpack('!siii',analyzeData1[4:17])#包括帧的模式，帧时序，帧数据长度和单监测点的信息数量
        #print "ffff",mode,sequence,frameLength,singleMonitorPointSamples
       # print u'人数检测：第%d秒的数据'%(sequence+1)
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
        
        for (i,eachPoint) in enumerate(DataPoint):
           csi_Name = dirList[i]+'\\CSI' + train_point +'.txt'
           
           #print csi_Name
           with open(csi_Name,"ab") as f:
               try:
                   for j in range(len(eachPoint)):  #9000
                     if  (not j%180 == 0) or j==0 :
                         f.write(str(round(eachPoint[j],4))+"  ")
                     else:
                         f.write('\n'+str(round(eachPoint[j],4))+"  ")
                   f.write('\n') 
               except:
                    print u"打开文件错误"
        count= count + 1
   print time.ctime(),u":训练结束"
   over = True
   
