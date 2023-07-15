from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from flask_bcrypt import Bcrypt
import re
from datetime import datetime

from extensions import db

bcrypt = Bcrypt()


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(length=254), unique=True, nullable=False)
    password = db.Column(db.String(length=254))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    sightings = db.relationship("Sighting", backref="user", lazy=True)
    comments = db.relationship("Comment", backref="user", lazy=True)
    locations = association_proxy("sightings", "location")

    @validates("email")
    def validate_email(self, key, email):
        assert (
            re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email)
            is not None
        ), "Invalid email address"
        return email

    def set_password(self, password):
        hashed_password = bcrypt.generate_password_hash(password)
        self.password = hashed_password.decode("utf-8")

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
        }

    def __repr__(self):
        return f"<User email={self.email}>"


class Location(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(254))
    state = db.Column(db.String(2))
    description = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    sightings = db.relationship("Sighting", backref="location", lazy=True)
    users = association_proxy("sightings", "user")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "state": self.state,
            "description": self.description,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    def __repr__(self):
        return f"<Location name={self.name} state={self.state} description={self.description}>"


class Sighting(db.Model):
    __tablename__ = "sightings"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"))
    sighting_date = db.Column(db.Date)
    sighting_time = db.Column(db.Time)
    description = db.Column(db.String(1500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    comments = db.relationship("Comment", backref="sighting", lazy=True)

    def to_dict(self):
        location = Location.query.get(self.location_id)
        return {
            "id": self.id,
            "user_id": self.user_id,
            "location_id": self.location_id,
            "location": location.to_dict() if location else None,
            "sighting_date": self.sighting_date.isoformat(),
            "sighting_time": self.sighting_time.isoformat(),
            "description": self.description,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "comments": [comment.to_dict() for comment in self.comments],
            "user": self.user.to_dict() if self.user else None,  # Include the user data
        }

    def __repr__(self):
        return f"<Sighting id={self.id} user_id={self.user_id} location_id={self.location_id} sighting_date={self.sighting_date}>"


class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    sighting_id = db.Column(db.Integer, db.ForeignKey("sightings.id"))
    comment_text = db.Column(db.String(1000))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "sighting_id": self.sighting_id,
            "comment_text": self.comment_text,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "user": self.user.to_dict() if self.user else None,  # Include the user data
        }

    def __repr__(self):
        return f"<Comment id={self.id} user_id={self.user_id} sighting_id={self.sighting_id}>"
