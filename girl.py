# Create a child class called girl that inherits from the Boy class
from boy import Boy

class Girl(Boy):

    def __init__(self):
        super().__init__()
        self.deep_voice = False
        self.high_voice = True

    def go_to_school(self):
        return print("I go to an all girls school")