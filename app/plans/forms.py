from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, SubmitField
from wtforms.validators import DataRequired

class PlanNameForm(FlaskForm):
    plan_name = StringField('Workout Plan Name', validators=[DataRequired()])
    submit = SubmitField('Submit')