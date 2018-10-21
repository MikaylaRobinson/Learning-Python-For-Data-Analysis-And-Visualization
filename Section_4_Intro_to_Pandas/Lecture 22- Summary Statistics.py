#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# In[2]:


arr = np.array([[1,2,np.nan],[np.nan,3,4]])


# In[3]:


dframe1 = DataFrame(arr,index=['A','B'],columns=['One','Two','Three'])


# In[4]:


dframe1


# Summing columns in a DataFrame ignores null values

# In[5]:


dframe1.sum()


# Summing rows in a DataFrame

# In[6]:


dframe1.sum(axis=1)


# Finding min or max values or their index

# In[7]:


dframe1.min()


# In[8]:


dframe1.idxmin()


# In[9]:


dframe1


# Finding accumulation sum

# In[11]:


dframe1.cumsum()


# Getting summary statistics

# In[12]:


dframe1.describe()


# In[15]:


from pandas_datareader import data as wd
import datetime


# In[18]:


prices = wd.get_data_yahoo(['CVX','XOM','BP'],start=datetime.datetime(2010,1,1),end=datetime.datetime(2013,1,1))['Adj Close']
prices.head()


# In[18]:


prices = wd.get_data_yahoo(['CVX','XOM','BP'],start=datetime.datetime(2010,1,1),end=datetime.datetime(2013,1,1))['Adj Close']
prices.head()


# In[20]:


volume = wd.get_data_yahoo(['CVX','XOM','BP'],start=datetime.datetime(2010,1,1),end=datetime.datetime(2013,1,1))['Volume']


# In[22]:


volume.head()


# In[23]:


rets = prices.pct_change()


# Correlation of stocks

# In[25]:


corr = rets.corr


# In[27]:


get_ipython().run_line_magic('matplotlib', 'inline')
prices.plot()


# In[29]:


import seaborn as sns 
import matplotlib.pyplot as plt


# In[36]:


sns.heatmap(rets.corr())


# Counting unique values

# In[38]:


ser1 = Series(['w','w','x','y','z','w','x','y','x','a'])
ser1


# In[39]:


ser1.unique()


# In[40]:


ser1.value_counts()


# In[ ]:




