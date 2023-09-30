# 9.1.1
print("Uppgift: 9.1.1")
print("--------------")

sum = 0

for i in range(1000001):    # för varje värde "i" har i loopen, adderas det värdet i variabeln "sum".
    sum += i
print(sum)

# 9.1.2
print()
print("Uppgift: 9.1.2")
print("--------------")

summa = 0

for i in range(1, 501, 2):  # "i" får värdet av alla udda heltal från 1 - 500
    summa += i              # varje värde "i" (udda tal) har adderas det värdet i variabeln "summa"
print(summa)