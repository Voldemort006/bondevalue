from db import db

class Seller(db.Model):
    __tablename__ = 'sellers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Integer)
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
       
    def json(self): 
        return {'name': self.name, 'price': self.price}
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    