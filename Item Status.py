#!/usr/bin/env python
# coding: utf-8

# In[80]:


import pandas as pd
import numpy as np
import os


# In[81]:


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


# In[82]:


# monthresult = ['total sale of Goods', 'Status']
monthresult = ['total sale of Goods']
productDetail = ['Sku', 'UPC', 'Catalogue N', 'Title', 'Label' ,'Arq COST', 'Cost Price' ,'V.S.P.', 'Latest SOH']
header = productDetail.copy()


# In[83]:


def findID(sku, Data):
    numb = 0
    for SKUref in Data['Sku']: 
        
        if str(sku) == str(SKUref): 
            return numb
        numb += 1
    return "This good with Sku of " + str(sku) + " is not in data." 


# In[84]:


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


# In[85]:


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


# In[86]:


# 'Existence on Shop'
def existence(sku, files):
    numExistence = 0
    for file in files:
        Data = pd.read_csv(file)
        try:
            ide = findID(sku, Data)
#             print(Data.loc[ide, 'Latest SOH'])
            if Data.loc[ide, 'Latest SOH'] > 0:
                numExistence +=1
            else:
                numExistence = 0
        except:
            numExistence = 0

    if numExistence > 3:
        numExistence = 3
    return numExistence


# In[87]:


monthRawData = pd.DataFrame(columns = list(header))


# In[88]:


for file in filesNoAdd:
    file = str(file).replace('.csv','')
    monthRawData[file + ' ' + monthresult[0]] = np.zeros(len(listOfGoods(files)))
monthRawData['Sku'] = listOfGoods(files)
#     print(monthresult)
#     for head in monthresult:
        

monthRawData['Latest SOH'] = np.zeros(len(monthRawData['Sku']))


# In[89]:


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


# In[90]:


average = []
for sku in monthRawData['Sku']:
    ide = findID(sku, monthRawData)
    average.append(np.round(np.sum(monthRawData.values[ide,-4:-1])/3,decimals=2))
#     if average[-1] == 0 and monthRawData.loc[ide, 'Latest SOH'] == 0:
#         average[-1] = 'No stock'
average1 = average.copy() 
monthRawData['3 months avrage sale'] = average1        
     


# In[93]:



delList =[]
for i in range(len(monthRawData['Sku'])):
  if monthRawData.loc[i, 'Latest SOH'] == 0:
      delList.append(i)
delList = delList[::-1]


# In[94]:


# average[13]


# In[95]:



for i in delList:
    del average[i]


# In[96]:


frame = pd.DataFrame(average)
x, y, z = frame[0].quantile([0.25, 0.5, 0.75])
# print(x,y,z)
# print(delList,average)


# In[97]:


Status = strs = ["" for x in range(len(monthRawData['Sku']))]


for i in range(len(monthRawData['Sku'])):
    
    if i in delList :
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

        
monthRawData['Stock Status'] = Status


# In[98]:


profit = []
for i in range(len(monthRawData['Sku'])):
    profit.append(average1[i]*(monthRawData.loc[i,'Cost Price'] - monthRawData.loc[i, 'Arq COST']))
profit1 = profit.copy()
monthRawData['profit'] = profit1


# In[99]:


# print(len(profit))


# In[100]:



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


# In[101]:


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


# In[102]:


finalStatus = []
for i in range(len(monthRawData['Sku'])):
    finalStatus.append(str(Status[i]) + ' - ' + str(profitStatus[i]))
monthRawData['Final Status'] = finalStatus


# In[103]:


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


# In[104]:


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


# In[105]:


monthRawData.to_csv('allMonthes.csv',index=False)


# In[24]:


#     df = pd.read_csv('allMonthes.csv')
#     newdf = df[df['Stock Status'] == 'Fast moving']
#     newdf = newdf.loc[:,['Sku', 'UPC', 'Catalogue N', 'Title', 'Label', 'Arq COST', "Cost Price", 'V.S.P.']].reindex()
#     newdf.to_html('fast moving.html')
#     .to_html('fast moing.html')
#     ['Sku', 'UPC', 'Catalogue N', 'Title', 'Label', 'Arq COST', "Cost Price", 'V.S.P.']


# In[ ]:


# date_index = pd.date_range('1/1/2010', periods=6, freq='D')
# df2 = pd.DataFrame({"prices": [100, 101, np.nan, 100, 89, 88]},
#                     index=date_index)

