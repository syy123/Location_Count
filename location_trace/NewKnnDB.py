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
from matplotlib import font_manager

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
        m = len(rows)
        n = len(rows[0]) - 1
        returnMat = zeros((m,n))
        classLabelVector = []
        for i in range(m):
            classLabelVector.append(rows[i][0])
            returnMat[i,:] = rows[i][1:]
        return returnMat,classLabelVector
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
    line = len(dataSet)
    pointCounts=len(set(labelsList))#测试点坐标
    numbers=line/pointCounts#每个测试点取得数据条数
    print "Line",line
    print "pointCounts",pointCounts
    print "numbers",numbers
    dataPoint=[]
    dataPointLabel=[]
    for i in range(pointCounts):
        dataPoint.append(dataSet[numbers*i:numbers*(i+1)])#将每个点处的数据存入dataPoint
        dataPointLabel.append(labelsList[numbers*i:numbers*(i+1)])
        
    DataList=[]
    returnLabels=[]
    count=(numbers-WindowsSize)/gap#滑动窗移动的次数
    for i in range(pointCounts):
        for j in range(count+1):
            dataLine=mean(dataPoint[i][j*gap:(WindowsSize+j*gap)],axis=0)
            DataList.append(dataLine)
            returnLabels.append(dataPointLabel[i][j*gap])
    Data = array(DataList)
    return Data,returnLabels

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
    #labelList=labelList1+labelList2
    return Data,dataPointLabel
    
def classify0(inX, dataSet, PositionVec, distanceTrunc):      #找出最近k点的坐标
    dataSetSize = dataSet.shape[0]                            #得到dataSet的行数
    diffMat = tile(inX, (dataSetSize,1)) - dataSet            #对输入向量进行矩阵扩展，并减去dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)                     #矩阵每行元素计算和值
    distances = sqDistances ** 0.5                            #计算得到距离矩阵(k,1)
    sortedDistIndicies = distances.argsort()                  #得到距离矩阵从小到大的索引值
    distanceRange = distances[sortedDistIndicies[-1]] - distances[sortedDistIndicies[0]] #计算距离矩阵范围
    distanceTrunc = distanceTrunc * distanceRange + distances[sortedDistIndicies[0]] #计算距离矩阵截断值
    voteIposition = []                                        #清空返回坐标矩阵
    distancesVec = []     
    for i in range(len(sortedDistIndicies)):                    #根据距离矩阵截断值获得截断索引值
        if distances[sortedDistIndicies[i]] > distanceTrunc:
            Truncindex = i
            break
    if Truncindex > global_MaxPoint:                                       #如果阶段索引值超过了最大点数则取最大点数
        Truncindex = global_MaxPoint
    for i in range(Truncindex):
        voteIposition.append(PositionVec[sortedDistIndicies[i]]) #得到距离坐标
        distancesVec.append(distances[sortedDistIndicies[i]]) #得到距离矩阵
    return voteIposition, distancesVec,Truncindex           #返回距离坐标矩阵及截断索引

def partdomain(LastPositons,tmpcount):                                     #对预测点进行分区域权重判断输出最有可能的界域
    MaxX = global_MaxX
    MaxY = global_MaxY
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
            median = (MaxY - MinY) / 2.0 + MinY
            for i in range(len(LastPositons)):
                if LastPositons[i][1] <= median:
                    Comparequanzhong[0] += tmpcount[i]
                    cmpposition1.append(LastPositons[i])
                    cmpcounts1.append(tmpcount[i])

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
        else:
            break    

    return LastPositons

def QuanzhongSorted(voteIposition,distancesVec,k):                         #对于测点进行统合同时计算总得权重总值并排序
    TmpPositions = []
    Count = []
    quanzhongsum = 0
    for i in range(k):
        quanzhongsum += i
            
    for Position in voteIposition:                                      #将k个点内出现的不同坐标点以距离远近不同权重进行求和
        if Position not in TmpPositions:
            TmpPositions.append(Position)
            quanzhong = float(k - voteIposition.index(Position)) / float(quanzhongsum)
            Count.append(quanzhong)
        else:
            index = TmpPositions.index(Position)
            quanzhong = float(k - voteIposition.index(Position)) / float(quanzhongsum)
            Count[index] += quanzhong

    tmpcount = sorted(Count)                                            #将求和得出的count进行排序，同时以此排序结果对坐标进行排序
    LastPositons = []
    for i in tmpcount:
        index = Count.index(i)
        LastPositons.append(TmpPositions[index])
    return LastPositons,tmpcount  
        
def Trianglecentroid(voteIposition,distancesVec,k):                        #得到最近的k个点后估算出坐标点
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
    
    #p1 = plt.plot(SortedDistanceVec,tmpY,color = 'r',label='MostCounts')

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
    p2 = plt.plot(SortedDistanceVec,tmpY,color = 'b',label=u'KNN改进')
    xmajorLocator = MultipleLocator(0.5) 
    ax.xaxis.set_major_locator(xmajorLocator) #设置坐标轴的间隔为300
    plt.xlim(0,6)#x轴的范围设置
    ymajorLocator = MultipleLocator(10) 
    ax.yaxis.set_major_locator(ymajorLocator) #设置坐标轴的间隔为300
    zh_font = font_manager.FontProperties(fname=r"C:\windows\fonts\simsun.ttc", size=14)
    plt.ylim(0,100)#x轴的范围设置
    plt.title(u"距离误差CDF",fontproperties=zh_font)
    plt.grid(True)
    plt.legend(prop=zh_font)
    plt.xlabel(u"距离误差(m)", fontproperties=zh_font)
    plt.ylabel(u"累积概率,(%)", fontproperties=zh_font)
    
def runFunc(trainName,testName):
    filename = testName
    inArrList,inLabelsVector = file2matrix(filename)
    inArrList,inLabelsVector = MoveAve(inArrList,inLabelsVector,800,10)
    inArrList=DataSubcarrierDiff(inArrList)
    inLabelsFloatVector = []
    for inLabels in inLabelsVector:
        inLabelsfloat = [float(re.sub(r"\D",'',inLabels.split(',')[0])),float(re.sub(r"\D",'',inLabels.split(',')[1]))]
        inLabelsFloatVector.append(inLabelsfloat)
        
    filename = trainName
    DataSet,LabelsVector = file2matrix(filename)  
    DataSet,LabelsVector = MoveAve(DataSet,LabelsVector,800,5)
    DataSet=DataSubcarrierDiff(DataSet)  
    LabelsFloatVector = []
    for Labels in LabelsVector:
        LabelFloat = [float(re.sub(r"\D",'',Labels.split(',')[0])),float(re.sub(r"\D",'',Labels.split(',')[1]))]
        LabelsFloatVector.append(LabelFloat)

    PositionResultVector = []#普通质心算法测试点坐标
    PositionResutVector1 = []#加权质心算法测试点坐标
    ErrorDistanceVector = []#普通质心算法误差矩阵
    ErrorDistanceVector1 = []#加权质心算法误差矩阵

    for i in range(len(inArrList)):#484
        inArr = inArrList[i]
        inLabels = inLabelsFloatVector[i]
        classifierPosition,distancevec,Truncindex = classify0(inArr, DataSet, LabelsFloatVector,0.1)
        PositionResult = Trianglecentroid(classifierPosition,distancevec,Truncindex)
        #print "Truncindex",Truncindex
        PositionResultVector.append(PositionResult[0])
        PositionResutVector1.append(PositionResult[1])
        ErrorDistance = caldistance(PositionResult[0],inLabels)  #计算预测坐标和实际坐标之间的距离
        ErrorDistance1 = caldistance(PositionResult[1],inLabels)
        ErrorDistanceVector.append(ErrorDistance)
        ErrorDistanceVector1.append(ErrorDistance1)
    return inLabelsFloatVector,PositionResultVector,PositionResutVector1,ErrorDistanceVector,ErrorDistanceVector1

        
if __name__ == '__main__':
    filename = r'F:\matlabCode624\location and trace\2016-5-7-10\Test_data\Testdata2000.db'
    inArrList,inLabelsVector = file2matrix(filename)
    inArrList,inLabelsVector = MoveAve(inArrList,inLabelsVector,800,10)
    inArrList=DataSubcarrierDiff(inArrList)
    inLabelsFloatVector = []
    for inLabels in inLabelsVector:
        inLabelsfloat = [float(re.sub(r"\D",'',inLabels.split(',')[0])),float(re.sub(r"\D",'',inLabels.split(',')[1]))]
        inLabelsFloatVector.append(inLabelsfloat)
        
    filename = r'F:\matlabCode624\location and trace\2016-5-7-16\Trainning_data\Trainingdata2000.db'   
    DataSet,LabelsVector = file2matrix(filename)  
    DataSet,LabelsVector = MoveAve(DataSet,LabelsVector,800,5)
    DataSet=DataSubcarrierDiff(DataSet)  
    LabelsFloatVector = []
    for Labels in LabelsVector:
        LabelFloat = [float(re.sub(r"\D",'',Labels.split(',')[0])),float(re.sub(r"\D",'',Labels.split(',')[1]))]
        LabelsFloatVector.append(LabelFloat)

    PositionResultVector = []#普通质心算法测试点坐标
    PositionResutVector1 = []#加权质心算法测试点坐标
    ErrorDistanceVector = []#普通质心算法误差矩阵
    ErrorDistanceVector1 = []#加权质心算法误差矩阵

    for i in range(len(inArrList)):#484
        inArr = inArrList[i]
        inLabels = inLabelsFloatVector[i]
        classifierPosition,distancevec,Truncindex = classify0(inArr, DataSet, LabelsFloatVector,0.1)
        PositionResult = Trianglecentroid(classifierPosition,distancevec,Truncindex)
        #print "Truncindex",Truncindex
        PositionResultVector.append(PositionResult[0])
        PositionResutVector1.append(PositionResult[1])
        ErrorDistance = caldistance(PositionResult[0],inLabels)  #计算预测坐标和实际坐标之间的距离
        ErrorDistance1 = caldistance(PositionResult[1],inLabels)
        ErrorDistanceVector.append(ErrorDistance)
        ErrorDistanceVector1.append(ErrorDistance1)
        
    f1 = plt.figure('fig1')
    for i in range(len(inLabelsFloatVector)):  #484
        p1 = plt.scatter(inLabelsFloatVector[i][0],inLabelsFloatVector[i][1],marker='o',color='m',s=100)
        
    for PositionResult in PositionResultVector:
        p2 = plt.scatter(PositionResult[0],PositionResult[1],marker='o',color='r',s=50)
    
    for PositionResult in PositionResutVector1:
        p3 = plt.scatter(PositionResult[0],PositionResult[1],marker='o',color='b',s=20)

    #横坐标是0-10， 纵坐标是0-6
    #p1:484个已知标签的测试数据的点   p2:484个QuanzhongSorted预测的点  p3: 484个partdomain预测的点
    
    f2 = plt.figure('fig2')
    tmpx = []
    for i in range(len(ErrorDistanceVector)):
        tmpx.append(i)
    
    p1 = plt.plot(tmpx,ErrorDistanceVector,color='r',label='MostCounts ')
    p2 = plt.plot(tmpx,ErrorDistanceVector1,color='b',label='SliceArea')

    #横坐标是0-484， 纵坐标是每个记录的距离误差，如果没误差的话是0
    #484个点的距离误差：输入一条带有标签（例如[8,2]）的记录，与数据库中的5784条记录匹配,匹配结果可能有误差
    
    plt.title("DistanceError") 
    plt.xlabel("Samples")
    plt.ylabel("Distance Error")
    plt.legend()
    
    ErrorMathPlot(ErrorDistanceVector,ErrorDistanceVector1)
    #横坐标是距离误差0米-6米， 纵坐标是0%-100%
    plt.show()
    
       
        
        
