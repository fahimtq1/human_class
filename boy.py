# Create class that inherits from Human class
from human import Human

class Boy(Human):

    def __init__(self):
        super().__init__()
        self.school = True
        self.deep_voice = True
        self.high_voice = False

    def play(self):
        return print("I like to play all day")

    def go_to_school(self):
        return print("I go to an all boys school")

    def homework(self):
        return print("I hate doing homework")