#!/usr/bin/env python
# coding: utf-8

# In[39]:


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
# init_notebook_mode(connected=True)

# import subprocess
# subprocess.check_call(['pip', 'install', 'numpy']) # install pkg
# subprocess.check_call(['pip', 'install',"--upgrade", 'numpy']) # upgrade pkg


# In[40]:


# sku = rawData.values[:189,0]
# upc = rawData.values[:189,1]
# Catalogue = rawData.values[:189,2]
# title = rawData.values[:189,3]
# label = rawData.values[:189,4]
# Cost_Price = rawData.values[:189,5]
# VSP = rawData.values[:189,6]


# In[41]:


# rawDatVal = []
# rawDatVal = rawData.values[:189,7:149]
# eachRaw = []
# allRawvalue = []
# BranchTotal = rawDatVal.sum(axis=0)

# for i in range(len(rawDatVal[:,0])):
#     for j in range(int((len(rawDatVal[0,:]))/3)):
        
#         k=3 * j 

#         eachRaw.append(rawDatVal[i,k])
#     eachRaw = np.array(eachRaw)
#     allRawvalue.append(eachRaw.sum())
#     eachRaw = []

# # rawData['Sum of sale for each goods'] = allRawvalue


# In[42]:



# eachRaw = []

# BranchTotal = rawDatVal.sum(axis=0)
# for j in range(int(len(rawDatVal[0,:])/3)):
#     k=3 * j 
#     sum = 0
#     for i in range(len(rawDatVal[:,0])):
#         sum += rawDatVal[i,k]
#     rawData.iloc[i+1,k] = sum
    

#     eachRaw = []
# # allRawvalue.append(np.array(allRawvalue).sum())
# # allRawvalue.append(np.array(allRawvalue).sum())


# In[43]:


# Virgin_Stock = []
# Virgin_Stock = pd.DataFrame(Virgin_Stock)
# Virgin_Stock['sku'] = sku
# Virgin_Stock['upc'] = upc
# Virgin_Stock['Catalogue'] = Catalogue
# Virgin_Stock['title'] = title
# Virgin_Stock['label'] = label
# Virgin_Stock['VMS Cost'] = Cost_Price
# Virgin_Stock['VSP'] = VSP


# Virgin_Stock[f1] = list(allRawvalue)


# In[44]:


# i = 1
# buf = np.zeros(len(Virgin_Stock.values[:,1]), dtype=int)



# ## i
# for j in range(i):
#     buf += np.array(Virgin_Stock.values[:,7+j], dtype = int)

# Virgin_Stock["TOTAL"] = buf
# ii = np.full(len(Virgin_Stock.values[:,1]) ,i )

# Virgin_Stock["AVG. WEEK"] = np.divide(Virgin_Stock["TOTAL"] , ii)
# Virgin_Stock['total VMS Cost'] = Virgin_Stock["TOTAL"] * Virgin_Stock['VMS Cost']
# Virgin_Stock['total V.S.P.'] = Virgin_Stock["TOTAL"] * Virgin_Stock['VSP']
# count = 0
# for head in list(rawData.head(0)):
#     if ".Sales Quantity" in head:
#         Virgin_Stock[head] = rawData[head]
#         try:
#             headNum = int(head.replace(".Sales Quantity",''))
#         except:
#             print(int(headNum)," can't be cast to int")
#         headNum = str(headNum)
#         Virgin_Stock['TOTAL' + headNum] = rawData.values[:189, count]
#         Virgin_Stock['VMS Cost' + headNum] = Virgin_Stock['VMS Cost'] * Virgin_Stock['TOTAL' + headNum]
#         Virgin_Stock['V.S.P.' + headNum] = Virgin_Stock['VSP'] * Virgin_Stock['TOTAL' + headNum]
#         Virgin_Stock['AVG. WEEK' + headNum] = np.divide(Virgin_Stock['TOTAL' + headNum] , ii)
#     count +=1
        


# In[45]:


#  Virgin_Stock['VMS Cost'] * Virgin_Stock['TOTAL' + headNum]


# In[46]:


numListOfBranch = ['401','402','404','405','412','416','417','423',
                   '424','425','426','429','444','490',]
listOfBranch = ['401', '401.VMS cost', '401.V.S.P.', '401.AVG. WEEK',
                '402', '402.VMS cost', '402.V.S.P.', '402.AVG. WEEK',
                '404', '404.VMS cost', '404.V.S.P.', '404.AVG. WEEK',
                '405', '405.VMS cost', '405.V.S.P.', '405.AVG. WEEK',
                '412', '412.VMS cost', '412.V.S.P.', '412.AVG. WEEK',
                '416', '416.VMS cost', '416.V.S.P.', '416.AVG. WEEK',
                '417', '417.VMS cost', '417.V.S.P.', '417.AVG. WEEK',
                '423', '423.VMS cost', '423.V.S.P.', '423.AVG. WEEK',
                '424', '424.VMS cost', '424.V.S.P.', '424.AVG. WEEK',
                '425', '425.VMS cost', '425.V.S.P.', '425.AVG. WEEK',
                '426', '426.VMS cost', '426.V.S.P.', '426.AVG. WEEK',
                '429', '429.VMS cost', '429.V.S.P.', '429.AVG. WEEK',
                '444', '444.VMS cost', '444.V.S.P.', '444.AVG. WEEK',
                '490', '490.VMS cost', '490.V.S.P.', '490.AVG. WEEK']

productDetail = ['Sku', 'UPC', 'Catalogue N', 'Title', 'Label' ,'Cost Price' ,'V.S.P.']
header = productDetail.copy()
header.extend(listOfBranch.copy())


# In[47]:


# findID(str(748116), rawData)
# rawData


# In[48]:


# noStock(748116,rawData)


# In[49]:


# monthRawData.iloc[155]['Sku']


# In[50]:



# df = pd.read_csv('hg.csv')


# def generate_table(dataframe, max_rows=10):
#     return html.Table(
#         # Header
#         [html.Tr([html.Th(col) for col in dataframe.columns])] +

#         # Body
#         [html.Tr([
#             html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
#         ]) for i in range(min(len(dataframe), max_rows))]
#     )


# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# app.layout = html.Div(children=[
#     html.H4(children='US Agriculture Exports (2011)'),
#     generate_table(df)
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)


# In[52]:


df = pd.read_csv('toalOfMonth.csv')

branchTot = []
for col in numListOfBranch:
    branchTot.append(df[col].sum())


# In[53]:




trace = go.Table(
    header=dict(values=numListOfBranch),
    cells=dict(values=branchTot))

data = [trace] 
plot(data, filename = 'basic_table')


# In[54]:




trace = go.Table(
    header=dict(values=numListOfBranch,
                line = dict(color='#7D7F80'),
                fill = dict(color='#a1c3d1'),
                align = ['left'] * 5),
    cells=dict(values=branchTot,
               line = dict(color='#7D7F80'),
               fill = dict(color='#EDFAFF'),
               align = ['left'] * 5))

layout = dict(width=1000, height=600)
data = [trace]
fig = dict(data=data, layout=layout)
plot(fig, filename = 'styled_table')


# In[56]:




# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv')
df = pd.read_csv('toalOfMonth.csv')

trace = go.Table(
    header=dict(values=list(numListOfBranch),
                fill = dict(color='#C2D4FF'),
                align = ['left'] * len(branchTot)),
                cells=dict(values=branchTot,
                fill = dict(color='#F5F8FF'),
                align = ['left'] * len(branchTot)))

data = [trace] 
plot(data, filename = 'pandas_table')


# In[57]:




# values = [[['Salaries', 'Office', 'Merchandise', 'Legal', '<b>TOTAL<br>EXPENSES</b>']],
# [["Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus"
#   +" vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
#   "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus"
#   +" vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
#   "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus"
#   +" vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
#   "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus"
#   + " vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
#   "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus"
#   +" vim. Id usu aeterno adversarium, summo mollis timeam vel ad"]]]


# trace0 = go.Table(
#   columnorder = [1,2],
#   columnwidth = [80,400],
#   header = dict(
#     values = [['<b>EXPENSES</b><br>as of July 2017'],
#                   ['<b>DESCRIPTION</b>']],
#     line = dict(color = '#506784'),
#     fill = dict(color = '#119DFF'),
#     align = ['left','center'],
#     font = dict(color = 'white', size = 12),
#     height = 40
#   ),
#   cells = dict(
#     values = values,
#     line = dict(color = '#506784'),
#     fill = dict(color = ['#25FEFD', 'white']),
#     align = ['left', 'center'],
#     font = dict(color = '#506784', size = 12),
#     height = 30
#     ))

# data = [trace0]

# plot(data, filename = "Row and Column Size")


# In[58]:




# headerColor = 'grey'
# rowEvenColor = 'lightgrey'
# rowOddColor = 'white'

# trace0 = go.Table(
#   header = dict(
#     values = [['<b>EXPENSES</b>'],
#                   ['<b>Q1</b>'],
#                   ['<b>Q2</b>'],
#                   ['<b>Q3</b>'],
#                   ['<b>Q4</b>']],
#     line = dict(color = '#506784'),
#     fill = dict(color = headerColor),
#     align = ['left','center'],
#     font = dict(color = 'white', size = 12)
#   ),
#   cells = dict(
#     values = [
#       [['Salaries', 'Office', 'Merchandise', 'Legal', '<b>TOTAL</b>']],
#       [[1200000, 20000, 80000, 2000, 12120000]],
#       [[1300000, 20000, 70000, 2000, 130902000]],
#       [[1300000, 20000, 120000, 2000, 131222000]],
#       [[1400000, 20000, 90000, 2000, 14102000]]],
#     line = dict(color = '#506784'),
#     fill = dict(color = [rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]),
#     align = ['left', 'center'],
#     font = dict(color = '#506784', size = 11)
#     ))

# data = [trace0]

# plot(data, filename = "alternating row colors")
if len(cl.scales['7']['seq']['Blues']) <= 14:
    color = cl.scales['7']['seq']['Blues']
    color.extend(cl.scales['7']['seq']['Blues'])
    len(color)


# In[59]:



colors = cl.scales['7']['seq']['Blues']
len(colors)

print(len(colors))

data = {'Branch' : list(numListOfBranch),
        'Total' : list(branchTot),
        'Color' : list(colors[:14])}
df = pd.DataFrame(data)


trace0 = go.Table(
  header = dict(
    values = ["Total Sale", "<b>Branch</b>"],
    line = dict(color = 'white'),
    fill = dict(color = 'white'),
    align = ['center'],
    font = dict(color = 'black', size = 12)
  ),
  cells = dict(
    values = [df.Total, df.Branch],
    line = dict(color = [df.Color]),
    fill = dict(color = [df.Color]),
    align = 'center',
    font = dict(color = 'black', size = 11)
    ))

data = [trace0]

plot(data, filename = "row variable color")


# In[60]:



# colors = cl.scales['9']['seq']['Reds']
# a = np.random.randint(low=0, high=9, size=10)
# b = np.random.randint(low=0, high=9, size=10)
# c = np.random.randint(low=0, high=9, size=10)


# trace0 = go.Table(
#   header = dict(
#     values = numListOfBranch,
#     line = dict(color = 'white'),
#     fill = dict(color = 'white'),
#     align = 'center',
#     font = dict(color = 'black', size = 12)
#   ),
#   cells = dict(
#     values =branchTot,
#     line = dict(color = [np.array(colors)[a],np.array(colors)[b],
#                         np.array(colors)[c]]),
#     fill = dict(color = [np.array(colors)[a],np.array(colors)[b],
#                         np.array(colors)[c]]),
#     align = 'center',
#     font = dict(color = 'white', size = 11)
#     ))

# data = [trace0]

# plot(data, filename = "cell variable color")


# In[61]:



# df = pd.read_csv("hg.csv")
# ff = df[['Sku','Catalogue N','Cost Price','V.S.P.','total sale of Goods','Status']]

# table = ff.create_table(df)
# # print(table)
# # table
# plot(table)
# pio.write_image(table, 'table.webp')
# pio.write_image(table, 'table.pdf')


# In[68]:


# import tkinter
# from tkinter import messagebox
# root = tkinter.Tk()
# root.withdraw()
# df = pd.read_csv("hg.csv")
# # messagebox.showinfo(str(df.std()))
# # messagebox.showinfo(str(df.mean()))
# # messagebox.showinfo(str(df.info()))
# # print(df.mean())
# # print(df.info())

# top = tkinter.Tk()
# def STD():
#     messagebox.showinfo('STD',str(df.std()))
# def mean():
#     messagebox.showinfo('Mean',str(df.mean()))
# def info():
#     messagebox.showinfo('Info', str(df.info()))

# B1 = tkinter.Button(top, text = 'STD', command = STD)
# B1.pack()



# B2 = tkinter.Button(top, text = 'Mean', command = mean)
# B2.pack()



# B3 = tkinter.Button(top,text = 'Info', command = info)
# B3.pack()

# top.mainloop()


# In[69]:



data = pd.read_csv('toalOfMonth.csv')

branchTot = []
for col in numListOfBranch:
    branchTot.append(data[col].sum())
    
data = [go.Bar(x=numListOfBranch,
            y=branchTot)]


plot(data, filename='jupyter-basic_bar')


# In[70]:




data = pd.read_csv('toalOfMonth.csv')

branchTot = []
for col in numListOfBranch:
    branchTot.append(data[col].sum())
N = 100
x = numListOfBranch
y = branchTot
colors = np.random.rand(N)
sz = np.random.rand(N)*30

fig = go.Figure()
fig.add_scatter(x=x,
                y=y,
                mode='markers',
                marker={'size': sz,
                        'color': colors,
                        'opacity': 0.6,
                        'colorscale': 'Viridis'
                       });
plot(fig)


# In[71]:



data = pd.read_csv('toalOfMonth.csv')

branchTot = []
for col in numListOfBranch:
    branchTot.append(data[col].sum())

x = numListOfBranch
y = branchTot
colors = np.random.rand(N)
  
data = go.Figure()
data.add_bar(x=x,
                y=y,
                marker={
                        'color': colors,
                        'opacity': 0.6,
                        'colorscale': 'Viridis'
                       })
pio.write_image(data, 'fig1.jpeg')
img_bytes = pio.to_image(data, format='svg')
pio.write_image(data, 'fig1.webp')
display(SVG(img_bytes))


# In[72]:


img_bytes = pio.to_image(data, format='png', width=600, height=400, scale=2)
Image(img_bytes)


# In[73]:


# %%time
# pio.write_image(data, 'fig1.jpeg')
# img_bytes = pio.to_image(data, format='svg')

# display(SVG(img_bytes))


# In[74]:



# df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/school_earnings.csv")

# trace_women = go.Bar(x=df.School,
#                   y=df.Women,
#                   name='Women',
#                   marker=dict(color='#ffcdd2'))

# trace_men = go.Bar(x=df.School,
#                 y=df.Men,
#                 name='Men',
#                 marker=dict(color='#A2D5F2'))

# trace_gap = go.Bar(x=df.School,
#                 y=df.Gap,
#                 name='Gap',
#                 marker=dict(color='#59606D'))

# data = [trace_women, trace_men, trace_gap]

# layout = go.Layout(title="Average Earnings for Graduates",
#                 xaxis=dict(title='School'),
#                 yaxis=dict(title='Salary (in thousands)'))

# fig = go.Figure(data=data, layout=layout)

# plot(fig, sharing='private', filename='jupyter-styled_bar')


# In[75]:



# mapbox_access_token = 'dfg'

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Nuclear%20Waste%20Sites%20on%20American%20Campuses.csv')
# site_lat = df.lat
# site_lon = df.lon
# locations_name = df.text

# data = [
#     go.Scattermapbox(
#         lat=site_lat,
#         lon=site_lon,
#         mode='markers',
#         marker=dict(
#             size=17,
#             color='rgb(255, 0, 0)',
#             opacity=0.7
#         ),
#         text=locations_name,
#         hoverinfo='text'
#     ),
#     go.Scattermapbox(
#         lat=site_lat,
#         lon=site_lon,
#         mode='markers',
#         marker=dict(
#             size=8,
#             color='rgb(242, 177, 172)',
#             opacity=0.7
#         ),
#         hoverinfo='none'
#     )]


# layout = go.Layout(
#     title='Nuclear Waste Sites on Campus',
#     autosize=True,
#     hovermode='closest',
#     showlegend=False,
#     mapbox=dict(
#         accesstoken=mapbox_access_token,
#         bearing=0,
#         center=dict(
#             lat=38,
#             lon=-94
#         ),
#         pitch=0,
#         zoom=3,
#         style='light'
#     ),
# )

# fig = dict(data=data, layout=layout)

# plot(fig, filename='jupyter-Nuclear Waste Sites on American Campuses')


# In[76]:



# s = np.linspace(0, 2 * np.pi, 240)
# t = np.linspace(0, np.pi, 240)
# tGrid, sGrid = np.meshgrid(s, t)

# r = 2 + np.sin(7 * sGrid + 5 * tGrid)  # r = 2 + sin(7s+5t)
# x = r * np.cos(sGrid) * np.sin(tGrid)  # x = r*cos(s)*sin(t)
# y = r * np.sin(sGrid) * np.sin(tGrid)  # y = r*sin(s)*sin(t)
# z = r * np.cos(tGrid)                  # z = r*cos(t)

# surface = go.Surface(x=x, y=y, z=z)
# data = [surface]

# layout = go.Layout(
#     title='Parametric Plot',
#     scene=dict(
#         xaxis=dict(
#             gridcolor='rgb(255, 255, 255)',
#             zerolinecolor='rgb(255, 255, 255)',
#             showbackground=True,
#             backgroundcolor='rgb(230, 230,230)'
#         ),
#         yaxis=dict(
#             gridcolor='rgb(255, 255, 255)',
#             zerolinecolor='rgb(255, 255, 255)',
#             showbackground=True,
#             backgroundcolor='rgb(230, 230,230)'
#         ),
#         zaxis=dict(
#             gridcolor='rgb(255, 255, 255)',
#             zerolinecolor='rgb(255, 255, 255)',
#             showbackground=True,
#             backgroundcolor='rgb(230, 230,230)'
#         )
#     )
# )

# fig = go.Figure(data=data, layout=layout)
# plot(fig, filename='jupyter-parametric_plot')


# In[77]:




# data = [dict(
#         visible = False,
#         line=dict(color='#00CED1', width=6),
#         name = '𝜈 = '+str(step),
#         x = np.arange(0,10,0.01),
#         y = np.sin(step*np.arange(0,10,0.01))) for step in np.arange(0,5,0.1)]
# data[10]['visible'] = True

# steps = []
# for i in range(len(data)):
#     step = dict(
#         method = 'restyle',
#         args = ['visible', [False] * len(data)],
#     )
#     step['args'][1][i] = True # Toggle i'th trace to "visible"
#     steps.append(step)

# sliders = [dict(
#     active = 10,
#     currentvalue = {"prefix": "Frequency: "},
#     pad = {"t": 50},
#     steps = steps
# )]

# layout = dict(sliders=sliders)
# fig = dict(data=data, layout=layout)

# plot(fig, filename='Sine Wave Slider')


# In[78]:




# YouTubeVideo("wupToqz1e2g")
# # YouTubeVideo('')


# In[79]:





# display(Math(r'F(k) = \int_{-\infty}^{\infty} f(x) e^{2\pi i k} dx'))


# In[80]:


# IFrame(src= "https://dash-simple-apps.plotly.host/dash-tableplot/", width="100%", height="850px", frameBorder="0")


# In[81]:



# IFrame(src= "https://dash-simple-apps.plotly.host/dash-tableplot/code", width="100%", height=500, frameBorder="0")


# In[82]:


toalOfMonth = pd.read_csv('toalOfMonth.csv')
numListOfBranch = ['401','402','404','405','412','416','417','423',
                   '424','425','426','429','444','490',]
branchTot = []
for col in numListOfBranch:
    branchTot.append(toalOfMonth[col].sum())
    
np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)


# In[83]:


data = [go.Box(y = branchTot, name = 'sale distribution',
               marker = dict(
                   size = 12,
                   color = 'rgb(120,56,98)',
                   symbol = 'pentagon',
                   line = {'width':2}
               ),
               boxmean=True, boxpoints = 'all')]
# boxmean = 'sd'
# boxpoints = 'outliers'
# boxpoints = 'suspectedoutliers
# boxpoints = False

layout = go.Layout(
    title = "sale distribution",
    xaxis = {'title':''},
    yaxis = dict(title = 'sale values'),
    hovermode = 'closest'
)

fig = go.Figure(data=data,layout=layout)
plot(fig, filename = "sale distribution of each branch")


# In[84]:


data = [go.Bar(x = numListOfBranch, y = branchTot,
               marker = dict(
                   color = 'rgb(18,95,200)',
                   line = {'width':2}
               ))]

layout = go.Layout(
    title = "sale distribution",
    xaxis = {'title':'Branches'},
    yaxis = dict(title = 'sale values'),
    hovermode = 'closest'
    
)

fig = go.Figure(data = data, layout = layout)

plot(fig, filename = 'sale amount of each branch')


# In[85]:



IFrame(src= "https://dash-simple-apps.plotly.host/dash-boxplot/",
       width="100%", height="650px", frameBorder="0")


# In[ ]:




