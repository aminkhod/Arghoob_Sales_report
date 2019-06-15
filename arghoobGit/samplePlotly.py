#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
# import os
# import plotly.io as pio
# import plotly.plotly as py
# import plotly.figure_factory as ff
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from  plotly.offline import plot
import dash_auth
# import plotly
# from IPython.display import SVG, display
# from IPython.display import Image
# from IPython.display import display, Math, Latex
# import colorlover as cl
# from IPython.display import HTML
# from IPython.display import IFrame
# from plotly.offline import iplot, init_notebook_mode
# from IPython.display import YouTubeVideo


# In[3]:


VALID_USERNAME_PASSWORD_PAIRS = [
    ['123', '123']
]


# In[4]:


app = dash.Dash('auth')
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)


# In[5]:


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


# In[6]:


df = pd.read_csv('toalOfMonth.csv')

branchTot = []
for col in numListOfBranch:
    branchTot.append(df[col].sum())


# In[7]:




# trace = go.Table(
#     header=dict(values=numListOfBranch),
#     cells=dict(values=branchTot))

# data = [trace] 
# plot(data, filename = 'basic_table')


# In[9]:




app = dash.Dash(__name__)
server = app.server

# df = pd.read_csv(
#     'https://gist.githubusercontent.com/chriddyp/' +
#     '5d1ea79569ed194d432e56108a04d188/raw/' +
#     'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
#     'gdp-life-exp-2007.csv')


app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Bar(
                    x=numListOfBranch,
                    y=branchTot,
#                     text=df[df['continent'] == i]['country'],
#                     mode='markers',
                    opacity=0.8,
                    marker={
#                         'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name='Total Sale')
#                 ) for i in numListOfBranch
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'Branches'},
                yaxis={'title': 'Sale'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server()


# In[ ]:




