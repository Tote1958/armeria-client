from flask import Flask
from app.config.database import *
def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    
    #from app.resources import client
    #app.register_blueprint(client, url_prefix='/api/v1')
    return app



