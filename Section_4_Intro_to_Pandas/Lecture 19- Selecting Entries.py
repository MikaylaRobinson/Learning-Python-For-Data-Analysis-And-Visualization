#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series,DataFrame


# In[2]:


ser1 = Series(np.arange(3),index=['A','B','C'])
ser1 = 2*ser1
ser1


# Call entry from index name, index, or index range

# In[3]:


ser1['B']


# In[4]:


ser1[1]


# In[5]:


ser1[0:3]


# In[6]:


ser1[['A','B']]


# Call values using an argument

# In[7]:


ser1[ser1>3]


# Change values using all of these methods

# In[8]:


ser1[ser1>3] = 10


# In[9]:


ser1


# In[10]:


dframe = DataFrame(np.arange(25).reshape((5,5)),index=['NYC','LA','SF','DC','Chi'],columns=['A','B','C','D','E'])


# In[11]:


dframe


# Select from a DataFrame by one or more column names

# In[12]:


dframe['B']


# In[13]:


dframe[['B','E']]


# In[14]:


dframe[dframe['C']>8]


# In[15]:


dframe


# In[16]:


dframe >10


# In[17]:


dframe.ix['LA']


# In[18]:


dframe.ix[1]


# In[ ]:




