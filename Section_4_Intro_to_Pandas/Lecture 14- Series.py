#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np

import pandas as pd

from pandas import Series, DataFrame


# In[5]:


obj = Series([3,6,9,12])
obj


# In[6]:


obj.values


# In[7]:


obj.index


# In[8]:


ww2_cas = Series([8700000,4300000,3000000,2100000,400000],index=['USSR','Germany','China','Japan','USA'])
ww2_cas


# In[9]:


ww2_cas['USA']


# In[10]:


ww2_cas[ww2_cas > 4000000]


# In[11]:


'USSR' in ww2_cas


# In[12]:


ww2_dict = ww2_cas.to_dict()
ww2_dict


# In[13]:


ww2_series = Series(ww2_dict)
ww2_series


# In[14]:


countries = ['China','Germany','Japan','USA','USSR','Argentina']


# In[15]:


obj2 = Series(ww2_dict, index=countries)
obj2


# In[16]:


pd.isnull(obj2)


# In[17]:


pd.notnull(obj2)


# In[18]:


ww2_series


# In[19]:


obj2


# In[20]:


ww2_series + obj2


# In[21]:


obj2.name = 'World War 2 Casualties'


# In[23]:


obj2.index.name = 'Countries'


# In[25]:


obj2


# In[ ]:




