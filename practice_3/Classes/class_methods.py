#Example1
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name + " says Woof!")

dog1 = Dog("Buddy")
dog1.bark()
#Example2
class Dog:
    species = "Canine"

    @classmethod
    def show_species(cls):
        print("All dogs are", cls.species)

Dog.show_species()

#Example3
class Dog:
    @staticmethod
    def info():
        print("Dogs are loyal animals")

Dog.info()
#Символ @ в Python называется декоратор. Он “оборачивает” функцию или метод и изменяет/добавляет к ней поведение.

