# -*- coding: utf-8 -*-
"""
Ment Caro 
"""
import random
import numpy as np
import matplotlib.pyplot as plt

def buffon():
    #针长l  间距d  针数n  格数T  矩形范围[d*T，d*T]
    d,l,n,T=1,0.6,500,10
    X=[random.uniform(0,d*T) for x in range(0,n)]
    Y=[random.uniform(0,d*T) for y in range(0,n)]
    PHI=[random.uniform(-np.pi/2,np.pi/2) for phi in range(0,n)]
    #记录与线相交的针
    MX,MY,MP=[],[],[]
    for x,phi in zip(X,PHI):
        y=x%d
        h=l*np.cos(phi)/2
        if y<h or d-y<h:
            MX[len(MX):]=[x]
            MY[len(MY):]=[Y[X.index(x)]]
            MP[len(MP):]=[PHI[X.index(x)]]
    p=len(MX)/len(X)     
    pi=2*l/d/p     
    plt.figure("Buffon's needle")
    plt.title('Pi={}'.format(pi)) 
    plt.xlim(-0.1,d*T+0.1)
    plt.ylim(-0.1,d*T+0.1)
    #画框架
    for x in np.arange(0,d*T+0.1,d):
        plt.plot([x]*2,[-0.1,d*T+0.1],'b-',linewidth=0.5)
    #画出所有的针    
    for phi,x,y in zip(PHI,X,Y):
        dx,dy=l/2*np.cos(phi),l/2*np.sin(phi)
        needle=[[x-dx,x+dx],[y-dy,y+dy]]
        plt.plot(x,y,'g.')
        plt.plot(needle[0],needle[1],'g-',linewidth=0.7)
    #画出与线相交的针
    for phi,x,y in zip(MP,MX,MY):
        dx,dy=l/2*np.cos(phi),l/2*np.sin(phi)
        needle=[[x-dx,x+dx],[y-dy,y+dy]]
        plt.plot(x,y,'r.')
        plt.plot(needle[0],needle[1],'r-',linewidth=0.7)  
    
    plt.show()

if __name__=='__main__':
    buffon()
