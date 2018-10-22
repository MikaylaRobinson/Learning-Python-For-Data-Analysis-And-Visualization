#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series,DataFrame


# In[2]:


years = [1990,1991,1992,2009,2012,2015,1987,1969,2013,2008,1999]


# In[3]:


decade_bins = [1960,1970,1980,1990,2000,2010,2020]


# Cut by a defined bin list

# In[4]:


decade_cat = pd.cut(years,decade_bins)


# In[5]:


decade_cat


# Call categories formed by the cut

# In[6]:


decade_cat.categories


# Count the values in each bin

# In[7]:


pd.value_counts(decade_cat)


# Cut by number of bins you want

# In[8]:


pd.cut(years,2,precision=1)


# In[ ]:




