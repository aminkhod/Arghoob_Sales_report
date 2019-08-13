#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import os
# import subprocess
# subprocess.check_call(['pip', 'install', 'numpy']) # install pkg
# subprocess.check_call(['pip', 'install',"--upgrade", 'numpy']) # upgrade pkg


# In[3]:


path = 'Weaks of Month/'

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


# In[4]:


numListOfBranch = ['401 Co','402 Co','404 Co','405 Co','412 Co','416 Co',
                   '417 Co','423 Co', '424 Co','425 Co','426 Co','429 Co','444 Co','490 Co']
listOfBranch = ['401 Co', '401.Arq COST', '401.Cost Price', '401.V.S.P.', '401.AVG. WEEK',
                '402 Co', '402.Arq COST', '402.Cost Price', '402.V.S.P.', '402.AVG. WEEK',
                '404 Co', '404.Arq COST', '404.Cost Price', '404.V.S.P.', '404.AVG. WEEK',
                '405 Co', '405.Arq COST', '405.Cost Price', '405.V.S.P.', '405.AVG. WEEK',
                '412 Co', '412.Arq COST', '412.Cost Price', '412.V.S.P.', '412.AVG. WEEK',
                '416 Co', '416.Arq COST', '416.Cost Price', '416.V.S.P.', '416.AVG. WEEK',
                '417 Co', '417.Arq COST', '417.Cost Price', '417.V.S.P.', '417.AVG. WEEK',
                '423 Co', '423.Arq COST', '423.Cost Price', '423.V.S.P.', '423.AVG. WEEK',
                '424 Co', '424.Arq COST', '424.Cost Price', '424.V.S.P.', '424.AVG. WEEK',
                '425 Co', '425.Arq COST', '425.Cost Price', '425.V.S.P.', '425.AVG. WEEK',
                '426 Co', '426.Arq COST', '426.Cost Price', '426.V.S.P.', '426.AVG. WEEK',
                '429 Co', '429.Arq COST', '429.Cost Price', '429.V.S.P.', '429.AVG. WEEK',
                '444 Co', '444.Arq COST', '444.Cost Price', '444.V.S.P.', '444.AVG. WEEK',
                '490 Co', '490.Arq COST', '490.Cost Price', '490.V.S.P.', '490.AVG. WEEK', 'Latest SOH']

productDetail = ['Sku', 'UPC', 'Catalogue N', 'Title', 'Label' ,'Arq COST', 'Cost Price' ,'V.S.P.']
header = productDetail.copy()
header.extend(listOfBranch.copy())


# In[5]:


def findID(sku, Data):
    numb = 0
    for SKUref in Data['Sku']:
        
        if str(sku) == str(SKUref):
            return numb
        numb += 1
    return "This good with Sku of " + sku + " is not in data." 


# In[6]:


def buildList(num, ide, productDetail, listOfBranch, rawData, final):
    producList = []
    qSum = 0
    for det in productDetail:
        producList.append(rawData[det][ide])
    for branch in listOfBranch:
        branch = branch.replace(' Co','')
        qbranch = str(branch + '.Quantit')
        head = str(branch + '.Sales Quantity')
        if head in rawData.head(0):
            try:
                producList.append(float(rawData[head][ide]))
                producList.append(float(rawData[head][ide]) * float(rawData['Arq COST'][ide]))
                producList.append(float(rawData[head][ide]) * float(rawData['Cost Price'][ide]))
                producList.append(float(rawData[head][ide]) * float(rawData['V.S.P.'][ide]))
                producList.append(float(rawData[head][ide]) / float(num))
            except:
                print("A number in raw data is string" , head, ide)
        if qbranch in rawData.head(0) and str(branch)!='444'and str(branch)!='490'and final==True:
            try:
                qSum = qSum + rawData[qbranch][ide]
            except:
                print("A number in raw data is string", qbranch, ide)
    producList.append(qSum)

                
    return producList


# In[7]:


def listAddition(Dataide, ide, num, productDetail, listOfBranch, rawData, monthRawData, final):
    colid = 8
    qSum = 0
    buf = 0
    for branch in listOfBranch:        
        branch = branch.replace(' Co','')
        qbranch = str(branch + '.Quantit')        
        head = str(branch + '.Sales Quantity')
        if head in rawData.head(0):
            buf = colid + 5
#             print(colid)
            monthRawData.iloc[Dataide, colid] = monthRawData.iloc[Dataide, colid] + rawData[head][ide]
            monthRawData.iloc[Dataide, colid+1] = monthRawData.iloc[Dataide, colid] * float(rawData['Arq COST'][ide])
            monthRawData.iloc[Dataide, colid+2] = monthRawData.iloc[Dataide, colid] * float(rawData['Cost Price'][ide])
            monthRawData.iloc[Dataide, colid+3] = monthRawData.iloc[Dataide, colid] * float(rawData['V.S.P.'][ide])
            monthRawData.iloc[Dataide, colid+4]= monthRawData.iloc[Dataide, colid] / float(num)
#         print(monthRawData)
        colid += 1
        if qbranch in rawData.head(0) and str(branch)!='444'and str(branch)!='490'and final==True:
            try:
                qSum = qSum + rawData[qbranch][ide]
            except:
                print("A number in raw data is string", qbranch, ide)

    if final:
#         print(qSum)
        
        monthRawData.iloc[Dataide,buf] = qSum
        
    return monthRawData


# In[8]:


def noStock(sku,rawData):
    sku = str(sku)
    try:
        i = findID(sku, rawData)
        i = int(i)
    except:
        return True
    for branch in numListOfBranch:        
        branch = branch.replace(' Co','')
        qbranch = str(branch + '.Quantit')
        if rawData.loc[i,qbranch] > 0 and str(branch)!='444'and str(branch)!='490':
            return False
    return True


# In[20]:


ArghoobCost = pd.read_excel('ARQOOB Cost.xlsx')
for f in files:
    rawData = pd.read_csv(f , encoding='latin1')
    i = 0
    for sku in rawData['Sku']:
        j = findID(sku, ArghoobCost)
        rawData.loc[i,'Arq COST'] = ArghoobCost.loc[j, 'Arq COST']
        i += 1
    rawData.to_csv(f, index=False)
# ArghoobCost


# In[186]:


# a = np.zeros(shape=(1,len(header)))
monthRawData = pd.DataFrame(columns = list(header))

fcount = len(files)
b = []
finalFile =False
for f in files:
#     f1 = (path + f)
    f1 = (f)
    rawData = pd.read_csv(f1 , encoding='latin1')

    if f == files[-1]:
        finalFile = True
    sid =0
    b = 0
    
    for sku in rawData['Sku']:
        if sku not in list(monthRawData['Sku']):
            df = pd.DataFrame([list(buildList(fcount, sid, productDetail,
                            listOfBranch, rawData, finalFile))], columns= list(header))
            monthRawData = monthRawData.append(df)
            
        else:
#             print(f,sid)
            Dataide = findID(sku, monthRawData)
            b = listAddition(Dataide, sid, fcount, productDetail, listOfBranch, rawData,
                             monthRawData, finalFile)
        sid +=1


# In[187]:


totalGoodSale = []
count = 0
for sku in monthRawData['Sku']:
    saleOfGood = []
    for numB in numListOfBranch:
        saleOfGood.append(monthRawData.iloc[count][numB])
    totalGoodSale.append(np.sum(saleOfGood))
    count += 1
monthRawData["total sale of Goods"] = totalGoodSale
status = []
for tot in totalGoodSale:
#     if tot == 0:
    if tot <= 0:
        status.append('Non moving')
    if (tot > 0) and (tot <=2):
        status.append('Slow moving')
    if tot > 2:
        status.append('Fast moving')
#

rawData = pd.read_csv(files[-1])

for i in range(len(status)):
#         print(i)
    try:
        if noStock(monthRawData.iloc[i]['Sku'],rawData) and status[i]=='Non moving':
            status[i] = 'Run out of stock'
    except:
        continue
#
monthRawData["Status"] = status


# In[188]:


monthRawData.to_csv("toalOfMonth.csv", index=False)


# In[ ]:




