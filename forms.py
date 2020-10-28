from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField



class AddForm(FlaskForm):
	name= StringField('Name of the puppy: ')
	submit= SubmitField('Add Puppy')


class DelForm(FlaskForm):
	id= IntegerField('ID number of puppy to be removed')
	submit= SubmitField('Remove Puppy')

class AddFormOwner(FlaskForm):
	name=StringField('Name of Owner')
	id=IntegerField('ID of the puppy')
	submit=SubmitField('Add Owner')



