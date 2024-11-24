from flask import Blueprint, render_template
from flask_socketio import SocketIO, emit
from app.models import Class
from datetime import datetime

routes = Blueprint('routes', __name__)
socketio = SocketIO(cors_allowed_origins="*")

@routes.route("/")
def index():
    return render_template("index.html")

@socketio.on("connect")
def handle_connect():
    emit_classes()

def emit_classes():
    today = datetime.now().strftime('%A')
    print(today)
    classes = Class.query.filter_by(day=today).all()
    print(classes)
    now = datetime.now().time()
    print(now)

    ongoing_class = next((c for c in classes if c.start_time <= now < c.end_time), None)

    data = {
        "today_classes": [{"subject": c.subject, "teacher": c.teacher, "room": c.room, "start_time": str(c.start_time), "end_time": str(c.end_time)} for c in classes],
        "current_class": {
            "subject": ongoing_class.subject,
            "teacher": ongoing_class.teacher,
            "room": ongoing_class.room,
            "start_time": str(ongoing_class.start_time),
            "end_time": str(ongoing_class.end_time)
        } if ongoing_class else {"message": "No ongoing class"}
    }

    emit("class_data", data)
