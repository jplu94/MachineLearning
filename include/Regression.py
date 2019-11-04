import numpy as np
import scipy as sp



def LinReg(x,y):
    print((x.shape))
    X = np.array(np.ones((len(x),1)))
    x = np.array([x])

    print(X.shape,x.shape)
    X = np.hstack([X,np.transpose(x)])
    w = np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(X),X)),np.transpose(X)),y)
    print(w)
    return w
