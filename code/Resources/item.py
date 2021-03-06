from flask_restful import Resource, reqparse
from Models.item import ItemModel

class Item(Resource): 
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='price cannot be empty')

    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'item not found'}, 404
    
    def post(self, name):    
        if ItemModel.find_by_name(name):
            return {'message': 'item already exists'}, 404
    
        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'])

        try:
            item.save_to_db()
        except:
            return {'message': 'internal error occured'}, 500
        return item.json(), 201

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, data['price'])
        else:
            item.price = data['price']
        
        item.save_to_db()
        return item.json()
    
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': 'item deleted'}


class Items(Resource):
    def get(self):
        return {"items": [item.json() for item in ItemModel.query.all()]}