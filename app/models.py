from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

class User(db.Model):
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(225))
    email = db.Column(db.String(225), unique = True, index = True)
    pass_secure = db.Column(db.String(225))
    pitches = db.relationship('Pitch', backref = 'pitch', lazy = "dynamic")


    @property
    def password(self):
        raise AttributeError("You cannot read the password attribute")

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    def __repr__(self):
        return f'User {self.username}'

@@ -20,4 +43,5 @@ class Pitch(db.Model):
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def __repr__(self):
        return f'User {self.username}' 
        return f'User {self.username}'


