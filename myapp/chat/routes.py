from email import message
from flask import Blueprint
from numpy import broadcast
from myapp import socketio
from flask_login import current_user
from flask_socketio import emit, join_room, leave_room
from myapp.models import History
from myapp import db


chat = Blueprint("chat", __name__)

@chat.route("/chat")
def mychat():
    return "chat"

@socketio.on("login_message")
def handle_message(data):
    print(data)

@socketio.on("global_message")
def global_message(json):
    history = History(user=current_user.username, message=json)
    db.session.add(history)
    db.session.commit()
    msg = {"username": current_user.username, "msg": json}
    emit("global_message", msg, broadcast=True, )


# This part still isn't working why?
#  Add functionality so users know when new users join and leave chat 
@socketio.on("join", namespace="/chat")
def join(message):
    room = db.session.get("room")
    join_room(room)
    msg = {"msg": message["username"] + " has joined the room."}
    emit("join", msg, broadcast=True, )

socketio.on("left", namespace="/chat")
def left(message):
    room = db.session.get("room")
    username = db.session.get("username")
    leave_room(room)
    db.session.clear()
    emit("status", {"msg": username + " has left the room."}, room=room)

# Where will this message be posted