import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:1234@localhost:5433/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # REPLACE 'user','password','localhost','dbname' wit your actual credentials

