from flask_restful import Resource, reqparse
from Models.order_items import OrderItemModel

class OrderItem(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('quantity',
                        type=float,
                        required=True,
                        help='quantity cannot be empty')
    parser.add_argument('item_id',
                        type=float,
                        required=True,
                        help='item_id cannot be empty')
    parser.add_argument('promotion_id',
                        type=float,
                        required=False)

    def get(self, id):
        orderItem = OrderItemModel.find_by_id(id)
        if orderItem:
            return orderItem.json()
        return {'message': 'orderItem not found'}, 404
    
    def post(self, id):
        data = OrderItem.parser.parse_args()
        orderItem = OrderItemModel(id, **data)

        try:
            orderItem.save_to_db()
        except:
            return {'message': 'internal error occured'}, 500
        return orderItem.json(), 201

    def put(self, id):
        data = OrderItem.parser.parse_args()
        orderItem = OrderItemModel.find_by_id(id)

        if orderItem is None:
            orderItem = OrderItemModel(id, **data)
        else:
            orderItem.quantity = data['quantity']
            orderItem.price = OrderItemModel.calculate(**data)
        
        orderItem.save_to_db()
        return orderItem.json()
    
    def delete(self, id):
        orderItem = OrderItemModel.find_by_id(id)
        if orderItem:
            orderItem.delete_from_db()
        return {'message': 'OrderItem deleted'}

