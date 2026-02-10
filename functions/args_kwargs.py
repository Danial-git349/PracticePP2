#Example1
def add_numbers(*args):
    print(args)
    print(sum(args))

add_numbers(1, 2, 3)
add_numbers(5, 10, 15, 20)
#Example2
def multiply_all(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply_all(2, 3, 4))

#Example3
def print_info(**kwargs):
    print(kwargs)

print_info(name="Ali", age=20, city="Almaty")

#Example4
def show_profile(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

show_profile(username="admin", role="moderator")

#Example5
def example(a, b, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)

example(1, 2, 3, 4, 5, x=10, y=20)
