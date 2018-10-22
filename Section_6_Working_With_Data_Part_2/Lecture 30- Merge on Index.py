#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# In[2]:


df_left = DataFrame({'key':['X','Y','Z','X','Y'],'data':range(5)})


# In[3]:


df_left


# In[4]:


df_right = DataFrame({'group_data':[10,20]},index=['X','Y'])


# In[5]:


df_right


# Merge using the key from the left DataFrame and the index from the right DataFrame

# In[6]:


pd.merge(df_left,df_right,left_on='key',right_index=True)


# Using a hierarchy index with merging

# In[8]:


df_left_hr = DataFrame({'key1':['SF','SF','SF','LA','LA'],'key2':[10,20,30,20,30],'data_set':np.arange(5.)})


# In[9]:


df_left_hr


# In[11]:


df_right_hr = DataFrame(np.arange(10).reshape(5,2),index=[['LA','LA','SF','SF','SF'],[20,10,10,10,20]],columns=['col_1','col_2'])


# In[12]:


df_right_hr


# In[13]:


pd.merge(df_left_hr,df_right_hr,left_on=['key1','key2'],right_index=True)


# Using join method to merge

# In[14]:


df_left.join(df_right)


# In[ ]:




