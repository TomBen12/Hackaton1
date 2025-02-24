import sys
import time
import random


class Narrator:

    def __init__(self):
        self.__delay = 0.035
        self.__dot_delay = 0.5
        self.__pause = 0.8

    def _say(self, text):
        i = 0
        while i < len(text):
            # 3 dots search#
            if text[i : i + 3] == "...":
                for dot in "...":
                    sys.stdout.write(dot)
                    sys.stdout.flush()
                    time.sleep(self.__dot_delay)  # Delay per dot
                i += 3  # Skip all three dots
            elif text[i : i + 7] == "[pause]":
                time.sleep(self.__pause)
                i += 7  # Skip the marker
            else:
                sys.stdout.write(text[i])
                sys.stdout.flush()
                time.sleep(self.__delay)
                i += 1
        print()

    def game_over(self):
        """Ends the game with a final message."""
        self._say(
            "\n[pause]Oh no... [pause]\n"
            "*--  GAME OVER.  --* [pause]\n"
            "Your journey has come to an end. [pause]\n"
            "But every failure is a lesson, and every lesson makes you stronger! [pause]\n"
            "Farewell, coder... Until we meet again. [pause]"
        )
        exit()

    def welcome(self):
        self._say(
            "\nWelcome to Developer Institute! [pause]\n"
            "This world is inhabited by passionate coders, each embarking on their own unique journey. [pause]\n"
            "Today, you take your first step into this exciting adventure! [pause]\n"
            "But First of all,[pause] let me itroduce you to the rules of this place.[pause]\n"
        )

    def not_valid_choice(self):
        self._say("Oops! That's not a valid option. Try again.")

    def not_valid_name(self):
        """Handles invalid name input."""
        self._say(
            "Oops! Your input is invalid. Names must be less than 15 characters and contain only letters. Try again."
        )

    def rules(self):
        self._say(
            "[pause]Listen closely![pause]\n"
            "The more you learn, the easier the final test will feel! [pause]\n"
            "But be careful![pause] If your determination reaches zero or if you fail the final test… [pause]\n"
            "it's GAME OVER! gulp... [pause]\n"
            "So stay sharp, keep pushing forward, and don't give up![pause]\n"
            "Your journey is just beginning…"
        )

    def what_is_your_name(self):
        self._say(
            "\nBefore we go any further, tell me [pause] what is your name? [pause]\n"
            "type your name and hit Enter!"
        )

    def beautiful_name(self, name):
        compliments = [
            f"{name} huh? [pause] Sounds like the name of a coding legend!",
            f"Ah, {name}! A name so powerful, even bugs fear you.",
            f"{name}? Yess![pause] That's the kind of name that makes JavaScript behave properly!",
            f"{name}? I like it! Short, sweet, and definitely main character... I mean[pause] student material!",
        ]
        compliment = random.choice(compliments)
        self._say(compliment)

    def what_kindo(self, name):
        self._say("[pause]Hmm... now, tell me")
        print(name, end="")
        self._say(", [pause]what kind of coder are you? [pause]\n")
        self._say("Are you more of a: [pause]\n")
        print(
            """
            [H] -Hustler- A relentless go-getter. 
                Knowledge '15'
                Determination '25'
            
            [S] -Sleeper- A quiet genius. 
                Knowledge '18'
                Determination '22'
            
            [G] -Gamer- A problem-solving strategist. 
                Knowledge '17'
                Determination '20'
            """
        )

    def all_set(self, player):

        self._say(
            f"[pause]Fantastic, {player.name}! [pause]\n"
            f"You're all set to begin your journey as a {player.type}. [pause]\n"
            "But before you go, always remember[pause]\n"
            "your stats are SUPER...[pause] ahem, I mean, [pause]\n"
            "very important![pause] They'll determine how challenging the final quiz will feel at the end of the day. [pause]\n"
            "So stay sharp, keep learning, and trust your instincts! [pause]\n"
            "Alright, [pause] enough talk. [pause] Let's get started! [pause]\n"
            f"And don't be late for your first class ok {player.name}!? \n"
        )

    def class_start(self, player):
        self._say("[pause].........[pause]")
        self._say(
            f"You just arrived in class, {player.name}, and before you even have time to say hi to your new classmates...[pause] "
            "BAM!!!! [pause]\n"
            "You're hit with your first quiz!\n"
        )

    def survived_quiz(self):
        responses = [
            "[pause]That was tough! I know! [pause]\nBut if you're still here, it means you made it!\nThe class can continue. [pause]",
            "[pause]Phew! That was intense... [pause]\nBut guess what? You survived! [pause]\nLet's keep going. [pause]",
            "[pause]You did it! [pause]\nI wasn't sure you'd make it, but here you are. [pause]\nNow, back to class! [pause]",
            "[pause]Congratulations! [pause]\nAnother quiz, another victory! [pause]\nNow let's move on before the next one sneaks up on us. [pause]",
            "[pause]Well done! [pause]\nYou fought through that quiz like a true coder. [pause]\nNow let's get back to work! [pause]",
            "[pause]That was brutal... [pause]\nBut hey, you're still standing! [pause]\nAlright, no time to rest—back to learning! [pause]",
        ]

        self._say(random.choice(responses))

    def class_continues(self):
        responses = [
            "[pause]Alright now... [pause] Back to learning! [pause]",
            "[pause]Break's over! [pause] Time to dive back into some serious coding. [pause]",
            "[pause]Hope you enjoyed that little distraction... [pause] Now, where were we? [pause] Oh right, back to learning! [pause]",
            "[pause]No more excuses! [pause] Time to focus and get back to work! [pause]",
            "[pause]Fun's over... [pause] or is it? [pause] Guess it depends on how much you like debugging! [pause] Let's continue. [pause]",
            "[pause]Okay, okay... enough delays! [pause] Let's get back to it before the next surprise quiz appears. [pause]",
        ]

        self._say(random.choice(responses))

    def waiting(self):
        self._say("......")

    def what_another_quiz(self):

        reactions = [
            "[pause]Wait... what?! [pause]\nAnother quiz already?! [pause]\nI hope you've been paying attention, because there's no turning back now! [pause]\nGet ready... it's quiz time! [pause]",
            "[pause]Seriously?! [pause]\nAnother quiz? [pause]\nI swear they multiply faster than bugs in a broken codebase... [pause]\nBrace yourself! [pause]",
            "[pause]Oh no... [pause]\nI had a bad feeling about this! [pause]\nAnother quiz is coming your way! [pause]\nLet's hope you're prepared... [pause]",
            "[pause]Again?! [pause]\nJust when you thought you could relax... [pause]\nAnother quiz sneaks up on you! [pause]\nTime to prove your skills! [pause]",
            "[pause]Surprise! [pause]\nGuess what? It's quiz time—again! [pause]\nAt this point, you should just accept your fate. [pause]\nLet's do this! [pause]",
            "[pause]You hear the dreaded words... [pause]\n'Everyone, get ready for another quiz!' [pause]\nYour soul momentarily leaves your body. [pause]\nStay strong... you got this! [pause]\n",
        ]

        self._say(random.choice(reactions))

    def somethig_is_happening(self):
        suspense_messages = [
            "[pause]Something feels... off. [pause]\nYou can't shake the feeling that something is about to happen. [pause]",
            "[pause]A strange silence fills the room... [pause]\nYou swear you heard something, but no one else reacts. [pause]",
            "[pause]You feel a shift in the air... [pause]\nLike the moment before a storm. [pause]",
            "[pause]For a split second, everything seems normal... [pause]\nToo normal. [pause]",
            "[pause]A distant sigh, a muffled chuckle... [pause]\nThen, a pause. [pause]\nSomething is coming. [pause]",
        ]
        suspense = random.choice(suspense_messages)
        self._say(suspense)

    def show_stats(self, player):
        stats = player.get_status()
        self._say(f"[pause]Here's where you stand, {player.name}: [pause]\n{stats}")
        input("\n[pause]Press Enter to continue...")

    def lunch_time(self):
        self._say(
            "[pause]It's lunchtime! [pause]\n"
            "You've been working hard, and you deserve a good meal. [pause]\n"
            "Take a break, refuel, and maybe even have a good conversation. [pause]"
        )

    def you_made_it_final(self):
        self._say(
            "[pause]You made it to the final quiz!! [pause]\n"
            "I hope you're ready... [pause] There's no turning back now! [pause]\n"
            "Let's see if all your hard work pays off! [pause]"
        )

    def here_comes_final_quiz(self):
        self._say(
            "[pause]Here it comes... [pause]\n"
            "**The FINAL QUIZ!!** [pause]\n"
            "This is the moment you've been preparing for. [pause]\n"
            "Give it everything you've got! [pause]"
        )

    def test_too_hard(self):
        self._say(
            "[pause]You take a quick peek at the final test... [pause]\n"
            "Your heart sinks. [pause]\n"
            "You don't recognize **anything**. [pause]\n"
            "Your mind goes blank, and panic sets in. [pause]\n"
            "You feel completely lost... [pause]\n"
            "You don't know what to do... [pause]\n"
        )
        self.game_over()

    def game_ending(self, player):
        self._say(
            "[pause]I can't believe it... [pause]\n"
            "**You did it!!!** [pause]\n"
            "You passed the final quiz!!!!! [pause]\n"
            "From a beginner to a true developer, you've grown so much! [pause]\n"
            "Your journey wasn't easy, but you never gave up. [pause]\n"
            "And now, I have no doubt... [pause] You will be an **amazing** developer! [pause]\n"
            "The world of coding is yours to explore! [pause]\n"
            "Before we go, let's take one last look at your final stats... [pause]\n"
        )

        self.show_stats(player)

        self._say(
            "[pause]And with that, your adventure comes to an end... [pause]\n"
            "***** THE END. ***** 👻 "
        )


# TEST##
# narrator = Narrator()

# narrator.welcome()
# narrator.what_is_your_name()
# narrator.what_type_are_you()
# narrator.all_set()
