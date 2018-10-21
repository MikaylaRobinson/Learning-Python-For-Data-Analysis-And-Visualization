#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# In[2]:


ser1 = Series(range(3),index=['C','A','B'])
ser1


# Sorting by index

# In[3]:


ser1.sort_index()


# In[5]:


ser1


# Using sort_values instead of order method because of the version of pandas

# In[7]:


ser1.sort_values()


# In[8]:


from numpy.random import randn


# In[9]:


ser2= Series(randn(10))
ser2


# In[12]:


ser2.sort_values()


# In[13]:


ser2.rank()


# In[14]:


ser3 = Series(randn(10))
ser3


# In[21]:


ser3.sort_values().rank()


# In[22]:


ser3


# In[ ]:




