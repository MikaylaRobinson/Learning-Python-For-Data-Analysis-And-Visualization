#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# Import excel file using pandas

# In[4]:


xlsfile = pd.ExcelFile('Lect_28.xlsx')


# Use parse to create a DataFrame

# In[5]:


dframe = xlsfile.parse('Sheet1')


# In[6]:


dframe


# In[ ]:




