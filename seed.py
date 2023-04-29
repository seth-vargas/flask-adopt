from app import app
from models import Pet, db

db.drop_all()
db.create_all()

p1 = Pet(name="Woofy", species="dog", photo_url="https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fcf-images.us-east-1.prod.boltdns.net%2Fv1%2Fstatic%2F6157254766001%2Fbb4021ff-c791-467b-8510-789c7295ca5e%2F15d7b825-6259-4ae9-988c-1b1f7174b6e1%2F1280x720%2Fmatch%2Fimage.jpg")

p2 = Pet(name="Porchetta", species="porqupine", photo_url="https://animals.sandiegozoo.org/sites/default/files/2016-09/animals_hero_porcupine.jpg", age=1, notes="This is a porqupine!")

p3 = Pet(name="Snargle", species="dog", photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4OPBibmFcA0jgIPbN-6wPiy37vbmfQN7SAg&usqp=CAU", available=False)

p4 = Pet(name="Missing", species="unknown", photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvG59zelJvr0cdxANOTgYmpi3XSMXpQMVZYqnMjTh3XQ&s", available=False)

db.session.add_all([p1, p2, p3, p4])
db.session.commit()
