#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# In[2]:


from pandas import read_html


# Creating a DataFrame using html data

# In[3]:


url = 'http://www.fdic.gov/bank/individual/failed/banklist.html'


# In[4]:


dframe_list = pd.io.html.read_html(url)


# In[5]:


dframe = dframe_list[0]
dframe


# Finding the columns within the DataFrame

# In[6]:


dframe.columns.values

