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


# In[7]:


tips = sns.load_dataset('tips')


# In[3]:


tips.head()


# In[4]:


sns.lmplot('total_bill','tip',tips)


# In[10]:


sns.lmplot('total_bill','tip',tips,order=4,scatter_kws={'marker':'o','color':'indianred'},line_kws={'linewidth':1,'color':'blue'})


# Scatterplot without fitting it to a regression

# In[12]:


sns.lmplot('total_bill','tip',tips,fit_reg=False)


# In[13]:


tips['tip_pect']=100*(tips['tip']/tips['total_bill'])


# In[14]:


tips.head()


# In[15]:


sns.lmplot('size','tip_pect',tips)


# In[16]:


sns.lmplot('size','tip_pect',tips,x_jitter=.1)


# Show the estimates for each bin

# In[17]:


sns.lmplot('size','tip_pect',tips,x_estimator=np.mean)


# In[18]:


sns.lmplot('total_bill','tip_pect',tips,hue='sex',markers=['x','o'])


# In[19]:


sns.lmplot('total_bill','tip_pect',tips,hue='day')


# Local regression

# In[21]:


sns.lmplot('total_bill','tip_pect',tips,lowess=True,line_kws={'color':'black'})


# In[22]:


sns.regplot('total_bill','tip_pect',tips)


# In[27]:


fig, (axis1,axis2) = plt.subplots(1,2,sharey=True)
sns.regplot('total_bill','tip_pect',tips,ax=axis1)
sns.violinplot(y=tips['tip_pect'],x=tips['size'],palette='Reds_r',ax=axis2)


# In[ ]:




