#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd
from pandas import Series,DataFrame


# In[2]:


ser1 = Series([1,2,3,4,1,2,3,4])
ser1


# Call the .replace(value_you_want_to_replace, what_you_replace_it_with)

# In[4]:


ser1.replace(1,np.nan)


# Replace more than one value using a list

# In[5]:


ser1.replace([1,4],[100,400])


# Pass dictionaries to replace a key with its value

# In[6]:


ser1.replace({4:np.nan})


# In[ ]:




