from flask import Flask, render_template
from data import bikes, chargeCount, chargeDesc
import pandas as pd
from features import bikeLocations #the features data...
from bokeh.plotting import figure
from bokeh.embed import components
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
    #chart
    charges = ["Low Level", "Medium Level", "High Level"]
    plot = figure(plot_width=400, plot_height=400,
        title="Bar Chart of Charge Level of Open Jump Bikes",
        x_range=charges, tools="hover")
    plot.vbar(x=charges, width = 0.5, bottom = 0,
        top=[chargeCount["Low Charge"],chargeCount["Medium Charge"] ,chargeCount["High Charge"]],
        color="crimson")
    #chart
    script, div = components(plot)
    return render_template(
        'map.html',
        title = title,
        MAPBOX_ACCESS_KEY = MAPBOX_ACCESS_KEY,
        bikeLocations = bikeLocations,
        tables = [bikes.to_html(classes='dataset1')],
        chargeTable = [chargeCount.to_html(classes='dataset2')],
        CdescribeTable = [chargeDesc.to_html(classes='dataset3')],
        the_div=div, the_script=script
    )

if __name__ == '__main__':
    app.run()
