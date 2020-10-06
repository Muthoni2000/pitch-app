from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(225))
    email = db.Column(db.String(225), unique = True, index = True)
    pass_secure = db.Column(db.String(225))
    pitches = db.relationship('Pitch', backref = 'pitch', lazy = "dynamic")
    name = db.Column(db.String(225))
    email = db.Column(db.String)
    bio = db.Column(db.String)
    profile_pic  = db.Column(db.String)

    pitches = db.relationship('Pitch', backref = 'name', lazy = "dynamic")
    comments = db.relationship('Comment', backref = 'name', lazy = "dynamic")



    def save_user(self):
        db.session.add(self)
        db.session.commit()



    @classmethod
    def get_users(cls, id):
        users_list = User.query.filter_by(user_id = id)
        return users_list


    @property
@@ -18,30 +34,57 @@ def password(self):

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)
        self.pass_code = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
        return check_password_hash(self.pass_code,password)


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    def __repr__(self):
        return f'User {self.username}'
        return f'User {self.name}'


class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key = True)
    pitch_title = db.Column(db.String(225))
    pitch_content = db.Column(db.String(225))
    pitch_category = db.Column(db.String(225))
    category = db.Column(db.String)
    title = db.Column(db.String) 
    content = db.Column(db.String)

    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref = 'pitch_id', lazy = "dynamic")

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls, category):
        pitches_list = Pitch.query.filter_by(category = category)
        return pitches_list



    def __repr__(self):
        return f'User {self.username}'
        return f'User {self.name}'

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key = True)
    mention = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()



