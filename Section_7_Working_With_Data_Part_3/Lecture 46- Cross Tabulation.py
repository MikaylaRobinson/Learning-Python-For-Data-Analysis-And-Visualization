#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


from io import StringIO


# In[4]:


data="""Sample Animal Intelligence
1 Dog Smart
2 Dog Smart
3 Cat Dumb
4 Cat Dumb
5 Dog Dumb
6 Cat Smart"""


# In[5]:


dframe = pd.read_table(StringIO(data),sep='\s+')


# In[6]:


dframe


# In[8]:


pd.crosstab(dframe.Animal,dframe.Intelligence,margins=True)


# In[ ]:




