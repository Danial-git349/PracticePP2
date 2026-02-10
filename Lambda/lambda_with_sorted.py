#Example1
numbers = [5, 2, 9, 1, 7]

sorted_numbers = sorted(numbers)
print(sorted_numbers)

#Example2
numbers = [5, 2, 9, 1, 7]

sorted_numbers_desc = sorted(numbers, reverse=True)
print(sorted_numbers_desc)

#Example3
words = ["apple", "banana", "kiwi", "cherry"]

sorted_by_length = sorted(words, key=lambda x: len(x))
print(sorted_by_length)

#Example4
words = ["apple", "banana", "kiwi", "cherry"]

sorted_by_last_char = sorted(words, key=lambda x: x[-1])
print(sorted_by_last_char)

#Example5
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 30}
]

sorted_people = sorted(people, key=lambda x: x["age"])
print(sorted_people)
