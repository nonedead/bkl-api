from flask import Flask
from flask_restful import Api , Resource


app = Flask(__name__)
api = Api(app)


class Restrictions(Resource):
    def get(self):
        cargo_limit = 340000
        collateral_limit = 15000000000
        return {
            "message": "success",
            "data": 
            {
                "volume_limit": cargo_limit,
                "collateral_limit": collateral_limit
            }
        }, 200

api.add_resource(Restrictions , "/api/restrictions")