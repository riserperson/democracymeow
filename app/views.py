from flask import g, render_template, redirect, request, session, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from app import app
from app.forms import Login

'''
@app.before_request
def before_request():
    if request.url.startswith('http://'):
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)
'''

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = Login()
    if form.validate_on_submit():
        if form.data['pw'] == 'Oprah2020':
            session['logged_in'] = True
            return redirect(url_for('episodes'))
    return render_template('index.html', form=form)    

@app.route('/episodes')
def episodes():
    if 'logged_in' in session.keys():
        if session['logged_in'] == True:
            return render_template('episodes.html')
    else:
        return redirect(url_for('index'))

