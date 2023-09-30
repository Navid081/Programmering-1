"""
Övning – Fixa koden
myScore = input("Your score: ")
if myScore > 99:
print("Winner!")
else:
print("Try again 😭")
TypeError: '>' not supported between instances of 'str' and 'int'
"""""

# Lösning – Fixa koden
#myScore = input("Your score: ")
myScore = int(input("Your score: "))

if myScore > 99:
    print("Winner!")
else:
    print("Try again ")
#TypeError: '>' not supported between instances of 'str' and 'int'

# man kan fixa problemet på olika platser som t ex, man kan casta det på rad 16