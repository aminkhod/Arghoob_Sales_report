
from flask import Flask, render_template,request, Response, send_file
import pandas as pd
import os
import json
import plotly.graph_objs as go
from  plotly.offline import plot, iplot
import plotly
import numpy as np
from datetime import datetime, timedelta

from plotly.graph_objs import *

# from plotly.offline import download_plotlyjs, init_notebook_mode
# from flask import json, request
# from plotly import figure_factory as FF
# from flaskext.mysql import MySQL
# from werkzeug import generate_password_hash, check_password_hash
# import plotly.io as pio
# import plotly.plotly as py
# import plotly.figure_factory as ff
# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# from IPython.display import SVG, display
# from IPython.display import Image
# from IPython.display import display, Math, Latex
# import colorlover as cl
# from IPython.display import HTML
# from IPython.display import IFrame



app = Flask(__name__)

# mysql = MySQL()
#
# # MySQL configurations
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = ''
# app.config['MYSQL_DATABASE_DB'] = 'BucketList'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# mysql.init_app(app)
#
# conn = mysql.connect()
# cursor = conn.cursor()

path = '../Monthes/'

files = []
filesNoAdd = []

for r, d, f in os.walk(path):
    for file in f:
        if '.csv' in file:
            files.append(os.path.join(r, file))
            filesNoAdd.append(file)
monthDate = []
for f in filesNoAdd:
    monthDate.append(f.replace('.csv',''))

df = pd.read_csv('allMonthes.csv')
# yV = []
# for i in range(len(files)):
#     yV.append(df.values[:,i + 8])
numListOfBranch = ['401 Co','402 Co','404 Co','405 Co','412 Co','416 Co',
                   '417 Co','423 Co', '424 Co','425 Co','426 Co','429 Co','444 Co','490 Co']
listOfBranch = ['total sale of Goods', 'Latest SOH',
                '401 Co', '401.Arq COST', '401.Cost Price', '401.V.S.P.', '401.AVG. WEEK',
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
                '490 Co', '490.Arq COST', '490.Cost Price', '490.V.S.P.', '490.AVG. WEEK']

productDetail = ['Sku', 'Catalogue N', 'Title', 'Label' ,'Arq COST', 'Cost Price' ,'V.S.P.']
header = productDetail.copy()
header.extend(listOfBranch.copy())
# @app.route("/")
# def hello():
#     return '''
#         <html><body>
#         Hello. <a href="/getPlotCSV">Click me.</a>
#         </body></html>
#             '''
@app.route("/")
def template():
    return render_template("template.html")
@app.route('/home')
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")
@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/MonthlySale', methods=['POST'])
def btnMonthlySale():
    path = '../Monthes/'
    files = []
    filesNoAdd = []
    for r, d, f in os.walk(path):
        for file in f:
            if '.csv' in file:
                files.append(os.path.join(r, file))
                filesNoAdd.append(file)
    cell = []
    for file in files:
        df = pd.read_csv(file)
        branchTot = []
        date = file.replace('../Monthes/','')
        date = date.replace('.csv','')
        branchTot.append(date)
        for col in listOfBranch:
            branchTot.append(round(df[col].sum(),2))
        cell.append(branchTot)

    head = ['Date']
    head.extend(listOfBranch)
    trace = go.Table(

                header=dict(values=head),

                cells=dict(values=np.transpose(cell)))

    data = Data([trace])
    layout = Layout(
        title='2019 sale for each months',
        width=6000
        )
    fig = Figure(data=data, layout=layout)
    # fig = Figure(data=data)
    plot(fig, filename='Monthly_Sale.html')
    return render_template("Monthly_Sale.html")


@app.route('/BranchSale',methods=['POST'])
def BranchSale():
    path = '../Monthes/'
    files = []
    filesNoAdd = []
    for r, d, f in os.walk(path):
        for file in f:
            if '.csv' in file:
                files.append(os.path.join(r, file))
                filesNoAdd.append(file)
    cell = []
    for file in files:
        df = pd.read_csv(file)
        branchTot = []
        for col in numListOfBranch:
            branchTot.append(round(df[col].sum(),2))
        cell.append(branchTot)



    traces = []
    for i in range(len(files)):
        trace = go.Bar(
        y=cell[i],
        x=numListOfBranch,
        name=monthDate[i]
        )
        traces.append(trace)


    data = Data(traces)
    layout = Layout(
        title='2019 sale for each months',
        updatemenus=list([
            dict(
                x=-0.05,
                y=1,
                yanchor='top',
                buttons=list([
                    dict(
                        args=['visible', [True, True, True, True, True]],
                        label='All',
                        method='restyle'
                    ),
                    dict(
                        args=['visible', [True, False, False, False, False]],
                        label=monthDate[0],
                        method='restyle'
                    ),
                    dict(
                        args=['visible', [False, True, False, False, False]],
                        label=monthDate[1],
                        method='restyle'
                    ),
                    dict(
                        args=['visible', [False, False, True, False, False]],
                        label=monthDate[2],
                        method='restyle'
                    ),
                    dict(
                        args=['visible', [False, False, False, True, False]],
                        label=monthDate[3],
                        method='restyle'
                    ),
                    dict(
                        args=['visible', [False, False, False, False, True]],
                        label=monthDate[4],
                        method='restyle'
                    )
                ]),
            )
        ]),
    )
    fig = Figure(data=data, layout=layout)
    plot(fig,filename='Sale_Of_Goods.html')
    return render_template('Sale_Of_Goods.html')

@app.route('/FastMoving',methods=['POST'])
def FastMoving():
    df = pd.read_csv('allMonthes.csv')
    newdf = df[df['Stock Status'] == 'Fast moving']
    newdf = newdf.loc[:,['Sku', 'Catalogue N', 'Title', 'Label',
                         'Arq COST', "Cost Price", 'V.S.P.', 'Latest SOH','Reordering']].reindex()
    trace = go.Table(
        header=dict(values=['Sku', 'Catalogue N', 'Title', 'Label',
                            'Arq COST', "Cost Price", 'V.S.P.', 'Latest SOH','Reordering']),
        cells=dict(values=np.transpose(newdf.values[:,:])))
    layout = Layout(
        title='Fast Moving Goods',
        width=1300
        )
    data = [trace]
    fig = Figure(data=data, layout=layout)
    plot(fig, filename = 'FastMoving.html')
    return render_template('FastMoving.html')


@app.route('/NonMoving',methods=['POST'])
def NonMoving():
    df = pd.read_csv('allMonthes.csv')
    newdf = df[df['Stock Status'] == 'Non moving']
    newdf = newdf.loc[:,['Sku', 'Catalogue N', 'Title', 'Label',
                         'Arq COST', "Cost Price", 'V.S.P.',
                         'Non Moving Action','Reordering']].reindex()
    trace = go.Table(
        header=dict(values=['Sku', 'Catalogue N', 'Title',
                            'Label', 'Arq COST', "Cost Price",
                            'V.S.P.', 'Non Moving Action', 'Reordering']),
        cells=dict(values=np.transpose(newdf.values[:,:])))
    layout = Layout(
        title='Non Moving Goods',
        width=1300
        )
    data = [trace]
    fig = Figure(data=data, layout=layout)
    plot(fig, filename='NonMoving.html')
    return render_template('NonMoving.html')
def create_plot():
    monthesLenght = [31,28,31,30,31,30,31,31,30,31,30,31]
    df = pd.read_csv('allMonthes.csv')
    foo = [filesNoAdd[i].replace('.csv',' total sale of Goods') for i in range(len(filesNoAdd))]
    list = ['Sku', 'Catalogue N', 'Label', 'Arq COST',
            'Cost Price', 'V.S.P.', 'Latest SOH']
    newdf = df[list]

    totalQtySold = np.zeros(len(df['Sku']))
    totalArghoobCost = np.zeros(len(df['Sku']))
    totalArqhoobPrice = np.zeros(len(df['Sku']))

    for i in range(len(foo)):
        cName = foo[i].replace(' total sale of Goods',': QTY SOLD')
        newdf[cName] = df[foo[i]]
        newdf[cName+'Arqoob Cost'] = df[foo[i]] * df['Arq COST']
        newdf[cName+'QTY SOLD VALUE'] = df[foo[i]] * df['Cost Price']
        list.extend([cName,cName+'Arqoob Cost',cName+'QTY SOLD VALUE'])
        totalQtySold += newdf[cName]
        totalArghoobCost += newdf[cName+'Arqoob Cost']
        totalArqhoobPrice += newdf[cName+'QTY SOLD VALUE']

    qtyAvgDay = round(totalQtySold/np.sum(monthesLenght[:len(foo)]),2)
    qtyAvgMonth = round(totalQtySold/len(foo),2)
    valueAvgMonth = round(totalArqhoobPrice/len(foo),2)
    qtyStockValue = newdf['Latest SOH'] * newdf['Cost Price']
    DaysStockInHand = round(newdf['Latest SOH'] / qtyAvgDay,2)
    WeeksStockInHand = round(DaysStockInHand/7,0)
    MonthesStockInHand = round(DaysStockInHand/30,0)
    i = 0
    CurrentStockCoverUpto = []
    for i in range(len(DaysStockInHand)):
        try:
            int(DaysStockInHand[i])

        except:
            DaysStockInHand[i] = 0
    for N in DaysStockInHand:
        if(N!=0):
            CurrentStockCoverUpto.append(str(datetime.now() + timedelta(days=N))[:10])
        else:
            CurrentStockCoverUpto.append('null')
        i +=1


    newdf['Total Qty Sold'], newdf['Total Arghoob Cost'],newdf['Total Arqhoob Price'],\
    newdf['Qty Avg Day'], newdf['Qty Avg Month'], newdf['Value Avg Month'],\
    newdf['Qty Stock Value'], newdf['Days Stock in Hand'],newdf['Current stock cover upto (Week)'], \
    newdf['Current stock cover upto (Month)'], newdf['Current stock cover upto (Date)'] = \
                totalQtySold, totalArghoobCost,totalArqhoobPrice,qtyAvgDay, qtyAvgMonth,\
                valueAvgMonth, qtyStockValue,DaysStockInHand, WeeksStockInHand, MonthesStockInHand,\
                CurrentStockCoverUpto
    newdf.to_csv('Profit Table.csv',index=False)
    list.extend(['Total Qty Sold', 'Total Arghoob Cost', 'Total Arqhoob Price',
                 'Qty Avg Day', 'Qty Avg Month','Value Avg Month', 'Qty Stock Value',
                 'Days Stock in Hand', 'Current stock cover upto (Week)',
                 'Current stock cover upto (Month)','Current stock cover upto (Date)'])
    trace = go.Table(
        header=dict(values=list),
        cells=dict(values=np.transpose(newdf.values[:,:])))
    layout = Layout(
        title='Profit Table',
        width=3600,
        )
    data = [trace]
    fig = Figure(data=data, layout=layout)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

@app.route('/bar', methods=['GET', 'POST'])
def change_features():
    feature = request.args['selected']
    graphJSON= create_plot(feature)
    return graphJSON

@app.route('/Stock_forecast')
def Stock_forecast():
    bar = create_plot()
    return render_template('Profit Table.html', plot=bar)

@app.route('/ItemRestock')
def ItemRestock():
    Restockdf = pd.read_csv('Profit Table.csv')
    Restockdf = Restockdf[Restockdf['Days Stock in Hand']<=10]
    Restockdf.to_csv('ItemRestock.csv')
    with open('ItemRestock.csv') as fp:
        csv = fp.read()
    return Response(csv, mimetype="text/csv",
                headers={"Content-disposition":
                         "attachment; filename=Items to be Restock.csv"})
@app.route('/ItemMonitor')
def ItemMonitor():
    Monitordf = pd.read_csv('Profit Table.csv')
    Monitordf = Monitordf[Monitordf['Latest SOH']/Monitordf['Total Qty Sold']>=4]
    Monitordf.to_csv('ItemMonitor.csv')
    with open('ItemMonitor.csv') as fp:
        csv = fp.read()
    return Response(csv, mimetype="text/csv",
                headers={"Content-disposition":
                         "attachment; filename=Items to be Monitor.csv"})

# @app.route('/index')
# def index():
#     bar = create_plot()
#     return render_template('index.html', plot=bar)

if __name__ == "__main__":
    app.run(debug=True)
