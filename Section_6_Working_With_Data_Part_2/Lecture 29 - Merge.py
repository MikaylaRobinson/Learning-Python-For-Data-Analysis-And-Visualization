#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# In[5]:


dframe1 = DataFrame({'key':['X','Z','Y','Z','X','X'],'data_set_1':np.arange(6)})
dframe1


# In[6]:


dframe2 = DataFrame({'key':['Q','Y','Z'],'data_set_2':[1,2,3]})
dframe2


# Merge the DataFrames overlapping where the keys match

# In[7]:


pd.merge(dframe1,dframe2)


# Merge on a specific column

# In[8]:


pd.merge(dframe1,dframe2, on='key')


# You can add a left argument where the key and index values for the left DataFrame are used

# In[9]:


pd.merge(dframe1,dframe2,on='key',how='left')


# You can also do a right merge where the keys from the right DataFrame will be used

# In[10]:


pd.merge(dframe1,dframe2,on='key',how='right')


# To use both keys, you can do a union of the keys

# In[11]:


pd.merge(dframe1,dframe2,on='key',how='outer')


# In[13]:


dframe3 = DataFrame({'key':['X','X','X','Y','Z','Z'],'data_set_3':range(6)})


# In[14]:


dframe4 = DataFrame({'key':['Y','Y','X','X','Z'],'data_set_4':range(5)})


# In[15]:


dframe3


# In[16]:


dframe4


# In[17]:


pd.merge(dframe3,dframe4)


# Merging with multiple keys

# In[18]:


df_left = DataFrame({'key1':['SF','SF','LA'],'key2':['one','two','one'],'left_data':[10,20,30]})


# In[20]:


df_right = DataFrame({'key1':['SF','SF','LA','LA'],'key2':['one','one','one','two'],'right_data':[40,50,60,70]})


# In[21]:


df_left


# In[22]:


df_right


# In[26]:


pd.merge(df_left,df_right,on=['key1','key2'],how='outer')


# Pandas will automatically edit column names if you merge DataFrames with the same column names

# In[24]:


pd.merge(df_left,df_right,on='key1')


# You could specify the column names yourself in place of the automatic suffix

# In[27]:


pd.merge(df_left,df_right,on='key1',suffixes=('_lefty','_righty'))


# In[ ]:




