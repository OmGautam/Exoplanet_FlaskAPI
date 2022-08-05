from flask import Flask,jsonify,request
from data import data

app = Flask(__name__)
@app.route("/")

def index():
    return jsonify({
        "data":data,
        "message":"Success!"
    }), 200

@app.route("/planets")

def planets():
    name = request.args.get("names")
    planet_data = next(item for item in data if item["names"] == name)
    return jsonify({
        "data":planet_data,
        "message":"Success!"
    }), 200

if __name__ == "__main__":
    app.run()

