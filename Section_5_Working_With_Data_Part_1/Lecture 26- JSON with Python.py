#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# In[2]:


json_obj = """
{   "zoo_animal": "Lion",
    "food": ["Meat", "Veggies", "Honey"],
    "fur": "Golden",
    "clothes": null, 
    "diet": [{"zoo_animal": "Gazelle", "food":"grass", "fur": "Brown"}]
}
"""


# In[3]:


import json


# Loading JSON data

# In[4]:


data= json.loads(json_obj)


# In[5]:


data


# Converting back to JSON

# In[6]:


json.dumps(data)


# Opening JSON data within a DataFrame

# In[7]:


dframe = DataFrame(data['diet'])


# In[8]:


dframe


# In[ ]:




