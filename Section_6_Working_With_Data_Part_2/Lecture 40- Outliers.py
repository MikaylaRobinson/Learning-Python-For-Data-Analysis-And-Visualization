#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series,DataFrame


# In[2]:


np.random.seed(12345)


# In[3]:


dframe = DataFrame(np.random.randn(1000,4))


# In[4]:


dframe.head()


# In[5]:


dframe.tail()


# In[7]:


dframe.describe()


# In[8]:


col = dframe[0]


# In[9]:


col.head()


# In[10]:


col[np.abs(col)>3]


# In[11]:


dframe[(np.abs(dframe)>3).any(1)]


# In[12]:


dframe[np.abs(dframe)>3] = np.sign(dframe)*3


# In[13]:


dframe.describe()


# Capping the values allowed so that they will be within -3 and 3

# In[ ]:




