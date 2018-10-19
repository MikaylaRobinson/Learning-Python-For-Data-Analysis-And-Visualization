#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy.random import randn


# In[2]:


ser1 = Series([1,2,3,4],index = ['A','B','C','D'])
ser1


# In[3]:


ser2 = ser1.reindex(['A','B','C','D','E','F'])
ser2


# In[4]:


ser2.reindex(['A','B','C','D','E','F','G'], fill_value=0)


# In[6]:


ser3 = Series(['USA','Mexico','Canada'],index=[0,5,10])
ser3


# In[7]:


ranger = range(15)
ranger


# In[8]:


ranger


# In[9]:


ser3.reindex(ranger,method='ffill')


# In[10]:


dframe = DataFrame(randn(25).reshape((5,5)),index=['A','B','D','E','F'],columns=['col1','col2','col3','col4','col5'])
dframe


# In[13]:


dframe2 = dframe.reindex(['A','B','C','D','E','F'])


# In[14]:


dframe2


# In[15]:


new_columns = ['col1','col2','col3','col4','col5','col6']


# In[16]:


dframe2.reindex(columns=new_columns)


# In[17]:


dframe


# In[18]:


dframe.ix[['A','B','C','D','E','F'],new_columns]


# In[ ]:




