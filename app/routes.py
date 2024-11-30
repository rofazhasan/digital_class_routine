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
    classes_today = Class.query.filter_by(day=today).all()
    now = datetime.now().time()
    
    ongoing_class = next((c for c in classes_today if c.start_time <= now < c.end_time), None)

    weekly_classes = []
    days = ["Saturday", "Sunday","Monday", "Tuesday", "Wednesday"]
    
    for day in days:
        day_classes = Class.query.filter_by(day=day).all()
        weekly_classes.append({
            "day": day,
            "classes": [{"subject": c.subject, "teacher": c.teacher, "start_time": str(c.start_time), "end_time": str(c.end_time)} for c in day_classes]
        })

    data = {
        "today_classes": [{"subject": c.subject, "teacher": c.teacher, "room": c.room, "start_time": str(datetime.strptime(str(c.start_time) , "%H:%M:%S").strftime("%I:%M:%S %p")), "end_time": str(datetime.strptime(str(c.end_time) , "%H:%M:%S").strftime("%I:%M:%S %p"))} for c in classes],
        "current_class": {
            "subject": ongoing_class.subject,
            "teacher": ongoing_class.teacher,
            "room": ongoing_class.room,
            "start_time": str(ongoing_class.start_time),
            "end_time": str(ongoing_class.end_time)
        } if ongoing_class else {"message": "No ongoing class"}
    },
        "weekly_classes": weekly_classes
    }

    emit("class_data", data)
