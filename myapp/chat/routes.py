from email import message
from flask import Blueprint
from numpy import broadcast
from myapp import socketio
from flask_login import current_user
from flask_socketio import emit
from myapp.models import History
from myapp import db


chat = Blueprint('chat', __name__)

@chat.route("/chat")
def mychat():
    return "chat"

@socketio.on('login_message')
def handle_message(data):
    print(data)

@socketio.on("global_message")
def global_message(json):
    history = History(user=current_user.username, message=json)
    db.session.add(history)
    db.session.commit()
    msg = {"username": current_user.username, "msg": json}
    emit("global_message", msg, broadcast=True, )
