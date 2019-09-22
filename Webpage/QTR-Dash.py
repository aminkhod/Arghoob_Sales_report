from flask import Flask, render_template,request, Response
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

path = '../QTRMonthes/'

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

numListOfBranch = ['301 Co','302 Co','306 Co','307 Co']
listOfBranch = ['total sale of Goods', 'Latest SOH',
                '301 Co', '301.Arq COST', '301.Cost Price', '301.V.S.P.', '301.AVG. WEEK',
                '302 Co', '302.Arq COST', '302.Cost Price', '302.V.S.P.', '302.AVG. WEEK',
                '306 Co', '306.Arq COST', '306.Cost Price', '306.V.S.P.', '306.AVG. WEEK',
                '307 Co', '307.Arq COST', '307.Cost Price', '307.V.S.P.', '307.AVG. WEEK',]

productDetail = ['Sku','UPC', 'Catalogue N', 'Title', 'Label' ,'Arq COST', 'Cost Price' ,'V.S.P.']
header = productDetail.copy()
header.extend(listOfBranch.copy())

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
    path = '../QTRMonthes/'
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
        date = file.replace('../QTRMonthes/','')
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

    plot(fig, filename='Monthly_Sale.html')
    return render_template("Monthly_Sale.html")


@app.route('/BranchSale',methods=['POST'])
def BranchSale():
    path = '../QTRMonthes/'
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
    newdf['Arq COST'] = np.round(newdf['Arq COST'],2)
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
    newdf = newdf.loc[:,['Sku','UPC', 'Catalogue N', 'Title', 'Label',
                         'Arq COST', "Cost Price", 'V.S.P.',
                         'Non Moving Action','Reordering']].reindex()
    newdf['Arq COST'] = np.round(newdf['Arq COST'],2)
    trace = go.Table(
        header=dict(values=['Sku', 'UPC', 'Catalogue N', 'Title',
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

def create_plot(filesNoAdd):
    monthesLenght = [31,28,31,30,31,30,31,31,30,31,30,31]
    df = pd.read_csv('allMonthes.csv')
    foo = [filesNoAdd[i].replace('.csv',' total sale of Goods') for i in range(len(filesNoAdd))]
    list = ['Sku','UPC', 'Catalogue N', 'Label', 'Arq COST',
            'Cost Price', 'V.S.P.', 'Latest SOH']
    newdf = df[list]
    newdf['Arq COST'] = np.round(newdf['Arq COST'],2)

    totalQtySold = np.zeros(len(df['Sku']))
    totalArqoobCost = np.zeros(len(df['Sku']))
    totalArqhoobPrice = np.zeros(len(df['Sku']))
    df['Arq COST'] = np.round(df['Arq COST'],2)
    for i in range(len(foo)):
        cName = foo[i].replace(' total sale of Goods',': QTY SOLD')
        newdf[cName] = df[foo[i]]

        newdf[cName+' Arqoob Cost'] = np.round(df[foo[i]] * df['Arq COST'],2)
        newdf[cName+' Arqoob Cost'] = np.round(newdf[cName+' Arqoob Cost'],2)

        newdf[cName+' QTY SOLD VALUE'] = np.round(df[foo[i]] * df['Cost Price'],2)
        list.extend([cName,cName+' Arqoob Cost',cName+' QTY SOLD VALUE'])
        totalQtySold += newdf[cName]
        totalArqoobCost += newdf[cName+' Arqoob Cost']
        totalArqhoobPrice += newdf[cName+' QTY SOLD VALUE']
    totalArqoobCost = round(totalArqoobCost,2)
    qtyAvgDay = round(totalQtySold/np.sum(monthesLenght[:len(foo)]),2)
    qtyAvgMonth = round(totalQtySold/len(foo),2)
    valueAvgMonth = round(totalArqhoobPrice/len(foo),2)
    qtyStockValue = round(newdf['Latest SOH'] * newdf['Cost Price'],2)
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


    newdf['Total Qty Sold'], newdf['Total Arqoob Cost'],newdf['Total Arqhoob Price'],\
    newdf['Qty Avg Day'], newdf['Qty Avg Month'], newdf['Value Avg Month'],\
    newdf['Qty Stock Value'], newdf['Days Stock in Hand'],newdf['Current stock cover upto (Week)'], \
    newdf['Current stock cover upto (Month)'], newdf['Current stock cover upto (Date)'] = \
                totalQtySold, totalArqoobCost,totalArqhoobPrice,qtyAvgDay, qtyAvgMonth,\
                valueAvgMonth, qtyStockValue,DaysStockInHand, WeeksStockInHand, MonthesStockInHand,\
                CurrentStockCoverUpto
    newdf.to_csv('Profit Table.csv',index=False)
    list.extend(['Total Qty Sold', 'Total Arqoob Cost', 'Total Arqhoob Price',
                 'Qty Avg Day', 'Qty Avg Month','Value Avg Month', 'Qty Stock Value',
                 'Days Stock in Hand', 'Current stock cover upto (Week)',
                 'Current stock cover upto (Month)','Current stock cover upto (Date)'])
    trace = go.Table(
        header=dict(values=list),
        cells=dict(values=np.transpose(newdf.values[:,:])))
    layout = Layout(
        title='Profit Table',
        width=4800,
		height=630
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
    bar = create_plot(filesNoAdd)
    return render_template('Stock_forecast.html', plot=bar)

@app.route('/ItemRestock')
def ItemRestock():
    Restockdf = pd.read_csv('Profit Table.csv')
    Restockdf = Restockdf[Restockdf['Days Stock in Hand']<=10]
    Restockdf.to_csv('ItemRestock.csv', index=False)
    with open('ItemRestock.csv') as fp:
        csv = fp.read()
    return Response(csv, mimetype="text/csv",
                headers={"Content-disposition":
                         "attachment; filename=Items to be Restock.csv"})

@app.route('/ItemMonitor')
def ItemMonitor():
    Monitordf = pd.read_csv('Profit Table.csv')
    Monitordf = Monitordf[Monitordf['Latest SOH']/Monitordf['Total Qty Sold']>=4]
    Monitordf.to_csv('ItemMonitor.csv', index=False)
    with open('ItemMonitor.csv') as fp:
        csv = fp.read()
    return Response(csv, mimetype="text/csv",
                headers={"Content-disposition":
                         "attachment; filename=Items to be Monitor.csv"})

@app.route('/ItemNonMoving')
def ItemNonMoving():
    df = pd.read_csv('allMonthes.csv')
    newdf = df[df['Stock Status'] == 'Non moving']
    newdf.to_csv('nonMovingItem.csv', index=False)
    with open('nonMovingItem.csv') as fp:
        csv = fp.read()
    return Response(csv, mimetype="text/csv",
                headers={"Content-disposition":
                         "attachment; filename= Non Moving Item.csv"})


if __name__ == "__main__":
    app.run(debug=True)
