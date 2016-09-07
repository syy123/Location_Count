#!/usr/bin/env python
#coding:utf-8

import os
import operator
import sqlite3

Labelslocation = [(0,0),(0,2),(0,4),(0,6),(2,0),(2,2),(2,4),(2,6),(4,0),(4,2),(4,4),(4,6),(6,0),(6,2),(6,4),(6,6),(8,0),(8,2),(8,4),(8,6),(10,0),(10,2),(10,4),(10,6)]
Recordlocation = [(0,0),(0,3),(4,0),(4,3),'labels']

def CreateDB(dbfilename):
    con = sqlite3.connect(dbfilename)
    c = con.cursor()
    c.execute("drop table if exists datacounts")
    sqlfield = r'(label text,'
    for i in range(180):
        if i < 179:
            sqlfield += r'data'+str(i+1)+r' double'+r','
        else:
            sqlfield += r'data'+str(i+1)+r' double'+r')'
    sqls = r'create table datacounts'+sqlfield
    c.execute(sqls)
    con.commit()
    con.close()
    return True

def ReadTXT(filename):
    Data = []
    ftxt = open(filename,'r')
    for line in ftxt.readlines():
        line = line.strip()
        stringlist = line.split()
        DataLine = []
        for i in range(3):
            for j in range(30):
                tmp = float(stringlist[j+i*60])**2+float(stringlist[j+30+i*60])**2
                DataLine.append(tmp**0.5)
        Data.append(DataLine)
    return Data   ##[[90],[90],...[90]]   文件行数

def ReadTXTAndWriteXLS(filename):
    Data = ReadTXT(filename)
    if len(Data) < 2000:
        count = 2000 - len(Data)
        for i in range(count):
            Data.append(Data[len(Data)-1]) ##凑2000
    if len(Data) > 2000:
        Data = Data[:2000]  ##读入文件前2000行
    m = len(Data)  ##2000
    n = len(Data[0])  ##90
    filenamelist = os.path.split(filename)
    if 'point0' in filenamelist[0]:
        Cow = 1
    if 'point1' in filenamelist[0]:
        Cow = 2
    if 'point2' in filenamelist[0]:
        Cow = 3
    if 'point3' in filenamelist[0]:
        Cow = 4
    
    if 'CSI00_00.txt' == filenamelist[1]:
        Labels = 0
    if 'CSI00_02.txt' == filenamelist[1]:
        Labels = 1
    if 'CSI00_04.txt' == filenamelist[1]:
        Labels = 2
    if 'CSI00_06.txt' == filenamelist[1]:
        Labels = 3
    if 'CSI02_00.txt' == filenamelist[1]:
        Labels = 4
    if 'CSI02_02.txt' == filenamelist[1]:
        Labels = 5
    if 'CSI02_04.txt' == filenamelist[1]:
        Labels = 6
    if 'CSI02_06.txt' == filenamelist[1]:
        Labels = 7
    if 'CSI04_00.txt' == filenamelist[1]:
        Labels = 8
    if 'CSI04_02.txt' == filenamelist[1]:
        Labels = 9
    if 'CSI04_04.txt' == filenamelist[1]:
        Labels = 10
    if 'CSI04_06.txt' == filenamelist[1]:
        Labels = 11
    if 'CSI06_00.txt' == filenamelist[1]:
        Labels = 12
    if 'CSI06_02.txt' == filenamelist[1]:
        Labels = 13
    if 'CSI06_04.txt' == filenamelist[1]:
        Labels = 14
    if 'CSI06_06.txt' == filenamelist[1]:
        Labels = 15
    if 'CSI08_00.txt' == filenamelist[1]:
        Labels = 16
    if 'CSI08_02.txt' == filenamelist[1]:
        Labels = 17
    if 'CSI08_04.txt' == filenamelist[1]:
        Labels = 18
    if 'CSI08_06.txt' == filenamelist[1]:
        Labels = 19
    if 'CSI10_00.txt' == filenamelist[1]:
        Labels = 20
    if 'CSI10_02.txt' == filenamelist[1]:
        Labels = 21
    if 'CSI10_04.txt' == filenamelist[1]:
        Labels = 22
    if 'CSI10_06.txt' == filenamelist[1]:
        Labels = 23
    return Data,Cow,Labels,m

def Hebing(data,cowlist,labellist,pointcount):
    ## data =[48],cowlist=[1,1,1,1..1  2,2,2,2,2,2],labellist=[0,1,2,..23,0,1,2,..23],pointcount=2000
    labellist = labellist[:24]
    datahebing = []
    labelshebing = []
    datacow1 = []
    datacow2 = []
    datacow3 = []
    datacow4 = []
    for i in range(len(cowlist)):
        if cowlist[i] == 1:
            datacow1 += data[i]   #datacow1 = [24]  [[90],[90]..2000个]  监测点1的24个指纹点数据
        elif cowlist[i] == 2:
            datacow2 += data[i]
        elif cowlist[i] == 3:
            datacow3 += data[i]
        else:
            datacow4 += data[i]
    for i in range(len(datacow1)):
        #datahebingline = datacow1[i]+datacow2[i]+datacow3[i]+datacow4[i]
        datahebingline = datacow1[i]+datacow2[i]  ##合并监测点1和2
        datahebing.append(datahebingline)
    for label in labellist:
        for i in range(pointcount):
            labelshebing.append(Labelslocation[label])
    return datahebing,labelshebing
def Writesql(data,labels,dbfilename):
    
    con = sqlite3.connect(dbfilename)
    c = con.cursor()
    for i in range(len(data)):
        sqlfield = r'(label,'
        sqldata = r'("'+str(labels[i])+r'",'
        for j in range(len(data[i])):
            if j < len(data[i])-1:
                sqlfield += r'data'+str(j+1)+r','
                sqldata += str(data[i][j]) + r','
            else:
                sqlfield += r'data'+str(j+1)+r')'
                sqldata += str(data[i][j]) + r')'
        sqls = r'insert into datacounts'+sqlfield+r' values'+sqldata
        con.execute(sqls)
    con.commit()
    con.close()
    return True


if __name__ == '__main__':
    frlist1 = []
    fileDir = r'F:\matlabCode624\location and trace\2016-8-14-20\Trainning_data'
    dbfilename = fileDir + r'\2PointTrainningdata500.db'
    CreateDB(dbfilename)
    for root,dirs,files in os.walk(fileDir):
        for fr in files:
            frlist1.append(os.path.join(root,fr))
    labelslist = []
    Data = []
    cowlist = []
    for fr in frlist1:  #48
        if ('CSI' in fr) and (os.path.splitext(fr)[1] == '.txt'):
            data,cow,label,pointcount = ReadTXTAndWriteXLS(fr)
            labelslist.append(label)
            Data.append(data)  #Data是三维的
            cowlist.append(cow)
   # print len(Data),len(Data[0]),len(Data[0][0])
    datahebing,labelshebing = Hebing(Data,cowlist,labelslist,pointcount)
    Writesql(datahebing,labelshebing,dbfilename)
    os.system("pause")

            
        
        
        
    
            
