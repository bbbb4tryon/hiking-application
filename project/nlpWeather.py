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



//We import the spacy library and load the English language model.
//We define a function extract_information(text) to extract weather conditions and activity types from the input text using NLP techniques.
//We modify the /suggest-clothing route to accept POST requests containing JSON data with a text field.
//Inside the /suggest-clothing route, we call the extract_information() function to extract weather conditions and activity types from the input text.
//We then use these extracted conditions and types to query the database for suitable clothing items.
//Finally, we return the suggested clothing items in JSON format `text`.
