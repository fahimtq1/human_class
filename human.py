# Create parent class called Human
class Human:

    def __init__(self):  # initialise the attributes that will be part of this class and inherited by each child class
        self.eyes = True
        self.nose = True
        self.mouth = True

    def sleep(self, name):   # method to show you can have variables that are specific to methods that don't belong to the whole class
        return print(f"{name.capitalize()} likes to sleep for 8 hours")

    def eat(self, no_meals):   # once an object of the class is made, the method requires another input
        return print(f"I like to eat {no_meals} meals a day")

    def drink(self):
        fav_drink = input("What is your favourite drink? ")
        return print(f"I like to drink {fav_drink}")



