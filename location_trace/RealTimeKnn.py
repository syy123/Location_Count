#!/usr/bin/env python
#coding:utf-8

from numpy import *
import os
#import xlrd
import matplotlib.pyplot as plt
import sqlite3
import re
from matplotlib.ticker import MultipleLocator, FuncFormatter
import numpy as np
import time

global_MaxPoint = 100                                         #指纹点单点最高数据行数
global_MaxX = 10.0                                              #定位区域最大X
global_MaxY = 6.0                                               #定位区域最大Y


def file2matrix(filename):                                              #读取EXCEL或DB文件矩阵
    if os.path.splitext(filename)[1] == '.db':
        con = sqlite3.connect(filename)
        cu = con.cursor()
        con.row_factory = sqlite3.Row
        sqls = r'select * from datacounts'
        cu.execute(sqls)
        rows = cu.fetchall()   
        m = len(rows)          #datacounts表中有多少条   48000
        n = len(rows[0]) - 1   #  361-1 = 360
        returnMat = zeros((m,n))
        classLabelVector = []
        for i in range(m):
            classLabelVector.append(rows[i][0])
            returnMat[i,:] = rows[i][1:]
        return returnMat,classLabelVector  #48000*360矩阵   [48000]列表
    elif os.path.splitext(filename)[1] == '.xls':
        fxls = xlrd.open_workbook(filename)
        for i in range(4):
            rs = fxls.sheet_by_index(i)
            numberOfLines = rs.nrows
            tmpMat = zeros((numberOfLines,90))
            classLabelVector = []
            index = 0
            for j in range(0,rs.nrows):
                colnames = rs.row_values(j)
                tmpMat[index,:] = colnames[:90]
                index += 1
                classLabelVector.append(colnames[-1])
            if i == 0 :
                returnMat = tmpMat
            else:
                returnMat = returnMat.transpose()
                tmpMat = tmpMat.transpose()
                returnMat = vstack((returnMat,tmpMat))
                returnMat = returnMat.transpose()
        '''fxls = xlrd.open_workbook(filename)
        rs = fxls.sheet_by_index(0)
        numberOfLines = rs.nrows
        returnMat = zeros((numberOfLines-1,12))
        classLabelVector = []
        index = 0
        for i in range(1,rs.nrows):
            colnames = rs.row_values(i)
            returnMat[index,:] = colnames[:12]
            index += 1
            classLabelVector.append(colnames[-1])'''
        return returnMat,classLabelVector
    else:
        raise NameError('We Have a Problem -- \
    That file is not recognized')

def nopersondatafile2matrix(filename):
    fxls = xlrd.open_workbook(filename)
    for i in range(4):
        rs = fxls.sheet_by_index(i)
        numberOfLines = rs.nrows
        returnNopersondataMat = zeros((numberOfLines,90))
        classLabelVector = []
        index = 0
        for j in range(0,rs.nrows):
            colnames = rs.row_values(j)
            returnNopersondataMat[index,:] = colnames[:90]
            index += 1
        if i == 0 :
            returnMat = returnNopersondataMat
        else:
            returnMat = returnMat.transpose()
            returnNopersondataMat = returnNopersondataMat.transpose()
            returnMat = vstack((returnMat,returnNopersondataMat))
            returnMat = returnMat.transpose()
    returnNopersondataMatAve=np.mean(returnMat,axis=0)
    print len(returnNopersondataMatAve)
    return returnNopersondataMatAve

def DataMinusNoPerson(Data,NopersonData):
    numbers=len(Data)
    print len(NopersonData)
    print "Data",len(Data)
    print len(NopersonData)
    returnMatDiff=Data-tile(NopersonData, (numbers,1))
    return np.abs(returnMatDiff)
    
def labels2float(labels):                                                   #将label转化为float类型，方便后续计算
    labelsfloat = []
    for label in labels:
        labelfloat = [float(re.sub(r"\D",'',label.split(',')[0])),float(re.sub(r"\D",'',label.split(',')[1]))]
        labelsfloat.append(labelfloat)

def caldistance(position1,position2):                                   #计算两坐标之间的距离
    distance = ((position1[0] - position2[0])*0.5)**2 + ((position1[1] - position2[1])*0.5)**2
    distance = distance ** 0.5
    return distance

def AveInArr(dataSet,labelsList,Avek):                                  #求矩阵平均函数
    DataSet = []
    returnLabels = []
    Line = len(dataSet)
    indexCount = Line / Avek
    for index in range(indexCount):
        tmpdata = dataSet[index*Avek:index*Avek+Avek]
        tmpline = mean(tmpdata,axis=0)
        DataSet.append(tmpline)
        returnLabels.append(labelsList[index*Avek])
    DataSet = array(DataSet)
    return DataSet,returnLabels

def MoveAve(dataSet,labelsList,WindowsSize,gap):                 #滑动平均函数
    line = len(dataSet)                 #(第一次)48000*360   (第二次)5784 * 348 
    pointCounts=len(set(labelsList))#测试点坐标  ，(第一次)24 (第二次) 24
    numbers=line/pointCounts#每个测试点取得数据条数  #(第一次)2000   (第二次)241
    print "Line",line   
    print "pointCounts",pointCounts
    print "numbers",numbers
    dataPoint=[]
    dataPointLabel=[]
    for i in range(pointCounts):
        dataPoint.append(dataSet[numbers*i:numbers*(i+1)])#(第一次)[ [2000*360],[2000*360]...[2000*360] ]24个  (第二次) [ [241*348] ,[241*348]...[241*348]] 24个
        dataPointLabel.append(labelsList[numbers*i:numbers*(i+1)])  #(第一次)[[2000]...[2000]]24个    (第二次) [[241]...[241]]24个
        
    DataList=[]
    returnLabels=[]
    count=(numbers-WindowsSize)/gap#滑动窗移动的次数  (第一次)240  (第二次) 141
    
    for i in range(pointCounts):  #24
        for j in range(count+1):  #(第一次)241  (第二次)142
            dataLine=mean(dataPoint[i][j*gap:(WindowsSize+j*gap)],axis=0)   # (第一次) 将2000*360矩阵的0-800行进行平均，得到1行。。依次
            DataList.append(dataLine)     #(第一次)一个dataLine是长度360的向量，一个点共241个向量 ，共24个点   [ [1*360],[1*360]... ]  24*241=5784个
                                          #(第二次)一个dataLine是长度348的向量，一个点共142个向量 ，共24个点   [ [1*348],[1*348]... ]  24*142=3408个
            returnLabels.append(dataPointLabel[i][j*gap])               #(第一次)[ (0,0)*241 ,(0,2)*241 ...(10,6)*241]   总len是24*241=5784
                                                                        #(第二次)[ [0.0,0.0]*142 ,[0.0,2.0]*142 ...[10.0,6.0]*142]   总len是24*142=3408
    Data = array(DataList)    #(第一次)5784*360  
    return Data,returnLabels    #  (第一次)5784*360矩阵,[5784]列表  (第二次)3408*348矩阵，[3408]列表

def RealTimeDataMoveAve(dataSet,WindowsSize,gap):                 #滑动平均函数
                # dataSet=50*348的误差矩阵   WindowsSize=10  gap=5      
    
    line = len(dataSet)    
    DataList=[]
    count=(line-WindowsSize)/gap#滑动窗移动的次数
    for i in range(count+1):  # 9
        dataLine=mean(dataSet[i*gap:(WindowsSize+i*gap)],axis=0)
        DataList.append(dataLine)
    Data = array(DataList)
  
    return Data

def DataSubcarrierDiff(Data):   #5784*360     #50*360
    #print "len(Data)",len(Data)
    width =len(Data[0])*29/30   #348
    liuCount = len(Data[0])/30
    DataDiff = zeros((len(Data),width))
    for k in range(len(Data)): #5784        #50
        for i in range(liuCount):
            for j in range(29):
                DataDiff[k,29*i+j]=Data[k,30*i+j+1]-Data[k,30*i+j]
    Data=np.abs(DataDiff)
    return Data     #5784*348    #50*348

def DataDiffAveAndVar(DataDiff,labelsList,WindowsSize,gap):
    line = len(DataDiff)
    pointCounts=len(set(labelsList))#测试点坐标
    numbers=line/pointCounts#每个测试点取得数据条数
    dataPoint=[]
    dataPointLabel=[]
    for i in range(pointCounts):
        dataPoint.append(DataDiff[numbers*i:numbers*(i+1)])#将每个点处的数据存入dataPoint
        dataPointLabel.append(labelsList[numbers*i:numbers*(i+1)])
        
    DataList=[]
    returnLabels=[]
    count=(numbers-WindowsSize)/gap#滑动窗移动的次数
    for i in range(pointCounts):
        for j in range(count+1):
            dataLineMean=mean(dataPoint[i][j*gap:(WindowsSize+j*gap)],axis=0)#按列求平均值
            varValue=var(dataPoint[i][j*gap:(WindowsSize+j*gap)],axis=0)
            #var=mean(dataPoint[i][j*gap:(WindowsSize+j*gap)]**2,axis=0)-dataLineMean**2#方差
            DataList.append(dataLineMean.tolist())
            #DataList.append(var)
            returnLabels.append(dataPointLabel[i][j*gap])
    #print len(DataList[0])
    Data = array(DataList)
    return Data,returnLabels
def TruncationFunc(Data):
    for i in range(len(Data)):
        CFROriginalComplex=[]
        for x in range(len(Data[0])/2):
            CFROriginalComplex.append(complex(float(Data[i][2*x]),float(Data[i][2*x+1])))
        for j in range(12):
            CIRAmplitude=[]
            CFRFilter=[]
            CIR=np.fft.ifft(CFROriginalComplex[j*30:(j+1)*30])
            for j in range(len(CIR)):
                Amplitude=((CIR[j].real)**2+(CIR[j].imag)**2)**0.5
                CIRAmplitude.append(Amplitude)
            for j in range(1,len(CIRAmplitude)):
                if CIRAmplitude[j-1]<CIRAmplitude[j] and CIRAmplitude[j]>CIRAmplitude[j+1]:
                    FirstPeakValue=CIRAmplitude[i]
                    break
            for j in range(len(CIRAmplitude)):
                if CIRAmplitude[j]<0.5*FirstPeakValue:
                    CIR[j]=0   
            CFRFilter=np.fft.fft(CIR)
            for j in range(len(CFRFilter)):
                CFRFilterValue.append(round(((CFRFilter[j].real)**2+(CFRFilter[j].imag)**2)**0.5,4))#取小数点后的四位有效数字
                #CFRFilterValue.append(round(CFRFilter[j].imag,4))
    return Data
def DataMatMerge(Data1,labelsList1,Data2,labelsList2):
    line = len(Data1)
    pointCounts=len(set(labelsList1))#测试点坐标
    numbers=line/pointCounts#每个测试点取得数据条数
    dataPoint=[]
    dataPointLabel=[]
    for i in range(pointCounts):
        dataPoint=dataPoint+np.concatenate((Data1[numbers*i:numbers*(i+1)],Data2[numbers*i:numbers*(i+1)])).tolist()#将每个点处的数据存入dataPoint
        dataPointLabel=dataPointLabel+labelsList1[numbers*i:numbers*(i+1)]+labelsList2[numbers*i:numbers*(i+1)]
        #print "dataPoint",len(dataPoint)
        #print "dataPointLabel",len(dataPointLabel)
    Data=np.array(dataPoint)
    print len(Data)
    #labelList=labelList1+labelList2
    return Data,dataPointLabel
    
def classify0(inX, dataSet, PositionVec, distanceTrunc):      #找出最近k点的坐标

    #inX = [348]   dataSet= 3408*348矩阵  PositionVec=[ [0.0,0.0]*142 ,[0.0,2.0]*142 ...[10.0,6.0]*142]   distanceTrunc=0.1
    
    dataSetSize = dataSet.shape[0]                            #dataSet.shape = (3408,348)  ,得到dataSet的行数
    diffMat = tile(inX, (dataSetSize,1)) - dataSet            # 将inX扩展到和dataSet一样的行数  并减去dataSet
                                                              #diffMat = 3408*348   
    sqDiffMat = diffMat ** 2                                  #sqDuffMat = 3408*348
    sqDistances = sqDiffMat.sum(axis = 1)                     #矩阵每行元素计算和值  sqDistances = [3408]向量 ，平方和
    distances = sqDistances ** 0.5                            #计算得到距离矩阵(k,1)  distances =[3408]向量 ，取根号
    sortedDistIndicies = distances.argsort()                  #得到距离矩阵从小到大的索引值   sortedDistIndicies = [3408]向量 ，索引排序
    distanceRange = distances[sortedDistIndicies[-1]] - distances[sortedDistIndicies[0]] #计算距离矩阵范围  , （最大值-最小值）
    distanceTrunc = distanceTrunc * distanceRange + distances[sortedDistIndicies[0]] #计算距离矩阵截断值 ,  【最小值+（最大值-最小值）*0.1】
    voteIposition = []                                        #清空返回坐标矩阵
    distancesVec = []
    for i in range(len(sortedDistIndicies)):                  #根据距离矩阵截断值获得截断索引值 3408
        if distances[sortedDistIndicies[i]] > distanceTrunc:
            Truncindex = i                  
            break                                             # 找出第一个大于 距离矩阵截断值 的索引值
    
    if Truncindex > global_MaxPoint:                         #如果阶段索引值超过了最大点数（100）则取最大点数
        Truncindex = global_MaxPoint
    for i in range(Truncindex):
        voteIposition.append(PositionVec[sortedDistIndicies[i]]) #得到距离坐标  [[8.0, 2.0], [8.0, 2.0]....]
        distancesVec.append(distances[sortedDistIndicies[i]])    #得到距离矩阵   [12.019411182260638, 12.019416144806179,...]
    #print voteIposition,distancesVec,Truncindex
    return voteIposition, distancesVec,Truncindex           #返回距离坐标矩阵及截断索引

def partdomain(LastPositons,tmpcount):                                     #对预测点进行分区域权重判断输出最有可能的界域

    # 按权值从小到大顺序返回LastPositons=[[8.0, 2.0], [6.0, 0.0]] ，和它们的权值tmpcount = [0.6868686868686872, 1.0266666666666662]
    # 一般情况下返回值 LastPositons = LastPositons[-1]

    
    MaxX = global_MaxX   #10
    MaxY = global_MaxY   #6
    MinX = 0.0
    MinY = 0.0
    
    while(1):
        Comparequanzhong = [0.0,0.0]
        Pointcount1 = 0
        Pointcount2 = 0
        cmpposition1 = []
        cmpposition2 = []
        cmpcounts1 = []
        cmpcounts2 = []
        if (MaxY - MinY > 0.5)and(len(LastPositons) > 1):
            median = (MaxY - MinY) / 2.0 + MinY   # 3
            for i in range(len(LastPositons)):
                if LastPositons[i][1] <= median:   # 2 <= 3   0<=3
                    Comparequanzhong[0] += tmpcount[i]    # Comparequanzhong = [0.6868686868686872+1.0266666666666662,0.0]
                    cmpposition1.append(LastPositons[i])   # cmpposition1 = [[8.0, 2.0],[6.0, 0.0]]
                    cmpcounts1.append(tmpcount[i])   # cmpcounts1 = [0.6868686868686872,1.0266666666666662]

                if LastPositons[i][1] >= median:
                    Comparequanzhong[1] += tmpcount[i]
                    cmpposition2.append(LastPositons[i])
                    cmpcounts2.append(tmpcount[i])
            #Y轴两分后进行比较        
            if  Comparequanzhong[0] > Comparequanzhong[1]:
                MaxY = median
                LastPositons = cmpposition1
                tmpcount = cmpcounts1 
            if Comparequanzhong[0] < Comparequanzhong[1]:
                MinY = median
                LastPositons = cmpposition2
                tmpcount = cmpcounts2
            #print "here1",cmpposition1,cmpposition2,cmpcounts1,cmpcounts2,LastPositons,tmpcount
            #print LastPositons,tmpcount
        else:
            break
        Comparequanzhong = [0.0,0.0]
        cmpposition1 = []
        cmpposition2 = []
        cmpcounts1 = []
        cmpcounts2 = []
        if (MaxX - MinX > 0.5)and(len(LastPositons) > 1):
            median = (MaxX - MinX) / 2.0 + MinX
            for i in range(len(LastPositons)):
                if LastPositons[i][0] <= median:
                    Comparequanzhong[0] += tmpcount[i]
                    cmpposition1.append(LastPositons[i])
                    cmpcounts1.append(tmpcount[i])

                if LastPositons[i][0] >= median:
                    Comparequanzhong[1] += tmpcount[i]
                    cmpposition2.append(LastPositons[i])
                    cmpcounts2.append(tmpcount[i])
            #X轴两分后进行比较
            if  Comparequanzhong[0] > Comparequanzhong[1]:
                MaxX = median
                LastPositons = cmpposition1
                tmpcount = cmpcounts1                      
            if Comparequanzhong[0] < Comparequanzhong[1]:
                MinX = median
                LastPositons = cmpposition2
                tmpcount = cmpcounts2
            #print "here2",cmpposition1,cmpposition2,cmpcounts1,cmpcounts2,LastPositons,tmpcount
        else:
            break    
    
    return LastPositons

def QuanzhongSorted(voteIposition,distancesVec,k):                         #对于测点进行统合同时计算总得权重总值并排序
##   voteIposition=[[8.0, 2.0], [8.0, 2.0]....]   distancesVec=[12.019411182260638, 12.019416144806179,...]  k=100

    # 长度为k,距离从小到大排列的向量distancesVec，以及此距离所对应的坐标向量voteIposition，里面可能包含[8.0, 2.0]，[6.0, 0.0]等坐标点
    # 对这些坐标按距离进行权重排序，比如坐标向量中前23个坐标是[8,2]，第24个坐标出现[6,0]，则它们的权值分别是100/4950 ,76/4950
    # 最后返回加权好的，按权值从小到大排列的坐标排序

    
    TmpPositions = []
    Count = []
    quanzhongsum = 0
    for i in range(k):  #100
        quanzhongsum += i    #4950
            
    for Position in voteIposition:                                      #将k个点内出现的不同坐标点以距离远近不同权重进行求和
        if Position not in TmpPositions:
            TmpPositions.append(Position)     #TmpPositions=[[6.0, 0.0]]     [[6.0, 0.0], [8.0, 2.0]]  ...
            quanzhong = float(k - voteIposition.index(Position)) / float(quanzhongsum)
            Count.append(quanzhong)       #Count=[100/4950, ]   [0.4646464646464648, 0.015555555555555555]
           # print TmpPositions,"a",Count
        else:
            index = TmpPositions.index(Position)
            quanzhong = float(k - voteIposition.index(Position)) / float(quanzhongsum)
            Count[index] += quanzhong
          #  print quanzhong,"b",Count
    tmpcount = sorted(Count)                        #将求和得出的count进行排序，同时以此排序结果对坐标进行排序  tmpcount=[0.6868686868686872, 1.0266666666666662]
    LastPositons = []                               
    for i in tmpcount:
        index = Count.index(i)
        LastPositons.append(TmpPositions[index])    #LastPositons = [[8.0, 2.0], [6.0, 0.0]]
    return LastPositons,tmpcount  
        
def Trianglecentroid(voteIposition,distancesVec,k):                        #得到最近的k个点后估算出坐标点

##   voteIposition=[[8.0, 2.0], [8.0, 2.0]....]   distancesVec=[12.019411182260638, 12.019416144806179,...]  k=100

    PositionResult = []
    if distancesVec[0] == 0:
        PositionResult.append(voteIposition[0])
        PositionResult.append(voteIposition[0])
    else:
        LastPositons,LastCounts = QuanzhongSorted(voteIposition,distancesVec,k)
        PositionResult.append(LastPositons[-1])  
        
        LastPositons = partdomain(LastPositons,LastCounts)
        PositionResult.append(LastPositons[-1])
    return PositionResult  

def ErrorMathPlot(DistanceVec,DistanceVec1):                                #概率与误差关系绘图函数                               
    f1 = plt.figure('fig3')
    SortedDistanceVec = []
    tmpY = []
    DistanceVec = asarray(DistanceVec)
    sortedDistIndicies = DistanceVec.argsort()
    for i in range(len(DistanceVec)):
        SortedDistanceVec.append(DistanceVec[sortedDistIndicies[i]])
    Count = len(SortedDistanceVec)
    for i in range(Count):
        tmpY.append(float(i+1)/float(Count)*100)
    
    p1 = plt.plot(SortedDistanceVec,tmpY,color = 'r',label='MostCounts')

    SortedDistanceVec = []
    tmpY = []
    DistanceVec = asarray(DistanceVec1)
    sortedDistIndicies = DistanceVec.argsort()
    for i in range(len(DistanceVec)):
        SortedDistanceVec.append(DistanceVec[sortedDistIndicies[i]])
    Count = len(SortedDistanceVec)
    print "Count",Count
    for i in range(Count):
        tmpY.append(float(i+1)/float(Count)*100)
    ax = plt.gca()
    ax.set_xticks(linspace(0,10,20))
    ax.set_yticks(linspace(0,100,10))
    plt.grid(True)
    p2 = plt.plot(SortedDistanceVec,tmpY,color = 'b',label='SliceArea')
    xmajorLocator = MultipleLocator(0.5) 
    ax.xaxis.set_major_locator(xmajorLocator) #设置坐标轴的间隔为300
    plt.xlim(0,6)#x轴的范围设置
    ymajorLocator = MultipleLocator(10) 
    ax.yaxis.set_major_locator(ymajorLocator) #设置坐标轴的间隔为300
    plt.ylim(0,100)#x轴的范围设置
    plt.title("Distance Error CDF")
    plt.grid(True)
    plt.legend()
    plt.xlabel("Distance error (m)")
    plt.ylabel("Probability,(%)")


    
def DataProcessAndKnnAlgorithm(ReceiveData1,DataSet,LabelsFloatVector):

    #参数 ReceiveData1=50*360    DataSet=3408*348  LabelsFloatVector=[ [0.0,0.0]*142 ,[0.0,2.0]*142 ...[10.0,6.0]*142] 
    #返回值PositionResultVector = [[8,2],...9个],    PositionResultVector1 = [[8,2],...9个]
    
    ReceiveData = DataSubcarrierDiff(ReceiveData1)  #返回值 ReceiveData1=50*348
    ReceiveData = RealTimeDataMoveAve(ReceiveData,10,5) #返回值 ReceiveData1=9*348
    PositionResultVector = []#普通质心算法测试点坐标
    PositionResultVector1 = []#加权质心算法测试点坐标
    ErrorDistanceVector = []#普通质心算法误差矩阵
    ErrorDistanceVector1 = []#加权质心算法误差矩阵
    for i in range(len(ReceiveData)):  # 9
        #inArr=np.random.random(348)
        inArr = ReceiveData[i] #实时数据矩阵的第i行
        start = time.clock()
    
        classifierPosition,distancevec,Truncindex = classify0(inArr, DataSet, LabelsFloatVector,0.1)
        #classifierPositions是距离从小到大排序的前100个坐标的向量,distancevec是距离从小到大排序的前100个值的向量,Truncindex=100
        PositionResult = Trianglecentroid(classifierPosition,distancevec,Truncindex)
        #PositionResult = [[8,2],[8,2]] 分别是QuanzhongSorted(Most Count)，partdomain(Slice Area)的返回结果
        end = time.clock()
        #print "read: %f s" % (end - start)
        #print "Truncindex",Truncindex
        PositionResultVector.append(PositionResult[0])
        PositionResultVector1.append(PositionResult[1])
        #print "最大概率估计出的位置：",PositionResult[0]
        #print "划分区域估计出的位置：",PositionResult[1]
        #KalmanFilter(PositionResult[0])
        #KalmanFilter(PositionResult[0])
##        print "Most Count：",PositionResult[0]
##        print "Slice Area：",PositionResult[1]
        #return PositionResult[0],PositionResult[1]
    return PositionResultVector,PositionResultVector1






        
        
    #print PositionResultVector,'\n',PositionResutVector1

    '''f1 = plt.figure('fig1')
    #for i in range(len(inLabelsFloatVector)):
    #    p1 = plt.scatter(inLabelsFloatVector[i][0],inLabelsFloatVector[i][1],marker='o',color='m',s=100)
        
    for PositionResult in PositionResultVector:
        p2 = plt.scatter(PositionResult[0],PositionResult[1],marker='o',color='r',s=50)
    
    for PositionResult in PositionResultVector1:
        p3 = plt.scatter(PositionResult[0],PositionResult[1],marker='o',color='b',s=20)'''
    
    ''' f2 = plt.figure('fig2')
    tmpx = []
    for i in range(len(ErrorDistanceVector)):
        tmpx.append(i)
    
    p1 = plt.plot(tmpx,ErrorDistanceVector,color='r',label='MostCounts ')
    p2 = plt.plot(tmpx,ErrorDistanceVector1,color='b',label='SliceArea')
    plt.title("DistanceError")
    plt.xlabel("Samples")
    plt.ylabel("Distance Error")
    plt.legend()
    
    ErrorMathPlot(ErrorDistanceVector,ErrorDistanceVector1)'''
    #plt.show()
    
       
        
        
