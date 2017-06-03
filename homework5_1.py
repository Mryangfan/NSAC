# -*- coding: utf-8 -*-
'''
calculate the root of f=z**3-1 and plot fractal picture with Newton's method
'''
import numpy as np
import pylab as pl
import time

start=time.time()
X1,X2,X3,Y1,Y2,Y3=[],[],[],[],[],[]
a=1.732  #a=np.sqrt(3)
z=-1-1j

#分形图像素[2000,2000]
for i in range(0,2000):
    z=z+0.001-z.imag*1j-1j
    for j in range(0,2000):
        z=z+0.001j
        r=z
        for k in range(0,15):
            r2=r-(r**3-1)/(3*r*r)
            r=r2
        if abs(r-1)<0.0001:
            X1[len(X1):]=[z.real]
            Y1[len(Y1):]=[z.imag]
        elif abs(r+1/2-a/2*1j)<0.0001:
             X2[len(X2):]=[z.real]
             Y2[len(Y2):]=[z.imag]
        elif abs(r+1/2+a/2*1j)<0.0001:
             X3[len(X3):]=[z.real]
             Y3[len(Y3):]=[z.imag]
            
pl.plot(X1,Y1,'r.',X2,Y2,'b.',X3,Y3,'g.')
pl.show()
stop=time.time()
print("time=",stop-start)
