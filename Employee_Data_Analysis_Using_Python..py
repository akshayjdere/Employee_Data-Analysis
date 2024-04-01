#!/usr/bin/env python
# coding: utf-8

# ## Importing primary libraries 

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import  warnings
warnings.filterwarnings('ignore')


# ##  """(1) Data loading""" 

# In[2]:


emp = pd.read_csv('C:\\Users\\Akshay\\Downloads\\Employee.csv',encoding = 'latin-1')


# In[3]:


emp.head(3)


# In[4]:


emp.tail(3)


# ##   """(2) **Exploring the dataset**

# In[5]:


emp.shape


# In[6]:


emp.dtypes


# ## """Plotting different variables"""

# In[9]:


## a. Checking for no.of distinct values in each column in the dataset
emp.nunique()


# In[11]:


## """b. Number of employees gender wise"""
plt.figure(figsize=(4,4))
sns.set_style('whitegrid')
col={'Male':'green','Female':'red'}
e=sns.countplot(data=emp,x='Gender',palette=col)
for i in e.containers:
  e.bar_label(i)


# In[12]:


## """c. Exploring Education level of employees"""
plt.figure(figsize=(4,4))
col={'Male':'green','Female':'red'}
m=sns.countplot(data=emp,x='Education',hue='Gender',palette=col)
for i in m.containers:
  m.bar_label(i)


# In[13]:


## """d. Employees from different cities"""
plt.figure(figsize=(4,4))
col={'Male':'green','Female':'red'}
s=sns.countplot(data=emp,x='City',hue='Gender',palette=col)
for i in s.containers:
  s.bar_label(i)


# In[14]:


## """e. Year of joining"""
plt.figure(figsize=(5,5))
col={'Male':'green','Female':'red'}
s=sns.countplot(data=emp,x='JoiningYear',hue='Gender',palette=col)
for i in s.containers:
  s.bar_label(i)


# In[15]:


## """More employees joined in the year 2017 f. Age of employees"""

sns.set(font_scale=0.5)
plt.figure(figsize=(7,7))
col={'Male':'green','Female':'red'}
f=sns.countplot(data=emp,x='Age',hue='Gender',palette=col)
for i in f.containers:
  f.bar_label(i)


# In[16]:


plt.figure(figsize=(7,7))
d=sns.FacetGrid(emp,col='Gender')
d.map(sns.countplot,'Age')


# In[17]:


## """g. Payment and joining year"""

sns.set(font_scale=0.6)
sns.lineplot(data=emp,x='JoiningYear',y='PaymentTier',hue='Gender')


# In[18]:


## """h. Number of employees benched"""

sns.set(font_scale=0.6)
col={'Male':'green','Female':'red'}
s=sns.countplot(data=emp,x='EverBenched',hue='Gender',palette=col)
for i in s.containers:
  s.bar_label(i)


# In[19]:


## """i. Experience"""

sns.set(font_scale=0.6)
plt.figure(figsize=(6,6))
sns.set_style('whitegrid')
col={'Male':'green','Female':'red'}
s=sns.countplot(data=emp,x='ExperienceInCurrentDomain',hue='Gender',palette=col)
for i in s.containers:
  s.bar_label(i)


# In[20]:


## """j. Leave or not"""

sns.set(font_scale=0.6)
plt.figure(figsize=(6,6))
sns.set_style('whitegrid')
col={'Male':'green','Female':'red'}
s=sns.countplot(data=emp,x='LeaveOrNot',hue='Gender',palette=col)
for i in s.containers:
  s.bar_label(i)


# In[21]:


## """k. Correlation"""

sns.set(font_scale=0.8)
corr=emp.corr()
sns.heatmap(corr,annot=True,fmt='.2f')


# In[ ]:




