# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 23:35:56 2021

@author: bebo
"""
import matplotlib.pyplot as plt
import numpy as np
import time

def f1(x):
    return 1.0 / np.exp(x)

def f2(x):
    return np.log(x)

x = np.arange(0.01,10,0.1) 
#vs x = np.linspace(0.01,10,0.1)

y1 = f1(x)
y2 = f2(x)

plt.plot(x,y1,'blue')
plt.plot(x,y2,'red')

plt.fill_between(x, y1, y2, color='yellow')

plt.grid()

plt.xlim(0,10)
plt.ylim(-1,2.5)

plt.title('Coloriage',fontsize=10)

plt.show()

time.sleep(2)


plt.plot(x,y1,'turquoise')
plt.plot(x,y2,'green')

plt.fill_between(x, y1, y2, where=y1<y2, color='pink')

plt.grid()

plt.xlim(0,10)
plt.ylim(-1,2.5)
plt.title('Coloriage',fontsize=10)

plt.show()
#plt.close()
