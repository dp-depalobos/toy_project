from flask_restful import Resource, reqparse
from Models.promotion import PromotionModel

class Promotion(Resource): 
    parser = reqparse.RequestParser()
    parser.add_argument('discount',
                        type=int,
                        required=True,
                        help='discount cannot be empty')

    def get(self, name):
        promotion = PromotionModel.find_by_name(name)
        if promotion:
            return promotion.json()
        return {'message': 'promotion not found'}, 404
    
    def post(self, name):
        if PromotionModel.find_by_name(name):
            return {'message': 'promotion already exists'}, 404
    
        data = Promotion.parser.parse_args()
        promotion = PromotionModel(name, data['discount'])

        try:
            promotion.save_to_db()
        except:
            return {'message': 'internal error occured'}, 500
        return promotion.json(), 201

    def put(self, name):
        data = Promotion.parser.parse_args()
        promotion = PromotionModel.find_by_name(name)

        if promotion is None:
            promotion = PromotionModel(name, data['discount'])
        else:
            promotion.discount = data['discount']
        
        promotion.save_to_db()
        return promotion.json()
    
    def delete(self, name):
        item = PromotionModel.find_by_name(name)
        if item:
            item.delete_from_db()
        
        return {'message': 'promotion deleted'}


class Promotions(Resource):
    def get(self):
        return {"promotions": [promotion.json() for promotion in PromotionModel.query.all()]}