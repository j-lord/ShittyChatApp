from myapp import db
from datetime import datetime
from myapp import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# create user table
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(70))
    joining_date = db.Column(db.DateTime, default=datetime.now)
    password = db.Column(db.String(400))
    is_Client = db.Column(db.String(400))

    def __repr__(self):
        return f"{self.username}, {self.email}"

# create table for chat history
class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(40))
    message = db.Column(db.String(400))
    is_Client_Message = db.Column(db.String(400))

    def __repr__(self):
        return f"{self.user}, {self.message}"
