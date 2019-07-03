#!/usr/bin/env python
# coding: utf-8

# In[70]:


import pandas as pd
import numpy as np
import os


# In[244]:


path = 'Monthes/'

files = []
filesNoAdd = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.csv' in file:
            files.append(os.path.join(r, file))
            filesNoAdd.append(file)

for f in filesNoAdd:
    print(f)


# In[245]:


# monthresult = ['total sale of Goods', 'Status']
monthresult = ['total sale of Goods']
productDetail = ['Sku', 'UPC', 'Catalogue N', 'Title', 'Label' ,'Arq COST', 'Cost Price' ,'V.S.P.', 'Latest SOH']
header = productDetail.copy()


# In[246]:


def findID(sku, Data):
    numb = 0
    for SKUref in Data['Sku']: 
        
        if str(sku) == str(SKUref): 
            return numb
        numb += 1
    return "This good with Sku of " + str(sku) + " is not in data." 


# In[247]:


def listOfGoods(files):
    listOfSku = []
    for file in files:
        rawData = pd.read_csv(file, encoding='latin1')
        for i in range(len(rawData['Sku'])):
                if rawData.loc[ i , 'Sku'] in listOfSku:
                       continue
                else:
                       listOfSku.append(rawData.loc[i,'Sku' ])
                       
    return listOfSku


# In[248]:


def buildList(file, ide, productDetail, monthresult, rawData, sku,monthRawData, finalFile):

    for det in productDetail:
        if det =='Sku':
            continue
        monthRawData.loc[findID(sku, monthRawData),det] = rawData[det][ide]
    file = str(file).replace('.csv','')
    file = file.replace('Monthes/','')
    for head in monthresult:
        monthRawData.loc[findID(sku, monthRawData), file + ' ' + head] = rawData[head][ide]
    if finalFile:
        monthRawData.loc[findID(sku, monthRawData), 'Latest SOH'] = rawData['Latest SOH'][ide]
    return monthRawData


# In[249]:


# 'Existence on Shop'
def existence(sku, files):
    numExistence = 0
    for file in files:
        Data = pd.read_csv(file)
        try:
            ide = findID(sku, Data)
            if Data.loc[ide, 'Latest SOH'] > 0:
                numExistence +=1
            else:
                numExistence = 0
        except:
            numExistence = 0

    if numExistence > 3:
        numExistence = 3
    return numExistence


# In[250]:


monthRawData = pd.DataFrame(columns = list(header))


# In[251]:


for file in filesNoAdd:
    monthRawData['Sku'] = listOfGoods(files)
    for head in monthresult:
        
        file = str(file).replace('.csv','')
        monthRawData[file + ' ' + head] = np.zeros(len(listOfGoods(files)))
monthRawData['Latest SOH'] = np.zeros(len(monthRawData['Sku']))


# In[252]:


# a = np.zeros(shape=(1,len(header)))
# monthRawData = pd.DataFrame(columns = list(header))
fcount = len(files)
b = []
finalFile =False
for file in files:
    rawData = pd.read_csv(file , encoding='latin1')
    sid =0
    if file ==files[-1]:
        finalFile = True
    Existence = []
#     b = 0
    for sku in rawData['Sku']:
        monthRawData = buildList(file, sid, productDetail, monthresult,
                                 rawData,sku,monthRawData, finalFile)
        if finalFile:
            e = existence(sku, files)
            if e == 3:
                Existence.append('Min ' + str(e) + ' months')
            elif e <= 1:
                Existence.append(str(e) + ' month')
            else:
                Existence.append(str(e) + ' months')
#             try:
#                 ide = findID(sku, monthRawData)
#                 average.append((np.sum(monthRawData.values[ide,-1:-3]))/3)
#             except:
#                 average.append(0)
        sid +=1
monthRawData['Existence on Shop'] =Existence


# In[253]:


average = []
for sku in monthRawData['Sku']:
    ide = findID(sku, monthRawData)
    average.append(np.round(np.sum(monthRawData.values[ide,-4:-1])/3,decimals=2))
#     if average[-1] == 0 and monthRawData.loc[ide, 'Latest SOH'] == 0:
#         average[-1] = 'No stock'
average1 = average.copy() 
monthRawData['3 months avrage sale'] = average1        
     


# In[254]:



delList =[]
for i in range(len(monthRawData['Sku'])):
  if average[i] == 0 and monthRawData.loc[i, 'Latest SOH'] == 0:
      delList.append(i)
delList = delList[::-1]


# In[255]:



for i in delList:
    del average[i]


# In[256]:


frame = pd.DataFrame(average)
x, y, z = frame[0].quantile([0.25, 0.5, 0.75])
# print(x,y,z)
# print(delList,average)


# In[257]:


Status = strs = ["" for x in range(len(monthRawData['Sku']))]


for i in range(len(monthRawData['Sku'])):
    if i in delList:
        Status[i] = 'Run out of stock'
    elif average[0] >= z:
        Status[i] = 'Fast moving'
        del average[0]
    elif average[0] <= x:
        Status[i] = 'Non moving'
        del average[0]
    elif average[0] < z and average[0] > x:
        Status[i] = 'Slow moving'
        del average[0]
    
monthRawData['Status'] = Status


# In[258]:


profit = []
for i in range(len(monthRawData['Sku'])):
    profit.append(average1[i]*(monthRawData.loc[i,'Cost Price'] - monthRawData.loc[i, 'Arq COST']))
profit1 = profit.copy()
monthRawData['profit'] = profit1


# In[259]:


# print(len(profit))


# In[260]:



delList =[]
for i in range(len(monthRawData['Sku'])):
    if profit[i] == 0:
        delList.append(i)
delList = delList[::-1]

for i in delList:
    del profit[i]
frame = pd.DataFrame(profit)
x, y, z = frame[0].quantile([0.25, 0.5, 0.75])
print(x,y,z)
# print(delList,profit)


# In[261]:


profitStatus = strs = ["" for x in range(len(monthRawData['Sku']))]


for i in range(len(monthRawData['Sku'])):
    if i in delList:
        profitStatus[i] = 'Run out of stock'
    elif profit[0] >= z:
        profitStatus[i] = 'Most profitable'
        del profit[0]
    elif profit[0] <= x:
        profitStatus[i] = 'Less profitable'
        del profit[0]
    else:
        profitStatus[i] = 'Profitable'
        del profit[0]
    
monthRawData['Profit status'] = profitStatus


# In[262]:


finalStatus = []
for i in range(len(monthRawData['Sku'])):
    finalStatus.append(str(Status[i]) + ' - ' + str(profitStatus[i]))
monthRawData['Final Status'] = finalStatus


# In[263]:


nonMovingAction = []
for i in range(len(monthRawData['Sku'])):
    if Existence[i] == 'Min 3 months' and Status[i] == 'Non moving':
        nonMovingAction.append('Buying Price')
    elif Existence[i] == '2 months' and Status[i] == 'Non moving':
        nonMovingAction.append('Discount')
    elif Existence[i] == '1 month' and Status[i] == 'Non moving':
        nonMovingAction.append('Transfer')
    else:
        nonMovingAction.append('-')
monthRawData['Non Moving Action'] = nonMovingAction


# In[268]:


#=IF(O5="Run out of stock - Most Profitable","No Stock - Reorder",
# IF(O5="Fast Moving - Most Profitable","Profitable - Reorder",
# IF(O5="Run out of stock - Less Profitable","Stop Ordering", " - ")))
Reordering = []
for i in range(len(monthRawData['Sku'])):
    if finalStatus[i] == 'Run out of stock - Most profitable':
        Reordering.append('Non Stock - Reorder')
    elif finalStatus[i] == 'Fast moving - Most profitable':
        Reordering.append('Profitable - Reorder')
    elif finalStatus[i] == 'Run out of stock - Less profitable':
        Reordering.append('Stop Ordering')
    else:
        Reordering.append('-')
monthRawData['Reordering'] = Reordering


# In[269]:


monthRawData.to_csv('allMonthes.csv',index=False)


# In[ ]:



