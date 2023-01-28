# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 14:36:30 2023

@author: saubh
"""

import numpy as np
import matplotlib.pyplot as plt

r0=np.arange(0,4,0.1)
x0=.25
gen=50
xf=[]

for i in r0:
    x_gen=[]
    for j in range(gen):
        xf_r=i*x0*(1-x0)
        x0=xf_r
        x_gen+=[x0]
    # plt.plot(range(1,gen+1),x_gen)
    # plt.ylabel("Population size")
    # plt.xlabel("time")
    # plt.suptitle("R0=%s"%round(i,1))
    # plt.show()
    xf+=[x0]
    x0=.25
         
plt.plot(r0,xf)
plt.xlabel("R0")
plt.ylabel("Pop size after %s generations" %gen)
plt.show()