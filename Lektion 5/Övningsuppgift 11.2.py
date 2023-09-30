import json

my_chars = '["abc", "\u00e5\u00e4\u00f6", "123"]'
my_chars = json.loads(my_chars)

for element in my_chars:
    print(element)