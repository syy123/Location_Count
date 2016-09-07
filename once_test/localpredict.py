# -*- coding: utf-8 -*-
"""
Created on Wed Aug 03 19:22:21 2016

@author: Administrator
"""

import numpy as np
import sys
path='E:\Located\libsvm-3.21\python'
sys.path.append(path)
from svmutil import *

csivar01 = np.loadtxt('E:/Located/mydata/noperson1_csivarseg.txt')
csivar02 = np.loadtxt('E:/Located/mydata/noperson2_csivarseg.txt')
csivar03 = np.loadtxt('E:/Located/mydata/noperson3_csivarseg.txt')
csivar04 = np.loadtxt('E:/Located/mydata/noperson4_csivarseg.txt')

csivar11 = np.loadtxt('E:/Located/mydata/oneperson1_csivarseg.txt')
csivar12 = np.loadtxt('E:/Located/mydata/oneperson2_csivarseg.txt')
csivar13 = np.loadtxt('E:/Located/mydata/oneperson3_csivarseg.txt')
csivar14 = np.loadtxt('E:/Located/mydata/oneperson4_csivarseg.txt')

csivar21 = np.loadtxt('E:/Located/mydata/twoperson1_csivarseg.txt')
csivar22 = np.loadtxt('E:/Located/mydata/twoperson2_csivarseg.txt')
csivar23 = np.loadtxt('E:/Located/mydata/twoperson3_csivarseg.txt')
csivar24 = np.loadtxt('E:/Located/mydata/twoperson4_csivarseg.txt')

csivar31 = np.loadtxt('E:/Located/mydata/threeperson1_csivarseg.txt')
csivar32 = np.loadtxt('E:/Located/mydata/threeperson2_csivarseg.txt')
csivar33 = np.loadtxt('E:/Located/mydata/threeperson3_csivarseg.txt')
csivar34 = np.loadtxt('E:/Located/mydata/threeperson4_csivarseg.txt')

csivar41 = np.loadtxt('E:/Located/mydata/fourperson1_csivarseg.txt')
csivar42 = np.loadtxt('E:/Located/mydata/fourperson2_csivarseg.txt')
csivar43 = np.loadtxt('E:/Located/mydata/fourperson3_csivarseg.txt')
csivar44 = np.loadtxt('E:/Located/mydata/fourperson4_csivarseg.txt')

csivar51 = np.loadtxt('E:/Located/mydata/fiveperson1_csivarseg.txt')
csivar52 = np.loadtxt('E:/Located/mydata/fiveperson2_csivarseg.txt')
csivar53 = np.loadtxt('E:/Located/mydata/fiveperson3_csivarseg.txt')
csivar54 = np.loadtxt('E:/Located/mydata/fiveperson4_csivarseg.txt')

csivar61 = np.loadtxt('E:/Located/mydata/sixperson1_csivarseg.txt')
csivar62 = np.loadtxt('E:/Located/mydata/sixperson2_csivarseg.txt')
csivar63 = np.loadtxt('E:/Located/mydata/sixperson3_csivarseg.txt')
csivar64 = np.loadtxt('E:/Located/mydata/sixperson4_csivarseg.txt')

m=100
csivar01 = csivar01.tolist()[m:]
csivar02 = csivar02.tolist()[m:]
csivar03 = csivar03.tolist()[m:]
csivar04 = csivar04.tolist()[m:]
csivar11 = csivar11.tolist()[m:]
csivar12 = csivar12.tolist()[m:]
csivar13 = csivar13.tolist()[m:]
csivar14 = csivar14.tolist()[m:]
csivar21 = csivar21.tolist()[m:]
csivar22 = csivar22.tolist()[m:]
csivar23 = csivar23.tolist()[m:]
csivar24 = csivar24.tolist()[m:]
csivar31 = csivar31.tolist()[m:]
csivar32 = csivar32.tolist()[m:]
csivar33 = csivar33.tolist()[m:]
csivar34 = csivar34.tolist()[m:]
csivar41 = csivar41.tolist()[m:]
csivar42 = csivar42.tolist()[m:]
csivar43 = csivar43.tolist()[m:]
csivar44 = csivar44.tolist()[m:]
csivar51 = csivar51.tolist()[m:]
csivar52 = csivar52.tolist()[m:]
csivar53 = csivar53.tolist()[m:]
csivar54 = csivar54.tolist()[m:]
csivar61 = csivar61.tolist()[m:]
csivar62 = csivar62.tolist()[m:]
csivar63 = csivar63.tolist()[m:]
csivar64 = csivar64.tolist()[m:]

data = []
n=100
for i in range(7*m):
    data.append([])
    for j in range(360):
        data[i].append(0)
for i in range(m):
    data[i] = csivar01[i]+csivar02[i]+csivar03[i]+csivar04[i]
for i in range(m,2*m):
    data[i] = csivar11[i%m]+csivar12[i%m]+csivar13[i%m]+csivar14[i%m]
for i in range(2*m,3*m):
    data[i] = csivar21[i%(2*m)]+csivar22[i%(2*m)]+csivar23[i%(2*m)]+csivar24[i%(2*m)]
for i in range(3*m,4*m):
    data[i] = csivar31[i%(3*m)]+csivar32[i%(3*m)]+csivar33[i%(3*m)]+csivar34[i%(3*m)]
for i in range(4*m,5*m):
    data[i] = csivar41[i%(4*m)]+csivar42[i%(4*m)]+csivar43[i%(4*m)]+csivar44[i%(4*m)]
for i in range(5*m,6*m):
    data[i] = csivar51[i%(5*m)]+csivar52[i%(5*m)]+csivar53[i%(5*m)]+csivar54[i%(5*m)]
for i in range(6*m,7*m):
    data[i] = csivar61[i%(6*m)]+csivar62[i%(6*m)]+csivar63[i%(6*m)]+csivar64[i%(6*m)]
print 'len data',len(data)
#print len(data[0])
model = svm_load_model('sixperson_model.txt')
testdata = []
result = []
sum0 = []
sum1=[]
sum2=[]
sum3=[]
sum4=[]
sum5=[]
sum6=[]
for i in range(n):
    testdata.append(data[i])
    [p_label,acc,dic] = svm_predict([0],testdata,model)   
    testdata=[]
    result.append(p_label)
for item in result:
    sum0.append(result.count(item))
    result=[]

for i in range(n,2*n):
    testdata.append(data[i])
    [p_label,acc,dic] = svm_predict([1],testdata,model)   
    result.append(p_label)
    testdata=[]
for item in result:
    sum1.append(result.count(item))
    result=[]
    
for i in range(2*n,3*n):
    testdata.append(data[i])
    [p_label,acc,dic] = svm_predict([2],testdata,model)   
    result.append(p_label)
    testdata=[]
for item in result:
    sum2.append(result.count(item))
    result=[]

for i in range(3*n,4*n):
    testdata.append(data[i])
    [p_label,acc,dic] = svm_predict([3],testdata,model)   
    result.append(p_label)
    testdata=[]
for item in result:
    sum3.append(result.count(item))
    result=[]

for i in range(4*n,5*n):
    testdata.append(data[i])
    [p_label,acc,dic] = svm_predict([4],testdata,model)   
    result.append(p_label)
    testdata=[]
for item in result:
    sum4.append(result.count(item))
    result=[]
    
for i in range(5*n,6*n):
    testdata.append(data[i])
    [p_label,acc,dic] = svm_predict([5],testdata,model)   
    result.append(p_label)
    testdata=[]
for item in result:
    sum5.append(result.count(item))
    result=[]
    
for i in range(6*n,7*n):
    testdata.append(data[i])
    [p_label,acc,dic] = svm_predict([6],testdata,model)   
    result.append(p_label)
    testdata=[]
for item in result:
    sum6.append(result.count(item))
    result=[]

'''print 'sum0=',sum0
print 'sum1=',sum1
print 'sum2=',sum2
print 'sum3=',sum3
print 'sum4=',sum4
print 'sum5=',sum5
print 'sum6=',sum6
'''
        
        