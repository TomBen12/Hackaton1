class Student:
    def __init__(self):
        self.name = ""
        self.type = ""
        self.knowledge_points = 0
        self.determination_points = 0

    def set_name(self, name):
        self.name = name

    def adjust_knowledge(self, amount):

        self.knowledge_points += amount

    def adjust_determination(self, amount):

        self.determination_points += amount

    def set_type(self, type):
        self.type = type
