# -*- coding: utf-8 -*-
"""Introduction Data Visualisations using Python by LetsUgragde

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11QELXNK0QoHRpAcxy1VpyygrYRXzbntr
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib as mlp
import matplotlib.pyplot as plt
# %matplotlib inline

print(mlp.__version__)

from numpy.random import randn, randint, uniform, sample

a = np.arange(0,10)
b = np.arange(20,30)
plt.plot(a,b)
plt.title("Summa..")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

x = np.arange(0,4 * np.pi, 0.1)
y = np.sin(x)
plt.title("Sin Waveform")

plt.plot(x,y, color="r")
plt.show()

"""Assignment day 1"""

x = np.arange(0,10)
y = x*x
plt.plot(x,y,"r.--")

x = np.arange(0,4 * np.pi, 0.1)
y = np.sin(x)
plt.title("Sin Waveform")

plt.subplot(3,2,2)
plt.plot(x,y,color="b")
plt.subplot(3,2,1)
plt.plot(x,y,color="g")
plt.subplot(3,2,3)
plt.plot(x,y,color="y")

plt.subplot(3,2,4)
plt.plot(x,y,"b*--")
plt.subplot(3,2,5)
plt.plot(x,y,"g*--")
plt.subplot(3,2,6)
plt.plot(x,y,"yo")

"""Assignment 2 day 1"""

days = np.arange(1,8)
sales = [160,150,140,145,175,165,180]
plt.plot(days,sales,"b*--")
plt.show()

days = np.arange(1,8)
sales1 = [160,150,140,145,175,165,180]
sales2 = [70,90,160,150,140,145,175]
plt.plot(days,sales1,"b--")
plt.plot(days,sales2,"r--")
plt.show()
