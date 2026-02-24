# Code #3: Generator Examples

print("=== Generator Examples ===")

# Example 1: Basic generator function
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1
print("Example 1 - Count up to 5:", list(count_up_to(5)))

# Example 2: Generator expression
squares = (x*x for x in range(5))
print("Example 2 - Squares 0-4:", list(squares))

# Example 3: Lazy evaluation
def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
print("Example 3 - Even numbers 0-10:", list(even_numbers(11)))

# Example 4: Using generator in loop
print("Example 4 - Print numbers 1-5:")
for num in count_up_to(5):
    print(num, end=" ")
print()