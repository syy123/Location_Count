# -*- coding: cp936 -*-
import time
import math
import struct
import numpy as np
from read_bfee import *

### buf是接收到的字节流（包），每个包是215字节
def read_bf_buffer(buf):
    
    buflen = len(buf)
    #print '正在read_bf_buffer函数中...\t读取的缓存长度为:',buflen

    ret = []            ## 存储返回的结构体（字典）
    for i in range(int(math.ceil(buflen/95))):
        ret.append(dict())
    cur = -1            ## 指向缓存的当前位置
    count = -1          ## 输出记录的数量
    broken_perm = 0     ## Flag位
    triangle = [1,3,6]  ## What perm should sum to for 1,2,3 antennas
    pos = 0

    while cur < (buflen - 3 - 215):
        a,=struct.unpack("B",buf[pos])
        b,=struct.unpack("B",buf[pos+1])
        field_len = a*256+b   ## 数据包长度
        #print "field_len is ",field_len
        pos = pos + 2
        code = buf[pos]
        #print "code is", code.encode('string-escape')
        pos = pos + 1
        cur = cur + 3
        bytes = ""
        if (code == '\xbb'):  # get beamforming（波束形成） or phy data
            bytes = buf[pos:(pos + field_len-1)]
            pos = pos + field_len - 1
            cur = cur + field_len - 1 
            #print '位置pos是: %d, 当前cur是: %d, read_bfee的字节长度是: %d\n'%(pos,cur,len(bytes))
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
                ## 用(1,2,3)列置换原先的(3,1,2)列
                ## print "置换"
    #print 'cur : %d  pos : %d\n'%(cur, pos)
    #print "缓存解析完成..."
    return ret[0:count+1]
















            
