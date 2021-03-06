
from flask import Flask, render_template
import pandas as pd
import os
import plotly.graph_objs as go
from  plotly.offline import plot
import numpy as np
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
# import plotly
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
yV = []
for i in range(5):
    yV.append(df.values[:,i + 8])
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

productDetail = ['Sku', 'UPC', 'Catalogue N', 'Title', 'Label' ,'Arq COST', 'Cost Price' ,'V.S.P.']
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


@app.route('/GoodsSale',methods=['POST'])
def GoodsSale():
	# read the posted values from the UI
	# _name = request.form['inputName']
	# _email = request.form['inputEmail']
	# _password = request.form['inputPassword']
    #
	# _hashed_password = generate_password_hash(_password)
	# cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
    #
	# data = cursor.fetchall()
    #
	# if len(data) is 0:
	# 	conn.commit()
	# 	return json.dumps({'message':'User created successfully !'})
	# else:
	# 	return json.dumps({'error':str(data[0])})

    # countries = ['United States', 'China', 'South Korea', 'Hungary', 'Austraila', 'Canada']

    gold = yV[0]
    silver = yV[1]
    bronze = yV[2]
    total = yV[3]

    trace1 = Bar(
    #     x=countries,
        y=gold,
        # line=Line(
        #     color='#FFD700',
        #     width=3
        # ),
        name=monthDate[0]
    )

    trace2 = Bar(
        y=silver,
        name=monthDate[1]
    )

    trace3 = Bar(
        y=bronze,
        name=monthDate[2]
    )

    trace4 = Bar(
        y=total,
        name=monthDate[3]
    )
    trace5 = Bar(
        y=total,
        name=monthDate[4]
    )

    data = Data([trace1, trace2, trace3, trace4,trace5])
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
    newdf = newdf.loc[:,['Sku', 'UPC', 'Catalogue N', 'Title', 'Label',
                         'Arq COST', "Cost Price", 'V.S.P.', 'Latest SOH','Reordering']].reindex()
    trace = go.Table(
        header=dict(values=['Sku', 'UPC', 'Catalogue N', 'Title', 'Label',
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
    newdf = newdf.loc[:,['Sku', 'UPC', 'Catalogue N', 'Title', 'Label',
                         'Arq COST', "Cost Price", 'V.S.P.',
                         'Non Moving Action','Reordering']].reindex()
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
    plot(fig, filename = 'NonMoving.html')
    return render_template('NonMoving.html')

if __name__ == "__main__":
    app.run(debug=True)
