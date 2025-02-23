from db_manager import NeonDatabaseManager
from quizz_api_tool import QuizzApiTool


##Script to insert Question to tables in db
my_quizz_api_tool = QuizzApiTool()
my_db_manager = NeonDatabaseManager()

raw = my_quizz_api_tool.get_raw_questions(
    "easy", "HTML", 20
)  ##pick a difficulty, tag(topic), number of questions to be added to database.
treated = my_quizz_api_tool.treat_raw_questions(raw)
my_db_manager.connect_to_db()
my_db_manager.insert_questions("easy_questions", treated)  ##choose table in db
my_db_manager.close_connection()

# Test retrieving question from DB
# test = NeonDatabaseManager()
# test.connect_to_db()
# print(test.retrieve_question_at_random(1, "easy_questions"))
# test.close_connection()
