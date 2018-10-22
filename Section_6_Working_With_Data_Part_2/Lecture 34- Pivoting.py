#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series,DataFrame


# In[2]:


# Lets create some data to play with:

# Note: It is not necessary to understand how this dataset was made to understand this Lecture.

#import pandas testing utility
import pandas.util.testing as tm; tm.N = 3

#Create a unpivoted function
def unpivot(frame):
    N, K = frame.shape
    
    data = {'value' : frame.values.ravel('F'),
            'variable' : np.asarray(frame.columns).repeat(N),
            'date' : np.tile(np.asarray(frame.index), K)}
    
    # Return the DataFrame
    return DataFrame(data, columns=['date', 'variable', 'value'])

#Set the DataFrame we'll be using
dframe = unpivot(tm.makeTimeDataFrame())


# In[3]:


dframe


# Pivot method with the arguments defining row, columns, and fill values

# In[4]:


dframe_piv = dframe.pivot('date','variable','value')


# In[5]:


dframe_piv


# In[ ]:




