from flask import render_template
from app import app

@app.route('/2')
@app.route('/index2')
def index2():
    user = {'username': 'Miguel'}
    return render_template('index2.html', title='Home', user=user)
