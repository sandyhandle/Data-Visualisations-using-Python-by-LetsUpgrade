# -*- coding: utf-8 -*-
"""Data Visualisations using Python - Day 2 by LetsUgragde.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16NHJ9Mt1g8TM444vyh246njLlQLU6dHv
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import seaborn as sns
from numpy.random import randn, randint, uniform, sample
import matplotlib as mlp
import matplotlib.pyplot as plt
# %matplotlib inline

x = [1,3,5,7,9]
y = [2,4,2,5,6]
plt.barh(x,y)
plt.barh([2,4,6,8,10],[2,4,6,3,5])

a = np.array([1,2,3,4,5])
plt.hist(a)

iris = sns.load_dataset('iris')
iris.head(6)

iris.plot()

df = iris.drop(["species"],axis = 1)
df.head()

df.plot(kind="hist",color="#eeccff",alpha=0.9,figsize=(15,15))

df.plot.scatter(x ="petal_width" ,y = "petal_length",c="sepal_length",figsize = [15,15])

"""
**Assignment: Day 2**"""

df = pd.DataFrame(randn(10,4),columns=["a","b","c","d"])
df.plot.bar(figsize=[15,15])
