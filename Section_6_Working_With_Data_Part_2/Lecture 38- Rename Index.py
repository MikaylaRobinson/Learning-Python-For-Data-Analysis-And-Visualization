#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series,DataFrame


# In[3]:


dframe = DataFrame(np.arange(12).reshape(3,4),index=['NY','LA','SF'],columns=['A','B','C','D'])
dframe


# Making city initials lowercase

# In[4]:


dframe.index.map(str.lower)


# In[5]:


dframe.index = dframe.index.map(str.lower)


# In[6]:


dframe


# Reframe makes a transformed version without modifying the original version

# In[7]:


dframe.rename(index=str.title,columns=str.lower)


# In[8]:


dframe.rename(index={'ny':'NEW YORK'},columns={'A':'ALPHA'})


# To make the changes permanent:

# In[9]:


dframe.rename(index={'ny':'NEW YORK'},inplace=True)


# In[10]:


dframe


# In[ ]:




