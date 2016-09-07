   # -*- coding: cp936 -*-
import wx
import os
import sys
import re
import numpy as np
from numpy import *
import matplotlib
from matplotlib.ticker import MultipleLocator, FuncFormatter
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar
from socket import *
import time
import threading
import random
from Queue import Queue 
import struct
from data_process import *
import data_training
from sys import path
#path.append(r'F:\matlabCode624\location and trace') #�����module��·����ӽ���
path.append(r'.\libsvm-master\python')
from matplotlib import font_manager
import RealTimeKnn
import NewKnnDB
import pprint
from svmutil import *


class MyFrame(wx.Frame):
   def OnClickStart(self,event): 
         def HeatMap(subFigureTitle,minRange,maxRange,xxlabel="sequence",yylabel="Index of subcarries"):
            extent=(0,1,0,1)            
            #ָ��colormap
            cmap=matplotlib.cm.jet
            #����ÿ��ͼ��colormap��colorbar����ʾ��Χ��һ���ģ�����һ��
            norm=matplotlib.colors.Normalize(vmin=MinValue,vmax=MaxValue)         
            
            gci=self.axes.imshow(np.transpose(CFRAmplitudeSum[minRange:maxRange,:]),origin='lower',
                           interpolation='bilinear',extent=extent,cmap=cmap,norm=norm)
            self.figure.colorbar(gci)
            
            labelNum=(maxRange-minRange)/10
            self.axes.set_xticks(np.linspace(0,1,labelNum+1))            
            xticks=[]
            for i in range(labelNum):
                xticks.append(i*10)                
            self.axes.set_xticklabels(xticks)
            
            self.axes.set_yticks(np.linspace(0,1,7))
            self.axes.set_yticklabels( ('0', '5', '10', '15', '20','25','30'))

            #����label           
            self.axes.set_title(subFigureTitle)            
            self.axes.set_xlabel(xxlabel)  
            self.axes.set_ylabel(yylabel)
            
            
        #����ͼ����    
         def LineChart(subFigureTitle,minRange,maxRange,sumMode='CFR',xxlabel="subcarries",yylabel="amplitude value"):
            if sumMode=='CFR':
               numbers=np.arange(30)
               AmplitudeSum = CFRAmplitudeSum 
            else :
               xxlabel="delay/50ns"
               yylabel="amplitude value"
               AmplitudeSum = CIRAmplitudeSum
               numbers=[]
               for i in range(30):
                    #N=30��T=1/��f=1.5΢�룬Ts=50����
                    numbers.append(i) #802.11n����Ϊ20MHZ���ŵ�״̬��Ϣѡȡ30�����ز�����ÿ�����ز������f=2/3MHZ����f=fs/N=1/(NTs)=1/T,NΪ����������
                                    #fsΪ����Ƶ�ʣ�TsΪ���������NTs���ǲ���ǰģ���źŵĳ���T
                  
            for i in range(minRange,maxRange):
               self.axes.plot(numbers,AmplitudeSum[i,:])
            self.axes.set_title(subFigureTitle)
            self.axes.set_xlabel(xxlabel)
            self.axes.set_ylabel(yylabel)  
                     
        #�ĸ������ͬһָ�Ƶ�Ĵ���data
         def ReadTXT(testNumbers,minRange,maxRange,monitorPointCode,positionCode,date):
            fileDir=os.path.abspath("")
            frlist1 = []
            data=[]
            for root,dirs,files in os.walk(fileDir):
##                print root,dirs,files
                for fr in files:
                    frlist1.append(os.path.join(root,fr))
                    #print frlist1[-1]
            
            for fr in frlist1:  
                if monitorPointCode=="all":                   
                    a=positionCode[0].strip('(').strip(')').replace(',','_')#������(00,00)������ȥ����','�ַ��滻Ϊ'_'
                  
                    if ('CSI'+str(a) in fr) and (os.path.splitext(fr)[1] == '.txt') and ('Trainning_data' in fr) and (str(date) in fr):#��ѡ�ļ��������ļ�����
                        #print fr

                        ftxt = open(fr,'r')#����ѡ���ļ�
                        index=0
                        for line in ftxt.readlines():
                            line = line.strip()
                      
                            stringlist = line.split('  ')
                            tmpArr = []
                            for i in range(minRange,maxRange):
                                tmpArr.append(float(stringlist[i]))#ÿ������ѡ��ǰǰ60�����ݣ�Ҳ����һ�������ϵ�����
                            data.append(tmpArr)#�ĸ������ͬһ����λ�õ��ļ����ݴ���Data
                            index=index+1
                            
                            if index==testNumbers:#ÿ���ļ�ֻȡ150������,Data�ĳ���Ϊ600
                                break
                else :
                    for i in range(len(positionCode)):
                        a=positionCode[i].strip('(').strip(')').replace(',','_')
                        #print a
                        #print fr
                        if (str(monitorPointCode) in fr) and ('CSI'+str(a) in fr) and (os.path.splitext(fr)[1] == '.txt') and ('Trainning_data' in fr) and (str(date) in fr):#��ѡ�ļ��������ļ�����
                            #print monitorPointCode
                            ftxt = open(fr,'r')#����ѡ���ļ�
                            index=0
                            for line in ftxt.readlines():
                                line = line.strip()#ȥ��ÿ����β�Ŀո�\n
                                stringlist = line.split('  ')#�ַ�������ɵ����ַ�
                                tmpArr = []

                                for i in range(minRange,maxRange):
                                    tmpArr.append(float(stringlist[i]))#ÿ������ѡ��ǰǰ60�����ݣ�Ҳ����һ�������ϵ�����
                                data.append(tmpArr)#һ������Ķ������λ�õ��ļ����ݴ���Data
                                index=index+1
                                if index==testNumbers:#ÿ���ļ�ֻȡ150������,Data�ĳ���Ϊ150*ָ�Ƶ���
                                    break
            return data

         def CalculateAmplitude(Data,monitorPointCode):
            MaxValue=0.0
            MinValue=0.0
            if monitorPointCode=='all':
                CFRAmplitudeSum=zeros((4*count,30))#����ĸ������ͬһ����λ�õ�CFR��ֵ,ÿ�����괦ȡ150������
                CIRAmplitudeSum=zeros((4*count,30))#����ĸ������ͬһ����λ�õ�CIR��ֵ��ÿ�����괦ȡ150������
            else:   
                CFRAmplitudeSum=zeros((len(selectSampleList)*count,30))#���һ������Ķ������λ�õ�CFR��ֵ,ÿ�����괦ȡ150������
                CIRAmplitudeSum=zeros((len(selectSampleList)*count,30))#���һ������Ķ������λ�õ�CIR��ֵ��ÿ�����괦ȡ150������
            for i in range(len(Data)):
                CFR=[]
                CIR=[]
                CFRComplex=[]
                CIRAmplitude=[]
     
                for j in range(30):
                    #print Data[i][j]
                    sum=(float(Data[i][j]))**2+(float(Data[i][j+30]))**2
                    CFR.append(round(sum**0.5,4))#���ÿ��CFR�ķ�ֵ
                    CFRComplex.append(complex(float(Data[i][j]),float(Data[i][j+30])))#ʵ��CFRתΪ����CFR
                
                CIR=np.fft.ifft(CFRComplex[:30])#����CFR���и���Ҷ�任
                for k in range(len(CIR)):
                    Amplitude=((CIR[k].real)**2+(CIR[k].imag)**2)**0.5
                    CIRAmplitude.append(Amplitude)#ÿ��CIR�ķ�ֵ
   
                CFRAmplitudeSum[i,:]=CFR  #��30��CFR��ֵ�浽��i��,��600��               
                CIRAmplitudeSum[i,:]=CIRAmplitude
                CFR.sort()

                if (MaxValue<CFR[-1]):
                    MaxValue=CFR[-1]#�ҵ�CFR�����ֵ
                if (MinValue>CFR[0]):
                    MinValue=CFR[0]#�ҵ�CFR����Сֵ
            return CFRAmplitudeSum,CIRAmplitudeSum,MinValue,MaxValue

         if TYPE == 1:
          #  try:      
            monitorPointCode=self.monitorCombox.GetValue()
            graphCode=self.graghCombox.GetValue()
            CIRCFRCode=self.cirCfrCombox.GetValue()
            chooseDate=self.dateCombox.GetValue()
            selectSampleList=[]   #��¼��ѡȡ��ָ������
            
            #self.staticTC.AppendText('ѡ�������Ϊ��\n')
            for i in range(len(self.positionList)):
                if self.positionCombox.IsChecked(i)==True:
                    selectSampleList.append(self.positionList[i])
                    #self.staticTC.AppendText(self.positionList[i]+'\n')            
            
            count=150 #ÿ���ļ�ѡ��150������                       
            Data=ReadTXT(count,60,120,monitorPointCode,selectSampleList,chooseDate)#0-60����һ����60-120����2�������ϵ�CSI��120-180����3�������ϵ�CSI��
                                                                       # һ��CSI����30�����ݣ��ļ��е�CSI����ʵ�����鲿ֵ
            global MinValue,MaxValue,CFRAmplitudeSum,CIRAmplitudeSum
            CFRAmplitudeSum,CIRAmplitudeSum,MinValue,MaxValue=CalculateAmplitude(Data,monitorPointCode)
            self.figure.clf()
            if (monitorPointCode=='all') and (graphCode=='heatMap') and (CIRCFRCode=='CFR'):
                for i in range(4):
                    self.axes = self.figure.add_subplot(221+i)
                    HeatMap("MonitorPoint"+str(i),i*count,(i+1)*count)
                self.canvas.draw()
            elif (monitorPointCode=='all') and (graphCode=='lineChart') and (CIRCFRCode=='CIR'):                               
                for i in range(4):
                   self.axes = self.figure.add_subplot(221+i)
                   LineChart("MonitorPoint"+str(i),i*count,(i+1)*count,sumMode='CIR')        
                self.canvas.draw()
            elif (monitorPointCode=='all') and (graphCode=='lineChart') and (CIRCFRCode=='CFR'):                               
                for i in range(4):
                   self.axes = self.figure.add_subplot(221+i)
                   LineChart("MonitorPoint"+str(i),i*count,(i+1)*count)       
                self.canvas.draw()        
            elif (monitorPointCode!='all') and (graphCode=='heatMap') and (CIRCFRCode=='CFR'):               
                self.axes = self.figure.add_subplot(111)
                pointX = monitorPointCode[-1].encode('utf-8')             
                HeatMap("MonitorPoint"+pointX, 0, len(selectSampleList)*count)
                self.canvas.draw()
            else:
                #self.staticTC.AppendText('��֧������ѡ��ʽ...\n')
                self.statusbar.SetStatusText("��֧�����ַ�ʽ...")      
            #except:
             #   #self.staticTC.AppendText('�׳��쳣...\n')
             #   self.statusbar.SetStatusText("�׳��쳣...")
         elif TYPE == 0:
           # try:
               ##��ȡ�ؼ���ֵ     
               traingFile = self.trainingName     
               testFile = self.testName
               typechooseList = []
               for i in range(len(self.typechooseList)):
                  if self.typechooseCombox.IsChecked(i)==True:
                      typechooseList.append(self.typechooseList[i])
               dataQueue=Queue()               
               def ProgressDialogShow():  #���������
                       progressMax = 100
                       dialog = wx.ProgressDialog("A progress box", "Time remaining", progressMax, 
                       style= wx.PD_CAN_ABORT | wx.PD_ELAPSED_TIME | wx.PD_REMAINING_TIME)
                       keepGoing = True
                       global count
                       count = 0 
                       while  keepGoing and count < progressMax:
                          #print count
                          count = count + 1  
                          wx.Sleep(1)             
                          keepGoing = dialog.Update(count)  
                       dialog.Destroy()
               class  ReadDatabase(threading.Thread):         
                  def __init__(self,t_name):
                     threading.Thread.__init__(self,name=t_name)                          
                  def run(self):
                     print "��ʼ���ؾ�̬��λ�����ݿ�"
                     inLabelsFloatVector,PositionResultVector,PositionResutVector1,ErrorDistanceVector,ErrorDistanceVector1 = NewKnnDB.runFunc(traingFile,testFile)                     
                     print "���ؾ�̬��λ�����ݿ����"
                     global count
                     count = 100
                     dataQueue.put(inLabelsFloatVector)
                     dataQueue.put(PositionResultVector)
                     dataQueue.put(PositionResutVector1)
                     dataQueue.put(ErrorDistanceVector)
                     dataQueue.put(ErrorDistanceVector1)   
               def plotResult():
                  inLabelsFloatVector = dataQueue.get()
                  PositionResultVector = dataQueue.get()
                  PositionResutVector1= dataQueue.get()
                  ErrorDistanceVector= dataQueue.get()
                  ErrorDistanceVector1= dataQueue.get()
                  try:
                     self.figure.clf()
                  except:
                     pass
                  if  '\xb2\xe2\xca\xd4\xbd\xe1\xb9\xfb' in typechooseList:   ###Ԥ����
                     if len(typechooseList)== 1 :
                         self.axes = self.figure.add_subplot(111)
                     else:
                         self.axes = self.figure.add_subplot(221)
                     for i in range(len(inLabelsFloatVector)):  #484             
                         self.axes.scatter(inLabelsFloatVector[i][0],inLabelsFloatVector[i][1],marker='o',color='m',s=100)                        
                     for PositionResult in PositionResultVector:
                         self.axes.scatter(PositionResult[0],PositionResult[1],marker='o',color='r',s=50)                      
                     for PositionResult in PositionResutVector1:
                         self.axes.scatter(PositionResult[0],PositionResult[1],marker='o',color='b',s=20)
                     self.axes.set_title('Result')
                     self.axes.legend(loc = 'upper right')                   
                  if '\xbe\xe0\xc0\xeb\xce\xf3\xb2\xee' in typechooseList:    ###�������
                      if len(typechooseList)== 1 :
                         self.axes = self.figure.add_subplot(111)
                      else:
                         self.axes = self.figure.add_subplot(222)
                      tmpx = []
                      for i in range(len(ErrorDistanceVector)):
                          tmpx.append(i)
                      self.axes.plot(tmpx,ErrorDistanceVector,color='r',label='MostCounts ')
                      self.axes.plot(tmpx,ErrorDistanceVector1,color='b',label='SliceArea')
                      #��������0-484�� ��������ÿ����¼�ľ��������û���Ļ���0
                      #484����ľ���������һ�����б�ǩ������[8,2]���ļ�¼�������ݿ��е�5784����¼ƥ��,ƥ�������������               
                      self.axes.set_title("DistanceError") 
                      self.axes.set_xlabel("Samples")
                      self.axes.set_ylabel("Distance Error")
                      self.axes.legend(loc = 'upper right')   
                  if '\xce\xf3\xb2\xee\xb7\xd6\xb2\xbc' in typechooseList:    ###���ֲ�
                      if len(typechooseList)== 1 :
                         self.axes = self.figure.add_subplot(111)
                      else:
                         self.axes = self.figure.add_subplot(223)
                      tmpY = []
                      SortedDistanceVec = []
                      DistanceVec = asarray(ErrorDistanceVector1)
                      sortedDistIndicies = DistanceVec.argsort()
                      for i in range(len(DistanceVec)):
                          SortedDistanceVec.append(DistanceVec[sortedDistIndicies[i]])
                      Count = len(SortedDistanceVec)
                      print "Count",Count
                      for i in range(Count):
                          tmpY.append(float(i+1)/float(Count)*100)                 
                      self.axes.set_xticks(linspace(0,10,20))
                      self.axes.set_yticks(linspace(0,100,10))
                      self.axes.grid(True)
                      self.axes.plot(SortedDistanceVec,tmpY,color = 'b',label=u'KNN�Ľ�')
                      xmajorLocator = MultipleLocator(0.5) 
                      self.axes.xaxis.set_major_locator(xmajorLocator) #����������ļ��Ϊ300
                      self.axes.set_xlim(0,6)#x��ķ�Χ����
                      ymajorLocator = MultipleLocator(10) 
                      self.axes.yaxis.set_major_locator(ymajorLocator) #����������ļ��Ϊ300
                      zh_font = font_manager.FontProperties(fname=r"C:\windows\fonts\simsun.ttc", size=14)
                      self.axes.set_ylim(0,100)#x��ķ�Χ����
                      self.axes.legend(prop=zh_font)
                      self.axes.set_title(u"�������CDF",fontproperties=zh_font)
                      self.axes.set_xlabel(u"�������(m)", fontproperties=zh_font)
                      self.axes.set_ylabel(u"�ۻ�����,(%)", fontproperties=zh_font)
                  self.canvas.draw()
               thread1 = ReadDatabase('readDatabase')               
               thread2 = threading.Thread(target = plotResult)
               thread1.start()
               thread2.start()
               ProgressDialogShow()
##            except:
##               print "wrong!~"              
   def OnQuit(self,event):
      sys.exit(0)

##########################################  ѵ��   #########################################################################
########################################################################################################################
########################################################################################################################
##��ԲԲ�İ�ť�ĺ���
   def OnTrainModel(self, event):
        #global Flag
        #global CONNECTSTATE
        global queue      
        if Case == 0:   ############  ��԰԰д�� #######################                                
           #if CONNECTSTATE:  
           data = {"name":"SunYuana"}
           dlg = MyDialog(data)
           dlg.ShowModal()
           dlg.Destroy()           
           #wx.MessageBox("�������ѵ��ʱ��Ϊ"+dlg.time_t.GetValue()+"��,"+"����Ϊ"+dlg.person_t.GetValue()+"���ˣ�")
           self.personCtrl.SetValue(str(data.get("currentPerson")))
           self.timeCtrl.SetValue(str(data.get("time")))
           #self.personCtrl.AppendText(dlg.person_t.GetValue()+",")

           if (str(data.get("currentPerson")) != 'None') and (str(data.get("time")) != 'None'):
               global Flag 
               Flag = True
               train_time = int(self.timeCtrl.GetValue())
               print " ѵ��ʱ��",train_time
               currentPerson = int(self.personCtrl.GetValue())
               def analyze_data(queue, train_time):
                   for i in range(train_time):
                       print "��",i,"�ε���ȡ���к���"
                       var = real_time_data_process(queue)
                       self.testdata.append(var)
                       self.testlabel.append(currentPerson)   
                       print "��",i,"�δ�����"
                   show1 = 'len(self.testlabel)='+str(len(self.testlabel))+','+'len(self.testdata)='+str(len(self.testdata))+','+'len(self.testdata[0]=)'+str(len(self.testdata[0]))+'\n'
                   self.DisplayText.AppendText(str(show1)) 
                   self.DisplayText.AppendText('��ǰ����:%d ѵ����ϣ���������������...\n'%currentPerson)
                   global Flag 
                   Flag = False
               DataProThread = DataProcessThread(analyze_data,(queue,train_time),'analyze')     
               #showthread = threading.Thread(target = showText)
               DataProThread.start() 
               
               self.DisplayText.AppendText('��ǰ����:%d ��ʼѵ��...\n'%currentPerson)
           else:              
               wx.MessageBox(u"�����µ��ѵ����ť���ò�����")               
               Flag = False
               
           #showthread.start()
        elif Case == 1:     ############  ���д�� #######################      
             #global CONNECTSTATE             
             ####### �������ļ������� ##############################
             data={"name":"guantao"}
             dlg = data_training.trainingDialog(data)
             dlg.ShowModal()
             dlg.Destroy()
             #strs = dlg.position_t.GetValue() #2,0
             strs = str(data.get('position'))             
             if (self.timeCtrl.GetValue() != 'None') and (strs != 'None'):
                 #print u"��ʱ���г��ȣ�",queue.qsize()
                 for i in range(queue.qsize()):
                   queue.get()
                # print u"������գ�", queue.qsize()
                 x = strs.split(' ')
                 if len(x[0]) == 1:
                    x[0] = '0'+ x[0]
                 if len(x[1]) == 1:
                    x[1] = '0'+ x[1]
                 pointString = u'('+x[0]+','+x[1]+')'
                 a=(pointString,)             
                 #print pointString
                 self.positionCombox.SetCheckedStrings(a) #����Ҫ�����ַ���Ԫ��
                 self.timeCtrl.SetValue(str(data.get('time')))   
                 #global Flag
                 Flag = True
                 #print Flag
                 positionList = []
                 for i in range(len(self.positionList)):
                   if self.positionCombox.IsChecked(i)==True:
                      positionList.append(self.positionList[i])
                      
                 choosepoint = positionList[0]   ##�����ѡָ�Ƶ�            
                 train_point = choosepoint.strip('(').strip(')').replace(',','_')#������(00,00)������ȥ����','�ַ��滻Ϊ'_'             
                 train_time = int(dlg.time_t.GetValue())  ##���ѵ��ʱ��
                 path = os.getcwd()
                 (year,month,day,hour)=time.localtime()[0],time.localtime()[1],time.localtime()[2],time.localtime()[3]
                 title = str(year)+'-'+str(month)+'-'+str(day)+'-'+str(hour)
                 filename =  os.path.join(path, title)
                 if self.CreatDIR:
                    while os.path.exists(filename):
                       filename = filename+'(1)'
                    CreatFileName = filename + '\\Trainning_data'
                 else:
                     while os.path.exists(filename):
                       filename = filename+'(1)'
                     filename = filename[:-3]
                     CreatFileName = filename + '\\Trainning_data'
                 def showText1():
                      while ( data_training.over == False):
                         time.sleep(1)
                      self.DisplayText.AppendText('��ǰ����ѵ�����...\n')     
                      global Flag
                      Flag = False
                ###################################################
      #���ӳɹ������ѵ��
                 if self.CreatDIR:   ##�Ƿ���Ҫ�����ļ��У���һ�ε�ѵ����Ҫ��
                  # print "CreatDir","True"
                   filename1 = filename+'\\Trainning_data'
                   point0Name = filename1+'\\point0_00_00'
                   point1Name = filename1+'\\point1_10_00'
                   point2Name = filename1+'\\point2_10_06'
                   point3Name = filename1+'\\point3_00_06'
                   os.makedirs(filename)
                   os.makedirs(filename1)
                   os.makedirs(point0Name)
                   os.makedirs(point1Name)
                   os.makedirs(point2Name)
                   os.makedirs(point3Name)
                   self.DisplayText.AppendText('�����ļ��У�'+filename+'\n')
                   self.DisplayText.AppendText('�����ļ��У�'+filename1+'\n')
                   self.DisplayText.AppendText('�����ļ��У�'+point0Name+'\n')
                   self.DisplayText.AppendText('�����ļ��У�'+point1Name+'\n')
                   self.DisplayText.AppendText('�����ļ��У�'+point2Name+'\n')
                   self.DisplayText.AppendText('�����ļ��У�'+point3Name+'\n')
                   self.CreatDIR = False                     
                   data_trainingThread = threading.Thread(target=data_training.real_time_data_Training,args=(filename1,train_point,queue,train_time))
                   info = "ѵ�����꣺"+choosepoint+"\tѵ��ʱ�䣺"+str(train_time)+"��\t��ʼѵ��...\n"
                   self.DisplayText.AppendText(info)
                   showthread = threading.Thread(target = showText1)
                   data_trainingThread.start()
                   showthread.start()                                                      
                 else:             ##���ǵ�һ�ε��ѵ��ʱ�����贴���µ��ļ���
                  # print "CreatDir","False"
                   data_trainingThread = threading.Thread(target=data_training.real_time_data_Training,args=(CreatFileName,train_point,queue,train_time))      
                   showthread = threading.Thread(target = showText1)
                   info = "ѵ�����꣺"+choosepoint+"\tѵ��ʱ�䣺"+str(train_time)+"��\t��ʼѵ��...\n"
                   self.DisplayText.AppendText(info)
                   data_trainingThread.start() 
                   showthread.start()   
             else:
                 wx.MessageBox(u"����ѵ����ť�������ò�����")
                 for i in range(len(self.positionList)):
                   if self.positionCombox.IsChecked(i)==True:
                      self.positionCombox.Check(i, False)
                 #global Flag
                 Flag = False
                                                     
   def OnTrainOver(self, event):
      #global server_train
      if Case == 0:
         self.DisplayText.AppendText('\tѵ����ϣ�\n')
         model = svm_train(self.testlabel, self.testdata, '-t 2 -c 3.5 -g 0.000015 -e 0.000001')
         svm_save_model('libsvm_model.txt',model)
         self.DisplayText.AppendText('\tѵ��ģ�����ɣ�\n')
         self.timeCtrl.Clear()
         self.personCtrl.Clear()
         self.testdata = []
         self.testlabel = []
      elif Case == 1:
         self.timeCtrl.Clear()
         for i in range(len(self.positionList)):
           if self.positionCombox.IsChecked(i)==True:
              self.positionCombox.Check(i, False)  
         self.DisplayText.AppendText("\tѵ�����....\n")

##########################################################################################################################################
##############################################    ʵʱ          ###########################################################################
##########################################################################################################################################           
   def OnClickClose(self,event):
      def realtime_plot():
        while TYPE == 2:
           try:
            #print "type1",TYPE  
            start = time.clock()
            global queue
            data = queue.get()  
            monitorPointCode=self.monitorCombox.GetValue()
            graphCode=self.graghCombox.GetValue()
            CIRCFRCode=self.cirCfrCombox.GetValue()
            tianxianCode=self.tianxianCombox.GetValue()
            plotindex = 221 #4������ķָ�
            plotcount = 4   #4�������ͼ��
            plotObj = 0
            if monitorPointCode != 'all':
               plotindex = 111  #������ķָ�
               plotcount = 1    #�������ͼ��
               plotObj = int(monitorPointCode[-1]) #�ڼ�������
            perPoint = data[4:]     #��ȥǰ4���ֽ�      
            (mode,timeCount,dataLength,pointCSI) = struct.unpack("!1s1i1i1i",perPoint[0:13])
            #print mode ,timeCount,dataLength,pointCSI
            perPointByte = pointCSI*180*4+1  ##36001
            countPoint = dataLength/perPointByte ## ʵ����2 ����4?
            print "�ж��ٸ�point��",countPoint
            unpackformat = "!"+("1s"+str((perPointByte-1)/4)+"f")*countPoint
            allpointtuple = struct.unpack(unpackformat,perPoint[13:])                        
            #��144016�ֽڰ�����˳��ת��Ϊ(mode,timeCount,datalength,pointCSI)�� allpointtuple
            pointTupleList =[]
            for i in range(countPoint): ## ʵ����2  3 ����4?
               pointtuple=allpointtuple[(perPointByte*i/4+i+1):(perPointByte*(i+1)/4+i+1)]
               pointTupleList.append(pointtuple)             
               
            plotlist = []            
            for pointTuple in pointTupleList:               
               for i in range(pointCSI):   #pointCSI=50 �� 150
                  temp=list(pointTuple[180*i:180+180*i])
                  plotlist.append(temp)        #plotlist=[(180),(180)����,(180)],200�� ��600��
            plotArry =[]
            for eachRecord in plotlist:    #plotlist=[(180),(180)����,(180)],200�� ��600��                 
                  tianxianIndex = int(tianxianCode)-1                     
                  tmpArr = eachRecord[60*tianxianIndex:60+60*tianxianIndex]  # ѡ��ڼ������ߵ�60������                     
                  plotArry.append(tmpArr)     #plotArry=[(60),(60)����,(60)],200��
           # print len(plotArry) , len(plotArry[98]),len(plotArry[99])  #100 60
            CFRAmplitudeSum=zeros((pointCSI*4,30))#���4������CFR��ֵ,ÿ��ȡ50�����ݻ�150��
            CIRAmplitudeSum=zeros((pointCSI*4,30))#���4������CIR��ֵ,ÿ��ȡ50�����ݻ�150��
            MaxValue=0.0
            MinValue=0.0
            for i in range(len(plotArry)):                
                CFRAmplitude=[]
                CIRComplex=[]
                CFRComplex=[]
                CIRAmplitude=[]     
                for j in range(30):                   
                    sum=(plotArry[i][j])**2+(plotArry[i][j+30])**2
                    CFRAmplitude.append(round(sum**0.5,4))   #���ÿ��CFR�ķ�ֵ
                    CFRComplex.append(complex(plotArry[i][j],plotArry[i][j+30]))#ʵ��CFRתΪ����CFR                
                CIRComplex=np.fft.ifft(CFRComplex[:30])      #����CFR���и���Ҷ�任
                for k in range(len(CIRComplex)):
                    Amplitude=((CIRComplex[k].real)**2+(CIRComplex[k].imag)**2)**0.5
                    CIRAmplitude.append(Amplitude) #ÿ��CIR�ķ�ֵ   
                CFRAmplitudeSum[i,:]=CFRAmplitude  #��30��CFR��ֵ�浽��i��           
                CIRAmplitudeSum[i,:]=CIRAmplitude
                CFRAmplitude.sort()
                if (MaxValue<CFRAmplitude[-1]):
                    MaxValue=CFRAmplitude[-1]   #�ҵ�CFR�����ֵ

        ####################(    30�����ز��ķ�ֵ����ͼ   )##################################
            try:
               self.figure.clf()
            except:
               pass           
            if(graphCode == 'lineChart'):
               for index in range(plotcount):    #plotcount=1��4
                  self.axes = self.figure.add_subplot(plotindex+index) #plotindex��111��221
                  if (CIRCFRCode == 'CFR'):                        
                     for i in range(pointCSI):   #pointCSI=50 �� 150
                        self.axes.plot(np.arange(30),CFRAmplitudeSum[index*pointCSI+plotObj*pointCSI+i,:],color='r')
                     self.axes.set_title('ponit'+str(index+plotObj)+' CFRAmplitude')#plotcount=1ʱ��index=0,plotObj�Ǽ��㣻plotcount=4ʱ��index�Ǽ���,plotObj=0
                     self.axes.set_ylim(0,40)
                     self.axes.set_xlabel("subcarrier")
                     self.axes.set_ylabel("amplitude value")
                  else:
                     for i in range(pointCSI):   #pointCSI=50 �� 150
                        self.axes.plot(np.arange(30),CIRAmplitudeSum[index*pointCSI+plotObj*pointCSI+i,:],color='r')
                     self.axes.set_title('ponit'+str(index+plotObj)+' CIRAmplitude')#plotcount=1ʱ��index=0,plotObj�Ǽ��㣻plotcount=4ʱ��index�Ǽ���,plotObj=0
                     self.axes.set_ylim(0,15)
                     self.axes.set_xlabel("delay/50ns")
                     self.axes.set_ylabel("amplitude value")
               self.canvas.draw()
         #########################(   �ȶ�ͼ    )############################################
            else:
               for index in range(plotcount):  #plotcount=1��4
                  self.axes = self.figure.add_subplot(plotindex+index) #plotindex��111��221 
                  extent=(0,1,0,1)            
                  cmap=matplotlib.cm.jet
                  norm=matplotlib.colors.Normalize(vmin=0,vmax=40)        # pointCSI = 50 �� 150              
                  gci=self.axes.imshow(np.transpose(CFRAmplitudeSum[(pointCSI*index+plotObj*pointCSI):(pointCSI+pointCSI*index+plotObj*pointCSI),:]),origin='lower',
                                 interpolation='bilinear',extent=extent,cmap=cmap,norm=norm)
                  self.figure.colorbar(gci)            
                  self.axes.set_xticks(np.linspace(0,1,6))
                  #print type(self.axes)
                  self.axes.set_xticklabels(np.linspace(0,pointCSI,6))           
                  self.axes.set_yticks(np.linspace(0,1,7))
                  self.axes.set_yticklabels(np.linspace(0,30,7))       
                  self.axes.set_title('ponit'+str(index+plotObj)+' HeatMap')            
                  self.axes.set_xlabel('sequence')  
                  self.axes.set_ylabel("subcarrier")
               self.canvas.draw()
        ######################################################################################                             
            end = time.clock()
            print "this is",timeCount,"time's data,","cost ",end-start
           except:               
            print "wrong here"
            realtime_plot()
      def realtime_count():
          global queue
          VAR = real_time_data_process(queue)
          testlabel = 0
          model = svm_load_model('libsvm_model.txt')
          [p, m, n] = svm_predict([testlabel], [VAR], model)
          self.DisplayText.AppendText("%s:  ����Ϊ%d\n" % (time.ctime(),p[0]))
            #self.statusbar.SetStatusText("��ǰ����Ϊ%d," % p[0])     
      def realtime_locate():
        # print "types2",TYPE
         Q = np.array([1e-5,1e-5]) # process variance   Q=array([0.00001,0.00001])
         # ��������ռ�  
         xhat=np.zeros((2,2))      # a posteri estimate of x �˲�����ֵ  
         P=np.zeros((2,2))         # a posteri error estimate�˲�����Э�������  
         xhatminus=np.zeros((2,1)) # a priori estimate of x ����ֵ  
         Pminus=np.zeros((2,1))    # a priori error estimate����Э�������  
         K=np.zeros((2,1))         # gain or blending factor����������
         I=np.ones((2,1))
         R = np.array([0.1**2,0.1**2]) # estimate of measurement variance, change to see effect  
         # intial guesses  
         xhat[:,0] = [0.0,0.0] 
         P[:,0] = [1.0,1.0]
         def KalmanFilter(PositionResult): ## PositionResult = array([ 8.,  2.])
             # Ԥ��  
             xhatminus = xhat[:,0]  #X(k|k-1) = AX(k-1|k-1) + BU(k) + W(k),A=1,BU(k) = 0  
             Pminus = P[:,0]+Q      #P(k|k-1) = AP(k-1|k-1)A' + Q(k) ,A=1  
             # xhatminus=array([[ 0.,  0.])      Pminus=array([ 1.00001,  1.00001])
             # ����  
             K = Pminus/( Pminus+R ) #Kg(k)=P(k|k-1)H'/[HP(k|k-1)H' + R],H=1
             #  K=array([ 0.99009911,  0.99009911])
             xhat[:,1] = xhatminus+K*(PositionResult-xhatminus) #X(k|k) = X(k|k-1) + Kg(k)[Z(k) - HX(k|k-1)], H=1
             #x=xhat[1]
             P[:,1] = (1-K)*Pminus #P(k|k) = (1 - Kg(k)H)P(k|k-1), H=1
             return xhat[:,1],P[:,1]
         while TYPE == 3 or TYPE == 4:
            start = time.clock()
            global queue
            analyzeData1 = queue.get()   #�������Ϊ����blockΪTrue��get()��ʹ�����߳���ͣ��ֱ������Ŀ���á�
           
            (mode ,sequence ,frameLength ,singleMonitorPointSamples)=struct.unpack('!siii',analyzeData1[4:17])#����֡��ģʽ��֡ʱ��֡���ݳ��Ⱥ͵��������Ϣ����
           # print "ffff",mode,sequence,frameLength,singleMonitorPointSamples
           # print "��%d�������"%(sequence+1)
            singleMonitorPointSamples=singleMonitorPointSamples*180#180=3*(30+30):һ���������ݰ���3������ÿһ������30��ʵ����30���鲿
            MonitorPointNum=frameLength/(singleMonitorPointSamples*4+1)#1:ÿ��������ռ�ֽڣ�singleMonitorPointSamples*4��ÿ���������ݵ��ֽ���
            parameter="s%df"%singleMonitorPointSamples
            
            #!��ʾʹ�������ֽ�˳����룬��Ϊ���ǵ������Ǵ������н��յ��ģ��������ϴ��͵�ʱ�����������ֽ�˳���
            DataAllPoint=struct.unpack("!"+parameter*MonitorPointNum,analyzeData1[17:])#analyzeData1���ֽ�ת��Ϊ36000��float������,
            DataPoint=[]
            for i in range(MonitorPointNum):
               DataPoint.append(DataAllPoint[singleMonitorPointSamples*i+i+1:singleMonitorPointSamples*(i+1)+i+1])
            #[(9000),(9000),(9000),(9000)]
            #print "DataPoint",len(DataPoint),len(DataPoint[0]),len(DataPoint[1]),len(DataPoint[2]),len(DataPoint[3]),DataAllPoint[0],DataAllPoint[9001],DataAllPoint[18002],DataAllPoint[27003]
            
            AllMonitorPointListLineAmplitude=[]#���м���ÿ������ķ�ֵ
            MonitorPointListFlowAmplitude=[]#ÿһ�����ķ�ֵ
            for i in range(len(DataPoint)):
               MonitorPointListLineAmplitude=[]#ÿ����������������ÿһ������ķ�ֵ
               for j in range(len(DataPoint[i])/60):#ÿһ��������30��ʵ����30���鲿��len(DataPoint[i])/60��ʾ���ĸ���
                  for k in range(30):
                     MonitorPointListFlowAmplitude.append(round(((float(DataPoint[i][k+j*60]))**2+(float(DataPoint[i][j*60+k+30]))**2)**0.5,4))#����ÿһ�����ķ�ֵ
                  if((j+1)%3==0):
                     MonitorPointListLineAmplitude.append(MonitorPointListFlowAmplitude)#MonitorPointListLineAmplitude��ʾÿһ�����ݵķ�ֵ
                     MonitorPointListFlowAmplitude=[]#ÿһ�����ķ�ֵ ��3�������һ������                                                                  
               AllMonitorPointListLineAmplitude.append(MonitorPointListLineAmplitude)                                                                          
            #print "AllMonitorPointListLineAmplitude",len(AllMonitorPointListLineAmplitude),len(AllMonitorPointListLineAmplitude[0]),len(AllMonitorPointListLineAmplitude[0][0])
            #  Flow=[90]   Line =[[90],[90],[90]...[90]] 50��   AllLine = [[line],[line],[line],[line]] 
               
            for i in range(1,len(AllMonitorPointListLineAmplitude)):
               for j in range(len(AllMonitorPointListLineAmplitude[i])):  #50
                  AllMonitorPointListLineAmplitude[0][j]=AllMonitorPointListLineAmplitude[0][j]+AllMonitorPointListLineAmplitude[i][j]#�ĸ������������ϲ���һ������
            ReceiveDataMerge=[]
            for i in range(len(AllMonitorPointListLineAmplitude[0])):
               #print len(ReceiveDataListPoint[0][i])
               ReceiveDataMerge.append(AllMonitorPointListLineAmplitude[0][i])
            #print "����",len(ReceiveDataMerge),len(ReceiveDataMerge[0])   ##���� 50 360(4������ʱ)
            #ReceiveDataMerge = [[360],[360],[360]...[360]]  50��
            global DataSet,LabelsFloatVector
            
            PositionResult,PositionResult1=RealTimeKnn.DataProcessAndKnnAlgorithm(asarray(ReceiveDataMerge),DataSet,LabelsFloatVector)
            # asarray(ReceiveDataMerge)  ��Ϊ50*360�ľ���   DataSet(3408*348)  LabelsFloatVector[3408]
            # PositionResult=[[8.0,2.0]...9��],PositionResult1=[[8.0,2.0]...9��]
            
            xPoint=[]  ##���ڴ洢�˲��������,len = 9
            yPoint=[]
            for i in range(len(PositionResult)):  #9
                PositionResultVector=np.array([PositionResult[i][0],PositionResult[i][1]])  ##array([ 8.,  2.]) 
                location,locationcov=KalmanFilter(PositionResultVector) ##location=array([ 7.92079286,  1.98019822]),locationcov=array([ 0.00990099,  0.00990099])
                #print "KalmanԤ������",location,locationcov
                xPoint.append(location[0])
                yPoint.append(location[1])
                xhat[:,0] = location 
                P[:,0] = locationcov
            tracePointX.append(xPoint[-1])
            tracePointY.append(yPoint[-1])            
            try:
               self.figure.clf()
            except:
               pass
            try:
               if TYPE == 3:      
                  self.axes = self.figure.add_subplot(111)
                  self.axes.scatter(xPoint[-1],yPoint[-1],marker='o',color='r',label='current')
                  self.axes.set_xticks(np.linspace(0,10,6))
                  self.axes.set_yticks(np.linspace(0,6,4))   
                  self.axes.set_xticklabels( ('0', '2', '4', '6', '8','10'))
                  self.axes.set_yticklabels( ('0', '2', '4', '6'))
                  self.axes.set_title('Real-time Location')
                  self.axes.legend(loc = 'upper right')
                  self.axes.grid(True)
##                  for index in range(len(xPoint)):
##                     self.axes.scatter(xPoint[index],yPoint[index],marker='o',color='r')
##                     time.sleep(0.05)
                  self.canvas.draw()
                  self.statusbar.SetStatusText("Ԥ������Ϊ��[%f,%f]" % (xPoint[-1],yPoint[-1]))                  
               elif TYPE == 4 and len(xPoint)>= 5:                           
                  self.axes = self.figure.add_subplot(111)
                  self.axes.scatter(tracePointX[-5:-1],tracePointY[-5:-1],marker='x',color='r',label='past')
                  self.axes.scatter(tracePointX[-1],tracePointY[-1],marker='o',color='b',label='current')
                  self.axes.plot(tracePointX[-5:],tracePointY[-5:])
                  self.axes.set_xticks(np.linspace(0,10,6))
                  self.axes.set_yticks(np.linspace(0,6,4))   
                  self.axes.set_xticklabels( ('0', '2', '4', '6', '8','10'))
                  self.axes.set_yticklabels( ('0', '2', '4', '6'))
                  self.axes.set_title('Real-time Trace')
                  self.axes.legend(loc = 'upper right')
                  self.axes.grid(True)
                  self.canvas.draw()
                  self.statusbar.SetStatusText("Ԥ������Ϊ��[%f,%f]" % (xPoint[-1],yPoint[-1]))
            except:
                  pass
         #################################
            end = time.clock()
            print "��%d�������"%(sequence),"slice and locate cost ",end-start
            
      class ReceiveData(threading.Thread):
         def __init__(self,t_name,queue):
            threading.Thread.__init__(self,name=t_name)
            self.dataqueue=queue
         def run(self):
            global client
            #self.statusbar.SetStatusText("���ڽ�������...")
            data1=''
            while True:           
                recvdata = client.recv(BUFSIZ)
                data1=data1+recvdata
                #print "%r"%recvdata[:4]
                global Flag
                if len(data1)>17:
                    if '\xff\xff\xff\xff' in data1[:4]:
                       start = time.clock()
                       if (int(struct.unpack("!i",data1[9:13])[0])==len(data1[17:])):  #�����򲿷ֳ���144004
                           print "Flag",Flag
                           if Flag:
                               self.dataqueue.put(data1) 
                               end=time.clock()               
                           data1=''
                           
      class  AnalyzeDataAndAlgorithm(threading.Thread):         
         def __init__(self,t_name,queue):
            threading.Thread.__init__(self,name=t_name)
            self.dataqueue=queue            
         def run(self):   
            while True:
               if TYPE == 2:
                  realtime_plot()
               elif TYPE == 3 or TYPE == 4:
                  realtime_locate()
               elif TYPE == 5:
                  realtime_count() 
               '''elif TYPE == 6:
                  #self.DisplayText.AppendText("ѵ������...")
                  pass
               elif TYPE == 7:
                  #self.DisplayText.AppendText("ѵ������...")
                  pass'''
      #try:      
      HOST = '10.170.38.146'
      global PORT,client
      PORT = 10009
      ADDR =(HOST,PORT)        
      BUFSIZ = 1024*1024*5        
      client = socket(AF_INET,SOCK_STREAM)
      client.connect(ADDR)
      self.closeButton.SetLabel("���ӳɹ�")
      global queue
      queue=Queue()
      global tracePointX,tracePointY
      global Flag
      Flag = True   #True��ʾ������ӵ����� False��ʾ��ǰ���ݲ���Ӷ��У��л���frame6��7��û��ѵ����ťʱ��False��
      tracePointX=[]
      tracePointY=[]
      self.statusbar.SetStatusText("���ӳɹ�, ��������...")
      receiveData = ReceiveData('rev',queue)   ##�߳���
      analyzeDataAndAlgorithm = AnalyzeDataAndAlgorithm('send',queue)  ##�߳���
      receiveData.start()
      analyzeDataAndAlgorithm.start()
      #except:
      #self.statusbar.SetStatusText("bind error...")
   def OnClickStop(self,event):     
      #self.server.close()
      global client
      client.close()
      self.figure.clf()
      self.canvas.draw()
      
   def OnExit(self,event):
      ret = wx.MessageBox('ȷ��Ҫ�˳���',  'Confirm', wx.OK|wx.CANCEL)
      if ret == wx.OK:
         try:
            global client
            client.close()
            event.Skip()
         except:
            event.Skip()
#################################################  ����Ϊ���ִ��룬���ÿ�############################################################
##################################################################################################################################           
   def ChangeToframe0(self,event):      
      self.figure.clf()
      #self.canvas.draw()
      global TYPE
      TYPE = 0
      self.mainbox.Show(self.box3)
      self.monitorST.Show(False)
      self.monitorCombox.Show(False)
      self.cirCfrST.Show(False)
      self.cirCfrCombox.Show(False)
      self.graghST.Show(False)
      self.graghCombox.Show(False)
      self.positionST.Show(False)
      self.positionCombox.Show(False)
      self.dateST.Show(False)
      self.dateCombox.Show(False)
      self.tianxianST.Show(False)
      self.tianxianCombox.Show(False)
      
      self.traingdatachooseLabel.Show(True)
      self.traingdatachooseText.Show(True)
      self.traingdatachooseButton.Show(True)
      self.testdatachooseLabel.Show(True)
      self.testdatachooseText.Show(True)
      self.testdatachooseButton.Show(True)
      self.TypechooseLabel.Show(True)
      self.typechooseCombox.Show(True)
      
      self.box1.Hide(self.box1_10)
      self.box1.Hide(self.box1_11)
      
      #self.onConnectButton.Show(False)
      self.onTrainButton.Show(False)
      self.onTrainOverButton.Show(False)
      
      self.box5_Border.Hide(self.DisplayText)
      self.DisplayText.Clear()
      self.box5_Border.Show(self.box5)
      self.startButton.Show(True)
      self.closeButton.Show(False)
      self.stopButton.Show(True)
      self.box1.Layout()
      self.box1_Border.Layout()
      self.box2.Layout()
      self.box2_Border.Layout()
      self.box5.Layout()
      self.box5_Border.Layout()
      self.box6.Layout()
      self.mainbox.Layout()
      
   def ChangeToframe1(self,event):      
      self.figure.clf()
      global TYPE
      TYPE = 1
      #self.canvas.draw()
      self.mainbox.Show(self.box3)
      self.monitorST.Show(True)
      self.monitorCombox.Show(True)
      self.cirCfrST.Show(True)
      self.cirCfrCombox.Show(True)
      self.graghST.Show(True)
      self.graghCombox.Show(True)
      self.positionST.Show(True)
      self.positionCombox.Show(True)
      self.dateST.Show(True)
      self.dateCombox.Show(True)
      self.tianxianST.Show(False)
      self.tianxianCombox.Show(False)
      self.startButton.Show(True)
      self.closeButton.Show(False)
      self.stopButton.Show(True)
            
      self.traingdatachooseLabel.Show(False)
      self.traingdatachooseText.Show(False)
      self.traingdatachooseButton.Show(False)
      self.testdatachooseLabel.Show(False)
      self.testdatachooseText.Show(False)
      self.testdatachooseButton.Show(False)
      self.TypechooseLabel.Show(False)
      self.typechooseCombox.Show(False)
      self.box1.Hide(self.box1_10)
      self.box1.Hide(self.box1_11)
      
      #self.onConnectButton.Show(False)
      self.onTrainButton.Show(False)
      self.onTrainOverButton.Show(False)
      self.box5_Border.Hide(self.DisplayText)
      self.DisplayText.Clear()
      self.box5_Border.Show(self.box5)
      self.box1.Layout()
      self.box1_Border.Layout()
      self.box2.Layout()
      self.box2_Border.Layout()
      self.box5.Layout()
      self.box5_Border.Layout()
      self.box6.Layout()
      self.mainbox.Layout()
      
   def ChangeToframe2(self,event):
      global Flag
      Flag = True
      global TYPE
      TYPE = 2
      try:
         self.figure.clf()
         #self.canvas.draw()
      except:
         pass
      self.positionST.Show(False)
      self.positionCombox.Show(False)
      self.dateST.Show(False)
      self.dateCombox.Show(False)
      self.startButton.Show(False)
      self.closeButton.Show(True)
      self.tianxianST.Show(True)
      self.tianxianCombox.Show(True)
      self.monitorST.Show(True)
      self.monitorCombox.Show(True)
      self.graghST.Show(True)
      self.graghCombox.Show(True)
      self.cirCfrST.Show(True)
      self.cirCfrCombox.Show(True)
      self.stopButton.Show(True)
      self.traingdatachooseLabel.Show(False)
      self.traingdatachooseText.Show(False)
      self.traingdatachooseButton.Show(False)
      self.testdatachooseLabel.Show(False)
      self.testdatachooseText.Show(False)
      self.testdatachooseButton.Show(False)
      self.TypechooseLabel.Show(False)
      self.typechooseCombox.Show(False)
      
      self.box1.Hide(self.box1_10)
      self.box1.Hide(self.box1_11)
      
      #self.onConnectButton.Show(False)
      self.onTrainButton.Show(False)
      self.onTrainOverButton.Show(False)
      self.box5_Border.Hide(self.DisplayText)
      self.DisplayText.Clear()
      self.box5_Border.Show(self.box5)
      
      self.box1.Layout()
      self.box1_Border.Layout()
      self.box2.Layout()
      self.box2_Border.Layout()
      self.box5.Layout()
      self.box5_Border.Layout()
      self.box6.Layout()
      self.mainbox.Layout()

   def ChangeToframe3(self,event):
      global Flag
      Flag = True
      if currentProgress != 100:
           dlg = wx.MessageDialog(None, u"���ݿ����ڶ�ȡ��,��ȴ�...", u"��ʾ", wx.OK | wx.ICON_INFORMATION)
           self.statusbar.SetStatusText("���ڶ�ȡ���ݿ⣬��ȴ�...")
           if dlg.ShowModal() == wx.ID_YES:
               self.Close(True)
           dlg.Destroy()
      else:
         global TYPE
         TYPE = 3   
         try:
            self.figure.clf()
            self.axes = self.figure.add_subplot(111)
            self.axes.set_title('Real-time Location')
            self.axes.set_xticks(np.linspace(0,10,6))
            self.axes.set_yticks(np.linspace(0,6,4))   
            self.axes.set_xticklabels( ('0', '2', '4', '6', '8','10'))
            self.axes.set_yticklabels( ('0', '2', '4', '6'))
            self.axes.grid(True)
            self.canvas.draw() 
         except:
            pass    
         self.mainbox.Hide(self.box3)  
         self.box5_Border.Hide(self.DisplayText)
         self.box5_Border.Show(self.box5)
         self.mainbox.Layout()   
          
   def ChangeToframe4(self,event):
      global Flag
      Flag = True
      if currentProgress != 100:
           dlg = wx.MessageDialog(None, u"���ݿ����ڶ�ȡ��,��ȴ�...", u"��ʾ", wx.OK | wx.ICON_INFORMATION)
           self.statusbar.SetStatusText("���ڶ�ȡ���ݿ⣬��ȴ�...")
           if dlg.ShowModal() == wx.ID_YES:
               self.Close(True)
           dlg.Destroy()
      else:
         global TYPE
         TYPE = 4   
         try:
            self.figure.clf()
            self.axes = self.figure.add_subplot(111)
            self.axes.set_title('Real-time Trace')
            self.axes.set_xticks(np.linspace(0,10,6))
            self.axes.set_yticks(np.linspace(0,6,4))   
            self.axes.set_xticklabels( ('0', '2', '4', '6', '8','10'))
            self.axes.set_yticklabels( ('0', '2', '4', '6'))
            self.axes.grid(True)
            self.canvas.draw() 
         except:
            pass
         self.mainbox.Hide(self.box3)  
         self.box5_Border.Hide(self.DisplayText)
         self.box5_Border.Show(self.box5)
         self.mainbox.Layout()            
      
   def ChangeToframe5(self,event):
      global TYPE
      TYPE = 5 
      global Flag
      Flag = True
      self.mainbox.Hide(self.box3)    
      self.box5_Border.Show(self.DisplayText)
      self.DisplayText.Clear()
      self.box5_Border.Hide(self.box5)
      self.box5_Border.Layout()
      self.box6.Layout()
      self.mainbox.Layout()
   def ChangeToframe6(self,event):
      global TYPE
      TYPE = 6
      global Flag
      Flag = False
      
      global Case
      Case = 0
      self.mainbox.Show(self.box3)
      self.box1.Hide(self.box1_1)
      self.box1.Hide(self.box1_2)
      self.box1.Hide(self.box1_3)
      self.box1.Hide(self.box1_4)
      self.box1.Hide(self.box1_5)
      self.box1.Hide(self.box1_6)
      self.box1.Hide(self.box1_7)
      self.box1.Hide(self.box1_8)
      self.box1.Hide(self.box1_9)
      self.box1.Show(self.box1_10)
      self.box1.Show(self.box1_11)
      self.box1.Layout()

      self.startButton.Show(False)
      self.closeButton.Show(False)
      self.stopButton.Show(False)      
      #self.onConnectButton.Show(True)
      self.onTrainButton.Show(True)
      self.onTrainOverButton.Show(True)
      
      self.box2.Layout()
      
      self.box5_Border.Show(self.DisplayText)
      self.DisplayText.Clear()
      self.DisplayText.AppendText("����ѵ����ť���ò�����")
      self.box5_Border.Hide(self.box5)
      self.box5_Border.Layout()
      self.mainbox.Layout()
   
   def ChangeToframe7(self,event):
      global TYPE
      TYPE = 7
      global Flag
      Flag = False
      
      global Case
      Case = 1
      for i in range(len(self.positionList)):
           if self.positionCombox.IsChecked(i)==True:
              self.positionCombox.Check(i, False)
      
      self.mainbox.Show(self.box3)
      self.box1.Hide(self.box1_1)
      self.box1.Hide(self.box1_2)
      self.box1.Hide(self.box1_3)
      self.box1.Hide(self.box1_4)
      self.box1.Show(self.box1_5)
      self.box1.Hide(self.box1_6)
      self.box1.Hide(self.box1_7)
      self.box1.Hide(self.box1_8)
      self.box1.Hide(self.box1_9)
      self.box1.Hide(self.box1_10)
      self.box1.Show(self.box1_11)
      self.box1.Layout()

      self.startButton.Show(False)
      self.closeButton.Show(False)
      self.stopButton.Show(False)
      #self.onConnectButton.Show(True)
      self.onTrainButton.Show(True)
      self.onTrainOverButton.Show(True)
      
      self.box2.Layout()
      
      self.box5_Border.Show(self.DisplayText)
      self.DisplayText.Clear()
      self.DisplayText.AppendText("����ѵ����ť���ò�����\nָ�Ƶ��ı���д��ʽ����: 2 0��10 6\n")
      self.box5_Border.Hide(self.box5)
      self.box5_Border.Layout()
      self.mainbox.Layout()
       
   
   def OndataChoose1(self,event):      
      dialog = wx.FileDialog(self,"ѡ�����ݿ�",os.getcwd(),style=wx.OPEN,wildcard="*.db")
     #�����и����ģ̬�Ի���ͷ�ģ̬�Ի���. ������Ҫ�Ĳ������ģ̬�Ի�������������¼�����Ӧ,
     #����ģ̬�Ի�����ʾʱ,�����Խ��������Ĳ���. �˴���ģ̬�Ի�����ʾ. �䷵��ֵ��wx.ID_OK,wx.ID_CANEL;
      if dialog.ShowModal() == wx.ID_OK:
        self.trainingName = dialog.GetPath()
        fileName =  dialog.GetPath().split("\\")[-1]
        self.traingdatachooseText.SetValue(fileName)  
      dialog.Destroy()
   def OndataChoose2(self,event):      
      dialog = wx.FileDialog(self,"ѡ�����ݿ�",os.getcwd(),style=wx.OPEN,wildcard="*.db")
      if dialog.ShowModal() == wx.ID_OK:
        self.testName = dialog.GetPath()
        fileName =  dialog.GetPath().split("\\")[-1]
        self.testdatachooseText.SetValue(fileName)          
      dialog.Destroy()
   def __init__(self,parent,iD,title):         
#��ȡ���ݿ�
     def ReadDataBase():
        global DataSet,LabelsFloatVector,currentProgress
        t1 = time.clock()
        print "��ʼ��ȡ���ݿ�"
        currentProgress = 0
        self.statusbar.SetStatusText("���ڶ�ȡ���ݿ⣬��ȴ�...")
       # filename = r'.\2016-8-13-22\Trainning_data\2PointTrainningdata500.db'   #2��Point�����ݿ�
       # filename = r'.\2016-5-7-16\Trainning_data\Trainingdata2000.db'   #4��Point�����ݿ�
        filename = r'.\2016-8-14-22\Trainning_data\2PointTrainningdata500.db'   #3��Point�����ݿ�
        DataSet,LabelsVector = RealTimeKnn.file2matrix(filename)  ## 48000*360�ľ���  list = [2000��(0,0) ,2000��(0,2) ...2000��(10,6)]
        DataSet,LabelsVector = RealTimeKnn.MoveAve(DataSet,LabelsVector,800,5)     ## 5784*360�ľ���  list = [241��(0,0) ,241��(0,2) ...241��(10,6)]
        DataSet              = RealTimeKnn.DataSubcarrierDiff(DataSet)   ##  5784*348�����ز��������
        DataSet,LabelsVector = RealTimeKnn.MoveAve(DataSet,LabelsVector,100,1) ## 3408*348�����ز��������  list = [(0,0)*142 ,(0,2)*142 ...(10,6)*142] 
        LabelsFloatVector = []
        for Labels in LabelsVector:
           LabelFloat = [float(re.sub(r"\D",'',Labels.split(',')[0])),float(re.sub(r"\D",'',Labels.split(',')[1]))]  #re.sub('[abc]', 'o', 'caps')  'oops'  
           LabelsFloatVector.append(LabelFloat)
         
        currentProgress = 100   
        t2 = time.clock()
        print "��ȡ���ݿ⻨��",t2-t1
        self.statusbar.SetStatusText("���ݿ���سɹ�...")
        return DataSet,LabelsFloatVector
#���������
     def ProgressDialogShow():
        progressMax = 100
        dialog = wx.ProgressDialog("A progress box", "Time remaining", progressMax, 
        style= wx.PD_CAN_ABORT | wx.PD_ELAPSED_TIME | wx.PD_REMAINING_TIME)  
        keepGoing = True  
        count = 0  
        while keepGoing and count < progressMax:  
           count = count + 4  
           wx.Sleep(1)             
           keepGoing = dialog.Update(count)  
        dialog.Destroy()
#��ȡ��Ŀ¼�����������
     def GETDate():
         fileDir=os.path.abspath("")
         date=[]         
         for root,dirs,files in os.walk(fileDir): #����ÿ��Ŀ¼�� ( ����Ŀ¼�б��ļ��б�)
            #print root,dirs,files
            for fr in dirs:
               if ('2016' in fr):
                  date.append(fr)
         return date
     
     wx.Frame.__init__(self,parent,iD,title)
     self.statusbar = self.CreateStatusBar()
     self.statusbar.SetStatusText("�ȴ���������...")
   
     thread = threading.Thread(target=ReadDataBase)
     thread.start()
     global TYPE
     TYPE = 1
     self.panel = wx.Panel(self,-1)
     #���������
     self.monitorList = ['all','point0','point1','point2','point3']
     self.monitorST = wx.StaticText(self.panel,-1,'�����㣺',style = wx.ALIGN_LEFT)
     self.monitorCombox = wx.ComboBox(self.panel,-1,'all',choices=self.monitorList)

     #���ӻ�ͼ�ε�����
     graghList = ['heatMap','lineChart']
     self.graghST = wx.StaticText(self.panel,-1,'��ʾ��ʽ��',style = wx.ALIGN_LEFT)
     self.graghCombox = wx.ComboBox(self.panel,-1,'heatMap',choices=graghList)

     #CIR/CFR
     cirCfrList = ['CIR','CFR']
     self.cirCfrST = wx.StaticText(self.panel,-1,'CIR/CFR��',style = wx.ALIGN_LEFT)
     self.cirCfrCombox = wx.ComboBox(self.panel,-1,'CFR',choices=cirCfrList)
     
    
     self.positionList = ['(00,00)','(02,00)','(04,00)','(06,00)','(08,00)',
                     '(10,00)','(00,02)','(02,02)','(04,02)','(06,02)',
                     '(08,02)','(10,02)','(00,04)','(02,04)','(04,04)',
                     '(06,04)','(08,04)','(10,04)','(00,06)','(02,06)',
                     '(04,06)','(06,06)','(08,06)','(10,06)']
     self.positionST = wx.StaticText(self.panel,-1,'ָ�Ƶ����꣺',style = wx.ALIGN_LEFT)
     self.positionCombox = wx.CheckListBox(self.panel,-1,choices=self.positionList,
                                      size=(90,20),style=wx.LB_MULTIPLE)
     #����ѡ��
     self.dateST = wx.StaticText(self.panel,-1,'����ѡ��',style = wx.ALIGN_LEFT)
     self.dateCombox = wx.ComboBox(self.panel,-1,'��ѡ������',choices=GETDate())

     #����ѡ��
     self.tianxianList = ['1','2','3']
     self.tianxianST = wx.StaticText(self.panel,-1,'����ѡ��',style = wx.ALIGN_LEFT)
     self.tianxianCombox = wx.ComboBox(self.panel,-1,'2',choices=self.tianxianList)
     self.tianxianST.Show(False)
     self.tianxianCombox.Show(False)  

     #ѵ�����ݿ�ѡ��
     self.traingdatachooseLabel = wx.StaticText(self.panel,-1,'ѵ�����ݣ�',style = wx.ALIGN_LEFT)
     self.traingdatachooseText = wx.TextCtrl(self.panel,-1,"",style=wx.TE_READONLY)
     self.traingdatachooseText.SetValue('��ѡ��ѵ������')  
     self.traingdatachooseButton = wx.Button(self.panel , -1, 'Choose' , size =(50, 20))
     self.Bind(wx.EVT_BUTTON,self.OndataChoose1,self.traingdatachooseButton)
     self.traingdatachooseLabel.Show(False)
     self.traingdatachooseText.Show(False)
     self.traingdatachooseButton.Show(False)
     #�������ݿ�ѡ��
     self.testdatachooseLabel = wx.StaticText(self.panel,-1,'�������ݣ�',style = wx.ALIGN_LEFT)
     self.testdatachooseText = wx.TextCtrl(self.panel,-1,"",style=wx.TE_READONLY)
     self.testdatachooseText.SetValue('��ѡ���������')  
     self.testdatachooseButton = wx.Button(self.panel , -1, 'Choose' ,size =(50, 20))
     self.Bind(wx.EVT_BUTTON,self.OndataChoose2,self.testdatachooseButton)
     self.testdatachooseLabel.Show(False)
     self.testdatachooseText.Show(False)
     self.testdatachooseButton.Show(False)
     #ͼ��ѡ��
     self.TypechooseLabel = wx.StaticText(self.panel,-1,'ͼ��ѡ��',style = wx.ALIGN_LEFT)
     self.typechooseList = ['���Խ��','�������','���ֲ�']
     self.typechooseCombox = wx.CheckListBox(self.panel,-1,choices=self.typechooseList,
                                      size=(90,50),style=wx.LB_MULTIPLE)
     self.typechooseCombox.SetChecked([0,1,2])
     self.TypechooseLabel.Show(False)
     self.typechooseCombox.Show(False)   
     self.personLabel = wx.StaticText(self.panel, -1, "��           ��:")
     self.personCtrl = wx.TextCtrl(self.panel, -1)
     self.personCtrl.SetEditable(False)
     
     self.timeLabel = wx.StaticText(self.panel, -1, "ѵ��ʱ��(��):")
     self.timeCtrl = wx.TextCtrl(self.panel, -1)
     self.timeCtrl.SetEditable(False)
     self.box1_7 = wx.BoxSizer()
     self.box1_7.Add(self.traingdatachooseLabel,1,wx.ALL|wx.EXPAND,0)
     self.box1_7.Add(self.traingdatachooseText,0,wx.ALL,0)
     self.box1_7.Add(self.traingdatachooseButton,0,wx.LEFT,5)
     self.box1_8 = wx.BoxSizer()
     self.box1_8.Add(self.testdatachooseLabel,1,wx.ALL|wx.EXPAND,0)
     self.box1_8.Add(self.testdatachooseText,0,wx.ALL,0)
     self.box1_8.Add(self.testdatachooseButton,0,wx.LEFT,5)
     self.box1_9 = wx.BoxSizer()
     self.box1_9.Add(self.TypechooseLabel,1,wx.ALL|wx.EXPAND,0)
     self.box1_9.Add(self.typechooseCombox,2,wx.ALL,0)
     self.box1_1 = wx.BoxSizer()
     self.box1_1.Add(self.dateST,1,wx.ALL|wx.EXPAND,0)
     self.box1_1.Add(self.dateCombox,1,wx.ALL|wx.EXPAND,0)
     self.box1_2 = wx.BoxSizer()
     self.box1_2.Add(self.monitorST,1,wx.ALL|wx.EXPAND,0)
     self.box1_2.Add(self.monitorCombox,1,wx.ALL|wx.EXPAND,0)
     self.box1_3 = wx.BoxSizer()
     self.box1_3.Add(self.graghST,1,wx.ALL|wx.EXPAND,0)
     self.box1_3.Add(self.graghCombox,1,wx.ALL|wx.EXPAND,0)
     self.box1_4 = wx.BoxSizer()
     self.box1_4.Add(self.cirCfrST,1,wx.ALL|wx.EXPAND,0)
     self.box1_4.Add(self.cirCfrCombox,1,wx.ALL|wx.EXPAND,0)
     self.box1_5 = wx.BoxSizer()
     self.box1_5.Add(self.positionST,1,wx.ALL|wx.EXPAND,0)
     self.box1_5.Add(self.positionCombox,1,wx.ALL|wx.EXPAND,0)
     self.box1_6 = wx.BoxSizer()     
     self.box1_6.Add(self.tianxianST,1,wx.ALL|wx.EXPAND,0)
     self.box1_6.Add(self.tianxianCombox,1,wx.ALL|wx.EXPAND,0)     
     self.box1_10 = wx.BoxSizer()
     self.box1_10.Add(self.personLabel,0,wx.ALL,0)
     self.box1_10.Add(self.personCtrl, 1,wx.ALL,0)     
     self.box1_11 = wx.BoxSizer()
     self.box1_11.Add(self.timeLabel,0,wx.ALL,0)
     self.box1_11.Add(self.timeCtrl, 1,wx.ALL,0)
           
     self.box1 = wx.BoxSizer(wx.VERTICAL)
     self.box1.Add(self.box1_1,1,wx.EXPAND|wx.ALL,0)
     self.box1.Add(self.box1_2,1,wx.EXPAND|wx.ALL,0)
     self.box1.Add(self.box1_3,1,wx.EXPAND|wx.ALL,0)
     self.box1.Add(self.box1_4,1,wx.EXPAND|wx.ALL,0)
     self.box1.Add(self.box1_11,1,wx.EXPAND|wx.ALL,0)
     self.box1.Add(self.box1_6,1,wx.EXPAND|wx.ALL,0)
     self.box1.Add(self.box1_7,1,wx.EXPAND|wx.ALL,0)
     self.box1.Add(self.box1_8,1,wx.EXPAND|wx.ALL,0)
     self.box1.Add(self.box1_9,1,wx.EXPAND|wx.ALL,0)
     self.box1.Add(self.box1_10,1,wx.EXPAND|wx.ALL,0)
     self.box1.Add(self.box1_5,1,wx.EXPAND|wx.ALL,0)
     self.box1.Hide(self.box1_10)
     self.box1.Hide(self.box1_11)
     
     self.box1_sb = wx.StaticBox(self.panel,-1,'      ����  ')
     self.box1_Border=wx.StaticBoxSizer(self.box1_sb,wx.VERTICAL)
     self.box1_Border.Add(self.box1,1,wx.ALL,15)


     self.startButton = wx.Button(self.panel,-1,'����')
     self.Bind(wx.EVT_BUTTON,self.OnClickStart,self.startButton)
     self.stopButton = wx.Button(self.panel,-1,'ֹͣ')
     self.Bind(wx.EVT_BUTTON,self.OnClickStop,self.stopButton)
     self.closeButton = wx.Button(self.panel,-1,'��������')
     self.Bind(wx.EVT_BUTTON,self.OnClickClose,self.closeButton)
     self.closeButton.Show(False)
     
     #��ԲԲ�ӵĿؼ�  ��ԲԲ��ѵ����ť
     '''self.onConnectButton = wx.Button(self.panel, -1, '����')
     self.onConnectButton.Show(False)
     self.Bind(wx.EVT_BUTTON,self.OnConnect, self.onConnectButton)'''
     self.onTrainButton = wx.Button(self.panel, -1, 'ѵ��')
     self.onTrainButton.Show(False)
     self.Bind(wx.EVT_BUTTON,self.OnTrainModel, self.onTrainButton)
     
     #��ԲԲ�ӵĿؼ�  ���ε�ѵ����ť
     self.onTrainOverButton = wx.Button(self.panel, -1, '����')
     self.onTrainOverButton.Show(False)
     self.Bind(wx.EVT_BUTTON,self.OnTrainOver, self.onTrainOverButton)
     
     self.box2 = wx.BoxSizer()
     self.box2.Add(self.startButton,0,wx.ALL,20)
     self.box2.Add(self.closeButton,0,wx.ALL,20)
     self.box2.Add(self.stopButton,0,wx.ALL,20)
     #self.box2.Add(self.onConnectButton,0,wx.ALL,20)
     self.box2.Add(self.onTrainButton,0,wx.ALL,20)
     self.box2.Add(self.onTrainOverButton,0,wx.ALL,20)

     self.box2_sb = wx.StaticBox(self.panel,-1,'     ��ť  ')
     self.box2_Border=wx.StaticBoxSizer(self.box2_sb,wx.VERTICAL)
     self.box2_Border.Add(self.box2,wx.ALL,15)

     self.box3 = wx.BoxSizer(wx.VERTICAL)
     self.box3.Add(self.box1_Border,1,wx.EXPAND|wx.ALL,3)
     self.box3.Add(self.box2_Border,0,wx.EXPAND|wx.ALL,3)
     
     #self.staticTC=wx.TextCtrl(panel,-1,"",style=wx.TE_MULTILINE)
     #box4 = wx.BoxSizer()
     #box4.Add(self.staticTC,1,wx.EXPAND|wx.ALL)
     #box4_Border=wx.StaticBoxSizer(wx.StaticBox(panel,-1,'״̬��ʾ'),wx.VERTICAL)
     #box4_Border.Add(box4,1,wx.EXPAND|wx.ALL,5)

     self.Bind(wx.EVT_CLOSE,self.OnExit)  #��д���Ͻ��˳���
     self.menubar=wx.MenuBar()
     self.file=wx.Menu()
     self.menubar.Append(self.file,'&��̬')     
     self.file.Append(101,'&��̬��ͼ','���ػ�ͼ���������Ա���')
     self.file.Append(102,'&��̬��λ','���ض�λ���������Ա��أ�������������')
     self.file.Append(103,'&�˳�','�˳�����')
     self.file.AppendSeparator()
     wx.EVT_MENU(self, 101, self.ChangeToframe1)
     wx.EVT_MENU(self, 102, self.ChangeToframe0)
     wx.EVT_MENU(self, 103, self.OnQuit)
     self.file2=wx.Menu()
     self.menubar.Append(self.file2,'&ʵʱ')
     self.file2.Append(201,'&ʵʱ��ͼ','ʵʱ��ͼ����������Զ��') #kind=wx.ITEM_RADIO
     self.file2.Append(202,'&ʵʱ��λ','ʵʱ��λ����������Զ��')
     self.file2.Append(203,'&��λ׷��','���ж�λ׷��')
     self.file2.Append(204,'&��������','��������Ԥ��')
     self.file3=wx.Menu()
     self.menubar.Append(self.file3,'&ѵ��')
     self.file3.Append(301,'&����ѵ��','ʵʱѵ��') #kind=wx.ITEM_RADIO
     self.file3.Append(302,'&��λѵ��','ʵʱѵ��') #kind=wx.ITEM_RADIO
     wx.EVT_MENU(self, 201, self.ChangeToframe2)
     wx.EVT_MENU(self, 202, self.ChangeToframe3)
     wx.EVT_MENU(self, 203, self.ChangeToframe4)
     wx.EVT_MENU(self, 204, self.ChangeToframe5)     
     wx.EVT_MENU(self, 301, self.ChangeToframe6)
     wx.EVT_MENU(self, 302, self.ChangeToframe7)
     
     self.file2.AppendSeparator()
     self.file3.AppendSeparator()
     self.SetMenuBar(self.menubar)     

     self.figure = Figure()
     self.axes = self.figure
     self.canvas = FigureCanvas(self.panel, -1, self.figure)
     self.toolbar = NavigationToolbar(self.canvas)
     self.DisplayText=wx.TextCtrl(self.panel,-1,"",style=wx.TE_MULTILINE)
     #self.DisplayText.Show(False)
     self.box5 = wx.BoxSizer(wx.VERTICAL)
     self.box5.Add(self.toolbar,0,wx.EXPAND|wx.ALL)
     self.box5.Add(self.canvas,1,wx.EXPAND|wx.ALL)
     self.box5_Border=wx.StaticBoxSizer(wx.StaticBox(self.panel,-1,'״̬��ʾ'),wx.VERTICAL)
     self.box5_Border.Add(self.box5,1,wx.EXPAND|wx.ALL,5)
     self.box5_Border.Add(self.DisplayText,1,wx.EXPAND|wx.ALL,5)     
     self.box5_Border.Hide(self.DisplayText)
     
     self.box6 = wx.BoxSizer(wx.VERTICAL)
     self.box6.Add(self.box5_Border,4,wx.EXPAND|wx.ALL,3)
     #self.box6.Add(self.DisplayText,4,wx.EXPAND|wx.ALL,3)
     #box6.Add(box4_Border,1,wx.EXPAND|wx.ALL,10)     

     self.mainbox = wx.BoxSizer()
     self.mainbox.Add(self.box3,0,wx.EXPAND|wx.ALL,3)
     self.mainbox.Add(self.box6,1,wx.EXPAND|wx.ALL,3)
     
     self.panel.SetSizer(self.mainbox)
     self.mainbox.Fit(self)
     self.mainbox.SetSizeHints(self)
     self.testlabel=[]  #syy
     self.testdata=[]   #syy
     self.CreatDIR = True
class MyApp(wx.App):
    def OnInit(self):
        frame= MyFrame(None,-1,'���ӻ�����')
        frame.Show(True)
        return True

def mainFunc():
    app = MyApp(0)
    app.MainLoop()

if __name__=='__main__':
    mainFunc()
 
