# OOP example with Human classes task

## Human Class

```python
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
```

## Male Class

```python
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
```

## Female Class

```python
# Create child class called Female of the Male class for re-usability of code
from male import Male

class Female(Male):   # inheriting from Male class for efficiency

    def __init__(self):
        super().__init__()
        self.pregnancy = True   # change the attributes to be specific to the female class
        self.test_dominant = False
        self.oest_dominant = True

    def paternity_leave(self):   # cannot remove a method from parent class after inheritance, so edited to be class specific
        pass

    def maternity_leave(self):
        return print("If I have a child, I will get maternity leave")

    def get_married(self):
        return print("I want to get married one day and be a bride")   # editing a method from Male class to be Female class specific

    def give_birth(self):   # define a new function that is only in this child class
        return print("If I get")
```

## Boy Class

```python
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
```

## Girl Class

```python
# Create child class called girl that inherits from the Boy class
from boy import Boy

class Girl(Boy):

    def __init__(self):
        super().__init__()
        self.deep_voice = False
        self.high_voice = True

    def go_to_school(self):
        return print("I go to an all girls school")
```

## Jargon
- ```pass```- this is used as a placeholder, so that code can be edited in its place later
- ```super()```- this function is used to allow a child class to inherit methods and attributes from a parent class
- ```init()```- this function is used to initialise attributes that belong to a class