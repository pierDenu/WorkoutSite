from flask import Flask
from flask_migrate import Migrate

from app.extensions import db

from app.main import bp as main_bp
from app.plans import plans_bp
from app.workouts import workouts_bp
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    migrate = Migrate(app, db)

    # Register blueprints here
    app.register_blueprint(main_bp)
    app.register_blueprint(workouts_bp)
    app.register_blueprint(plans_bp)

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app