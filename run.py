'''
Created on 30 Jul 2019

@author: w.c.horrel
'''


from app import app
from db import db

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

