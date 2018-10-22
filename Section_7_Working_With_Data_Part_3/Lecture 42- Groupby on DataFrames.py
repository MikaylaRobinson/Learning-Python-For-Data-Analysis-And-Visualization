#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import DataFrame, Series


# In[2]:


dframe = DataFrame({'k1':['X','X','Y','Y','Z'],'k2':['alpha','beta','alpha','beta','alpha'],'dataset1':np.random.randn(5),'dataset2':np.random.randn(5)})
dframe


# In[3]:


group1 = dframe['dataset1'].groupby(dframe['k1'])


# In[4]:


group1


# In[5]:


group1.mean()


# In[6]:


cities = np.array(['NY','LA','LA','NY','NY'])
month = np.array(['JAN','FEB','JAN','FEB','JAN'])


# In[7]:


dframe['dataset1'].groupby([cities,month]).mean()


# In[8]:


dframe


# In[9]:


dframe.groupby('k1').mean()


# In[10]:


dframe.groupby(['k1','k2']).mean()


# In[11]:


dframe.groupby(['k1']).size()


# In[12]:


dframe


# Group by keys

# In[14]:


for name,group in dframe.groupby('k1'):
    print ("This is the %s group" %name)
    print (group)
    print ('\n')


# In[17]:


for (k1,k2),group in dframe.groupby(['k1','k2']):
    print("Key1 = %s Key2 = %s" %(k1,k2))
    print (group)
    print ('\n')


# In[18]:


group_dict = dict(list(dframe.groupby('k1')))


# In[19]:


group_dict['X']


# In[20]:


group_dict_axis1 = dict(list(dframe.groupby(dframe.dtypes,axis=1)))


# In[21]:


group_dict_axis1


# Group by columns

# In[22]:


dataset2_group = dframe.groupby(['k1','k2'])[['dataset2']]
dataset2_group.mean()


# In[ ]:




