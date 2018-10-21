#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# In[6]:


import webbrowser
website='http://en.wikipedia.org/wiki/NFL_win-loss_records'
webbrowser.open(website)


# In[8]:


nfl_frame = pd.read_clipboard()


# In[9]:


nfl_frame


# Using .columns, the output is a list of all column names

# In[10]:


nfl_frame.columns


# In[20]:


nfl_frame.columns = nfl_frame.columns.str.strip()


# In[21]:


nfl_frame.columns


# There are two ways to call the data from a particular column. DataFrame_name.column_name or DataFrame_name['column_name']

# In[23]:


nfl_frame.Team


# In[24]:


nfl_frame['First NFL Season']


# Calling more than one column

# In[25]:


DataFrame(nfl_frame,columns=['Team','First NFL Season'])


# In[26]:


DataFrame(nfl_frame,columns=['Team','First NFL Season','Stadium'])


# In[27]:


nfl_frame


# Calling the first 3 rows and then the last 3 rows

# In[28]:


nfl_frame.head(3)


# In[29]:


nfl_frame.tail(3)


# Indexing also gives rows as the output

# In[30]:


nfl_frame.ix[3]


# Assigning this value for stadium will assign it for all rows

# In[31]:


nfl_frame['Stadium'] = "Levi's Stadium"


# In[32]:


nfl_frame


# In[33]:


nfl_frame['Stadium'] = np.arange(5)


# In[34]:


nfl_frame


# You can add a series to a DataFrame to assign values to only specific rows

# In[35]:


stadiums = Series(["Levi's Stadium","AT&T Stadium"],index=[4,0])


# In[36]:


stadiums


# In[37]:


nfl_frame['Stadium'] = stadiums


# In[38]:


nfl_frame


# Deleting a column from a DataFrame

# In[40]:


del nfl_frame['Stadium']


# In[41]:


nfl_frame


# Making a DataFrame using a dictionary

# In[42]:


data = {'City':['SF','LA','NYC'],'Population':[837000,3880000,8400000]}


# In[43]:


city_frame = DataFrame(data)


# In[44]:


city_frame


# In[ ]:




