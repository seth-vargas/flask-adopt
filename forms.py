from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    name = StringField("Enter name", validators=[InputRequired(message="Pet name cannot be blank")])
    species = SelectField("Enter species", validators=[InputRequired(message="Pet species cannot be blank")], choices=[("dog", "Dog"), ("cat", "Cat"), ("porcupine", "Porcupine")])
    photo_url = StringField("Enter URL for photo", validators=[URL(), Optional()])
    age = IntegerField("Enter age", validators=[Optional(), NumberRange(min=0, max=30, message=f"The input must be between 0 and 30.")])
    notes = StringField("Enter notes about pet", validators=[Optional()])

class EditPetForm(FlaskForm):
    photo_url = StringField("Enter URL for photo", validators=[URL(), Optional()])
    notes = StringField("Enter notes about pet", validators=[Optional()])
    available = BooleanField("Is this pet avaliable")
