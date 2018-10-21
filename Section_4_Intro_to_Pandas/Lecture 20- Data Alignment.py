#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# When adding series, the data is aligned by index and the result is null if the index is not present in both series

# In[7]:


ser1 = Series([0,1,2],index=['A','B','C'])
ser1


# In[8]:


ser2 = Series([3,4,5,6],index=['A','B','C','D'])
ser2


# In[9]:


ser1 + ser2


# DataFrames can also be added like series

# In[10]:


dframe1 = DataFrame(np.arange(4).reshape((2,2)),columns=list('AB'),index=['NYC','LA'])
dframe1


# In[11]:


dframe2 = DataFrame(np.arange(9).reshape((3,3)),columns=list('ADC'),index=['NYC','SF','LA'])
dframe2


# In[12]:


dframe1 + dframe2


# In[13]:


dframe1 


# You can use fill values to replace null values

# In[14]:


dframe1.add(dframe2,fill_value=0)


# In[15]:


dframe2


# Using a DataFrame to create a series. 

# In[16]:


ser3 = dframe2.iloc[0]
ser3


# In[17]:


dframe2-ser3


# In[ ]:




