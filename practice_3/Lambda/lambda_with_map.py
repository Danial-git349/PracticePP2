#Example1
def square(x):
    return x * x

numbers = [1, 2, 3, 4]

result = map(square, numbers)

print(list(result))
numbers = [1, 2, 3, 4]

result = map(lambda x: x * x, numbers)
print(list(result))

#Example2
a = [1, 2, 3]
b = [4, 5, 6]

result = map(lambda x, y: x + y, a, b)
print(list(result))

#Example3
strings = ["1", "2", "3"]

numbers = list(map(int, strings))
print(numbers)


#Example4
strings = ["1", "5", "10", "7"]

result = map(lambda x: int(x) * 2, strings)

print(list(result))

#Example5
names = ["Ali", "Sara", "Daniyal"]

result = map(lambda x: "Mr./Ms. " + x, names)

print(list(result))
