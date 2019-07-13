
from flask import Flask, render_template, json, request
import pandas as pd
import os
import plotly.graph_objs as go
from  plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import numpy as np
from plotly.tools import FigureFactory as FF
from plotly.graph_objs import *

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
# pd.r

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
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.csv' in file:
            files.append(os.path.join(r, file))
            filesNoAdd.append(file)
monthDate = []
for f in filesNoAdd:
    monthDate.append(f.replace('.csv',''))
# print(monthDate)

df = pd.read_csv('allMonthes.csv')
yV = []
for i in range(5):
    yV.append(df.values[:,i + 8])
numListOfBranch = ['401 Co','402 Co','404 Co','405 Co','412 Co','416 Co','417 Co','423 Co',
                   '424 Co','425 Co','426 Co','429 Co','444 Co','490 Co',]
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
    df = pd.read_csv('../Monthes/01-2019.csv')
    branchTot1 = []
    for col in numListOfBranch:
    	branchTot1.append(df[col].sum())
    	trace5 = go.Table(
    		header=dict(values=numListOfBranch),
    		cells=dict(values=branchTot1))

    df = pd.read_csv('../Monthes/02-2019.csv')
    branchTot2 = []
    for col in numListOfBranch:
    	branchTot2.append(df[col].sum())
    	trace6 = go.Table(
    		header=dict(values=numListOfBranch),
    		cells=dict(values=branchTot2))

    df = pd.read_csv('../Monthes/03-2019.csv')
    branchTot3 = []
    for col in numListOfBranch:
    	branchTot3.append(df[col].sum())
    	trace7 = go.Table(
    		header=dict(values=numListOfBranch),
    		cells=dict(values=branchTot3))

    df = pd.read_csv('../Monthes/04-2019.csv')
    branchTot4 = []
    for col in numListOfBranch:
    	branchTot4.append(df[col].sum())
    	trace8 = go.Table(
    		header=dict(values=numListOfBranch),
    		cells=dict(values=branchTot4))
    df = pd.read_csv('../Monthes/05-2019.csv')
    branchTot4 = []
    for col in numListOfBranch:
    	branchTot4.append(df[col].sum())
    	trace9 = go.Table(
    		header=dict(values=numListOfBranch),
    		cells=dict(values=branchTot4))
    data = Data([trace5, trace6, trace7, trace8, trace9])
    layout = Layout(
        title='2019 sale for each months',
        updatemenus=list([
            dict(
                x=-0.05,
                y=1,
                yanchor='top',
                buttons=list([
                    dict(
                        args=['visible', [ True, False, False, False, False]],
                        label = monthDate[0],
                        method='restyle'
                    ),
                    dict(
                        args=['visible', [False, True, False, False, False]],
                        label = monthDate[1],
                        method='restyle'
                    ),
                    dict(
                        args=['visible', [False, False, True, False, False]],
                        label = monthDate[2],
                        method='restyle'
                    ),
                    dict(
                        args=['visible', [False, False, False, True, False]],
                        label = monthDate[3],
                        method='restyle'
                    ),
                    dict(
                        args=['visible', [False, False, False, False, True]],
                        label = monthDate[4],
                        method='restyle'
                        )
                    ]),
                )
            ]),
        )
    fig = Figure(data=data, layout=layout)
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
    #     x=countries,
        y=silver,
        # line=Line(
        #     color='#C0C0C0',
        #     width=3
        # ),
        name=monthDate[1]
    )

    trace3 = Bar(
    #     x=countries,
        y=bronze,
        # color='#BA8651',
        # line=Line(
        #     color='#BA8651',
        #     width=3
        # ),
        name=monthDate[2]
    )

    trace4 = Bar(
    #     x=countries,
        y=total,
        # color='#000000',
        # line=Line(
        #     color='#000000',
        #     width=4
        # ),
        name=monthDate[3]
    )
    trace5 = Bar(
    #     x=countries,
        y=total,
        # color='#000000',
        # line=Line(
        #     color='#000000',
        #     width=4
        # ),
        name=monthDate[4]
    )

    # data = [trace]
    # plot(data, filename = 'basic_table')
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

@app.route('/StockStatus',methods=['POST'])
def stockStatus():
    df = pd.read_csv('allMonthes.csv')
    newdf = df[df['Stock Status'] == 'Fast moving']
    newdf = newdf.loc[:,['Sku', 'UPC', 'Catalogue N', 'Title', 'Label', 'Arq COST', "Cost Price", 'V.S.P.']].reindex()

    r,c = newdf.shape
    z = np.random.randn(r,c)
    fig = FF.create_annotated_heatmap(z,  annotation_text=newdf.values[:,:])
    plot(fig, filename='fast moving.html')

    return render_template('fast moving.html')


if __name__ == "__main__":
    app.run(debug=True)
