# -*- coding: cp936 -*-
import time
import math
import struct
import numpy as np
from read_bfee import *

### buf�ǽ��յ����ֽ�����������ÿ������215�ֽ�
def read_bf_buffer(buf):
    
    buflen = len(buf)
    #print '����read_bf_buffer������...\t��ȡ�Ļ��泤��Ϊ:',buflen

    ret = []            ## �洢���صĽṹ�壨�ֵ䣩
    for i in range(int(math.ceil(buflen/95))):
        ret.append(dict())
    cur = -1            ## ָ�򻺴�ĵ�ǰλ��
    count = -1          ## �����¼������
    broken_perm = 0     ## Flagλ
    triangle = [1,3,6]  ## What perm should sum to for 1,2,3 antennas
    pos = 0

    while cur < (buflen - 3 - 215):
        a,=struct.unpack("B",buf[pos])
        b,=struct.unpack("B",buf[pos+1])
        field_len = a*256+b   ## ���ݰ�����
        #print "field_len is ",field_len
        pos = pos + 2
        code = buf[pos]
        #print "code is", code.encode('string-escape')
        pos = pos + 1
        cur = cur + 3
        bytes = ""
        if (code == '\xbb'):  # get beamforming�������γɣ� or phy data
            bytes = buf[pos:(pos + field_len-1)]
            pos = pos + field_len - 1
            cur = cur + field_len - 1 
            #print 'λ��pos��: %d, ��ǰcur��: %d, read_bfee���ֽڳ�����: %d\n'%(pos,cur,len(bytes))
            if len(bytes) != (field_len-1):
                break
        else:
            pos = pos - 1
            cur = cur - 1
            continue
        if (code == '\xbb'):
            count = count + 1
            ret[count] = read_bfee(bytes)
            perm = ret[count].get('perm')
            Nrx = ret[count].get('Nrx')
            if Nrx == 1:
                continue
            if sum(perm) != triangle[Nrx-1]:
                if broken_perm == 0:
                    broken_perm = 1
                    print "Found CSI (%s) with Nrx=%d and invalid perm=[%s]\n"
            else:
                csi = ret[count].get('csi')
                tmp = csi.copy()
                csi[perm[0]-1] = tmp[0]
                csi[perm[1]-1] = tmp[1]
                csi[perm[2]-1] = tmp[2]
                ## ��(1,2,3)���û�ԭ�ȵ�(3,1,2)��
                ## print "�û�"
    #print 'cur : %d  pos : %d\n'%(cur, pos)
    #print "����������..."
    return ret[0:count+1]
















            
