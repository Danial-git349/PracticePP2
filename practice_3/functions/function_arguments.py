#example1
def greet(name, age):
    print("Name:", name)
    print("Age:", age)

greet(age=20, name="Ali")

#example2
def power(base, exponent=2):
    print(base ** exponent)

power(5)
power(5, 3)

#example3
def change_number(x):
    x = 100

num = 10
change_number(num)
print(num)

#example4
def add_item(items):
    items.append("apple")

fruits = ["banana"]
add_item(fruits)
print(fruits)

#example5
def divide(a, b):
    if b == 0:
        print("Error: division by zero")
        return
    print(a / b)

divide(10, 2)
divide(10, 0)


