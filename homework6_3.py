# -*- coding: utf-8 -*-
"""
find the six root between 0 and 1 of p(x)
P(x)=924*x**6-2772*x**5+3150*x**4-1680*x**3+420*x*x-42*x+1
"""
import pylab as  pl
import numpy as np

#画出p(x)的图形
x=np.arange(0,1,0.001)
p=924*x**6-2772*x**5+3150*x**4-1680*x**3+420*x*x-42*x+1
pl.plot(x,p,'r-')
pl.show()

def p(x):
    p=924*x**6-2772*x**5+3150*x**4-1680*x**3+420*x*x-42*x+1
    return(p)

#p(x)的导数
def q(x):  
    q=6*924*x**5-5*2772*x**4+4*3150*x**3-3*1680*x*x+2*420*x-42
    return(q)

def main():
    root=[]
    for i in range(0,100):
        x=0.01*i
        if p(x)*p(x+0.01)<0:
            for j in range(1,10):
                x1=x-p(x)/q(x)
                if abs(x1-x)<1e-10:
                    x=x1
                    break
                else:  
                    x=x1
            root.append(x)
    print('the root of p(x) is\n',root)
'''   
    #检验
    for x in range(0,6): 
        print(p(root[x]))
'''

if __name__=='__main__':
    main()