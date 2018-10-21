#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# In[2]:


my_ser = Series([1,2,3,4],index=['A','B','C','D'])
my_ser


# In[3]:


my_index = my_ser.index


# In[4]:


my_index


# You can call an index or an index range

# In[5]:


my_index[2]


# In[6]:


my_index[2:]


# In[7]:


my_index[0]


# Indexed are immutable. You can't change index values

# In[8]:


my_index[0] = 'z'


# In[ ]:




