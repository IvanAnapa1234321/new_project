from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
 

@app.route('/', methods=['GET', 'POST'])
def index():
    title=''
    if request.method == 'POST':
        title = request.form['tegh1']
    return render_template('base.html',tegh1=title)

if __name__ == '__main__':
    app.run(debug=True)