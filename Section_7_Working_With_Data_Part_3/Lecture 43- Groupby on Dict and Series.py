#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# In[2]:


animals = DataFrame(np.arange(16).reshape(4,4), columns = ['W','Z','Y','Z'], index = ['Dog','Cat','Bird','Mouse'])


# In[3]:


animals


# In[6]:


animals.loc[1:2,['W','Y']] = np.nan


# In[7]:


animals


# In[8]:


behavior_map = {'W':'good','X':'bad','Y':'good','Z':'bad'}


# Groupby using the mapping within the dictionary

# In[9]:


animal_col = animals.groupby(behavior_map,axis=1)
animal_col.sum()


# In[10]:


behav_series = Series(behavior_map)
behav_series


# Use groupby with a series

# In[11]:


animals.groupby(behav_series,axis=1).count()


# Use groupby with functions

# In[14]:


animals.groupby(len).sum()


# In[15]:


keys = ['A','B','A','B']


# In[16]:


animals.groupby([len,keys]).max()


# Use groupby with an index hierarchy

# In[17]:


hier_col = pd.MultiIndex.from_arrays([['NY','NY','NY','SF','SF'],[1,2,3,1,2]],names=['City','sub_value'])


# In[18]:


dframe_hr = DataFrame(np.arange(25).reshape(5,5),columns=hier_col)


# In[19]:


dframe_hr = dframe_hr * 100


# In[20]:


dframe_hr


# In[ ]:




