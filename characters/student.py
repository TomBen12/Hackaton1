class Student:
    def __init__(self):
        self.name = ''
        self.knowledge_points = 0
        self.stress_points = 0
        self.determination_points = 100

    def set_name(self, name):
        self.name = name

    def adjust_stress(self, amount):

        self.stress_points += amount

    def adjust_knowledge(self, amount):

        self.knowledge_points += amount

    def adjust_determination(self, amount):

        self.determination_points += amount

    def get_status(self):

        return (
            f"\n {self.name} - Knowledge: {self.knowledge_points}, "
            f"Stress: {self.stress_points}, Determination: {self.determination_points}"
        )















