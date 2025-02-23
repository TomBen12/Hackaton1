from characters.student import Student


class Hustler(Student):
    def __init__(self, knowledge = 30, determination= 30):
        super().__init__()
        self.adjust_knowledge(knowledge)
        self.adjust_determination(determination)

    def description(self):
        return (
            "The Hustler: Works harder than anyone, absorbs knowledge fast, "
            "but stress is a constant battle. Needs to manage workload carefully."
        )

    def get_status(self):
        return (
            f"\n {self.name} - Knowledge: {self.knowledge_points}, "
            f"Determination: {self.determination_points}"
        )
        
