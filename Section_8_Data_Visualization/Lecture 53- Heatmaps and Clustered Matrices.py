#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from numpy.random import randn
import pandas as pd

from scipy import stats

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


flight_dframe = sns.load_dataset('flights')


# In[3]:


flight_dframe.head()


# In[4]:


flight_dframe = flight_dframe.pivot('month','year','passengers')


# In[5]:


flight_dframe


# In[6]:


sns.heatmap(flight_dframe)


# In[7]:


sns.heatmap(flight_dframe,annot=True,fmt='d')


# In[8]:


sns.heatmap(flight_dframe,center=flight_dframe.loc['January',1955])


# In[12]:


f,(axis1,axis2) = plt.subplots(2,1)
yearly_flights = flight_dframe.sum()

years= pd.Series(yearly_flights.index.values)
years = pd.DataFrame(years)

flights= pd.Series(yearly_flights.values)
flights = pd.DataFrame(flights)

year_dframe = pd.concat((years,flights),axis=1)
year_dframe.columns = ['Year','Flights']

sns.barplot('Year',y='Flights',data=year_dframe,ax=axis1)

sns.heatmap(flight_dframe,cmap='Blues',ax=axis2,cbar_kws={'orientation':'horizontal'})


# In[13]:


sns.clustermap(flight_dframe)


# In[14]:


sns.clustermap(flight_dframe,col_cluster=False)


# In[15]:


sns.clustermap(flight_dframe,standard_scale=1)


# In[16]:


sns.clustermap(flight_dframe,standard_scale=0)


# In[17]:


sns.clustermap(flight_dframe,z_score=1)


# In[ ]:




