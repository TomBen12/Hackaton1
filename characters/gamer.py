from characters.student import Student


class Gamer(Student):
    def __init__(self):
        super().__init__()
        self.adjust_knowledge(0)
        self.adjust_determination(-5)

    def description(self):
        return (
            "The Gamer: Stays determined even with little studying. Handles stress well, "
            "but starts off with no knowledge. Must balance gaming and studying carefully!"
        )

    def get_status(self):
        return (
            f"\n {self.name} - Knowledge: {self.knowledge_points}, "
            f"Determination: {self.determination_points}"
        )


# Testing
# player = Gamer()
# print(player.get_status())
