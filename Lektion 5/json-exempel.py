import json
import os

# Öppna filen för läsning
with open("numbers.json") as f:
    numbers = f.read()
    numbers = json.loads(numbers)
print(numbers)
print("-" * 20)
# Dubblera varje element
double_list = []
for i in numbers:
    double_list.append(i * 2)
print(double_list)

# Skriv in dubbleringarna.
with open("numbers.json", "w") as f:
    double_list = json.dumps(double_list)
    f.write(double_list)
