#Example1
def add(a, b):
    return a + b

result = add(3, 4)
print(result)

#Example2
def calculate(a, b):
    return a + b, a - b, a * b

sum_, diff, product = calculate(10, 5)
print(sum_, diff, product)

#Example3
def check_age(age):
    if age < 18:
        return "Access denied"
    return "Access granted"

print(check_age(16))
print(check_age(20))

#Example4
def square(x):
    return x * x

def sum_of_squares(a, b):
    return square(a) + square(b)

print(sum_of_squares(2, 3))

#Example5
def abs_value(x):
    if x < 0:
        return -x
    return x

print(abs_value(-10))
print(abs_value(7))
