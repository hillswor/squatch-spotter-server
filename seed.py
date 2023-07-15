from faker import Faker
from random import choice

from models import User, Location, Sighting, Comment
from extensions import db
from app import app

fake = Faker()


def clear_data():
    with app.app_context():
        db.session.query(User).delete()
        db.session.query(Location).delete()
        db.session.query(Sighting).delete()
        db.session.query(Comment).delete()
        db.session.commit()


def seed_db(num_users=10, num_locations=5, num_sightings=20, num_comments=50):
    with app.app_context():
        for _ in range(num_users):
            user = User(
                email=fake.unique.email(),
            )
            user.set_password("abc123")
            db.session.add(user)

        db.session.commit()

        # Get all users
        users = User.query.all()

        # Seed locations
        for _ in range(num_locations):
            location = Location(
                name=fake.city(),
                state=fake.state_abbr(),
                description=fake.text(max_nb_chars=200),
            )
            db.session.add(location)

        db.session.commit()

        # Get all locations
        locations = Location.query.all()

        # Seed sightings
        for _ in range(num_sightings):
            sighting = Sighting(
                user_id=choice(users).id,
                location_id=choice(locations).id,
                sighting_date=fake.date_this_year(),
                sighting_time=fake.time_object(),
                description=fake.text(max_nb_chars=1000),
                created_at=fake.date_time_this_year(),
                updated_at=fake.date_time_this_year(),
            )
            db.session.add(sighting)

        db.session.commit()

        # Get all sightings
        sightings = Sighting.query.all()

        # Seed comments
        for _ in range(num_comments):
            comment = Comment(
                user_id=choice(users).id,
                sighting_id=choice(sightings).id,
                comment_text=fake.text(max_nb_chars=500),
                created_at=fake.date_time_this_year(),
                updated_at=fake.date_time_this_year(),
            )
            db.session.add(comment)

        db.session.commit()


# Call the functions
clear_data()
seed_db()
