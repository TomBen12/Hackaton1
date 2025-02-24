# from characters.gamer import Gamer
from tool_box import game_over_check
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
            self.event_stack_overflow,
            self.event_typo_nightmare,
            self.event_keyboard_fail,
            self.event_peer_help,
            self.event_tutorial_blackhole,
            self.event_last_minute_bug,
            self.event_accidental_code_delete,
            self.event_presentation_panic,
            self.event_fast_debugging,
        ]
        self.lunch_events = [
            self.event_buffet_bonus,
            self.event_power_smoothie,
            self.event_deep_convo,
            self.event_quick_nap,
            self.event_coding_discussion,
            self.event_lucky_find,
            self.event_relaxing_music,
            self.event_mentorship_moment,
            self.event_lunch_and_learn,
            self.event_gourmet_meal,
        ]

    def play_random_event(self):
        rand_choice = random.choice(self.events)
        self.events[rand_choice]()
        game_over_check(self.player)

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
        self.narrator._say("Your group project partners aren't doing anything![pause]")
        print("Determination -5...")
        self.player.adjust_determination(-5)

    def event_debug_hell(self):
        self.narrator._say("You've been debugging for an hour with no progress![pause]")
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
            "The power go out, and your laptop is at 5 percent battery![pause]"
        )
        print("Determination -5...")
        self.player.adjust_determination(-5)

    def event_impostor_syndrome(self):
        self.narrator._say("A classmate asks you to explain a difficult topic.[pause]")
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

    def event_stack_overflow(self):
        self.narrator._say("You find a perfect solution on Stack Overflow![pause]")
        print("Knowledge +5!")
        self.player.adjust_knowledge(5)

    def event_typo_nightmare(self):
        self.narrator._say(
            "You spend 30 minutes debugging... turns out it was a typo![pause]"
        )
        print("Determination -5...")
        self.player.adjust_determination(-5)

    def event_keyboard_fail(self):
        self.narrator._say("Your keyboard suddenly stops working![pause]")
        print("Determination -5...")
        self.player.adjust_determination(-5)

    def event_peer_help(self):
        self.narrator._say("A classmate helps you fix a tricky bug![pause]")
        print("Knowledge +5!")
        print("Determination +5!")
        self.player.adjust_knowledge(5)
        self.player.adjust_determination(5)

    def event_tutorial_blackhole(self):
        self.narrator._say(
            "You start watching one tutorial... three hours later, you're still watching![pause]"
        )
        print("Knowledge +5!")
        print("Determination -5...")
        self.player.adjust_knowledge(5)
        self.player.adjust_determination(-5)

    def event_last_minute_bug(self):
        self.narrator._say(
            "You're about to submit your project... and then you find a bug![pause]"
        )
        print("Determination -5...")
        self.player.adjust_determination(-5)

    def event_accidental_code_delete(self):
        self.narrator._say("You accidentally delete an important file![pause]")
        print("Knowledge -5...")
        print("Determination -5...")
        self.player.adjust_knowledge(-5)
        self.player.adjust_determination(-5)

    def event_presentation_panic(self):
        self.narrator._say(
            "You have to present your project... and your mind goes blank![pause]"
        )
        print("Determination -5...")
        self.player.adjust_determination(-5)

    def event_fast_debugging(self):
        self.narrator._say("You solve a bug in record time![pause]")
        print("Knowledge +5!")
        print("Determination +5!")
        self.player.adjust_knowledge(5)
        self.player.adjust_determination(5)

    ### LUNCH EVENTS ###
    def play_random_lunch(self):
        rand_choice = random.choice(self.lunch_events)
        self.lunch_events[rand_choice]()

    def event_buffet_bonus(self):
        self.narrator._say(
            "You find an all-you-can-eat buffet! Best lunch ever![pause]"
        )
        print("Knowledge +8!")
        print("Determination +8!")
        self.player.adjust_knowledge(8)
        self.player.adjust_determination(8)

    def event_power_smoothie(self):
        self.narrator._say(
            "You try a new superfood smoothie. Brain boost activated![pause]"
        )
        print("Knowledge +6!")
        print("Determination +6!")
        self.player.adjust_knowledge(6)
        self.player.adjust_determination(6)

    def event_deep_convo(self):
        self.narrator._say(
            "You have an inspiring conversation with an experienced coder during lunch![pause]"
        )
        print("Knowledge +9!")
        print("Determination +9!")
        self.player.adjust_knowledge(9)
        self.player.adjust_determination(9)

    def event_quick_nap(self):
        self.narrator._say(
            "You take a 15-minute power nap. Feels like a full night's sleep![pause]"
        )
        print("Knowledge +7!")
        print("Determination +7!")
        self.player.adjust_knowledge(7)
        self.player.adjust_determination(7)

    def event_coding_discussion(self):
        self.narrator._say(
            "You and some classmates discuss coding problems over lunch![pause]"
        )
        print("Knowledge +6!")
        print("Determination +6!")
        self.player.adjust_knowledge(6)
        self.player.adjust_determination(6)

    def event_lucky_find(self):
        self.narrator._say(
            "You randomly stumble upon an amazing coding book at the café![pause]"
        )
        print("Knowledge +10!")
        print("Determination +10!")
        self.player.adjust_knowledge(10)
        self.player.adjust_determination(10)

    def event_relaxing_music(self):
        self.narrator._say(
            "You listen to some chill music while eating. Stress melts away![pause]"
        )
        print("Knowledge +5!")
        print("Determination +5!")
        self.player.adjust_knowledge(5)
        self.player.adjust_determination(5)

    def event_mentorship_moment(self):
        self.narrator._say(
            "A senior developer shares life-changing coding advice![pause]"
        )
        print("Knowledge +9!")
        print("Determination +9!")
        self.player.adjust_knowledge(9)
        self.player.adjust_determination(9)

    def event_lunch_and_learn(self):
        self.narrator._say(
            "You attend a Lunch & Learn session. Productivity at its peak![pause]"
        )
        print("Knowledge +7!")
        print("Determination +7!")
        self.player.adjust_knowledge(7)
        self.player.adjust_determination(7)

    def event_gourmet_meal(self):
        self.narrator._say(
            "You splurge on a fancy meal. Your brain and stomach are happy![pause]"
        )
        print("Knowledge +8!")
        print("Determination +8!")
        self.player.adjust_knowledge(8)
        self.player.adjust_determination(8)


##Testing
# gamer = Gamer()
# event_mnger = RandomEventManager(gamer)
# event_mnger.play_random_event()
