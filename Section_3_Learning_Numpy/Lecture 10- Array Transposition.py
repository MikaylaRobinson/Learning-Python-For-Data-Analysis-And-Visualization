#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# Create an array and format it to have 10 rows containing 5 values each

# In[2]:


arr = np.arange(50).reshape((10,5))


# In[3]:


arr


# Reverse the array formatting to now have 5 rows containing 10 values each

# In[4]:


arr.T


# Find the dot product of the original and new array

# In[5]:


np.dot(arr.T,arr)


# Create an array with a third argument. This creates an array containing 5 lists. Each list then has 5 rows containing 2 values each.

# In[6]:


arr3d = np.arange(50).reshape((5,5,2))
arr3d


# Combine the first row from each list, then the second rows, and so on...

# In[7]:


arr3d.transpose((1,0,2))


# Create an array and then swap the axes. This array goes from having 1 row with 3 values to 3 rows containing one value each.

# In[8]:


arr = np.array([[1,2,3]])


# In[9]:


arr


# In[10]:


arr.swapaxes(0,1)

