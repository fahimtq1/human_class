# Create a child class called Female of the Male class for re-usability of code
from male import Male

class Female(Male):   # inheriting from Male class for efficiency

    def __init__(self):
        super().__init__()
        self.pregnancy = True   # change the attributes to be specific to the female class
        self.test_dominant = False
        self.oest_dominant = True

    def paternity_leave(self):   # cannot remove a method from parent class after inheritance, so edited to be class specific
        return print("I don't get paternity leave, as a woman if I have a child I get materinity leave")

    def maternity_leave(self):
        return print("If I have a child, I will get maternity leave")

    def get_married(self):
        return print("I want to get married one day and be a bride")   # editing a method from Male class to be Female class specific

    def give_birth(self):   # define a new function that is only in this child class
        return print("If I get")
