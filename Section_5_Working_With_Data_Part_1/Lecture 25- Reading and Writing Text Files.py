#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# Creating a DataFrame from a .csv file

# In[2]:


dframe = pd.read_csv('lec25.csv')


# In[3]:


dframe


# Change the DataFrame headers by setting the headers when reading the file

# In[4]:


dframe = pd.read_csv('lec25.csv',header = None)


# In[5]:


dframe


# Create DataFrame using read_table. Since you are not defining that it is a .csv file, you must include that the data is separated by commas

# In[6]:


dframe = pd.read_table('lec25.csv',sep=',',header=None)


# In[7]:


dframe


# You can read specific rows from a file

# In[9]:


pd.read_csv('lec25.csv',header=None,nrows=2)


# Exporting a DataFrame to a file

# In[10]:


dframe.to_csv('mytextdata_out.csv')


# Showing the output of writing the DataFrame to a .csv file

# In[11]:


import sys


# In[12]:


dframe.to_csv(sys.stdout)


# You can change what is separating each data point

# In[13]:


dframe.to_csv(sys.stdout,sep='_')


# In[14]:


dframe.to_csv(sys.stdout,sep='?')


# Only writing some columns to the .csv file

# In[16]:


dframe.to_csv(sys.stdout,columns=[0,1,2])


# In[ ]:




