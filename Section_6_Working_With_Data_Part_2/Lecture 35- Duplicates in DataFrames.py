#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# In[2]:


dframe = DataFrame({'key1':['A']*2 + ['B']*3, 'key2':[2,2,2,3,3,]})


# In[3]:


dframe


# Finding where values are duplicated

# In[4]:


dframe.duplicated()


# Dropping duplicated values

# In[5]:


dframe.drop_duplicates()


# Dropping duplicates from a column specified in the argument

# In[6]:


dframe.drop_duplicates(['key1'])


# In[7]:


dframe


# Shows the last value found as a duplicate

# In[11]:


dframe.drop_duplicates(['key1'],keep='last')


# In[ ]:




