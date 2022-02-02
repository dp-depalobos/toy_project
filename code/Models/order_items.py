import warnings
from db import db
from Models.item import ItemModel
from Models.promotion import PromotionModel

class OrderItemModel(db.Model):
    __tablename__ = 'order-items'
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    promotion_id = db.Column(db.Integer, db.ForeignKey('promotions.id'))
    price = db.Column(db.Integer)

    items = db.relationship('ItemModel')
    promotions = db.relationship('PromotionModel')

    def __init__(self, id, quantity, item_id, promotion_id = 0):
        self.id = id
        self.quantity = quantity
        self.item_id = item_id
        self.promotion_id = promotion_id
        self.price = OrderItemModel.calculate(self.item_id,
                                              self.promotion_id,
                                              self.quantity)

    def json(self):
        return {'quantity': self.quantity,
                'item_id': self.item_id,
                'promotion_id': self.promotion_id,
                'price': self.price}

    def calculate(self):
        item = ItemModel.find_by_id(self.item_id)
        promotion = PromotionModel.find_by_id(self.promotion_id)
        if item & promotion:
            return self.quantity * item.get_price() \
                * (100 - promotion.get_discount()) / 100
        warnings.warn('item or promotion not found')
        return None

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()