#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# Split, apply, combine procedure are when data is separated, the data is manipulated and then recombined

# In[2]:


dframe_wine = pd.read_csv('winequality-red.csv',sep=';')


# In[4]:


dframe_wine.head()


# In[5]:


def ranker(df):
    df['alc_content_rank'] = np.arange(len(df)) +1
    return df


# In[7]:


dframe_wine.sort_values('alcohol',ascending = False, inplace=True)


# In[8]:


dframe_wine = dframe_wine.groupby('quality').apply(ranker)


# In[9]:


dframe_wine.head()


# In[10]:


num_of_qual = dframe_wine['quality'].value_counts()


# In[11]:


num_of_qual


# In[13]:


dframe_wine[dframe_wine.alc_content_rank == 1].head(len(num_of_qual))


# In[ ]:




