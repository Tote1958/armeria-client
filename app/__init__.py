from flask import Flask
from flask_caching import Cache
from app.config.database import *
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

from app.config import database
ma = Marshmallow()
db = SQLAlchemy()
migrate = Migrate()
cache = Cache()

def create_app():
    config_name = os.getenv('FLASK_ENV')
    app = Flask(__name__)

    #app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    f = config.factory(config_name if config_name else 'development')
    app.config.from_object(f)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app, config={'CACHE_TYPE': 'RedisCache'
                                ,'CACHE_DEFAULT_TIMEOUT':300, 'CACHE_REDIS_HOST':'localhost' #nombre del contenedor
                                ,'CACHE_REDIS_PORT':'6379','CACHE_REDIS_DB':'0',
                                'CACHE_REDIS_PASSWORD':'santino1234',
                                'CACHE_KEY_PREFIX':'armeria-client_'})
    
    
    from app.controllers import client
    app.register_blueprint(client, url_prefix='/api/v1')

    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app



