"""Database models."""
from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    """Model for user accounts."""

    __tablename__ = 'user'

    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(100),
                     nullable=False,
                     unique=False)
    email = db.Column(db.String(40),
                      unique=True,
                      nullable=False)
    password = db.Column(db.String(200),
                         primary_key=False,
                         unique=False,
                         nullable=False)
    birthday = db.Column(db.DateTime(60),
                        index=False,
                        unique=False,
                        nullable=False)
    gender = db.Column(db.DateTime(60),
                        nullable=False,
                        unique=False
                        )
    
    
    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)




class Profile(UserMixin, db.Model):
    """Model for user profile."""
    
    __tablename__ = 'user_profile'

    email = db.Column(db.String(40),
                      unique=True,
                      nullable=False,
                      primary_key=True)
    
    preference_gender = db.Column(db.String(6),
                                    unique=False,
                                    nullable=False)
    
    interests = db.Column(db.String(100),
                         unique=False,
                        nullable=True)
    
    client_type = db.Column(db.String(5),
                            unique=False,
                            nullable=False)
                            
    def __repr__(self):
        return 'User {}'.format(self.username)
