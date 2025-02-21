from student import Student


class Hustler(Student):
    def __init__(self):
        super().__init__()
        self.adjust_knowledge(30)
        self.adjust_stress(35)
        self.adjust_determination(-20)

    def description(self):
        return (
            "The Hustler: Works harder than anyone, absorbs knowledge fast, "
            "but stress is a constant battle. Needs to manage workload carefully."
        )

    def get_status(self):
        return (
            f"\n {self.name} - Knowledge: {self.knowledge_points}, "
            f"Stress: {self.stress_points}, Determination: {self.determination_points}"
        )
