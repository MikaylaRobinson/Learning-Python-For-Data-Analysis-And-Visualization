#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# In[2]:


dframe = DataFrame(np.arange(16).reshape(4,4))


# In[3]:


blender = np.random.permutation(4)


# In[4]:


blender


# In[5]:


dframe


# In[6]:


dframe.take(blender)


# In[7]:


box = np.array([1,2,3])


# In[8]:


shaker = np.random.randint(0,len(box),size=10)


# In[9]:


shaker


# In[10]:


hand_grabs = box.take(shaker)
hand_grabs


# In[ ]:




