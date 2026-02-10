#Example1
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        super().speak()  # вызываем метод родителя
        print("Woof!")

dog = Dog()
dog.speak()

#Example2

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # вызываем конструктор родителя
        self.breed = breed

dog = Dog("Buddy", "Labrador")
print(dog.name)
print(dog.breed)

