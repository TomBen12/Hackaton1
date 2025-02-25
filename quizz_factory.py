from backend.db_manager import NeonDatabaseManager
from narrator import Narrator
from tool_box import game_over_check

# from characters.gamer import Gamer


class Question:
    """A class representing a multiple-choice question."""

    def __init__(self, topic, question, correct_answer, *answers):
        self.topic = topic
        self.question = question
        self.correct_answer = correct_answer
        self.answers = answers


class Quizz_Maker:
    """This class has a method that creates and displays questions"""

    def __init__(self):
        self.db_manager = NeonDatabaseManager()
        self.quizz_narrator = Narrator()
        self.question_list = []

    def create_question_sequence(self, number, toughness):
        """creates a sequence of questions"""
        self.question_list = []
        self.db_manager.connect_to_db()

        try:
            question_sequence = self.db_manager.retrieve_question_at_random(
                number, toughness
            )
        except Exception as e:
            self.quizz_narrator._say(f"[pause]Error retrieving questions: {e}")
            return
        finally:
            self.db_manager.close_connection()

        # retrieved data into Question objects
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
        """displays a quiz with multiple questions and checks answers."""
        if not self.question_list:
            self.quizz_narrator._say(
                "[pause]No questions available. Please try again later."
            )
            return 0  # Exit if there are no questions

        good_answers = 0  # Track correct answers

        for question in self.question_list:
            self.quizz_narrator._say(question.question)

            # Display answer choices
            for index, answer in enumerate(question.answers, start=1):
                print(f"{index}. {answer}")

            # Get valid player input
            selected_answer = None
            while selected_answer is None:
                try:
                    user_answer = int(input("Your Answer: ").strip())

                    if 1 <= user_answer <= len(question.answers):
                        selected_answer = question.answers[user_answer - 1]
                    else:
                        self.quizz_narrator._say(
                            "[pause]Invalid choice. Enter a number from the options."
                        )
                except ValueError:
                    self.quizz_narrator._say(
                        "[pause]Invalid input. Please enter a number."
                    )

            # check if the answer is correct
            if selected_answer == question.correct_answer:
                self.quizz_narrator._say("...[pause]Correct Answer!")
                good_answers += 1
                player.adjust_knowledge(5)
                player.adjust_determination(2)
            else:
                self.quizz_narrator._say(
                    f"[pause]...Wrong answer! The correct answer was: {question.correct_answer}"
                )
                player.adjust_determination(-7)
                game_over_check(player)  # Check if player should continue

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
