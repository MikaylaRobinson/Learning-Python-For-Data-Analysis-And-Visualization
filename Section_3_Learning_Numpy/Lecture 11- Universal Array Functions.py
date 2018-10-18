#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[4]:


arr = np.arange(11)
arr


# Simple universal functions

# In[5]:


np.sqrt(arr)


# In[6]:


np.exp(arr)


# Using random arrays to demonstrate more universal functions

# In[7]:


A = np.random.randn(10)


# In[8]:


A


# In[9]:


B = np.random.randn(10)
B


# Add the values together in each location of two arrays

# In[10]:


np.add(A,B)


# Find the maximum value in a location between two arrays

# In[12]:


np.maximum(A,B)

