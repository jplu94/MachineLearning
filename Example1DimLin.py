#main example
#own
import include.creatData as cD
import include.Regression as R

#extern
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

print("HUHU")
a = 1 
b = 1 
x = np.linspace(0,10,10)
y = cD.creat1DimLinData(x,a,b)

w = R.LinReg(x,y)

fig, ax = plt.subplots()
ax.plot(x, y, 'o')
ax.plot(x, x*w[1]+w[0],'b',label='LinReg')
ax.plot(x, x*a+b,'r',label='ground True')
ax.grid()
#plt.xlim(0,10)
#plt.ylim(0,2)
plt.legend()
plt.show()
