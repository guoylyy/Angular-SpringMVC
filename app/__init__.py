from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='')
app.config.from_object('config')
db = SQLAlchemy(app)

def create_test_app():
	app.config.from_object('test_config')
	db  = SQLAlchemy(app)
	return app

from app.models import news
from app.models import user
from app.models import message
from app.models import conference
from app.models import pushs
from app.models import movie
from app.models import inform
from app.routes import index

from app.routes import informs
from app.routes import news
from app.routes import users
from app.routes import messages
from app.routes import conferences
from app.routes import pushs
from app.routes import image
from app.routes import movies
