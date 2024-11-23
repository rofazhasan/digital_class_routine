from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv


db = SQLAlchemy()

def init_app(app):
    app.config['SQLALCHEMY_DATABASE_URI']= "postgresql://classdb_ikhg_user:i0J5MvmIlZzQpVInUrNqeYPVNKUUEy1I@dpg-ct070rd6l47c7386hcb0-a.oregon-postgres.render.com/classdb_ikhg"
    db.init_app(app)
