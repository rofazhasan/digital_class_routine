from flask import Blueprint, render_template
from flask_socketio import SocketIO, emit
from app.models import Class
from datetime import datetime
import pytz
routes = Blueprint('routes', __name__)
socketio = SocketIO(cors_allowed_origins="*")

@routes.route("/")
def index():
    return render_template("index.html")

@socketio.on("connect")
def handle_connect():
    emit_classes()

def emit_classes():
    tz=pytz.timezone('Asia/Dhaka')
    today = datetime.now(tz).strftime('%A')
    classes_today = Class.query.filter_by(day=today).order_by(Class.id).all()
    now = datetime.now(tz).time()
    
    # Find the ongoing class
    ongoing_class = next((c for c in classes_today if c.start_time <= now < c.end_time), None)

    # Prepare weekly class data
    weekly_classes = []
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]
    
    for day in days:
        day_classes = Class.query.filter_by(day=day).order_by(Class.id).all()
        weekly_classes.append({
            "day": day,
            "classes": [{"subject": c.subject, "teacher": c.teacher, "start_time": str(datetime.strptime(str(c.start_time), "%H:%M:%S").strftime("%I:%M %p")), "end_time": str(datetime.strptime(str(c.end_time), "%H:%M:%S").strftime("%I:%M %p"))} for c in day_classes]
        })

    # Prepare data payload for the frontend
    data = {
        "today_classes": [
            {
                "subject": c.subject,
                "teacher": c.teacher,
                "room": c.room,
                "start_time": datetime.strptime(str(c.start_time), "%H:%M:%S").strftime("%I:%M %p"),
                "end_time": datetime.strptime(str(c.end_time), "%H:%M:%S").strftime("%I:%M %p")
            } 
            for c in classes_today
        ],
        "current_class": {
            "subject": ongoing_class.subject,
            "teacher": ongoing_class.teacher,
            "room": ongoing_class.room,
            "start_time": datetime.strptime(str(ongoing_class.start_time), "%H:%M:%S").strftime("%I:%M %p"),
            "end_time": datetime.strptime(str(ongoing_class.end_time), "%H:%M:%S").strftime("%I:%M %p")
        } if ongoing_class else None,  # Return None if no class is ongoing
        "weekly_classes": weekly_classes
    }

    emit("class_data", data)
@routes.route("/weeklyschedule")
def weekly_schedule():
    return render_template("weeklyschedule.html")

@routes.route("/weeklyschedule/<day>")
def weekly_class(day):
    classes = Class.query.filter_by(day=day).order_by(Class.id).all()
    return render_template("day_classes.html", day=day, classes=classes)

