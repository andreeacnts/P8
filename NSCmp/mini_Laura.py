
import numpy as np
import concurrent
import matplotlib.pyplot as plt
import timeit
import matplotlib.ticker as mtick

import smile_records

data = smile_ratio

def smile_ratio(a, A):
    x = data[:,3]
    y = data[:,4]
    xw = data[:,5]
    yh = data[:, 6]
   
    for i, el in enumerate(A):
        sRatio[i]=_((xw[i]/x[i])+ (yh[i]/y[i]))/2
    return sRatio


#vectorised version 

def _smile_ratio_vec(a,b,c,d)
