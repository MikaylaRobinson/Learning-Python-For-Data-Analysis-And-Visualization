#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# Using np.arange to create an array

# In[3]:


arr = np.arange(0,11)


# In[4]:


arr


# Calling different values from within the array

# In[5]:


arr[8]


# In[6]:


arr[1:5]


# In[7]:


arr[0:5]


# Replacing values in the first five positions of the array

# In[8]:


arr[0:5] = 100


# In[9]:


arr


# Restoring the original array

# In[11]:


arr = np.arange(0,11)


# In[12]:


arr


# Calling a section of the array and storing it in its own variable. The values within slice_of_arr are just a view of the original array, meaning changes to slice_of_arr will be seen in the original array. 

# In[13]:


slice_of_arr = arr[0:6]


# In[14]:


slice_of_arr


# In[15]:


slice_of_arr[:] = 99


# In[16]:


slice_of_arr


# In[17]:


arr


# Making a copy of an array

# In[18]:


arr_copy = arr.copy()


# In[19]:


arr_copy


# Creating a new array containing multiple lists

# In[20]:


arr_2d = np.array(([5,10,15],[20,25,20],[35,40,45]))
arr_2d


# When calling from an array like this, the first number specified calls the row position. The second value specifies the column position. 

# In[21]:


arr_2d[1]


# In[22]:


arr_2d[1][0]


# In[23]:


arr_2d


# In[24]:


arr_2d[:2,1:]


# In[25]:


arr_2d[2]


# Creating an array containing only zeros. The numbers within the argument specify the amount of rows and columns. 

# In[6]:


arr2d = np.zeros((10,8))


# In[7]:


arr2d


# Finding the value count per row

# In[8]:


arr_length = arr2d.shape[1]


# In[9]:


arr_length


# In[10]:


for i in range(arr_length):
    arr2d[i] = 1


# In[31]:


arr2d


# In[11]:


for i in range(arr_length):
    arr2d[i] = i


# In[13]:


arr2d


# In[35]:


arr2d[[2,4,6,8]]


# In[36]:


arr2d[[6,4,2,7]]


# In[ ]:




