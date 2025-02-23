from characters.student import Student


class Sleeper(Student):
    def __init__(self):
        super().__init__()
        self.adjust_knowledge(10)
        self.adjust_determination(0)

    def description(self):
        return (
            "The 9PM Sleeper: Always well-rested and stress-free, but learns at a steady pace. "
            "Perfect for players who prefer a balanced strategy."
        )

    def get_status(self):
        return (
            f"\n {self.name} - Knowledge: {self.knowledge_points}, "
            f"Determination: {self.determination_points}"
        )
