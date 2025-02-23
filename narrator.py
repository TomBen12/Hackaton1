import sys
import time
import random


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

    def game_over(self):
        self._say(
            "[pause]Oh no... [pause]\n"
            "GAME OVER. [pause]\n"
            "Your journey has come to an end. [pause]\n"
            "But every failure is a lesson, and every lesson makes you stronger! [pause]\n"
            "Will you try again? Or is this the end of your coding adventure?\n"
        )
        while True:
            choice = input("Do you want to restart? (Y/N): ").strip().upper()
            if choice == "Y":
                return "restart"  
            elif choice == "N":
                self._say("Farewell, coder... Until we meet again.")
                exit()
            else:
                self._say("Invalid choice. Please enter 'Y' to restart or 'N' to quit.")

    def welcome(self):
        self._say(
            "\nWelcome to Developer Institute! [pause]\n"
            "This world is inhabited by passionate coders, each embarking on their own unique journey. [pause]\n"
            "Today, you take your first step into this exciting adventure! [pause]\n"
            "But First of all, let me itroduce you to the rules of this place.[pause]\n"
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
                Knowledge 'x'
                Determination 'x'
            
            [S] -Sleeper- A quiet genius. 
                Knowledge 'x'
                Determination 'x'
            
            [G] -Gamer- A problem-solving strategist. 
                Knowledge 'x'
                Determination 'x'
            """
        )

    def all_set(self, player):

        self._say(
            f"[pause]Fantastic, {player.name}! [pause]\n"
            f"You're all set to begin your journey as a {player.type}. [pause]\n"
            "But before you go, always remember[pause]\n"
            "your stats are GIGA...[pause] ahem, I mean, [pause]\n"
            "very important! They'll determine how challenging the final quiz will feel at the end of the day. [pause]\n"
            "So stay sharp, keep learning, and trust your instincts! [pause]\n"
            "Alright, [pause] enough talk. [pause] Let's get started! [pause]\n"
            f"And don't be late for your first qui...[pause] I mean, class, {player.name}! \n"
        )

    def class_start(self, player):
        self._say("[pause].........[pause]")
        self._say(
            f"You just arrived in class, {player.name}, and before you even have time to say hi to your new classmates...[pause] "
            "BAM!!!! [pause]\n"
            "You're hit with your first quiz!")

    def survived_quiz(self):
        self._say("That was tough! I know![pause]\nBut if you're still here it means you made it!\n""The class can continue")

    def class_continues(self):
        self._say("[pause]Alright now... [pause] Back to learning! [pause]")

    def waiting(self):
        self._say(".........")

    def what_another_quiz(self):
        self._say(
            "[pause]Wait... what?! [pause]\n"
            "Another quiz already?! [pause]\n"
            "I hope you've been paying attention, because there's no turning back now! [pause]\n"
            "Get ready... it's quiz time! [pause]"
        )

    def another_quiz(self):
        self._say(
            "[pause]Are you serious?! [pause]\n"
            "Another quiz already?! [pause]\n"
            "I swear, these quizzes are multiplying on their own... [pause]\n"
            "Alright, brace yourself! [pause]\n"
            "Here comes another one! [pause]"
        )

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


# TEST##
# narrator = Narrator()

# narrator.welcome()
# narrator.what_is_your_name()
# narrator.what_type_are_you()
# narrator.all_set()
