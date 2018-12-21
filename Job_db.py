from flask_sqlalchemy import SQLAlchemy
import os
from Cover_Generator import app

basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =\
os.environ.get('DATABASE_URL') or\
 'sqlite:///'+os.path.join(basedir,'jobinfo.db')
app.config['SQLALCHEMY_TRAC_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Job_Info(db.Model):
  id = db.Column(db.Integer,primary_key=True)
  company_name=db.Column(db.String(140), index=True)
  position_name=db.Column(db.String(140),index=True)
  referred=db.Column(db.Boolean(),index=True, default=False)
  referrer=db.Column(db.String(140),index=True)
  projects=db.Column(db.String(150),index=True)
  reason=db.Column(db.String(300),index=True)

  def __repr__(self):
    return '<Job_Info {} at {}>'.format(self.position_name, self.company_name)
