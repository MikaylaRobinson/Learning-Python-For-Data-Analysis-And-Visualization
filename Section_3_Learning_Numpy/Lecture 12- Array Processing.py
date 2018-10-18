#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# Visualization using matplotlib

# In[4]:


points = np.arange(-5,5,.01)


# In[5]:


dx,dy = np.meshgrid(points,points)


# In[6]:


dx


# In[7]:


dy


# In[8]:


z = (np.sin(dx) + np.sin(dy))


# In[9]:


z


# In[10]:


plt.imshow(z)


# In[11]:


plt.imshow(z)
plt.colorbar()

plt.title('Plot for sin(x) + sin(y)')


# Call values from an array according to a set condtion

# In[12]:


A = np.array([1,2,3,4])
B = np.array([100,200,300,400])


# In[13]:


condition = np.array([True,True,False,False])


# In[14]:


answer = [(A_val if cond else B_val) for A_val, B_val, cond in zip(A,B,condition)]


# In[15]:


answer


# In[16]:


answer2 = np.where(condition,A,B)


# In[17]:


answer2


# Change values within the array according to the arguments. When the value is less than zero, change the value to zero. 

# In[18]:


from numpy.random import randn


# In[19]:


arr = randn(5,5)


# In[20]:


arr


# In[21]:


np.where(arr<0,0,arr)


# Other useful functions 

# In[22]:


arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr


# Find the sum of all values within the array

# In[23]:


arr.sum()


# Find the sum of each column

# In[24]:


arr.sum(0)


# Find the mean of all values within the array

# In[25]:


arr.mean()


# Find the standard deviation and variance 

# In[26]:


arr.std()


# In[27]:


arr.var()


# In[28]:


boo1_arr = np.array([True,False,True])


# If any values are true, then returns true.

# In[29]:


boo1_arr.any()


# All values must be true in order to return true

# In[30]:


boo1_arr.all()


# Create an array and sort them in numerical order

# In[31]:


arr = randn(5)


# In[32]:


arr


# In[33]:


arr.sort()


# In[34]:


arr


# Create an array of countries. Find a list of all countries represented without including repeats. 

# In[35]:


countries = np.array(['France','Germany', 'USA', 'Russia', 'USA', 'Mexico', 'Germany'])


# In[36]:


np.unique(countries)


# Search for countries within your array

# In[37]:


np.in1d(['France', 'USA', 'Sweden'],countries)

