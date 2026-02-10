#Example1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

print(p1.name, p1.age)
print(p2.name, p2.age)
#Example2
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is " + self.name)

p1 = Person("Charlie")
p1.greet()

#Example3
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Alice")
print(p1.name)  # Alice

p1.name = "Bob"
print(p1.name)  # Bob

#Example4
class Cat:
    def __init__(self, name):
        self.name = name  # имя кошки

my_cat = Cat("Mittens")
print(my_cat.name)

#Example5
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

my_book = Book("Harry Potter", "J.K. Rowling")
print(my_book.title)
print(my_book.author)

