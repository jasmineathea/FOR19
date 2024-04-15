from flask_wtf import FlaskForm
from wtforms import  SubmitField,  SelectField,  FloatField
from wtforms.validators import InputRequired

class BusForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Diesel', 'Diesel'), ('Electric', 'Electric'), ('Hybrid', 'Hybrid'), ('Hydrogen', 'Hydrogen')])
  submit = SubmitField('Submit')

class CarForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Gasoline', 'Gesoline'), ('Diesel', 'Diesel'), ('Electric','Electric'), ('Hybrid', 'Hybrid'), ('Hydrogen','Hydrogen')])
  submit = SubmitField('Submit')  

class PlaneForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Short-haul(Buisness)','Short-haul(Buisness)'),('Long-haul(Economy)','Long-haul(Economy)'),('Long-haul(First-class)','Long-haul(First-class)'),('International(Economy)', 'International(Economy)'),('International (Premium economy)','International (Premium economy)'),('International (Buisness)', 'International (Buisness)'),('International (First Class)','International (First Class)')])
  submit = SubmitField('Submit')
  
class FerryForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Regular', 'Regular'), ('High-speed', 'High-speed')])
  submit = SubmitField('Submit')  

class MotorbikeForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('≤125cc', '≤125cc'), ('125cc to 500cc', '125cc to 500cc'),('>500cc','>500cc')])
  submit = SubmitField('Submit')

class BicycleForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('No Fossil Fuel', 'No Fossil Fuel')])
  submit = SubmitField('Submit')  

class WalkForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('No Fossil Fuel', 'No Fossil Fuel')])
  submit = SubmitField('Submit')  
