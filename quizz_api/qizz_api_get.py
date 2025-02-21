import requests



class QuizzApiTool:
    '''retrieve raw JSON quizz data from quizz api given difficulty, topic and limit(count) by default easy, HTML, 3'''

    def __init__(self, difficulty='easy', topic='HTML', limit='10'):
        self.API_KEY = "wCMhptDGFDKTeY2mX6aSdwJqKpBCUMevi5pHdFdO"
        self.BASE_URL = "https://quizapi.io/api/v1/questions"
        self.difficulty = difficulty
        self.quizz_topic = topic
        self.limit = limit

        # Store params as an instance variable
        self.params = {
            "apiKey": self.API_KEY,
            "category": "code",
            "difficulty": self.difficulty,
            "tags": self.quizz_topic,
            "limit": self.limit,
        }

    def get_raw_questions(self):
        response = requests.get(self.BASE_URL, params=self.params)
        if response.status_code == 200:
            questions = response.json()
            return questions
        else:
            print(f"Error: {response.status_code}")
            return None

    def treat_raw_question(self, raw_questions):
        treated_questions = []
        for item in raw_questions:  # Loop through each question
            question = item['question']
            answers = item['answers']
            correct_answer = item['correct_answer']
            difficulty = item['difficulty']
            topic = item['tags'][0]["name"]
            one_question = {'question':question,
                            'answers':answers,
                            'correct_answer':correct_answer,
                            'difficulty':difficulty,
                            'topic':topic
                            }
            treated_questions.append(one_question)
        return treated_questions

# Exeple
# question_tool = QuizzApiTool()
# questions_raw = question_tool.get_raw_questions()
# question_tool.treat_raw_question(questions_raw)
# if questions:
#     print(questions)
