from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
 
class User(db.Model):
    email = db.Column(db.String(300), nullable=False, unique=True)
    phone = db.Column(db.Integer, primary_key=True)
    password=db.Column(db.String(100),nullable=False, unique=True)
 
 

 

 

 
 
        
