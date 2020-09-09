from flask import Flask , render_template
from flask_restful import Api , Resource
from werkzeug.utils import redirect


app = Flask(__name__)
api = Api(app)

@app.route("/")
def bkl_website():
    return redirect("https://gonekrabbing.supply/logistics/" , code=301)

@app.route("/api/docs")
def github():
    return redirect("https://github.com/nonedead/bkl-api" , code=301)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

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

if __name__=="__main__":
    app.run(debug=True)