from datetime import datetime

from flask import render_template, flash, redirect, url_for, request
from flask_babel import _
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app import ureg, get_locale, app, db
from app.enums.types import Type
from app.forms import LoginForm, RegistrationForm, EditProfileForm, AddCatForm, AddMeasureForm
from app.models import User, Cat, Measure


@app.get('/')
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    ureg.set_fmt_locale(get_locale())
    measures = current_user.cats.first().measures.all()
    form = AddCatForm()
    if form.validate_on_submit():
        cat = Cat(name=form.name.data, owner=current_user)
        db.session.add(cat)
        db.session.commit()
        flash('Congratulations, you have a new cat!')
    cats = current_user.cats.all()
    return render_template('index.html', title=_('Home'), cats=cats, form=form, measures=measures)


@app.route('/login', methods=['GET', 'POST'])
def login():
    ureg.set_fmt_locale(get_locale())
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title=_('Sign In'), form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/add_measure', methods=['GET', 'POST'])
@login_required
def add_measure():
    form = AddMeasureForm()
    choices = map(lambda t: (t.name, t.value), list(Type))
    form.type.choices = list(choices)
    if form.validate_on_submit():
        cat = current_user.cats.first()
        measure = Measure(type=form.type.data, cat=cat)
        db.session.add(measure)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('index'))
    return render_template('add_measure.html', title='Add Measure',
                           form=form)


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
