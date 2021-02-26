"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Personaje
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/people', methods=['GET'])
def handle_hello():
    people_query = Personaje.query.all()
    all_people = list(map(lambda x: x.serialize(), people_query))
    # if user_query is None:
    #     return "Not found", 404
    
    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "personajes": all_people
        
    }

    return jsonify(response_body), 200

@app.route('/people/<int:id>', methods=['GET'])
def get_personaje(id):
    personaje = Personaje.query.get(id).serialize()
    # if user_query is None:
    #     return "Not found", 404
    print(personaje)
    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "personaje": personaje
        
    }

    return jsonify(response_body), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
