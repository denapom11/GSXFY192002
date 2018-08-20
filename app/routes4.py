from flask import render_template
from app import app

@app.route('/4')
@app.route('/index4')
def index4():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Mountainview!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'GSX is so cool!'
        }
    ]
    return render_template('index4.html', title='Home', user=user, posts=posts)
