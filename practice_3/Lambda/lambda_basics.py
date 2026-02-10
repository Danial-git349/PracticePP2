#Example1
def add(a, b):
    return a + b

add_lambda = lambda a, b: a + b

print(add(2, 3))
print(add_lambda(2, 3))
#Example2
print((lambda x: x + 10)(5))

#Example3
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"

print(is_even(6))
print(is_even(7))

#Example4
def apply(func, value):
    return func(value)

print(apply(lambda x: x * 2, 5))

#Example5
def check(func, number):
    return func(number)

result = check(lambda x: x > 10, 15)
print(result)
