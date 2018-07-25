from flask import Flask, render_template
from data import bikes, chargeCount, chargeDesc
import pandas as pd
from features import bikeLocations #the features data...
#Insert data here
title='JumpBike Map and Viz'

MAPBOX_ACCESS_KEY = 'GET YOUR OWN KEY'
# POINTS = cordDict



# configuration
DEBUG = True
#Begin App
app = Flask(__name__)
app.config.from_object(__name__)
app.static_folder = 'static'
#Routes
@app.route('/')
@app.route('/home') 
def home():
    return render_template('home.html', title = title)

@app.route('/map')
def mapboxBike():
    return render_template(
        'map.html',
        title = title,
        MAPBOX_ACCESS_KEY = MAPBOX_ACCESS_KEY,
        bikeLocations = bikeLocations,
        tables = [bikes.to_html(classes='dataset1')],
        chargeTable = [chargeCount.to_html(classes='dataset2')],
        CdescribeTable = [chargeDesc.to_html(classes='dataset3')]
    )

if __name__ == '__main__':
    app.run()