from flask import render_template, request, redirect, url_for, flash #Import request from Flask
from app import app
from app.form import myForm #Import the form
from app.shopList import shops #Import the list
from app.mail import sendSuggestion

# Remeber to start env server when doing this
@app.route('/') #Route for the about page
@app.route('/about') 
def about():
    return render_template('index.html', title='DC Coffee')

@app.route('/coffee') #Route for the actual list, need to create JSON to serve the shops
def coffee():
    shops 
    return render_template('coffee.html', title='DC Coffee' ,shops=shops)   #Add the JSON

@app.route('/suggestions', methods=['GET', 'POST']) #Add the form here
def suggest():
    form = myForm()
    if form.validate_on_submit():
        print(flash("{},{},{},{},{}".format(
            form.firstName.data, form.lastName.data, form.email.data,
            form.find.data, form.socialMed.data)))
        print(form.firstName.data, form.lastName.data, form.email.data,form.find.data, form.socialMed.data)
        #data is being received, need to direct it...
        sendSuggestion(form)
        #Do it above...
        return redirect(url_for('coffee'))
    return render_template('suggest.html', title='DC Coffee', form = form)
    