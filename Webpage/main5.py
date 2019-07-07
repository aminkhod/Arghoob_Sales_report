
from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
import pandas as pd
import numpy as np
import os
import plotly.graph_objs as go

import plotly.plotly as py
import plotly.figure_factory as ff
import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
from  plotly.offline import plot
import plotly
import colorlover as cl

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()



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
    pd

if __name__ == "__main__":
    app.run(debug=True)
