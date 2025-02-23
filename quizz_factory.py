from backend.db_manager import NeonDatabaseManager
from narrator import Narrator

# from characters.gamer import Gamer


class Question:
    def __init__(self, topic, question, correct_answer, *answers):
        self.topic = topic
        self.question = question
        self.correct_answer = correct_answer
        self.answers = answers


class Quizz_Maker:
    """This class has a method that create and display questions"""

    def __init__(self):
        self.db_manager = NeonDatabaseManager()
        self.quizz_narrator = Narrator()
        self.question_list = []

    def create_question_sequence(self, number="3", toughness="easy_questions"):
        """this method create a sequence of 3 questions"""
        self.db_manager.connect_to_db()
        question_sequence = self.db_manager.retrieve_question_at_random(
            number, toughness
        )
        self.db_manager.close_connection()

        for q in question_sequence:
            topic = q["topic"]
            question_text = q["question"]
            correct_answer = q["correct_answer"]
            answers = [
                q["answer_a"],
                q["answer_b"],
                q["answer_c"],
                q["answer_d"],
            ]
            question_obj = Question(topic, question_text, correct_answer, *answers)
            self.question_list.append(question_obj)

    def display_quizz(self, player):
        """This method displays a quiz with multiple questions and checks answers."""
        good_answers = 0
        for question in self.question_list:
            self.quizz_narrator._say(question.question)

            for index, answer in enumerate(question.answers, start=1):
                print(f"{index}. {answer}")

            while True:
                try:
                    user_answer = int(input("Your Answer: "))

                    if 1 <= user_answer <= len(question.answers):
                        selected_answer = question.answers[user_answer - 1]
                        break
                    else:
                        print(
                            "Invalid choice. Please enter a number corresponding to an answer."
                        )
                except Exception:
                    print("Invalid input. Please enter a number.")

            if selected_answer == question.correct_answer:
                self.quizz_narrator._say("...[pause]Correct Answer!")
                good_answers += 1
                player.adjust_knowledge(6)
                player.adjust_determination(2)
            else:
                self.quizz_narrator._say(
                    f"[pause]...Wrong answer The correct answer was: {question.correct_answer}"
                )
                player.adjust_determination(-6)
        return good_answers


# quizz_maker = Quizz_Maker()
# question_seq = quizz_maker.create_question_sequence()
##-----------
# testing create_questions
# for q in question_seq:
#     print(q.topic, q.question,q.answers, "\n", q.correct_answer)
##------------
# testing display_quizz
# player = Gamer()
# quizz_maker.display_quizz(player)
