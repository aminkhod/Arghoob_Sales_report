
from flask import Flask, render_template, json, request
# from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash

import plotly
import pandas as pd
import numpy as np
import os
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
from plotly.graph_objs import *


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

@app.route('/signUp',methods=['POST'])
def signUp():
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

    trace1 = Scatter(
    #     x=countries,
        y=gold,
        line=Line(
            color='#FFD700',
            width=3
        ),
        name=monthDate[0]
    )

    trace2 = Scatter(
    #     x=countries,
        y=silver,
        line=Line(
            color='#C0C0C0',
            width=3
        ),
        name=monthDate[1]
    )

    trace3 = Scatter(
    #     x=countries,
        y=bronze,
        line=Line(
            color='#BA8651',
            width=3
        ),
        name=monthDate[2]
    )

    trace4 = Scatter(
    #     x=countries,
        y=total,
        line=Line(
            color='#000000',
            width=4
        ),
        name=monthDate[3]
    )

    data = Data([trace1, trace2, trace3, trace4])
    layout = Layout(
        title='2019 sale for each months',
        updatemenus=list([
            dict(
                x=-0.05,
                y=1,
                yanchor='top',
                buttons=list([
                    dict(
                        args=['visible', [True, True, True, True]],
                        label='All',
                        method='restyle'
                    ),
                    dict(
                        args=['visible', [True, False, False, False]],
                        label=monthDate[0],
                        method='restyle'
                    ),
                    dict(
                        args=['visible', [False, True, False, False]],
                        label=monthDate[1],
                        method='restyle'
                    ),
                    dict(
                        args=['visible', [False, False, True, False]],
                        label=monthDate[2],
                        method='restyle'
                    ),
                    dict(
                        args=['visible', [False, False, False, True]],
                        label=monthDate[3],
                        method='restyle'
                    )
                ]),
            )
        ]),
    )
    fig = Figure(data=data, layout=layout)
    iplot(fig)


if __name__ == "__main__":
    app.run(debug=True)
