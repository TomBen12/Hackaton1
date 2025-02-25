import requests
import os
from dotenv import load_dotenv


class QuizzApiTool:
    def __init__(self):
        load_dotenv()
        self.API_KEY = os.getenv("API_KEY")
        self.BASE_URL = "https://quizapi.io/api/v1/questions"

    def get_raw_questions(self, difficulty, topic, limit):
        params = {
            "apiKey": self.API_KEY,
            "category": "code",
            "difficulty": difficulty,
            "tags": topic,
            "limit": limit,
        }
        response = requests.get(self.BASE_URL, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None

    def treat_raw_questions(self, raw_questions):
        if not isinstance(raw_questions, list):
            print("raw_questions is not a list....")
            return []

        treated_questions = []
        for item in raw_questions:
            question = item.get("question", "No Question")
            answers = item.get("answers", {})
        
            correct_answer_key = None
            correct_answer_text = None
            if isinstance(item.get("correct_answers", {}), dict):
                for key, value in item["correct_answers"].items():
                    if value == "true":
                        correct_answer_key = key.replace("_correct", "")
                        correct_answer_text = answers.get(correct_answer_key, "Unknown")

            difficulty = item.get("difficulty", "Unknown")
            topic = item.get("tags", [{}])[0].get("name", "Unknown")

            question_data = {
                "question": question,
                "answers": answers,
                "correct_answer": correct_answer_text,
                "difficulty": difficulty,
                "topic": topic,
            }
            treated_questions.append(question_data)

        return treated_questions
