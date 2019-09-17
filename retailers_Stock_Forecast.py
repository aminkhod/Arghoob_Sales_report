#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd
import numpy as np
from datetime import datetime, timedelta


# In[43]:


consolidateSalesReports = pd.read_csv('Consolidate Sales Reports.csv', encoding='latin1')


# In[44]:


# numListOfBranch = ['401 Co','402 Co','404 Co','405 Co','412 Co','416 Co',
#                    '417 Co','423 Co', '424 Co','425 Co','426 Co','429 Co','444 Co','490 Co']

monthesList = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
               'August', 'September', 'October', 'November', 'December']
listOfBranch = ['ARQOOB SOH','Retailer SOH', 'Final_Cost', 'Month', 'Weeks',
                'Product Lead Time (Days)', 'Last Update']

productDetail = ['Part No', "Description", 'UPC']
header = productDetail.copy()
header.extend(listOfBranch.copy())


# In[45]:


supplierForecast = pd.DataFrame(columns = list(header))
for col in supplierForecast.columns:
    supplierForecast[col] = consolidateSalesReports[col]


# In[46]:


realMonthes = []
lastMonth = ''
for month in monthesList:
    try:
        supplierForecast[month + '_QTY'] = consolidateSalesReports[month[:3] + '_Total']
        realMonthes.append(month + '_QTY')
        lastMonth = month + '_QTY'
    except:
        continue


# In[110]:


QTY_Sold =0
for rm in realMonthes:
    QTY_Sold = QTY_Sold + supplierForecast[rm]
supplierForecast['QTY Sold'] = QTY_Sold

avgPerDay = []
avgPerMonth = []
i = 0
for m in supplierForecast['Month']:
    if supplierForecast.loc[i,lastMonth] == 0:
        if m == 0:
            avgPerDay.append(0)
            avgPerMonth.append(0)
        else:
            avgPerDay.append(np.around(QTY_Sold[i] / (m * 30), 2))
            avgPerMonth.append(np.around(QTY_Sold[i] / m,2))
    else:
        avgPerDay.append(np.around(QTY_Sold[i]/((m*30)+(supplierForecast.loc[i,'Weeks']*7)),2))
        avgPerMonth.append(np.around(QTY_Sold[i] / m,2))
    i += 1
supplierForecast['Avh per Day'],supplierForecast['Avg per Month'] = avgPerDay, avgPerMonth
i = 0
closingStock = []
for soh in supplierForecast['ARQOOB SOH']:
    try:
        int(supplierForecast.loc[i,'ARQOOB SOH'])
    except:
        supplierForecast.loc[i,'ARQOOB SOH'] = 0
    try:
        int(supplierForecast.loc[i,'Retailer SOH'])
    except:
        supplierForecast.loc[i,'Retailer SOH'] = 0
    closingStock.append(supplierForecast.loc[i,'Retailer SOH'] + supplierForecast.loc[i,'ARQOOB SOH'])
    i += 1

supplierForecast['Closing Stock'] = closingStock
i = 0
stockInHand = []
for cl in supplierForecast['Closing Stock']:
    if supplierForecast.loc[i,'Avh per Day'] !=0:
        stockInHand.append(cl/supplierForecast.loc[i,'Avh per Day'])
    else:
        stockInHand.append("Not Sold")
    i += 1
supplierForecast['Days Stock in Hand'] = stockInHand

i = 0
minStock = []
for day in supplierForecast['Days Stock in Hand']:
    try:
        minStock.append(int(supplierForecast.loc[i,'Days Stock in Hand']))
    except:
        minStock.append('-')
    
supplierForecast['Deviation from Minimum Stock Level'] = minStock


supplierForecast['MSL (2 Mont Covering)'] = supplierForecast['Avg per Month'] * 2

stockCover = []
i = 0 
for day in supplierForecast['Days Stock in Hand']:
    try:
        date_1 = supplierForecast.loc[i,'Last Update']

        stockCover.append(str(pd.to_datetime(date_1) + pd.DateOffset(days=int(day)))[:int(10)])
    except:    
        stockCover.append('Not Sold')
    i += 1
supplierForecast['Current Stock Cover upto (Date)'] = stockCover

ArrivalDate = []
i = 0 
for day in supplierForecast['Product Lead Time (Days)']:
    try:
        date_1 = supplierForecast.loc[i,'Last Update']
        newDate = str(pd.to_datetime(date_1) + pd.DateOffset(days=int(day)))[:int(10)]
        ArrivalDate.append(newDate)
    except:    
        ArrivalDate.append('Not Sold')
    i += 1
supplierForecast['Arrival Date'] = ArrivalDate


ArrivalDateETA = []
i = 0 
for day in supplierForecast['Arrival Date']:
    try:
        int(day[0])
        
        month= day[5:7]
        day = day.replace(month + '-',"")
        day = day + '-' + month
        
        coverDay = supplierForecast.loc[i,'Current Stock Cover upto (Date)']
        int(coverDay[0])
        month = coverDay[5:7]
        coverDay = coverDay.replace(month + '-', '')
        coverDay = coverDay + '-' + month
        dateList = [day, coverDay]
        maxList = max(dateList)
        
        month = maxList[5:7]
        maxList = maxList.replace(month + '-', '')
        maxList = maxList + '-' + month
        
        ArrivalDateETA.append(maxList)
    except:    
        ArrivalDateETA.append('Not Sold')
    i += 1
supplierForecast['Arrival Date (ETA)'] = ArrivalDateETA


requiredQTY = []
i = 0 
for day in supplierForecast['Product Lead Time (Days)']:
    try:
        avgPerDay = supplierForecast.loc[i,'Avh per Day']
        int(avgPerDay)      
        requiredQTY.append(str(np.round(day * avgPerDay,2)))
    except:    
        requiredQTY.append('Not Sold')
    i += 1
supplierForecast['required(Qty)'] = requiredQTY


balanceStock = []
i = 0 
for Qty in supplierForecast['required(Qty)']:
    try:
        closingStock = supplierForecast.loc[i,'Closing Stock']
        balanceStock.append(str(np.round(float(Qty) * float(closingStock),2)))
    except:    
        balanceStock.append('Not Sold')
    i += 1
supplierForecast['Balance Stock'] = balanceStock


minOrder = []
# i = 0 
# for Qty in supplierForecast['required(Qty)']:
#     try:
#         closingStock = supplierForecast.loc[i,'Closing Stock']
#         minOrder.append(str(np.round(float(Qty) * float(closingStock),2)))
#     except:    
#         minOrder.append('Not Sold')
#     i += 1
# supplierForecast['Minimum order QTY'] = minOrder
supplierForecast['Minimum order QTY'] = np.ones(len(supplierForecast['Balance Stock'] ))



POQTY = []
i = 0 
for Qty in supplierForecast['MSL (2 Mont Covering)']:
    try:

        BStock = supplierForecast.loc[i,'Balance Stock']        
        if float(Qty) - float(BStock) > 1 :
            POQTY.append(float(Qty) - float(BStock))
        else:
            POQTY.append(0)
    except:    
        POQTY.append('Not Sold')
    i += 1
supplierForecast['PO QTY'] = POQTY


POQTY = []
i = 0 
for Qty in supplierForecast['PO QTY']:
    try:

        aCost = supplierForecast.loc[i,'Final_Cost']        
        POQTY.append(float(Qty) * float(aCost))
    except:    
        POQTY.append('Not Sold')
    i += 1
supplierForecast['New PO Value'] = POQTY


POQTY = []
i = 0 
for Qty in supplierForecast['PO QTY']:
    try:

        aCost = supplierForecast.loc[i,'Avh per Day']        
        POQTY.append(float(Qty) / float(aCost))
    except:    
        POQTY.append('-')
    i += 1
supplierForecast['Stock Days inc On Order'] = POQTY


POQTY = []
i = 0 
for stockDays in supplierForecast['Stock Days inc On Order']:
    try:

        date = supplierForecast.loc[i,'Arrival Date (ETA)']
        newDate = str(pd.to_datetime(date) + pd.DateOffset(days=int(stockDays)))[:int(10)]
        POQTY.append(newDate)
    except:    
        POQTY.append('-')
    i += 1
supplierForecast['Stock cover upto (Date) Inc On Order'] = POQTY


# In[111]:


supplierForecast.to_csv('supplierForecast.csv', index=False)


# In[120]:


# str(pd.to_datetime(date_1) + pd.DateOffset(days=int(1)))[:int(10)]


# In[ ]:




