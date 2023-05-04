import numpy as np
import matplotlib.pyplot as plt

plt.axis([0,150,100,0])

r=40
alpha1=radians(0)
alpha2=radians(360)
dalpha=radians(2)
xc=75
yc=50
plt.scatter(xc,yc,s=10,color='k')
for alpha in np.arange(alpha1,alpha2,dalpha):
    x=xc+r*cos(alpha)
    y=yc+r*sin(alpha)
    plt.scatter(x,y,s=5,color='k')

plt.show()
