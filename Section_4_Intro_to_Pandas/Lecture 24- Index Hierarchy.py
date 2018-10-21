#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np 
import pandas as pd
from pandas import Series, DataFrame
from numpy.random import randn


# Series with multiple index levels

# In[4]:


ser = Series(randn(6),index = [[1,1,1,2,2,2],['a','b','c','a','b','c']])


# In[5]:


ser


# In[6]:


ser.index


# In[7]:


ser[1]


# In[8]:


ser[2]


# In[9]:


ser[:,'a']


# Creating a DataFrame from a multilevel series

# In[10]:


dframe = ser.unstack()


# In[11]:


dframe


# In[14]:


dframe2 = DataFrame(np.arange(16).reshape(4,4),index=[['a','a','b','b'],[1,2,1,2]],columns=[['NY','NY','LA','SF'],['cold','hot','hot','cold']])


# In[15]:


dframe2


# Naming the multiple index levels

# In[17]:


dframe2.index.names = ['INDEX_1','INDEX_2']
dframe2.columns.names = ['Cities','Temp']
dframe2


# Changing level order

# In[18]:


dframe2.swaplevel('Cities','Temp',axis=1)


# In[20]:


dframe2.sort_index(level=1)


# In[21]:


dframe2.sum(level='Temp',axis=1)


# In[ ]:




