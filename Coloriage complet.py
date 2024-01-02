# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 14:59:59 2022

@author: bebo
"""

import matplotlib.pyplot as plt
import numpy as np


def f1(x):
    return 1.0 / np.exp(x)

def f2(x):
    return np.log(x)

x = np.arange(0.01,10,0.1) 
#vs x = np.linspace(0.01,10,0.1)

y1 = f1(x)
y2 = f2(x)
plt.plot(x,y1,'turquoise')
plt.plot(x,y2,'blue')

plt.fill_between(x, y1, y2, where= y1<y2, color='pink')
plt.fill_between(x,y1,y2, where= y1>y2, color = 'blue')
#plt.fill_between(color = 'red')


plt.grid()

plt.xlim(0,10)
plt.ylim(-1,2.5)
plt.title('Coloriage',fontsize=10)

#plt.fill("j", "k", 'm',
#         data={"j": [0, 1, 2],
#               "k": [0, 1, 0]})

plt.show()