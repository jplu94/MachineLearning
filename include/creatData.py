#Creat data
import numpy as np
def creatNormal(x):
    mu, sigma = 0, 0.1 # mean and standard deviation
    s = np.random.normal(mu, sigma, len(x))
    return s  

def creat1DimLinData(x,a,b):
    s = creatNormal(x)
    print(s)
    y = a*x+b+s
    print(y)
    return y
