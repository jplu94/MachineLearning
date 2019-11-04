import numpy as np
import scipy as sp

def Polinom(x,j):
    return x**j

def LinReg(x,y,j):
    print((x.shape))
    X = np.array(np.ones((len(x),1)))
    x = np.array([x])

    print(X.shape,x.shape)
    for jrun in range(1,j+1):
        print("jrun",jrun)
        X = np.hstack([X,np.transpose(Polinom(x,jrun))])
    w = np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(X),X)),np.transpose(X)),y)
    print("!!w:",w)
    return w
