from app import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)

    def __repr__(self):
        return "<User '{}'>".format(self.username)

class Problem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    typ = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=True)
    difficulty = db.Column(db.Float, nullable=False)
    tags = db.Column(db.Text, nullable = True)
    result = db.Column(db.Text, nullable = False)
    options = db.Column(db.Text, nullable = True)
    options_type = db.Column(db.Text, nullable = True)
    image64 = db.Column(db.Text, nullable = True)
    submitter = db.Column(db.Text, nullable = False)

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    typ = db.Column(db.String(80), nullable=False)
    difficulty = db.Column(db.Float, nullable=False)
    problems = db.Column(db.Text)
    submitter = db.Column(db.Text)
    views = db.Column(db.Integer)
    

