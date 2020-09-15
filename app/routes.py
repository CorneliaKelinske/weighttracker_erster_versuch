from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Connie'}
    posts = [
        {
            'date' : {'month' : 'May', 'day': 3},
            'weight': 127
        },

        {
           'date' : {'month' : 'June', 'day': 3},
            'weight': 178 
        }

    ]
    return render_template('index.html', title="Home", user=user, posts=posts)