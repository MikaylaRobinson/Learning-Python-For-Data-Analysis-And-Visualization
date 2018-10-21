#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd
from pandas import Series, DataFrame


# In[2]:


data = Series(['one','two',np.nan,'four'])
data


# Finding missing data

# In[3]:


data.isnull()


# Dropping missing data

# In[4]:


data.dropna()


# In[5]:


dframe = DataFrame([[1,2,3],[np.nan,5,6],[7,np.nan,9],[np.nan,np.nan,np.nan]])
dframe


# Using .dropna in a DataFrame drops the entire row where there is missing data

# In[6]:


clean_dframe= dframe.dropna()
clean_dframe


# You must specify to only drop rows that are missing all data points

# In[7]:


dframe.dropna(how='all')


# Dropping columns with missing data

# In[8]:


dframe.dropna(axis=1)


# In[10]:


npn= np.nan
dframe2 = DataFrame([[1,2,3,npn],[2,npn,5,6],[npn,7,npn,9],[1,npn,npn,npn]])


# In[11]:


dframe2


# Dropping rows without a certain amount of data points

# In[12]:


dframe2.dropna(thresh=2)


# In[13]:


dframe2.dropna(thresh=3)


# In[14]:


dframe2


# Filling any null value

# In[16]:


dframe2.fillna(1)


# Filling null values according to column

# In[17]:


dframe2.fillna({0:0,1:1,2:2,3:3})


# In[18]:


dframe2.fillna(0)


# In[19]:


dframe2.fillna(0,inplace=True)


# In[ ]:


dframe

