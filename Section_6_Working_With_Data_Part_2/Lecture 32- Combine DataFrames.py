#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series,DataFrame


# In[2]:


ser1 = Series([2,np.nan,4,np.nan,6,np.nan],index=['Q','R','S','T','U','V'])
ser1


# In[3]:


ser2 = Series(np.arange(len(ser1)),dtype=np.float64,index=['Q','R','S','T','U','V'])
ser2


# Combining Series: Taking ser1 and where there are null values, insert the value from ser2

# In[4]:


Series(np.where(pd.isnull(ser1),ser2,ser1),index=ser1.index)


# In[5]:


ser1.combine_first(ser2)


# In[6]:


nan=np.nan
dframe_odds = DataFrame({'X':[1.,nan,3.,nan],'Y':[nan,5.,nan,7.],'Z':[nan,9.,nan,11]})


# In[8]:


dframe_evens = DataFrame({'X':[2.,4.,nan,6.,8.],'Y':[nan,10.,12.,14.,16.]})


# In[9]:


dframe_odds


# In[10]:


dframe_evens


# Combining DataFrames

# In[11]:


dframe_odds.combine_first(dframe_evens)


# In[ ]:




