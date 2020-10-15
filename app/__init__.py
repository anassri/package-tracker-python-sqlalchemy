from flask import Flask
from .config import Config
from .routes import packages
from flask_migrate import Migrate
from .models import db

app = Flask(__name__)

app.config.from_object(Config)
app.register_blueprint(packages.bp)
db.init_app(app)
migrate = Migrate(app, db)
