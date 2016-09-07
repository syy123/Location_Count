#!/usr/bin/env python
#coding:utf-8

from numpy import *
import os
import xlrd
import matplotlib.pyplot as plt
import sqlite3
import re
from matplotlib.ticker import MultipleLocator, FuncFormatter
import numpy as np
import time

from numpy import dot
from numpy import dot, sum, tile, linalg
from numpy.linalg import inv

'''from sys import path
path.append(r'E:\RSSI Localization\KNN Algorithm') #将存放module的路径添加进来
import KalmanFilter'''

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
    #returnNopersondataMatAve=np.mean(returnMat,axis=0)
    print len(returnMat)
    return returnMat

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

def RealTimeDataMoveAve(dataSet,WindowsSize,gap):                 #滑动平均函数
    line = len(dataSet) 
    DataList=[]
    count=(line-WindowsSize)/gap#滑动窗移动的次数
    for i in range(count+1):
        dataLine=mean(dataSet[i*gap:(WindowsSize+i*gap)],axis=0)
        DataList.append(dataLine)
    Data = array(DataList)
    return Data

def DataSubcarrierDiff(Data):
    print "len(Data)",len(Data)
    DataDiff = zeros((len(Data),348))
    print len(Data)
    for k in range(len(Data)):
        for i in range(12):
            for j in range(29):
                DataDiff[k,29*i+j]=Data[k,30*i+j+1]-Data[k,30*i+j]
    Data=np.abs(DataDiff)
    return Data

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
    print len(DataList[0])
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

'''def KalmanFilter(PositionResult):
    # 预测  
    xhatminus = xhat[:,0]  #X(k|k-1) = AX(k-1|k-1) + BU(k) + W(k),A=1,BU(k) = 0  
    Pminus = P[:,0]+Q      #P(k|k-1) = AP(k-1|k-1)A' + Q(k) ,A=1  

    # 更新  
    K = Pminus/( Pminus+R ) #Kg(k)=P(k|k-1)H'/[HP(k|k-1)H' + R],H=1
    #print "k",k,Pminus
    
    xhat[:,1] = xhatminus+K*(PositionResult-xhatminus) #X(k|k) = X(k|k-1) + Kg(k)[Z(k) - HX(k|k-1)], H=1
    #x=xhat[1]
    P[:,1] = (1-K)*Pminus #P(k|k) = (1 - Kg(k)H)P(k|k-1), H=1
    return xhat[:,1],P[:,1]'''
def kf_predict(X, P, A, Q, B, U):
    X = dot(A, X) + dot(B, U)
    P = dot(A, dot(P, A.T)) + Q
    return(X,P)


def kf_update(X, P, Y, H, R):
    IM = dot(H, X)
    IS = R + dot(H, dot(P, H.T))
    K = dot(P, dot(H.T, inv(IS)))
    X = X + dot(K, (Y-IM))
    P = P - dot(K, dot(IS, K.T))
    #LH = gauss_pdf(Y, IM, IS)
    
    return (X,P,K,IM,IS)

def gauss_pdf(X, M, S):
    if M.shape()[1] == 1:
        DX = X - tile(M, X.shape()[1])
        E = 0.5 * sum(DX * (dot(inv(S), DX)), axis=0)
        E = E + 0.5 * M.shape()[0] * log(2 * pi) + 0.5 * log(det(S))
        P = exp(-E)
    elif X.shape()[1] == 1:
        DX = tile(X, M.shape()[1])- M
        E = 0.5 * sum(DX * (dot(inv(S), DX)), axis=0)
        E = E + 0.5 * M.shape()[0] * log(2 * pi) + 0.5 * log(det(S))
        P = exp(-E)
    else:
        DX = X-M
        E = 0.5 * dot(DX.T, dot(inv(S), DX))
        E = E + 0.5 * M.shape()[0] * log(2 * pi) + 0.5 * log(det(S))
        P = exp(-E)

    return (P[0],E[0])
    
if __name__ == '__main__':
    filename = r'E:\RSSI Localization\2016-6-27-16\DataExcle\PersonMoveData17600.xls'
    ReceiveData1 = nopersondatafile2matrix(filename)
    ReceiveData=DataSubcarrierDiff(ReceiveData1)
    ReceiveData = RealTimeDataMoveAve(ReceiveData,100,50)
    
    filename = r'E:\RSSI Localization\2016-6-27-16\Trainning_data\Trainingdata2000.db'
    #filename = r'E:\RSSI Localization\2016-5-7-16\DataExcle\Trainingdata500.xls'
    DataSet,LabelsVector = file2matrix(filename)
    #DataSet,LabelsVector=DataMatMerge(DataSet1,LabelsVector1,DataSet2,LabelsVector2)
    print len(DataSet)
    print "LabelsVector",len(LabelsVector)
    #DataSet=DataMinusNoPerson(DataSet,noPersonArr2)
    DataSet,LabelsVector = MoveAve(DataSet,LabelsVector,800,5)
    DataSet=DataSubcarrierDiff(DataSet)
    DataSet,LabelsVector = MoveAve(DataSet,LabelsVector,100,1)
    #DataSet,LabelsVector = DataDiffAveAndVar(DataSet,LabelsVector,50,5)
    
    LabelsFloatVector = []
    for Labels in LabelsVector:
        LabelFloat = [float(re.sub(r"\D",'',Labels.split(',')[0])),float(re.sub(r"\D",'',Labels.split(',')[1]))]
        LabelsFloatVector.append(LabelFloat)

    

    '''#Q = np.array([1e-5,1e-5]) # process variance
    Q = np.array([1e-4,1e-4])    
    # 分配数组空间  
    xhat=np.zeros((2,2))      # a posteri estimate of x 滤波估计值  
    P=np.zeros((2,2))         # a posteri error estimate滤波估计协方差矩阵  
    xhatminus=np.zeros((2,1)) # a priori estimate of x 估计值  
    Pminus=np.zeros((2,1))    # a priori error estimate估计协方差矩阵  
    K=np.zeros((2,1))         # gain or blending factor卡尔曼增益
    I=np.ones((2,1))

    #R = np.array([0.1**2,0.1**2]) # estimate of measurement variance, change to see effect  
    R = np.array([0.1**2,0.1**2])
    # intial guesses  
    xhat[:,0] = [0.0,0.0] 
    P[:,0] = [0.5,0.5]'''
    dt=1
    a=0.2
    X=np.array([0,0])#初始状态对滤波效果影响较大
    P=np.array([[10,0],[0,10]])#初始状态协方差阵对滤波效果影响很小，都能较快收敛
    F=np.array([[1,0],[0,1]])
        
    Q=np.array([[5e-6,0],[0,5e-6]])#Q值越小越好
    H=np.array([[1,0],[0,1]])
    R=np.array([[0.001,0],[0,0.5]])#R取值较小滤波出现误差突然变大的情况；相反，如果取值偏大那么滤波误差变换较为缓慢
    

    PositionResultVectorx = []#普通质心算法测试点坐标
    PositionResultVectory=[]
    PositionResultVector1 = []#加权质心算法测试点坐标
    ErrorDistanceVector = []#普通质心算法误差矩阵
    ErrorDistanceVector1 = []#加权质心算法误差矩阵
    KalmanFilterLocVectorx=[]
    KalmanFilterLocVectory=[]
    for i in range(len(ReceiveData)):
        #inArr=np.random.random(348)
        inArr = ReceiveData[i]

        classifierPosition,distancevec,Truncindex = classify0(inArr, DataSet, LabelsFloatVector,0.1)
        PositionResult = Trianglecentroid(classifierPosition,distancevec,Truncindex)
        end = time.clock()
        #print "read: %f s" % (end - start)
        #print "Truncindex",Truncindex
        PositionResultVectorx.append(PositionResult[0][0])
        PositionResultVectory.append(PositionResult[0][1])
        #PositionResultVector1.append(PositionResult[1])
        #print "最大概率估计出的位置：",PositionResult[0]
        #print "划分区域估计出的位置：",PositionResult[1]
        #KalmanFilter(PositionResult[0])
        #KalmanFilter(PositionResult[0])
        print "Most Count：",PositionResult[0]
        #print "Slice Area：",PositionResult[1]
        '''#return PositionResult[0],PositionResult[1]
        PositionResult=np.array([PositionResult[0][0],PositionResult[0][1]])
        #print PositionResultVector.T
        
        location,locationcov=KalmanFilter(PositionResult)
        KalmanFilterLocVectorx.append(location[0])
        KalmanFilterLocVectory.append(location[1])
        print "Kalman预测坐标",location,locationcov
        xhat[:,0] = location 
        P[:,0] = locationcov'''
        PositionResult=np.array([PositionResult[0][0],PositionResult[0][1]])
        #print X,P
        (X,P)=kf_predict(X, P, F, Q, B=0, U=0)
        (X,P,K,IM,IS)=kf_update(X, P, PositionResult, H, R)
        #print X,P
        KalmanFilterLocVectorx.append(X[0])
        KalmanFilterLocVectory.append(X[1])
        print "Kalman预测坐标",X
    #return PositionResultVector,PositionResultVector1
        
        
    #print PositionResultVector,'\n',PositionResutVector1

    f1 = plt.figure('fig1')
    #for i in range(len(inLabelsFloatVector)):
    #    p1 = plt.scatter(inLabelsFloatVector[i][0],inLabelsFloatVector[i][1],marker='o',color='m',s=100)
        
    #for PositionResult in PositionResultVector:
    p2 = plt.plot(PositionResultVectorx,PositionResultVectory,color='r',label='BeforeKalmanFilter ')
    
    #for KalmanFilterPositionResult in KalmanFilterLocVector:
    p3 = plt.plot(KalmanFilterLocVectorx,KalmanFilterLocVectory,color='b',label='AfterKalmanFilter ')
    plt.legend()
    
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
    plt.show()
    
       
        
        
