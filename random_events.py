from characters.gamer import Gamer
from narrator import Narrator
import random


class RandomEventManager:
    def __init__(self, player):
        self.player = player
        self.narrator = Narrator()
        self.events = [
            self.event_explain_recurtion,
            self.event_program_bug,
            self.event_cofee_break,
            self.event_wifi_fail,
            self.event_git_conflict,
            self.event_spilled_cofee,
            self.event_good_student,
            self.event_lazy_team,
            self.event_debug_hell,
            self.event_extra_homeword,
            self.event_motivational_spech,
            self.event_power_outtage,
            self.event_impostor_syndrome,
            self.event_boink,
            self.event_daydream,
        ]

    def event_explain_recurtion(self):
        self.narrator._say("The instructor asks you to explain recursion![pause]")
        print("Knowledge +5!")
        self.player.adjust_knowledge(5)

    def event_program_bug(self):
        self.narrator._say("You are coding, but your code won't run![pause]")
        print("Determination -5...")
        self.player.adjust_determination(-5)

    def event_cofee_break(self):
        self.narrator._say("You feel tired. A coffee break sounds nice.[pause]")
        print("Determination +5!")
        self.player.adjust_determination(5)

    def event_wifi_fail(self):
        self.narrator._say("The WiFi suddenly goes down![pause]")
        print("Determination -5...")
        self.player.adjust_determination(-5)

    def event_git_conflict(self):
        self.narrator._say("You have a merge conflict on GitHub![pause]")
        print("Determination -5...")
        self.player.adjust_determination(-5)

    def event_spilled_cofee(self):
        self.narrator._say("Oops! Your coffee just spilled on your keyboard![pause]")
        print("Determination -5...")
        self.player.adjust_determination(-5)

    def event_good_student(self):
        self.narrator._say("You do an optional coding challenge.[pause]")
        print("Knowledge +5!")
        self.player.adjust_knowledge(5)

    def event_lazy_team(self):
        self.narrator._say("Your group project partners aren't doing anything!")
        print("Determination -5...")
        self.player.adjust_determination(-5)

    def event_debug_hell(self):
        self.narrator._say("You've been debugging for an hour with no progress!")
        print("Determination -5...")
        self.player.adjust_determination(-5)

    def event_extra_homeword(self):
        self.narrator._say("Your instructor announces extra homework[pause]")
        print("Knowledge +5!")
        print("Determination -5...")
        self.player.adjust_knowledge(5)
        self.player.adjust_determination(-5)

    def event_motivational_spech(self):
        self.narrator._say("A senior developer shares their success story.[pause]")
        print("Knowledge +5!")
        print("Determination +5!")
        self.player.adjust_knowledge(5)
        self.player.adjust_determination(5)

    def event_power_outtage(self):
        self.narrator._say(
            "The lights go out, and your laptop is at 5 percent battery![pause]"
        )
        print("Determination -5...")
        self.player.adjust_determination(-5)

    def event_impostor_syndrome(self):
        self.narrator._say("A classmate asks you to explain a difficult topic.")
        print("Determination -5...")
        self.player.adjust_determination(-5)

    def event_boink(self):
        self.narrator._say(
            "While coming back from a short break, a piece of wall fell on your head..."
        )
        print("Determination -5...")
        print("Knowledge -10...")
        self.player.adjust_knowledge(-10)
        self.player.adjust_determination(-5)

    def event_daydream(self):
        self.narrator._say("You start to daydream![pause]")
        print("Knowledge -5...")
        print("Determination +10!")
        self.player.adjust_knowledge(-5)
        self.player.adjust_determination(10)

    def play_random_event(self):
        rand_int = random.randint(0, len(self.events) - 1)
        self.events[rand_int]()

    
##Testing
# gamer = Gamer()
# event_mnger = RandomEventManager(gamer)
# event_mnger.play_random_event()
