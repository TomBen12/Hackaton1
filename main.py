from quizz_factory import Quizz_Maker
from narrator import Narrator
from characters.gamer import Gamer
from characters.hustler import Hustler
from characters.sleeper import Sleeper
import inputs_format_narate as inp


# def main():
###------Intro------###
my_quiz_maker = Quizz_Maker
narrator = Narrator()
narrator.welcome()
narrator.rules()
narrator.what_is_your_name()
name = inp.format_name_input()
narrator.beautiful_name(name)
narrator.what_kindo(name)
choice = inp.format_class_choice()

match choice:
    case "H":
        player = Hustler()
        player.set_type("Hustler")
    case "S":
        player = Sleeper()
        player.set_type("Sleeper")
    case "G":
        player = Gamer()
        player.set_type("Gamer")

player.set_name(name)
narrator.all_set(player)

###---- morning -----###
narrator.class_start(player)
q_list = my_quiz_maker.create_question_sequence(3,  "easy_questions")
my_quiz_maker.display_quizz(player)







# def morning_class(self):

#     # here the narator will prepare user for the first quizz
#     # before each quizz you can check you smartwatch
#     # first quizz happens here
#     # then a random even happens

#     pass


# def lunch_time(self, player):
#     # at luch time the narator speak to you , you can check your stats and
#     # you also go through 2 random events that impact your stats.
#     pass


# def evening_class(self, player):

#     # narator speaksto you about the evening class and that it is the last class before the quizz
#     # in the evening classs you also have a quizz and a random event that happens here
#     pass


# def final_quizz(self, player):
#     # the narratator explains to you that the whole point of your day was for this moment and if you are still alive until now you better have enough knowledge or else the test will feel incredibly hard.
#     # narator explain to you that
#     pass


# def end_game(self, player):
#     # if you survived the day and got at least 2/4 on the final quizz you win
#     pass
