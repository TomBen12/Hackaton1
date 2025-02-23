from narrator import Narrator

narrator = Narrator()


def format_name_input():
    while True:
        user_input = input("Enter your name: ").strip()
        if not user_input:
            narrator.not_valid_name()
        elif len(user_input) >= 15:
            narrator.not_valid_name()
        elif not user_input.isalpha():
            narrator.not_valid_name()
        else:
            return user_input

def format_class_choice():
    valid_classes = {"H", "S", "G"}

    while True:
        user_input = input("Choose your class [H/S/G]: ").strip().upper()
        
        if not user_input:
            narrator.not_valid_choice()
        elif user_input not in valid_classes:
            narrator.not_valid_choice()
        else:
            return user_input
