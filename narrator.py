import sys
import time


class Narrator:

    def __init__(self):
        self.__delay = 0.035
        self.__dot_delay = 0.5
        self.__pause = 0.8

    def _say(self, text):
        """Prints text character by character, making '...' print one dot at a time."""
        i = 0
        while i < len(text):
            if text[i : i + 3] == "...":  # Check for '...'
                for dot in "...":
                    sys.stdout.write(dot)
                    sys.stdout.flush()
                    time.sleep(self.__dot_delay)  # Delay per dot
                i += 3  # Skip all three dots
            elif text[i : i + 7] == "[pause]":  # Custom pause trigger
                time.sleep(self.__pause)
                i += 7  # Skip the marker
            else:
                sys.stdout.write(text[i])
                sys.stdout.flush()
                time.sleep(self.__delay)
                i += 1
        print()

    def new_game_intro(self):
        self._say(
            f"Welcome to Developer Institute! Your journey begins now... I'm sure you waited a long time for this day![pause] before we start[pause]\nlet's get to know you![pause]"
        )

    def what_is_your_name(self):
        self._say('What was your name again?')
        self._say('(Type your name and press enter)')

    def what_type_are_you(self):
        self._say('[pause]Are you more of a: [pause]')
        print(
            '''
        [H] -Hustler - Knowledge +30, Stress +35, Determination 70
        
        [S] -Sleeper - Knowledge +10, Stress +10, Determination 100
        
        [G] -Gamer - Knowledge 0, Stress +10, Determination 95
              '''
        )
        self._say('Yep... you are suposed to press a key and then Enter.')

    def all_set(self):
        self._say(
            '[pause]Great![pause]\nBefore you go [pause]\nAllways remember to check your SMART WATCH to keep track of your stats,\nThey are GIGAA... MEGAA...[pause]... sorry,\nVerry[pause] important and will impact how hard of a time you will have on your final quizz at the end of the day.[pause]\nLet\'s skip the chatter and get to it!\nDon\'t be late!\n'
        )
        self._say('')


#TEST##
narrator = Narrator()

# narrator.new_game_intro()
# narrator.what_is_your_name()
# narrator.what_type_are_you()
# narrator.all_set()
