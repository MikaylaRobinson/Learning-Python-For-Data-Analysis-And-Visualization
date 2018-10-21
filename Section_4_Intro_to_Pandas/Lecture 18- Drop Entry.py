#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd
from pandas import Series, DataFrame


# In[2]:


ser1 = Series(np.arange(3),index=['a','b','c'])
ser1


# Dropping an index

# In[3]:


ser1.drop('b')


# In[5]:


dframe1 = DataFrame(np.arange(9).reshape((3,3)),index=['SF','LA','NY'],columns=['pop','size','year'])
dframe1


# Dropping a row

# In[7]:


dframe1.drop('LA')


# In[8]:


dframe1


# In[9]:


dframe2 = dframe1.drop('LA')


# In[10]:


dframe2


# In[11]:


dframe1


# Dropping a column

# In[12]:


dframe1.drop('year',axis=1)


# In[ ]:




