from flask import Flask
from flask_caching import Cache
from app.config.database import *
from flask_marshmallow import Marshmallow

ma = Marshmallow()
cache = Cache()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)
    cache.init_app(app, config={'CACHE_TYPE': 'RedisCache','CACHE_DEFAULT_TIMEOUT':300, 'CACHE_REDIS_HOST':'redis.um.localhost','CACHE_REDIS_PORT':'6379','CACHE_REDIS_DB':'0', 'CACHE_REDIS_PASSWORD':'santino1234', 'CACHE_KEY_PREFIX':'armeria-client_'})
    
    
    from app.controllers import client
    app.register_blueprint(client, url_prefix='/api/v1')
    return app



