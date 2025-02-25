from quizz_factory import Quizz_Maker
from narrator import Narrator
from characters.gamer import Gamer
from characters.hustler import Hustler
from characters.sleeper import Sleeper
from random_events import RandomEventManager
import tool_box as tools


# def main():
###------Intro------###
def main():

    narrator = Narrator()
    narrator.welcome()
    narrator.rules()
    narrator.what_is_your_name()
    name = tools.format_name_input()
    narrator.beautiful_name(name)
    narrator.what_kindo(name)
    choice = tools.format_class_choice()

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
    my_quiz_maker = Quizz_Maker()
    q_list = my_quiz_maker.create_question_sequence(
        number=3, toughness="easy_questions"
    )
    my_quiz_maker.display_quizz(player)
    narrator.show_stats(player)
    narrator.survived_quiz()
    narrator.class_continues()
    narrator.waiting()
    narrator.somethig_is_happening()
    event_manager = RandomEventManager(player)
    event_manager.play_random_event()
    narrator.show_stats(player)
    narrator.class_continues()
    narrator.what_another_quiz()
    my_quiz_maker_2 = Quizz_Maker()
    q_list_2 = my_quiz_maker.create_question_sequence(
        number=3, toughness="easy_questions"
    )
    my_quiz_maker.display_quizz(player)
    narrator.show_stats(player)
    narrator.survived_quiz()
    narrator.class_continues()
    narrator.waiting()
    narrator.somethig_is_happening()
    event_manager = RandomEventManager(player)
    event_manager.play_random_event()
    narrator.show_stats(player)
    narrator.class_continues()
    narrator.waiting()
    narrator.lunch_time()
    event_manager = RandomEventManager(player)
    event_manager.play_random_lunch()
    narrator.show_stats(player)
    ## Evening ##
    narrator.waiting()
    narrator.class_continues()
    narrator.what_another_quiz()
    my_quiz_maker_3 = Quizz_Maker()
    q_list_3 = my_quiz_maker.create_question_sequence(
        number=3, toughness="easy_questions"
    )
    my_quiz_maker.display_quizz(player)
    narrator.show_stats(player)
    narrator.survived_quiz()
    narrator.class_continues()
    narrator.waiting()
    narrator.somethig_is_happening()
    event_manager = RandomEventManager(player)
    event_manager.play_random_event()
    narrator.show_stats(player)
    narrator.class_continues()
    narrator.waiting()
    narrator.you_made_it_final()
    if player.knowledge_points > 50:
        my_quiz_maker_final = Quizz_Maker()
        q_list_final = my_quiz_maker.create_question_sequence(
            number=6, toughness="easy_questions"
        )
    elif 30 < player.knowledge_points < 50:
        my_quiz_maker_final = Quizz_Maker()
        q_list_final = my_quiz_maker.create_question_sequence(
            number=6, toughness="medium_questions"
        )
    else:
        narrator.test_too_hard()

    narrator.game_ending()


main()
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
