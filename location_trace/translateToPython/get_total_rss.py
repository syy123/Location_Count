# -*- coding: cp936 -*-
import math

def dbinv(x):
    return 10**(x/10)

def get_total_rss(csi_st): # 输入结构体（字典）

    rssi_mag = 0
    rssi_a = csi_st.get('rssi_a')
    rssi_b = csi_st.get('rssi_b')
    rssi_c = csi_st.get('rssi_c')
    agc = csi_st.get('agc')
    if rssi_a != 0:
        rssi_mag = rssi_mag + dbinv(rssi_a)
    if rssi_b != 0:
        rssi_mag = rssi_mag + dbinv(rssi_b)        
    if rssi_c != 0:
        rssi_mag = rssi_mag + dbinv(rssi_c)

    return math.log10(rssi_mag)*10 - 44 - agc
