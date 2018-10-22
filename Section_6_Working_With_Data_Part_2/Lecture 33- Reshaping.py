#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series,DataFrame


# In[4]:


dframe1 = DataFrame(np.arange(8).reshape(2,4), index=pd.Index(['LA','SF'],name='city'),columns=pd.Index(['A','B','C','D'],name='letter'))
dframe1


# Using stack

# In[5]:


dframe_st = dframe1.stack()
dframe_st


# Returning it to a DataFrame

# In[6]:


dframe_st.unstack()


# In[7]:


dframe_st.unstack('letter')


# In[8]:


dframe_st.unstack('city')


# Null values with stack and unstack

# In[9]:


ser1 = Series([0,1,2],index=['Q','X','Y'])
ser2 = Series([4,5,6],index=['X','Y','Z'])


# In[10]:


dframe = pd.concat([ser1,ser2],keys=['Alpha','Beta'])
dframe


# In[11]:


dframe.unstack()


# The DataFrame has null values, but it will filter them out if you restack

# In[12]:


dframe.unstack().stack()


# In[13]:


dframe = dframe.unstack()
dframe


# You can use this argument (dropna=False) to keep the null values when restacking

# In[14]:


dframe.stack(dropna=False)


# In[ ]:




