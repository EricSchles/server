"""

Here the models for our database is defined.

I am using Postgres, Flask-SQLAlchemy for this application.

For an introduction to Flask-SQLAlchemy check out: http://flask-sqlalchemy.pocoo.org/2.1/
""" 
from app import db

class DataModel(db.Model):
    """
    Doc string goes here
    """
    __tablename__ = 'data_model'
    id = db.Column(db.Integer, primary_key=True)
    field = db.Column(db.String)


    def __init__(self, field):
        self.field = field


    def __str__(self):
        return repr(self.field)