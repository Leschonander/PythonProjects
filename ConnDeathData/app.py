from flask import Flask, render_template
from data import fentanylDeaths, cocaineDeaths, BenzodiazepineDeaths, maleDeaths, femaleDeaths
import pandas as pd

#Insert data here
title = 'CN Drug Death Statistics'

MAPBOX_ACCESS_KEY = 'NOT FOR YOU TO STEAL'


# configuration
DEBUG = True
#Begin App
app = Flask(__name__)
app.config.from_object(__name__)
app.static_folder = 'static'
#Routes
@app.route('/')
@app.route('/map') 
def home():
    return render_template('main.html', 
    title = title,
    MAPBOX_ACCESS_KEY = MAPBOX_ACCESS_KEY,
    fenTable = [fentanylDeaths.describe().to_html(classes='dataset1')],
    cocTable = [cocaineDeaths.describe().to_html(classes='dataset2')],
    benTable = [BenzodiazepineDeaths.describe().to_html(classes='dataset3')],
    memTable = [maleDeaths.describe().to_html(classes='dataset4')],
    femTable = [femaleDeaths.describe().to_html(classes='dataset5')]
    )


if __name__ == '__main__':
    app.run()