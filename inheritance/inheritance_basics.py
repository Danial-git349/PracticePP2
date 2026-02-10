#Example1
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):  # Dog наследует Animal
    pass

dog = Dog()
dog.speak()
#Example2
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def bark(self):
        print("Woof!")

dog = Dog()
dog.speak()  # метод родителя
dog.bark()   # метод дочернего класса

#Example3
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):  # переопределяем метод
        print("Woof!")

dog = Dog()
dog.speak()

