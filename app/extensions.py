"""
Extensions module

Each extension is initialized when app is created.
"""

from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO
from flask_pymongo import PyMongo


from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from apscheduler.schedulers.background import BackgroundScheduler
from flask_firebase_admin import FirebaseAdmin
# from firebase_admin import credentials,auth


db = SQLAlchemy()
mongo = PyMongo()

bcrypt = Bcrypt()
migrate = Migrate()
cors = CORS()
scheduler = BackgroundScheduler()
firebase = FirebaseAdmin() 
jwt = JWTManager()
ma = Marshmallow()
socketio = SocketIO()


