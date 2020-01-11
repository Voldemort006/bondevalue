from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, RadioField
from wtforms.validators import DataRequired


class InfoForm(FlaskForm): 
    name = StringField("Name", validators=[DataRequired()])
    customer_type = RadioField("Are you a buyer or seller?", choices=[('buyer','Buyer'),('seller','Seller')], default="buyer")
    price = IntegerField("Price(Should be greater than 0)", validators=[DataRequired()])
    submit = SubmitField("Submit")