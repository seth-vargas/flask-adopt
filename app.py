from flask import Flask, render_template, redirect, flash
from models import connect_db, Pet, db, default
from forms import AddPetForm, EditPetForm
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///sb_adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secret"
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# debug = DebugToolbarExtension(app)

connect_db(app)


@app.errorhandler(404)
def not_found(error):
    """ Handles 404 errors """
    return render_template("404.html")

@app.route("/")
def list_pets():
    """ Lists all pets in two lists, one is pets that are available and the other is unavailable pets """
    available_pets = Pet.query.filter_by(available = True).order_by(Pet.name).all()
    unavailable_pets = Pet.query.filter_by(available = False).order_by(Pet.name).all()
    return render_template("pets.html", available_pets=available_pets, unavailable_pets=unavailable_pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """ Handles /add. If request is GET, render form template. If the request is POST, handle the form data """
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data if form.photo_url.data else default
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)

        db.session.add(new_pet)
        db.session.commit()
        
        flash(f"{new_pet.name} has been successfully added!", "success")
        return redirect("/")
    else:
        return render_template("add-pet-form.html", form=form)

@app.route("/<int:id>", methods=["GET", "POST"])
def edit_pet(id):
    """ Handles editing a pet. If request is GET, render form template. If the request is POST, handle the form data """
    form = EditPetForm()
    pet = Pet.query.get_or_404(id)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data if form.photo_url.data else pet.photo_url
        pet.notes = form.notes.data if form.notes.data else pet.notes
        pet.available = form.available.data

        db.session.add(pet)
        db.session.commit()

        flash(f"{pet.name} has been successfully updated!", "success")
        return redirect(f"/")
    else:
        return render_template("pet-info.html", form=form, pet=pet)
