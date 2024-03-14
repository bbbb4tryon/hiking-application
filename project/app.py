# sets up three routes,'/', '/ranges', and '/clothing'...'/' returns a welcome message, the other two routes query the database for all ranges and clothing items and returns them in JSON format.  The '/clothing/<int:clothing_id>/ranges' route returns a single clothing item as a param and returns the ranges associtated with tthat item.

# NLP - Weather ----------------------------------------------------------
from flask import Flask, jsonify, request, abort
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Clothing, Ranges, Base

# Import NLP libraries
import spacy

# Load English tokenizer, tagger, parser, and NER
nlp = spacy.load("en_core_web_sm")

# create an engine to connect to the db
engine = create_engine('sqlite:///outdoors.db')
# create all tables defined in the models.py file
Base.metadata.create_all(engine)
# create a sessionmaker object to interact with the db
# 'bind' is a keyword argument that tells the sessionmaker object which db to connect to
Session = sessionmaker(bind=engine)
session = Session()
app = Flask(__name__)

# Define function to extract weather conditions and activity type from text
def extract_information(text):
    # Initialize variables to store extracted information
    weather_conditions = []
    activity_type = []

    # Process the input text using the NLP model
    doc = nlp(text)

    # Extract entities related to weather conditions and activity types
    for token in doc:
        if token.text.lower() in ["hot", "cold", "rainy", "sunny"]:
            weather_conditions.append(token.text.lower())
        elif token.text.lower() in ["hiking", "running", "skiing", "camping"]:
            activity_type.append(token.text.lower())

    return weather_conditions, activity_type

# Define the routes for the Flask application
@app.route('/')
def index():
    return "Welcome to the Outdoors! We've answered THAT eternal question: What should I wear on my adventure?"

@app.route('/suggest-clothing', methods=['POST'])
def suggest_clothing():
    # Ensure the request is in JSON format
    if not request.json or 'text' not in request.json:
        abort(400)  # Bad request

    # Get the text input from the request
    text_input = request.json['text']

    # Extract weather conditions and activity type from text
    weather_conditions, activity_type = extract_information(text_input)

    # Perform database query based on extracted information
    suggested_clothing = session.query(Clothing).filter(
        Clothing.function.like(f"%{' '.join(weather_conditions)}%"),
        Clothing.function.like(f"%{' '.join(activity_type)}%")
    ).all()

    # Convert the results into a list of dictionaries for JSON response
    result = [{'generic_name': clothing.generic_name, 'function': clothing.function} for clothing in suggested_clothing]

    return jsonify(result)

if __name__=='__main__':
    app.run(debug=True)

# NLP - Weather -end ----------------------------------------------------------
'''
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
'''
