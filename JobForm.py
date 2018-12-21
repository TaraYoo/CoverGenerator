from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, \
SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired
from Job_db import db, Job_Info

class Job_InfoForm(FlaskForm):
  company_name=StringField('Company Name',\
    validators=[DataRequired()])
  position_name=StringField('Position Name',\
    validators=[DataRequired()])
  referred=BooleanField('Is this through a referral?')
  referrer=StringField('Referrer Name')
  projects=SelectField('Select Project',\
    choices=[('Project1','Project1'),
              ('Project2','Project2')])
  reason=TextAreaField('Why this company?')
  submit=SubmitField('Submit')

  def initialize():
    db.create_all()

  def create_job():
    Job=Job_Info(company_name, position_name, referred, referrer,\
      projects, reason)
    db.session.add(Job)
    db.session.commit()


