from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable=False,unique=True)
    password = db.Column(db.String, nullable=False)

class participants(db.Model):
    __tablename__ = "participants"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    college = db.Column(db.String, nullable=False)
    mobile = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    e_id = db.Column(db.Integer, db.ForeignKey("events.id"), nullable=False)

class events(db.Model):
    __tablename__="events"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable=False)
