from flask import flash, render_template, url_for, redirect
from flask_login import login_required, current_user
from flask_babel import _

from app import db
from app.auth import bp
from app.core.enums import Type
from app.core.forms import AddCatForm, AddMeasureForm
from app.models import Cat, Measure


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    cat = current_user.cats.first()
    measures = ()
    if cat:
        measures = current_user.cats.first().measures.all()
    form = AddCatForm()
    if form.validate_on_submit():
        cat = Cat(name=form.name.data, owner=current_user)
        db.session.add(cat)
        db.session.commit()
        flash('Congratulations, you have a new cat!')
    cats = current_user.cats.all()
    return render_template('core/index.html', title=_('Home'), cats=cats, form=form, measures=measures)


@bp.route('/add_measure', methods=['GET', 'POST'])
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
        return redirect(url_for('auth.index'))
    return render_template('core/add_measure.html', title='Add Measure',
                           form=form)
