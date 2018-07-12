from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask('__name__')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sixers1983@localhost/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(30), unique=True)
    
    def __init_(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

if __name__ == '__main__':
    db.create_all()
    app.run(
        host = os.environ.get('$C9_IP'),
        port = os.environ.get('$C9_PORT'),
        debug = True
    )