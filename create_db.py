from flask import Flask
from models import User,db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///qwerty.db'
db.init_app(app)

 
if __name__ == '__main__':
    with app.app_context():
        db.create_all()


user1 =User(email='hnjuaeiyr',
        password='IUCBNWeicbwCWicniwCNIJNICW',
        phone=1)
        
db.session.add_all(User)
db.session.commit()
 
 
 