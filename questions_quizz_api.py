import db_connection as db_connection
import requests
import json

API_KEY = "wCMhptDGFDKTeY2mX6aSdwJqKpBCUMevi5pHdFdO"
BASE_URL = "https://quizapi.io/api/v1/questions"

def get_questions(category = "HTML",difficulty='easy'): #change function later to be able to change param dinamically
    params = {
        "apiKey": API_KEY,
        "category": "code",
        "difficulty": {difficulty},
        "tags": {category},
        "limit": 3,
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        questions = response.json()
        return questions
    else:
        print(f"Error: {response.status_code}")
        return None




##EX
questions = get_questions()
if questions:
    print(json.dumps(questions, indent=2))
