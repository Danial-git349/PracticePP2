#Example1
numbers = [1, 2, 3, 4, 5, 6]

# Выбираем только чётные числа
evens = filter(lambda x: x % 2 == 0, numbers)

print(list(evens))

#Example2
words = ["cat", "lion", "elephant", "dog"]

long_words = filter(lambda x: len(x) > 3, words)

print(list(long_words))

#Example3
numbers = [-5, 0, 3, 8, -2]

positive_numbers = filter(lambda x: x > 0, numbers)

print(list(positive_numbers))

#Example4
def is_odd(n):
    return n % 2 != 0

numbers = [1, 2, 3, 4, 5]
odds = filter(is_odd, numbers)

print(list(odds))

#Example5
words = ["apple", "banana", "cherry", "avocado", "pear"]

# Оставляем только слова, в которых есть буква "a"
words_with_a = filter(lambda x: "a" in x, words)

print(list(words_with_a))

