# Count the occurrences of 'o' in the string
string_example = "hello world"
print(string_example.count("o"))

# Check if the string ends with 'world'
print(string_example.endswith("world"))

# Find the position of 'lo' in the string
print(string_example.find("lo"))

# Find the index of 'lo' in the string
print(string_example.index("lo"))

# Join the elements of a list with a hyphen
list_example = ["a", "b", "c"]
print("-".join(list_example))

# Replace 'world' with 'Python' in the string
print(string_example.replace("world", "Python"))

# Split the string into a list of words
print(string_example.split())

# Split a multi-line string into a list of lines
multi_line_string = "Hello\nWorld"
print(multi_line_string.splitlines())

# Check if the string starts with 'hello'
print(string_example.startswith("hello"))

# Strip leading and trailing spaces from the string
whitespace_string = "   hello world   "
print(whitespace_string.strip())