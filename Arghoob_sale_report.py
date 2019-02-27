#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[5]:


rawData = pd.read_csv('RawData.csv')


# In[6]:


rawData


# In[48]:


rawDatVal = rawData.values[:116,3:45]


# In[49]:


rawDatVal = np.array(rawDatVal)
rawDatVal


# In[50]:


BranchTotal = rawDatVal.sum(axis=0)


# In[51]:


len(BranchTotal)


# In[87]:


BranchTotal


# In[88]:


eachRaw = []
allRawvalue = []
for i in range(len(rawDatVal[:,0])):
    for j in range(int((len(rawDatVal[1,:])-2)/3)):
        j=3*j + 2
        eachRaw.append(rawDatVal[i,j])
    eachRaw = np.array(eachRaw)
    allRawvalue.append(eachRaw.sum())
    eachRaw = []
    


# In[89]:


eachRaw


# In[90]:


allRawvalue


# In[91]:


eachRaw = []
SOH = []
for i in range(len(rawDatVal[:,0])):
    for j in range(int((len(rawDatVal[1,:]))/3)):
        j=3*j 
        eachRaw.append(rawDatVal[i,j])
    eachRaw = np.array(eachRaw)
    SOH.append(eachRaw.sum())
    eachRaw = []


# In[92]:


eachRaw


# In[93]:


SOH


# In[ ]:




