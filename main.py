from myapp import create_app, socketio
# from myapp import db
# from myapp.models import History

app = create_app(debug=True)


if __name__=="__main__":
    # with app.app_context():
    #     db.create_all()
    socketio.run(app)