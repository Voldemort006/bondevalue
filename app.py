import os

from flask import Flask, flash, render_template, session, redirect, url_for
from wtforms.validators import DataRequired

from models.buyer import Buyer
from models.seller import Seller
from match_customers import MatchCustomers
from form import InfoForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'siddharth'


@app.before_first_request
def create_tables(): 
    from db import db
    db.init_app(app)
    db.create_all

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InfoForm() 
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['customer_type'] = form.customer_type.data
        session['price'] = form.price.data

        if(form.customer_type.data == 'buyer'):
            buyer = Buyer(form.name.data, form.price.data)
            buyer.save_to_db()
        else:
            seller = Seller(form.name.data, form.price.data)
            seller.save_to_db()  
        
        flash("Data Submitted Succesfully")
        
        return redirect(url_for('matches'))

    return render_template('form.html', form=form)


@app.route('/matches')
def matches(): 
     buyer_data = Buyer.query.all()
     seller_data = Seller.query.all()
     matched_and_unmatched_customers = MatchCustomers.findmatch(buyer_data, seller_data)   
     return render_template('matches.html', matched = matched_and_unmatched_customers.get('matched',{}), 
     unmatched_buyers = matched_and_unmatched_customers.get('unmatched_buyers',[]),
     unmatched_sellers = matched_and_unmatched_customers.get('unmatched_sellers',[]))


if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
