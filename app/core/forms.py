from flask_wtf import FlaskForm
from wtforms import StringField, RadioField
from wtforms.validators import DataRequired
from flask_babel import _


class AddCatForm(FlaskForm):
    name = StringField(_('Name'), validators=[DataRequired()])


class AddMeasureForm(FlaskForm):
    type = RadioField('Type', validators=[DataRequired()])
