# person.py

class Person:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}!"

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age
