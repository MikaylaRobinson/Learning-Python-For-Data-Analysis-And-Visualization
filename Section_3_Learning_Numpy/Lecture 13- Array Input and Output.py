#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# Saving an array and recalling it. 

# In[2]:


arr = np.arange(5)
arr


# In[3]:


np.save('myarray',arr)


# In[4]:


arr = np.arange(10)
arr


# In[5]:


np.load('myarray.npy')


# In[6]:


arr1 = np.load('myarray.npy')
arr1


# Save and load more than one array

# In[7]:


arr2 = arr
arr2


# In[8]:


np.savez('ziparray.npz',x=arr1,y=arr2)


# In[9]:


archive_array = np.load('ziparray.npz')


# In[10]:


archive_array['x']


# In[11]:


archive_array['y']


# Save an array as a .txt file using commas to separate the values.

# In[12]:


arr = np.array([[1,2,3],[4,5,6]])
arr


# In[13]:


np.savetxt('mytextarray.txt',arr,delimiter=',')


# In[14]:


arr = np.loadtxt('mytextarray.txt', delimiter = ',')
arr

