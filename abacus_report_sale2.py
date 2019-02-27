#!/usr/bin/env python
# coding: utf-8

# In[68]:


import datetime
import csv

# weekNumber = timedelta.
# print('Week number:', weekNumber)
with open('RawData.csv', newline='') as f:
  reader = csv.reader(f)
  for row in reader:
    # do something here with `row`
    break
print(row[0])


# In[69]:


datetime.date(int(row[0][7:]),int(row[0][3:5]),int(row[0][0:2])).isocalendar()[1]


# In[70]:


timedelta


# In[71]:


import pandas as pd
import numpy as np


# In[72]:


rawData = pd.read_csv('RawData.csv', skiprows =1)


# In[73]:


rawData


# In[76]:


myframe = []
myframe = pd.DataFrame(myframe)


# In[ ]:




