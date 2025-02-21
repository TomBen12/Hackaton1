from student import Student

class Gamer(Student):
    def __init__(self):
        super().__init__()
        self.adjust_knowledge(0)
        self.adjust_stress(10)
        self.adjust_determination(-5)

    def description(self):
        return (
            "The Gamer: Stays determined even with little studying. Handles stress well, "
            "but starts off with no knowledge. Must balance gaming and studying carefully!"
        )


#Testing
player = Gamer()
print(player.get_status())

player.adjust_knowledge(150)
player.adjust_stress(-50)
player.adjust_determination(-120)

print(player.get_status())
