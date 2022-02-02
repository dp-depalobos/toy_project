from db import db

class PromotionModel(db.Model):
    __tablename__ = 'promotions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    discount = db.Column(db.Integer)

    def __init__(self, name, discount):
        self.name = name
        self.discount = discount

    def json(self):
        return {'name': self.name, 'discount': self.discount}

    def get_discount(self):
        return self.discount

    @classmethod
    def find_by_name(cls, name):
        if isinstance(name, str):
            return cls.query.filter_by(name=name).first()
        return None

    @classmethod
    def find_by_id(cls, id):
        if isinstance(id, int):
            return cls.query.filter_by(id=id).first()
        return None

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()