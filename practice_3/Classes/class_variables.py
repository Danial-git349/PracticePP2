#Example1
class Dog:
    def __init__(self, name):
        self.name = name  # переменная объекта

dog1 = Dog("Buddy")
dog2 = Dog("Charlie")

print(dog1.name)  # Buddy
print(dog2.name)  # Charlie

#Example2
class Dog:
    species = "Canine"  # переменная класса

dog1 = Dog("Buddy")
dog2 = Dog("Charlie")

print(dog1.species)  # Canine
print(dog2.species)  # Canine

# Меняем у класса
Dog.species = "Wolf"
print(dog1.species)  # Wolf
print(dog2.species)  # Wolf

#example3 
class Dog:
    species = "Canine"  # переменная класса

    def __init__(self, name):
        self.name = name  # переменная объекта

dog1 = Dog("Buddy")
dog2 = Dog("Charlie")

print(dog1.name, dog1.species)  # Buddy Canine
print(dog2.name, dog2.species)  # Charlie Canine

