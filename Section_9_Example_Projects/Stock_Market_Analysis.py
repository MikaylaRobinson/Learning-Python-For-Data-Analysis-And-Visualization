#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import DataFrame, Series


# In[2]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


from pandas_datareader.data import DataReader


# In[4]:


from datetime import datetime


# In[5]:


from __future__ import division


# In[6]:


tech_list = ['AAPL','GOOG','MSFT','AMZN']


# In[7]:


end = datetime.now()
start = datetime(end.year-1,end.month,end.day)


# In[8]:


for stock in tech_list:
    globals()[stock] = DataReader(stock,'yahoo',start,end)


# In[9]:


AAPL.describe()


# In[10]:


AAPL.info()


# In[11]:


AAPL['Adj Close'].plot(legend=True,figsize=(10,4))


# In[12]:


AAPL['Volume'].plot(legend=True,figsize=(10,4))


# In[13]:


ma_day = [10,20,50]

for ma in ma_day:
    column_name = "MA for %s days" %(str(ma))
    
    AAPL[column_name] = AAPL['Adj Close'].rolling(window=ma,center=False).mean()


# In[14]:


AAPL[['Adj Close','MA for 10 days','MA for 20 days','MA for 50 days']].plot(subplots=False,figsize=(10,4))


# In[15]:


AAPL['Daily Return'] = AAPL['Adj Close'].pct_change()

AAPL['Daily Return'].plot(figsize=(10,4),legend=True,linestyle='--',marker='o')


# In[16]:


sns.distplot(AAPL['Daily Return'].dropna(),bins=100,color='purple')


# In[17]:


AAPL['Daily Return'].hist(bins=100)


# In[18]:


closing_df = DataReader(tech_list,'yahoo',start,end)['Adj Close']


# In[19]:


closing_df.head()


# In[20]:


tech_rets = closing_df.pct_change()


# In[21]:


tech_rets.head()


# In[22]:


sns.jointplot('GOOG','GOOG',tech_rets,kind= 'scatter',color='seagreen')


# In[23]:


sns.jointplot('GOOG','MSFT',tech_rets,kind='scatter')


# In[24]:


sns.pairplot(tech_rets.dropna())


# In[25]:


returns_fig = sns.PairGrid(tech_rets.dropna())
returns_fig.map_upper(plt.scatter,color='purple')
returns_fig.map_lower(sns.kdeplot,cmap='cool_d')
returns_fig.map_diag(plt.hist,bins=30)


# In[26]:


returns_fig = sns.PairGrid(closing_df)
returns_fig.map_upper(plt.scatter,color='purple')
returns_fig.map_lower(sns.kdeplot,cmap='cool_d')
returns_fig.map_diag(plt.hist,bins=30)


# In[27]:


sns.heatmap(data=tech_rets.dropna().corr(),annot=True)


# In[28]:


rets = tech_rets.dropna()


# In[29]:


area = np.pi*20

plt.scatter(rets.mean(),rets.std(),s=area)

plt.xlabel('Expected Return')
plt.ylabel('Risk')

for label, x, y in zip(rets.columns, rets.mean(), rets.std()):
    plt.annotate(
        label,
        xy = (x, y), xytext = (50, 50),
        textcoords = 'offset points', ha = 'right', va= 'bottom',
        arrowprops = dict(arrowstyle = '-', connectionstyle = 'arc3,rad=-0.3'))


# Calculating Value at Risk

# In[30]:


sns.distplot(AAPL['Daily Return'].dropna(),bins=100,color='purple')


# In[31]:


rets.head()


# In[32]:


rets['AAPL'].quantile(0.05)


# Value at Risk with Monte Carlo Method

# In[33]:


days = 365

dt = 1/days

mu = rets.mean()['GOOG']

sigma = rets.std()['GOOG']


# In[39]:


def stock_monte_carlo(start_price,days,mu,sigma):
    
    price = np.zeros(days)
    price[0] = start_price
    
    shock = np.zeros(days)
    drift = np.zeros(days)
    
    for x in range(1,days):
        
        shock[x] = np.random.normal(loc=mu*dt,scale=sigma*np.sqrt(dt))
        
        drift[x] = mu * dt
        
        price[x] = price[x-1] + (price[x-1] * (drift[x] + shock[x]))
    
    return price


# In[35]:


GOOG.head()


# In[40]:


start_price = 1034.87

for run in range(100):
    plt.plot (stock_monte_carlo(start_price,days,mu,sigma))
    
plt.xlabel('Days')
plt.ylabel('Price')
plt.title('Monte Carlo Analysis for Google')


# In[41]:


runs = 10000

simulations = np.zeros(runs)

for run in range(runs):
    simulations[run] = stock_monte_carlo(start_price, days, mu, sigma)[days-1]


# In[44]:


q=np.percentile(simulations,1)

plt.hist(simulations,bins=200)

plt.figtext(0.6, 0.8, s="Start price: $%.2f" %start_price)

plt.figtext(0.6,0.7, "Mean final price: $%.2f" % simulations.mean())

plt.figtext(0.6, 0.6, "VaR(0.99): $%.2f" % (start_price - q,))

plt.figtext(0.15, 0.6, "q(0.99): $%.2f" % q)

plt.axvline(x=q, linewidth=4, color='r')

plt.title(u"Final price distribution for Google Stock after %s days" % days, weight = 'bold');


# In[ ]:




