#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np


# In[11]:


my_list1 = [1,2,3,4]


# In[12]:


my_array1 = np.array(my_list1)


# In[13]:


my_array1


# In[14]:


my_list2 = [11,22,33,44]


# In[15]:


my_lists = [my_list1,my_list2]


# In[16]:


my_array2 = np.array(my_lists)


# In[17]:


my_array2


# In[18]:


my_array2.shape


# In[19]:


my_array2.dtype


# In[20]:


np.zeros(5)


# In[21]:


my_zeros_array = np.zeros(5)


# In[22]:


my_zeros_array.dtype


# In[23]:


np.ones([5,5])


# In[24]:


np.empty(5)


# In[25]:


np.eye(5)


# In[26]:


np.arange(5)


# In[27]:


np.arange(5,50,2)


# In[ ]:




