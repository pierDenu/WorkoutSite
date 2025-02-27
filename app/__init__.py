from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    bootstrap.init_app(app)
    migrate = Migrate(app, db)

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.workouts import workouts_bp
    app.register_blueprint(workouts_bp)

    from app.plans import plans_bp
    app.register_blueprint(plans_bp)

    return app