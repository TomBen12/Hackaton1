class Student:
    def __init__(self):
        self.name = ""
        self.knowledge_points = 0
        self.determination_points = 100

    def set_name(self, name):
        self.name = name

    def adjust_knowledge(self, amount):

        self.knowledge_points += amount

    def adjust_determination(self, amount):

        self.determination_points += amount
