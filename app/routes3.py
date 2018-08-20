from flask import render_template
from app import app

@app.route('/3')
@app.route('/index3')
def index3():
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
    return render_template('index3.html', title='Home', user=user, posts=posts)
