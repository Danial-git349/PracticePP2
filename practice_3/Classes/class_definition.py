#Example1
class Dog:
    pass  

my_dog = Dog()
print(my_dog)
#Example2
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_dog = Dog("Buddy", 3)
print(my_dog.name)
print(my_dog.age)

#Example3
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(self.name + " says Woof!")

my_dog = Dog("Buddy")
my_dog.bark()

#Example4
class Dog:
    def __init__(self, name):
        self.name = name  # имя собаки

    def bark(self):
        print(self.name + " says Woof!")

my_dog = Dog("Buddy")
my_dog.bark()

#Example5
class Car:
    def __init__(self, brand):
        self.brand = brand  # марка машины

    def info(self):
        print("This car is a", self.brand)

my_car = Car("Toyota")
my_car.info()

