from flask import Flask
from app.routes import routes , socketio
from app.database import init_app

def create_app():
    app = Flask(__name__)
    init_app(app)
    app.register_blueprint(routes)
    socketio.init_app(app)
    return app
