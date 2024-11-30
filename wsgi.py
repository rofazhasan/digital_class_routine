from app import create_app
from app.routes import socketio
app = create_app()

if __name__ == "__main__":
    app.run()
