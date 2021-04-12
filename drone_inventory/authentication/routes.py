from flask import Blueprint, render_template


auth = Blueprint('auth', __name__, template_folder = 'auth_templates')

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    return render_template('signup.html')

@auth.route('/signin', methods = ['GET', 'POST'])
def signin():
    return render_template('signin.html')