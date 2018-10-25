#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from numpy.random import randn
import pandas as pd

from scipy import stats

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


dataset1 = randn(100)


# Making a default histogram

# In[3]:


plt.hist(dataset1)


# In[4]:


dataset2 = randn(80)


# Changing the color of a histogram

# In[6]:


plt.hist(dataset2,color='indianred')


# Putting two datasets on the same plot. Normed is used to normalize dataset and use two sets with different amounts of data points

# In[7]:


plt.hist(dataset1,normed=True,color='indianred',alpha=0.5,bins=20)
plt.hist(dataset2,normed=True,alpha=0.5,bins=20)


# In[8]:


data1 = randn(1000)
data2 = randn(1000)


# Joint plots 

# In[10]:


sns.jointplot(data1,data2)


# In[12]:


sns.jointplot(data1,data2,kind='hex')


# In[ ]:




