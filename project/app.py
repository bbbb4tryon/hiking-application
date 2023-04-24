# sets up three routes,'/', '/ranges', and '/clothing'...'/' returns a welcome message, the other two routes query the database for all ranges and clothing items and returns them in JSON format.  The '/clothing/<int:clothing_id>/ranges' route returns a single clothing item as a param and returns the ranges associtated with tthat item.

from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Clothing, Ranges, Base

#create an engine to connet to the db
engine = create_engine('sqlite:///outdoors.db')
# create all tabkes define in the models.py file
Base.metadata.create_all(engine)
# create a sessionmaker object to interact with the db
# 'bind' is a keyword argument that tells the sessionmaker object which db to connect to
Session = sessionmaker(bind=engine)
session = Session()
app = Flask(__name__)

#Define the routes for the Flask appcation
@app.route('/')
def index():
    return "Welcome to the Outdoors! We've answered THAT eternal question: What should I wear on my adventure?"

#queries the db and converts the results into a list of dictionaries adn returns them in JSON format... the return statement queries the db for all 'Ranges' items and returns them in JSON format... the 'jsonify' function converts the results into a list of dictionaries for the client-side to consume
@app.route('/ranges')
def get_ranges():
    all_ranges= session.query(Ranges).all()
    return jsonify([ranges.__dict__ for ranges in all_ranges])

# The variable created in the for loop is an element from the 'clothing' list, which represents a single Clothing object.
@app.route('/clothing')
def get_clothing():
    all_clothing= session.query(Clothing).all()
    return jsonify([clothing.__dict__ for clothing in all_clothing])

@app.route('/clothing/<int:clothing_id>/ranges')
def get_clothing_ranges(clothing_id):
    clothing = session.query(Clothing).get(clothing_id)
    ranges = clothing.ranges
    return jsonify([range.__dict__ for range in ranges])

if __name__=='__main__':
    app.run(debug=True)