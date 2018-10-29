#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pandas import Series,DataFrame


# In[2]:


titanic_df = pd.read_csv('train.csv')


# In[3]:


titanic_df.head()


# In[4]:


titanic_df.info()


# Who were the passengers on the Titanic? (Ages,Gender,Class,..etc)

# In[5]:


import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# Male vs. female passenger counts

# In[6]:


sns.countplot('Sex',data=titanic_df)


# Males vs. females in each class

# In[7]:


sns.countplot('Sex',data=titanic_df,hue='Pclass')


# In[8]:


sns.countplot('Pclass',data=titanic_df,hue='Sex')


# Male vs. female vs. child passenger counts

# In[9]:


def male_female_child(passenger):
    age,sex = passenger
    
    if age < 16:
        return 'child'
    else:
        return sex


# In[10]:


titanic_df['person'] = titanic_df[['Age','Sex']].apply(male_female_child,axis=1)


# In[11]:


titanic_df[0:10]


# In[12]:


sns.countplot('Pclass',data=titanic_df,hue='person')


# In[13]:


titanic_df['Age'].hist(bins=70)


# In[14]:


titanic_df['Age'].mean()


# In[15]:


titanic_df['person'].value_counts()


# In[16]:


fig = sns.FacetGrid(titanic_df,hue='Sex',aspect=4)
fig.map(sns.kdeplot,'Age',shade=True)

oldest= titanic_df['Age'].max()
fig.set(xlim=(0,oldest))

fig.add_legend()


# In[17]:


fig = sns.FacetGrid(titanic_df,hue='person',aspect=4)
fig.map(sns.kdeplot,'Age',shade=True)

oldest= titanic_df['Age'].max()
fig.set(xlim=(0,oldest))

fig.add_legend()


# In[18]:


fig = sns.FacetGrid(titanic_df,hue='Pclass',aspect=4)
fig.map(sns.kdeplot,'Age',shade=True)

oldest= titanic_df['Age'].max()
fig.set(xlim=(0,oldest))

fig.add_legend()


# What deck were the passengers on and how does that relate to their class?

# In[19]:


titanic_df.head()


# In[20]:


deck = titanic_df['Cabin'].dropna()


# In[21]:


deck.head()


# In[22]:


levels = []
for level in deck:
    levels.append(level[0])
cabin_df = DataFrame(levels)
cabin_df.columns = ['Cabin']
cabin_df['Cabin'].values.sort()
sns.countplot('Cabin',data=cabin_df,palette='winter_d')


# In[23]:


cabin_df = cabin_df[cabin_df.Cabin != 'T']
cabin_df['Cabin'].values.sort()
sns.countplot('Cabin',data=cabin_df,palette='summer')


# In[24]:


titanic_df.head()


# Where did the passengers come from?

# In[25]:


sns.countplot('Embarked',data=titanic_df,hue='Pclass',order=['C','Q','S'])


# Who was alone and who was with family?

# In[26]:


titanic_df.head()


# In[27]:


titanic_df['Alone'] = titanic_df.SibSp + titanic_df.Parch


# In[28]:


titanic_df['Alone']


# In[29]:


titanic_df['Alone'].loc[titanic_df['Alone']>0] = 'With Family'

titanic_df['Alone'].loc[titanic_df['Alone']==0] = 'Alone'


# In[30]:


titanic_df.head()


# In[31]:


sns.countplot('Alone',data=titanic_df,palette='Blues')


# What factors helped someone survive the sinking?

# In[32]:


titanic_df['Survivor'] = titanic_df.Survived.map({0:'no',1:'yes'})

sns.countplot('Survivor',data=titanic_df, palette='Set1')


# Was class a factor in survival?

# In[33]:


sns.catplot('Pclass','Survived',data=titanic_df,kind='point')


# Class and gender as a factor for survival

# In[34]:


sns.catplot('Pclass','Survived',data=titanic_df,hue='person',kind='point')


# Is age a factor in survival?

# In[35]:


sns.lmplot('Age','Survived',data=titanic_df)


# In[36]:


sns.lmplot('Age','Survived',hue='Pclass',data=titanic_df,palette='winter')


# In[37]:


generations = [10,20,40,60,80]

sns.lmplot('Age','Survived',hue='Pclass',data=titanic_df,palette='winter',x_bins=generations)


# How gender and age influenced survival

# In[38]:


sns.lmplot('Age','Survived',hue='Sex',data=titanic_df,palette='winter',x_bins=generations)


# Did the deck have an effect on the passengers survival rate? 

# In[39]:


titanic_df.head()


# In[40]:


titanic_df_no_null = titanic_df.dropna()

def Find_Deck(Cabin):
    Deck_Letter = Cabin[0]
    return Deck_Letter

titanic_df_no_null['Deck'] = titanic_df_no_null['Cabin'].apply(Find_Deck)


# In[42]:


titanic_df_no_null.head()


# In[51]:


titanic_df_no_null['Deck'].values.sort()
sns.catplot('Deck','Survived',data=titanic_df_no_null,palette='winter',kind='point')


# Did having a family member increase the odds of surviving the crash?

# In[52]:


titanic_df.head()


# In[55]:


sns.catplot('Alone','Survived',data=titanic_df,palette= 'cool',kind='point')


# In[ ]:




