#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# Concatenate in numpy

# In[2]:


arr1 = np.arange(9).reshape(3,3)
arr1


# Combine by rows

# In[3]:


np.concatenate([arr1,arr1],axis=1)


# Combine by column

# In[4]:


np.concatenate([arr1,arr1],axis=0)


# Concatenate in pandas

# In[5]:


ser1 = Series([0,1,2],index=['T','U','V'])
ser2 = Series([3,4],index=['X','Y'])


# In[6]:


ser1


# In[7]:


ser2


# In[8]:


pd.concat([ser1,ser2])


# Specifying the axis to concatenate. axis=1 will create a DataFrame

# In[9]:


pd.concat([ser1,ser2],axis=1)


# Adding markers or keys to the concatenate using index hierarchy

# In[11]:


pd.concat([ser1,ser2],keys=['cat1','cat2'])


# These methods work the same for DataFrames as they did for Series

# In[12]:


dframe1 = DataFrame(np.random.randn(4,3),columns=['X','Y','Z'])
dframe2 = DataFrame(np.random.randn(3,3),columns=['Y','Q','X'])


# In[13]:


dframe1


# In[14]:


dframe2


# In[15]:


pd.concat([dframe1,dframe2])


# Ignoring an index in the concatenate

# In[16]:


pd.concat([dframe1,dframe2],ignore_index=True)


# In[ ]:




