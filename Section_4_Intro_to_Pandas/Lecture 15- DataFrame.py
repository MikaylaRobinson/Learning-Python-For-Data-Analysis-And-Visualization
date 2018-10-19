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


# In[10]:


nfl_frame.columns


# In[19]:


nfl_frame.GP


# In[20]:


nfl_frame.columns = nfl_frame.columns.str.strip()


# In[21]:


nfl_frame.columns


# In[23]:


nfl_frame.Team


# In[24]:


nfl_frame['First NFL Season']


# In[25]:


DataFrame(nfl_frame,columns=['Team','First NFL Season'])


# In[26]:


DataFrame(nfl_frame,columns=['Team','First NFL Season','Stadium'])


# In[27]:


nfl_frame


# In[28]:


nfl_frame.head(3)


# In[29]:


nfl_frame.tail(3)


# In[30]:


nfl_frame.ix[3]


# In[31]:


nfl_frame['Stadium'] = "Levi's Stadium"


# In[32]:


nfl_frame


# In[33]:


nfl_frame['Stadium'] = np.arange(5)


# In[34]:


nfl_frame


# In[35]:


stadiums = Series(["Levi's Stadium","AT&T Stadium"],index=[4,0])


# In[36]:


stadiums


# In[37]:


nfl_frame['Stadium'] = stadiums


# In[38]:


nfl_frame


# In[40]:


del nfl_frame['Stadium']


# In[41]:


nfl_frame


# In[42]:


data = {'City':['SF','LA','NYC'],'Population':[837000,3880000,8400000]}


# In[43]:


city_frame = DataFrame(data)


# In[44]:


city_frame


# In[ ]:




