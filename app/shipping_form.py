#pylint: disable=import-error
from flask_wtf import FlaskForm
from wtforms.fields import (StringField, SelectField, BooleanField, SubmitField)
from wtforms.validators import DataRequired

class ShippingForm(FlaskForm):
    sender_name = StringField('Sender name', validators=[DataRequired()])
    recipient_name = StringField('Recipient name', validators=[DataRequired()])
    origin = SelectField('Origin', validators=[DataRequired()])
    destination = SelectField('Destination', validators=[DataRequired()])
    express = BooleanField('Express shipping')
    submit = SubmitField('Send')
    cancel = SubmitField('Cancel') 