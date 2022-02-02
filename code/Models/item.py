from db import db
import warnings

class ItemModel(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name': self.name, 'price': self.price}
    
    def get_price(self):
        return self.price

    @classmethod
    def find_by_id(cls, id):
        if isinstance(id, int):
            return cls.query.filter_by(id=id).first()
        warnings.warn('Type Error for argument')
        return None

    @classmethod
    def find_by_name(cls, name):
        if isinstance(name, str):
            return cls.query.filter_by(name=name).first()
        warnings.warn('Type Error for argument')
        return None
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()