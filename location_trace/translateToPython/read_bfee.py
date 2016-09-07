# -*- coding: cp936 -*-

import struct
import numpy as np
import sys

def read_bfee(bytes):
#----------------------------����һ��dict��Ϊ�ṹ�� ----------------------------------      
    Cstruct = {"timestamp_low":0,
		"bfee_count":0,
		"Nrx":0, "Ntx":0,
		"rssi_a":0, "rssi_b":0, "rssi_c":0,
		"noise":0,
		"agc":0,
		"perm":0,
		"rate":0,
		"csi":0}
    inBytes = struct.unpack("13B1b6B",bytes[0:20]) ##������ǰ20���ֽ� ,noise��signed char
#------------------------------ǰ20���ֽڵĽ���------------------------------------------
    timestamp_low = inBytes[0] + (inBytes[1] << 8) + (inBytes[2] << 16) + (inBytes[3] << 24)
    Cstruct["timestamp_low"] = timestamp_low
    
    bfee_count = inBytes[4] + (inBytes[5] << 8)
    Cstruct["bfee_count"] = bfee_count
    
    Nrx = inBytes[8]   
    Cstruct["Nrx"] = Nrx
    
    Ntx = inBytes[9]   
    Cstruct["Ntx"] = Ntx
    
    rssi_a = inBytes[10]
    Cstruct["rssi_a"] = rssi_a
    
    rssi_b = inBytes[11]
    Cstruct["rssi_b"] = rssi_b
    
    rssi_c = inBytes[12]
    Cstruct["rssi_c"] = rssi_c
    
    noise = inBytes[13]
    Cstruct["noise"] = noise
    
    agc = inBytes[14]
    Cstruct["agc"] = agc
    
    antenna_sel = inBytes[15]
    
    length = inBytes[16] + (inBytes[17] << 8)
    
    fake_rate_n_flags = inBytes[18] + (inBytes[19] << 8)
    Cstruct["rate"] = fake_rate_n_flags
    
    calc_len = (30 * (Nrx * Ntx * 8 * 2 + 3) + 7) / 8
    
    payload = struct.unpack("192B",bytes[20:]) ##��21���ֽ�--��212���ֽڣ���192�ֽ����ڽ���CSI
    csi = np.zeros((Nrx * Ntx ,30),dtype = complex)
    perm = np.zeros(3)
    
    # print Nrx,Ntx,rssi_a,rssi_b,rssi_c,noise
    if (length != calc_len):
        print "read_bfee_new:size","Wrong beamforming matrix size."
        sys.exit()
 #-------------------------------����CSI-------------------------------------------       
    index = 0
    remainder = 0   
    for i in range(30):
        index = index + 3
        remainder = index % 8
        for j in range(Nrx * Ntx):
            fir = (payload[index / 8] >> remainder)            
            sec = (payload[index/8+1] << (8-remainder))
            fir = fir & 255 #ȡ�Ͱ�λ
            sec = sec & 255 #ȡ�Ͱ�λ
            re = fir|sec
            if re > 128:  ##������λ��1 ��������
                re = -(((fir|sec)^255) + 1)
            
            fir = (payload[index/8+1] >> remainder)
            sec = (payload[index/8+2] << (8-remainder))            
            fir = fir & 255 #ȡ�Ͱ�λ
            sec = sec & 255 #ȡ�Ͱ�λ
            im = fir|sec  
            if im > 128:  ##������λ��1 ��������
                im = -(((fir|sec)^255) + 1)
            
            index = index + 16
        
            csi[j][i] = np.complex(float(re),float(im))
    Cstruct["csi"] = csi
 #-------------------------------����perm-------------------------------------------      
    perm[0] = ((antenna_sel) & 3) + 1
    perm[1] = ((antenna_sel >> 2) & 3) + 1
    perm[2] = ((antenna_sel >> 4) & 3) + 1
    Cstruct["perm"] = perm

 #-------------------------------���ؽṹ��-------------------------------------------     
    #print Cstruct  
    return Cstruct
    
    
    
    
