import json
import requests
import flask
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

##Fetch Garmin Data: Create a function to fetch the Garmin data from the URL. Let's call it fetch_garmin_data. Inside the function, use the requests module to send a GET request to the URL and retrieve the data.

def fetch_garmin_data():
    url = 'https://raw.githubusercontent.com/RoarkJ/Digital-Workout-Tracker/main/data/json/activities.json'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('Failed to fetch Garmin data.')
        return None
    
##Extract Required Information: Create a function to extract the required information from the fetched Garmin data. Let's call it extract_workout_info. Inside the function, parse the Garmin data and extract the necessary information 

def extract_workout_info(data):
    workout_info = []
    for activity in data['activities']:
        latitude = activity['latitude']
        longitude = activity['longitude']
        time = activity['time']
        heart_rate = activity['heart_rate']
        temperature = activity['temperature']
        # Add the extracted information to a list or data structure as needed
        workout_info.append({
            'latitude': latitude,
            'longitude': longitude,
            'time': time,
            'heart_rate': heart_rate,
            'temperature': temperature
        })
    return workout_info

##Integrate with Endpoint: Create an endpoint in your Flask app to handle the data retrieval and processing

@app.route('/workout-data', methods=['GET'])
def get_workout_data():
    # Fetch the Garmin data
    garmin_data = fetch_garmin_data()

    # Extract the required information
    workout_info = extract_workout_info(garmin_data)

    # Return the extracted data as a JSON response
    return flask.jsonify(workout_info)

if __name__ == '__main__':
    app.run()
    