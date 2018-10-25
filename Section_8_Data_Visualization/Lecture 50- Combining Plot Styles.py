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


# In[4]:


dataset = randn(100)


# Combines plots. Default is kde and histogram

# In[5]:


sns.distplot(dataset,bins=25)


# You can change the displayed plots by adding arguments

# In[6]:


sns.distplot(dataset,bins=25,rug=True,hist=False)


# Using dictionaries to edit each subplot

# In[7]:


sns.distplot(dataset,bins=25,
            kde_kws={'color':'indianred','label':'KDE PLOT'},
            hist_kws={'color':'blue','label':'HIST'})


# In[8]:


from pandas import Series

ser1 = Series(dataset,name='My_data')


# In[9]:


ser1


# In[10]:


sns.distplot(ser1,bins=25)


# In[ ]:




