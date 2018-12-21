from flask import Flask, render_template
from JobForm import Job_InfoForm
from CSRF_config import Config


app=Flask(__name__)
app.config.from_object(Config)

@app.route('/job', methods=['GET','POST'])
def get_details():
  form=Job_InfoForm()
  if form.validate_on_submit():
    return redirect(url_for('generate_cover'))

  return render_template('job_info.html',form=form)

@app.route('/cover_letter')
def generate_cover():
	return render_template('cover.html',
		CompanyName='A Company',
		JobName='This Job',
		Contact='Person',
		Referred=True,
		Referral='Name',
    Projects=[{'name':'Project1','tech':'Python, Django, Java'},
              {'name':'Project2','tech':'Javascript, HTML'}],
		Reason='I want to work for this company'
    )

if __name__=='__main__':
	app.run(debug=True)
