#!/usr/bin/env python
# coding: utf-8

# Importing and setting up the Boston housing data that is built into Scikit-learn.

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# In[2]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


from sklearn.datasets import load_boston


# In[4]:


boston = load_boston()


# In[6]:


print (boston.DESCR)


# Checking the data with a quick visualization to make sure we understand what results would make sense later. Looking at a histogram and a scatter plot.

# In[7]:


plt.hist(boston.target,bins=50)

plt.xlabel('Prices in $1000s')
plt.ylabel('Number of Houses')


# In[8]:


plt.scatter(boston.data[:,5],boston.target)
plt.ylabel('Price in $1000s')
plt.xlabel('Number of Rooms')


# Creating a DataFrame to be used as the data for a linear regression:

# In[9]:


boston_df = DataFrame(boston.data)
boston_df.columns = boston.feature_names
boston_df.head()


# In[10]:


boston_df['Price'] = boston.target  


# In[11]:


boston_df.head()


# This is the built in function in seaborn for linear regressions:

# In[13]:


sns.lmplot('RM','Price',data=boston_df)


# Now, using the Numpy Least Square Method for Univariate Linear Regression. The final product should be a recreation of the above plot that seaborn creates automatically:

# In[30]:


X = boston_df.RM


# In[31]:


X=np.vstack([boston_df.RM,np.ones(len(boston_df.RM))]).T


# In[32]:


X.shape


# In[33]:


Y = boston_df.Price


# In[34]:


X


# Getting m and b values for the best fit line (following y=mx + b)

# In[43]:


m , b = np.linalg.lstsq(X,Y,rcond=0)[0]


# In[44]:


print(m,b)


# In[47]:


plt.plot(boston_df.RM,boston_df.Price,'o')

x= boston_df.RM

plt.plot(x, m*x + b,'r',label='Best Fit Line')


# Finding the error in the best fit line:

# In[57]:


result = np.linalg.lstsq(X,Y,rcond=0)

error_total = result[1]

root_mean_square_error = np.sqrt(error_total/len(X))

print ("The root mean square error was %.2f" %root_mean_square_error)


# Using Scikit-Learn for a multivariate regression:

# In[59]:


import sklearn
from sklearn.linear_model import LinearRegression


# In[60]:


lreg = LinearRegression()


# In[61]:


X_multi = boston_df.drop('Price',1)
Y_target = boston_df.Price


# In[62]:


lreg.fit(X_multi,Y_target)


# In[63]:


print("The estimated intercept coefficient is %.2f" %lreg.intercept_)
print("The number of coefficients used was %d" %len(lreg.coef_))


# In[65]:


coeff_df = DataFrame(boston_df.columns)
coeff_df.columns = ['Features']

coeff_df['Coefficient Estimate'] = pd.Series(lreg.coef_)
coeff_df


# Training and Validation:

# In[67]:


X_train,X_test,Y_train,Y_test = sklearn.model_selection.train_test_split(X,boston_df.Price)


# In[68]:


print(X_train.shape,X_test.shape,Y_train.shape,Y_test.shape)


# Predicting house prices with the training and testing sets:

# In[69]:


lreg = LinearRegression()
lreg.fit(X_train,Y_train)


# In[71]:


pred_train = lreg.predict(X_train)
pred_test = lreg.predict(X_test)


# Finding mean square error:

# In[74]:


print("Fit a model with X_train and then find the mean square error with Y_train: %.2f" %np.mean((Y_train-pred_train)**2))

print("Fit a model with X_train and then find mean square error using X_test and Y_test: %.2f" %np.mean((Y_test-pred_test)**2))


# Using a residual plot to tell if the linear regression was appropriate for our data or if we needed to model it differently: 

# In[77]:


train = plt.scatter(pred_train,(pred_train-Y_train),c='b',alpha=0.5)

test = plt.scatter(pred_test,(pred_test-Y_test),c='r',alpha=0.5)

plt.hlines(y=0,xmin=-10,xmax=40)
plt.legend((train,test),('Training','Test'),loc='lower left')
plt.title('Residual Plots')


# This residual plot does not seem to have any particular pattern and the points seem to be scattered on either side of the zero line, supporting the use of a linear regression. 

# In[ ]:




