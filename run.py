from app import create_app
from app.routes import socketio

app = create_app()
socketio = SocketIO(app, cors_allowed_origins="*")  # or specify the correct origin




if __name__ == "__main__":
    socketio.run(app, debug=True)
