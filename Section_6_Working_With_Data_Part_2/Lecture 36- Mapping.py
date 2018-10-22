#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series,DataFrame


# In[3]:


dframe = DataFrame({'city':['Alma','Brian Head','Fox Park'],'altitude':[3158,3000,2762]})
dframe


# In[4]:


state_map = {'Alma':'Colorado','Brian Head':'Utah','Fox Park':'Wyoming'}


# Adding a column and using a dictionary to fill with values matched to a column that already exists in the DataFrame

# In[5]:


dframe['state'] = dframe['city'].map(state_map)


# In[6]:


dframe


# In[ ]:




