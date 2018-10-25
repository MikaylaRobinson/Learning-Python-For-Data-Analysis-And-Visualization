#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from numpy.random import randn
import pandas as pd

from scipy import stats

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


data1 = randn(100)
data2 = randn(100)


# In[10]:


sns.boxplot(data=[data1,data2])


# In[11]:


sns.boxplot(data=[data1,data2],whis=np.inf)


# In[18]:


sns.boxplot(data= data1, orient= 'h')


# When a boxplot is not sufficient

# In[19]:


data1 = stats.norm(0,5).rvs(100)
data2 = np.concatenate([stats.gamma(5).rvs(50)-1,-1*stats.gamma(5).rvs(50)])
sns.boxplot(data=[data1,data2],whis=np.inf)


# In[22]:


sns.violinplot(data=[data1,data2])


# In[23]:


sns.violinplot(data=data2,bw=0.01)


# In[24]:


sns.violinplot(data=data1,inner='stick')


# In[ ]:




