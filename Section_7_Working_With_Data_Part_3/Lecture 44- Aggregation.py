#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series,DataFrame


# Data aggregation: calling functions or methods that give a scalar result

# In[2]:


url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/'


# In[3]:


dframe_wine = pd.read_csv('winequality-red.csv',sep=';')


# In[4]:


dframe_wine.head()


# Finding the mean is an example of data aggregatiom

# In[5]:


dframe_wine['alcohol'].mean()


# In[6]:


dframe_wine


# Making your own aggregation function

# In[8]:


def max_to_min(arr):
    return arr.max() - arr.min()


# In[9]:


wino = dframe_wine.groupby('quality')


# In[10]:


wino.describe()


# In[11]:


wino.agg(max_to_min)


# In[12]:


wino.agg('mean')


# In[13]:


dframe_wine['qual/alc ratio'] = dframe_wine['quality']/dframe_wine['alcohol']


# In[14]:


dframe_wine.head()


# In[15]:


dframe_wine.pivot_table(index=['quality'])


# In[16]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[17]:


dframe_wine.plot(kind='scatter',x='quality',y='alcohol')


# In[ ]:




