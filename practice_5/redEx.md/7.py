def snake_to_camel(snake_str):
    # Split the string by underscore
    words = snake_str.split('_')
    
    # Keep first word lowercase, capitalize the rest
    camel_case = words[0] + ''.join(word.capitalize() for word in words[1:])
    
    return camel_case


# Test examples
test_strings = [
    "hello_world",
    "python_programming",
    "convert_snake_case",
    "example"
]

for s in test_strings:
    print(f"{s} -> {snake_to_camel(s)}")