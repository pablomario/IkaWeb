from flask import Blueprint, request, render_template

signup_bp = Blueprint('signup_bp', __name__)


@signup_bp.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

    return render_template('pages/signup/register.html')


@signup_bp.route('/confirmation')
def signup_confirm():
    return render_template('pages/signup/confirm.html')
