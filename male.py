# Create Male child class of Human parent class
from human import Human

class Male(Human):

    def __init__(self, job):
        super().__init__()   # super is used to inherit everything from parent class and initialises it in the child class
        self.pregnancy = False
        self.test_dominant = True
        self.oest_dominant = False
        self.__job = job   # private info that is only stored in this class

    def go_to_work(self):
        return print("I like to work to earn money")

    def paternity_leave(self):
        return print("If I have a child, I will get paternity leave")

    def get_married(self):
        return print("I want to get married one day and be a groom")
