from flask_wtf import FlaskForm #Flask proper
from wtforms import StringField #Fields are strings
from wtforms import SubmitField #Submit Field
from wtforms.validators import DataRequired #need to input info

class myForm(FlaskForm):
    firstName = StringField('First Name', validators=[DataRequired()])
    lastName = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    find = StringField('Find', validators=[DataRequired()])
    socialMed = StringField('Your social media', validators=[DataRequired()])
    submit = SubmitField('Submit')