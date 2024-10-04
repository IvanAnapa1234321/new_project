from flask import Flask, render_template, request
from models import User,db
app = Flask(__name__)
 

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['text']
        email = request.form['email']
        phone= request.form['phone'] 
        password=request.form['password']
        D=User(title=title,email=email,phone=phone,password=password)
        db.session.add(User)
        db.session.commit()
    else:  
        return render_template('base.html')


if __name__ == '__main__':
    app.run(debug=True)