from flask import Flask
from flask_restful import Api

from db import db
from Resources.item import Item, Items
from Resources.promotion import Promotion, Promotions
from Resources.order_items import OrderItem

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://chocosoup:chocosoup@localhost:5432/db'

@app.before_first_request
def create_tables():
    db.create_all()

api = Api(app)
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(Promotion, '/promotion/<string:name>')
api.add_resource(Promotions, '/promotions')
api.add_resource(OrderItem, '/order-item/<int:id>')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)