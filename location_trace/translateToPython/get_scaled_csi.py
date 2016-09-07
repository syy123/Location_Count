# -*- coding: cp936 -*-
import numpy as np
import math
from get_total_rss import *

def get_scaled_csi(csi_st):  # 读取结构体（字典）

    csi = csi_st.get('csi'); # 1*3*30复数矩阵
# Calculate the scale factor between normalized CSI and RSSI (mW)
    csi_sq = csi * (np.conj(csi))
    csi_sq.dtype = float     # 将复数形式转化为浮点型
    
    csi_pwr  = csi_sq.sum()
    rssi_pwr = dbinv(get_total_rss(csi_st))
    
# Scale CSI -> Signal power : rssi_pwr / (mean of csi_pwr)
    scale = rssi_pwr / (csi_pwr / 30)
    
# Thermal noise might be undefined if the trace was
# captured in monitor mode.
# ... If so, set it to -92    
    if (csi_st.get('noise') == -127):
        noise_db = -92
    else:
        noise_db = csi_st.get('noise')       
    thermal_noise_pwr = dbinv(noise_db)
    quant_error_pwr   = scale * (csi_st.get('Nrx') * csi_st.get('Ntx'))
    
# Total noise and error power
    total_noise_pwr = thermal_noise_pwr + quant_error_pwr
    
# 返回值
    ret = csi * math.sqrt(scale / total_noise_pwr)
    if(csi_st.get('Ntx') == 2):
        ret = ret * math.sqrt(2)
    elif (csi_st.get('Ntx') == 3):
        ret = ret * math.sqrt(dbinv(4.5))

    return ret
