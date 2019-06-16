#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os
import plotly.graph_objs as go
import plotly.io as pio
import plotly.plotly as py
import plotly.figure_factory as ff
import dash
import dash_core_components as dcc
import dash_html_components as html
from  plotly.offline import plot
import plotly
from IPython.display import SVG, display
from IPython.display import Image
from IPython.display import display, Math, Latex
import colorlover as cl
from IPython.display import HTML
from IPython.display import IFrame
from plotly.offline import iplot, init_notebook_mode
from IPython.display import YouTubeVideo
init_notebook_mode(connected=True)

# import subprocess
# subprocess.check_call(['pip', 'install', 'numpy']) # install pkg
# subprocess.check_call(['pip', 'install',"--upgrade", 'numpy']) # upgrade pkg


# In[2]:


path = '4Th Month/'

files = []
filesNoAdd = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.CSV' in file:
            files.append(os.path.join(r, file))
            filesNoAdd.append(file)

for f in filesNoAdd:
    print(f)


# In[3]:


# f1 = '04-05-2019'
for ff in filesNoAdd:
    f1 = (path+ ff)
    rawData = pd.read_csv(f1 , encoding='latin1')
    # rawData
    sku = rawData.values[:189,0]
    upc = rawData.values[:189,1]
    Catalogue = rawData.values[:189,2]
    title = rawData.values[:189,3]
    label = rawData.values[:189,4]
    Cost_Price = rawData.values[:189,5]
    VSP = rawData.values[:189,6]
    rawDatVal = []
    rawDatVal = rawData.values[:189,7:149]
    eachRaw = []
    allRawvalue = []
    BranchTotal = rawDatVal.sum(axis=0)

    for i in range(len(rawDatVal[:,0])):
        for j in range(int((len(rawDatVal[0,:]))/3)):

            k=3 * j 

            eachRaw.append(rawDatVal[i,k])
        eachRaw = np.array(eachRaw)
        allRawvalue.append(eachRaw.sum())
        eachRaw = []

    # rawData['Sum of sale for each goods'] = allRawvalue

    eachRaw = []

    BranchTotal = rawDatVal.sum(axis=0)
    for j in range(int(len(rawDatVal[0,:])/3)):
        k=3 * j 
        sum = 0
        for i in range(len(rawDatVal[:,0])):
            sum += rawDatVal[i,k]
        rawData.iloc[i+1,k] = sum


        eachRaw = []
    # allRawvalue.append(np.array(allRawvalue).sum())
    # allRawvalue.append(np.array(allRawvalue).sum())

    Virgin_Stock = []
    Virgin_Stock = pd.DataFrame(Virgin_Stock)
    Virgin_Stock['sku'] = sku
    Virgin_Stock['upc'] = upc
    Virgin_Stock['Catalogue'] = Catalogue
    Virgin_Stock['title'] = title
    Virgin_Stock['label'] = label
    Virgin_Stock['VMS Cost'] = Cost_Price
    Virgin_Stock['VSP'] = VSP


    Virgin_Stock[f1] = list(allRawvalue)

    i = 1
    buf = np.zeros([len(Virgin_Stock.values[:,1]),1], dtype=int)
    ## i
    for j in range(i):
        buf += np.reshape(np.array(Virgin_Stock.values[:,7+j], dtype = int),[189,1])

    Virgin_Stock["TOTAL"] = buf
    ii = np.full(len(Virgin_Stock.values[:,1]) ,i )

    Virgin_Stock["AVG. WEEK"] = np.divide(Virgin_Stock["TOTAL"] , ii)
    Virgin_Stock['total VMS Cost'] = Virgin_Stock["TOTAL"] * Virgin_Stock['VMS Cost']
    Virgin_Stock['total V.S.P.'] = Virgin_Stock["TOTAL"] * Virgin_Stock['VSP']
    count = 0
    for head in list(rawData.head(0)):
        if ".Sales Quantity" in head:
            Virgin_Stock[head] = rawData[head]
            try:
                headNum = int(head.replace(".Sales Quantity",''))
            except:
                print(int(headNum)," can't be cast to int")
            headNum = str(headNum)
            Virgin_Stock['TOTAL' + headNum] = rawData.values[:189, count]
            Virgin_Stock['VMS Cost' + headNum] = Virgin_Stock['VMS Cost'] * Virgin_Stock['TOTAL' + headNum]
            Virgin_Stock['V.S.P.' + headNum] = Virgin_Stock['VSP'] * Virgin_Stock['TOTAL' + headNum]
            Virgin_Stock['AVG. WEEK' + headNum] = np.divide(Virgin_Stock['TOTAL' + headNum] , ii)
        count +=1


# In[4]:


Virgin_Stock.to_csv('Virgin_Stock.csv', index =False)


# In[5]:


path = '4Th Month/'

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


# In[6]:


numListOfBranch = ['401 Co','402 Co','404 Co','405 Co','412 Co','416 Co',
                   '417 Co','423 Co', '424 Co','425 Co','426 Co','429 Co','444 Co','490 Co']
listOfBranch = ['401 Co', '401.VMS cost', '401.V.S.P.', '401.AVG. WEEK',
                '402 Co', '402.VMS cost', '402.V.S.P.', '402.AVG. WEEK',
                '404 Co', '404.VMS cost', '404.V.S.P.', '404.AVG. WEEK',
                '405 Co', '405.VMS cost', '405.V.S.P.', '405.AVG. WEEK',
                '412 Co', '412.VMS cost', '412.V.S.P.', '412.AVG. WEEK',
                '416 Co', '416.VMS cost', '416.V.S.P.', '416.AVG. WEEK',
                '417 Co', '417.VMS cost', '417.V.S.P.', '417.AVG. WEEK',
                '423 Co', '423.VMS cost', '423.V.S.P.', '423.AVG. WEEK',
                '424 Co', '424.VMS cost', '424.V.S.P.', '424.AVG. WEEK',
                '425 Co', '425.VMS cost', '425.V.S.P.', '425.AVG. WEEK',
                '426 Co', '426.VMS cost', '426.V.S.P.', '426.AVG. WEEK',
                '429 Co', '429.VMS cost', '429.V.S.P.', '429.AVG. WEEK',
                '444 Co', '444.VMS cost', '444.V.S.P.', '444.AVG. WEEK',
                '490 Co', '490.VMS cost', '490.V.S.P.', '490.AVG. WEEK']

productDetail = ['Sku', 'UPC', 'Catalogue N', 'Title', 'Label' ,'Cost Price' ,'V.S.P.']
header = productDetail.copy()
header.extend(listOfBranch.copy())


# In[7]:


def findID(sku, Data):
    numb = 0
    for SKUref in Data['Sku']:
        
        if str(sku) == str(SKUref):
            return numb
        numb += 1
    return "This good with Sku of " + sku + " is not in data." 


# In[18]:


def buildList(num, ide, productDetail, listOfBranch, rawData):
    
    producList = []
    for det in productDetail:
        producList.append(rawData[det][ide])
    for branch in listOfBranch:
        branch = branch.replace(' Co','')
        head = str(branch + '.Sales Quantity')
        if head in rawData.head(0):
            try:
                producList.append(float(rawData[head][ide]))
                producList.append(float(rawData[head][ide]) * float(rawData['V.S.P.'][ide]))
                producList.append(float(rawData[head][ide]) * float(rawData['Cost Price'][ide]))
                producList.append(float(rawData[head][ide]) / float(num))
                
            except:
                print("A number in raw data is string")
                
    return producList


# In[25]:


def listAddition(Dataide, ide, num, productDetail, listOfBranch, rawData, monthRawData):
    colid = 0
    for branch in listOfBranch:
        branch = branch.replace(' Co','')
        head = str(branch + '.Sales Quantity')
        if head in rawData.head(0):
            monthRawData.iloc[Dataide, colid+7] = monthRawData.iloc[Dataide, colid+7] + rawData[head][ide]
            monthRawData.iloc[Dataide, colid+8] = monthRawData.iloc[Dataide, colid+7] * float(rawData['V.S.P.'][ide])
            monthRawData.iloc[Dataide, colid+9] = monthRawData.iloc[Dataide, colid+7] * float(rawData['Cost Price'][ide])
            monthRawData.iloc[Dataide, colid+10]= monthRawData.iloc[Dataide, colid+7] / float(num)
        colid += 1
    return monthRawData


# In[26]:


def noStock(sku,rawData):
    sku = str(sku)
    i = findID(sku, rawData)
    if np.sum(rawData.values[i,7:45]) > 0:
        return False
    else:
        return True


# In[27]:


# a = np.zeros(shape=(1,len(header)))
monthRawData = pd.DataFrame(columns = list(header))

fcount = len(files)
b = []
for f in files:
#     f1 = (path + f)
    f1 = (f)
    rawData = pd.read_csv(f1 , encoding='latin1')

    
    sid =0
    b = 0
    for sku in rawData['Sku']:
        if sku not in list(monthRawData['Sku']):
            df = pd.DataFrame([list(buildList(fcount, sid, productDetail,
                                              listOfBranch, rawData))], columns= list(header))
            monthRawData = monthRawData.append(df)
            
        else:
            Dataide = findID(sku, monthRawData)
            b = listAddition(Dataide, sid, fcount, productDetail, listOfBranch, rawData, monthRawData)
        sid +=1


# In[28]:


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
        status.append('Not moving')
    if (tot > 0) and (tot <=2):
        status.append('Slow moving')
    if tot > 2:
        status.append('Fast moving')
#
for j in range(len(filesNoAdd)):
    rawData = pd.read_csv(files[j])

    for i in range(len(status)):
#         print(i)
        try:
            if noStock(monthRawData.iloc[i]['Sku'],rawData):
                status[i] = 'Run out of stock'
        except:
            continue
#
monthRawData["Status"] = status


# In[30]:


monthRawData.to_csv("toalOfMonth.csv", index=False)


# In[ ]:




