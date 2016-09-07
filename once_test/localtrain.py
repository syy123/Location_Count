 # -*- coding: utf-8 -*-
"""
Created on Wed Aug 03 11:36:32 2016

@author: Administrator
"""

import numpy as np
import sys
path='E:\Located\libsvm-3.21\python'
#path='E:\Located\GuanTao\matlab-four\libsvm-master\python'
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

csivar01 = csivar01.tolist()
#print type(csivar01)
csivar02 = csivar02.tolist()
csivar03 = csivar03.tolist()
csivar04 = csivar04.tolist()
csivar11 = csivar11.tolist()
csivar12 = csivar12.tolist()
csivar13 = csivar13.tolist()
csivar14 = csivar14.tolist()
csivar21 = csivar21.tolist()
csivar22 = csivar22.tolist()
csivar23 = csivar23.tolist()
csivar24 = csivar24.tolist()
csivar31 = csivar31.tolist()
csivar32 = csivar32.tolist()
csivar33 = csivar33.tolist()
csivar34 = csivar34.tolist()
csivar41 = csivar41.tolist()
csivar42 = csivar42.tolist()
csivar43 = csivar43.tolist()
csivar44 = csivar44.tolist()
csivar51 = csivar51.tolist()
csivar52 = csivar52.tolist()
csivar53 = csivar53.tolist()
csivar54 = csivar54.tolist()
csivar61 = csivar61.tolist()
csivar62 = csivar62.tolist()
csivar63 = csivar63.tolist()
csivar64 = csivar64.tolist()

m=100

data = []
label = []
for i in range(7*m):
    label.append(0)
    data.append([])
    for j in range(360):
        data[i].append(0)
for i in range(m):
    label[i] = 0
    data[i] = csivar01[i]+csivar02[i]+csivar03[i]+csivar04[i]
for i in range(m,2*m):
    label[i] = 1
    data[i] = csivar11[i%m]+csivar12[i%m]+csivar13[i%m]+csivar14[i%m]
for i in range(2*m,3*m):
    label[i] = 2
    data[i] = csivar21[i%(2*m)]+csivar22[i%(2*m)]+csivar23[i%(2*m)]+csivar24[i%(2*m)]
for i in range(3*m,4*m):
    label[i] = 3
    data[i] = csivar31[i%(3*m)]+csivar32[i%(3*m)]+csivar33[i%(3*m)]+csivar34[i%(3*m)]
for i in range(4*m,5*m):
    label[i] = 4
    data[i] = csivar41[i%(4*m)]+csivar42[i%(4*m)]+csivar43[i%(4*m)]+csivar44[i%(4*m)]
for i in range(5*m,6*m):
    label[i] = 5
    data[i] = csivar51[i%(5*m)]+csivar52[i%(5*m)]+csivar53[i%(5*m)]+csivar54[i%(5*m)]
for i in range(6*m,7*m):
    label[i] = 6
    data[i] = csivar61[i%(6*m)]+csivar62[i%(6*m)]+csivar63[i%(6*m)]+csivar64[i%(6*m)]
print len(data[0])
#pl.plot(np.arange(90),data[0])
#pl.show()
model = svm_train(label, data, '-t 2 -c 3.5 -g 0.000015 -e 0.000001')
svm_save_model('sixperson_model.txt',model)
print 'all done'