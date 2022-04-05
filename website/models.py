from . import db
from flask_login import UserMixin



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    Name = db.Column(db.String(50))

class Registration(db.Model): 
    Registration_ID = db.Column(db.Integer, primary_key=True)
    Reg_Name = db.Column(db.String(50))
    Email = db.Column(db.String(50), unique=True)
    Phone_Number = db.Column(db.String(10))
    Secondary_Number = db.Column(db.String(10))
    College_Name = db.Column(db.String(100))
    University_Name = db.Column(db.String(100))
    Branch = db.Column(db.String(100))
    Pointer = db.Column(db.Numeric(4,2))
    Sem_Year = db.Column(db.String(100))
    ATKT = db.Column(db.String(100))
    Experience = db.Column(db.String(50))
    City = db.Column(db.String(50))
    Selected_track = db.Column(db.String(100))
