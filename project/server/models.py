# project/server/models.py


import datetime

from project.server import app, db, bcrypt




class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, app.config.get('BCRYPT_LOG_ROUNDS')
        )
        self.registered_on = datetime.datetime.now()
        self.admin = admin

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def is_admin(self):
        if self.admin:
            return True
        else:
            return False


    def __repr__(self):
        return '<User {0}>'.format(self.email)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    prev = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    category = db.Column(db.String(255))

    def __init__(self, title, body, category, prev, pub_date=None):
        self.title = title
        self.prev = prev
        self.body = body

        self.pub_date = pub_date
        self.category = category

    def __repr__(self):
        return '<Post %r>' % self.title
