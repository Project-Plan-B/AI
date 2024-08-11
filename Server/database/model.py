from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Alert(db.Model):
    __tablename__ = 'alert'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(300), nullable=False)
    writing = db.Column(db.DateTime, default=datetime.now())


class Room(db.Model):
    __tablename__ = 'room'
    id = db.Column(db.Integer, primary_key=True)
    floor = db.Column(db.Integer, nullable=True)
    name = db.Column(db.String(30), nullable=True)
    confusion = db.Column(db.Integer, nullable=True)
