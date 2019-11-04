#main example
#own
import include.creatData as cD
import include.Regression as R

#extern
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

print("HUHU")
xmax = 10
a = 0.1 
b = 0 
x = np.linspace(0,xmax,10)
y = cD.creat1DimLinData(x,a,b)
Polinom = 9  
w = R.LinReg(x,y,Polinom)
yPol = np.zeros(len(x))
for i in range(Polinom+1):
    print("I",i)
    yPol += w[i]*x**i 
fig, ax = plt.subplots()
ax.plot(x, y, 'o')
ax.plot(x, yPol,'b',label='LinReg')
ax.plot(x, x*a+b,'r',label='ground True')
ax.grid()
plt.xlim(0,xmax)
#plt.ylim(-2,2)
plt.legend()
plt.show()
