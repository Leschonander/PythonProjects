from flask import Flask, render_template
from data import complaintAmount, df
import pandas as pd
#Insert data here
# print(df["Company"])

# configuration
DEBUG = True
#Begin App
app = Flask(__name__)
app.config.from_object(__name__)
app.static_folder = 'static'
#Routes
@app.route('/')
@app.route('/about') 
def home():
    complaintAmount
    return render_template('about.html', title='Consumer Complaints', complaintAmount = complaintAmount)
@app.route('/data')
def data():
    return render_template('data.html', title='Consumer Complaints', complaintAmount = complaintAmount  ,tables = [df.to_html(classes='dataset')])

if __name__ == '__main__':
    app.run()