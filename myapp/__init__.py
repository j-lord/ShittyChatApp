from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from myapp.config import Config
from flask_socketio import SocketIO
from engineio.async_drivers import eventlet
import os
import sys

login_manager = LoginManager()
login_manager.login_view = "user.login"
login_manager.login_message = "Please login to access Dashboard"
login_manager.login_message_category = "warning"
template_folder = os.path.join(sys._MEIPASS, 'templates')
static_folder = os.path.join(sys._MEIPASS, 'static')
db = SQLAlchemy()
socketio = SocketIO( always_connect=True,
    logger=True,
    async_mode='eventlet',
    engineio_logger=True)

def create_app(debug=False):
    app = Flask(__name__,template_folder=template_folder, static_folder=static_folder)
    app.config.from_object(Config)

    app.debug = debug

    login_manager.init_app(app)
    db.init_app(app)
    socketio.init_app(app)

    from myapp.user.routes import user
    app.register_blueprint(user)

    from myapp.chat.routes import chat
    app.register_blueprint(chat)

    return app