# Övn 10.2

tal_0 = 0
tal_1 = 0
tal_2 = 0
tal_3 = 0
tal_4 = 0
tal_5 = 0
tal_6 = 0
tal_7 = 0
tal_8 = 0
tal_9 = 0

with open(r"C:\Users\Navid\Desktop\Programmering 1\Lektion 5\numbers.csv", "r") as numbers:
    for number in numbers:
        cleaned_number = number.strip()
        if cleaned_number == "0":
            tal_0 += 1
        elif cleaned_number == "1":
            tal_1 += 1
        elif cleaned_number == "2":
            tal_2 += 1
        elif cleaned_number == "3":
            tal_3 += 1
        elif cleaned_number == "4":
            tal_4 += 1
        elif cleaned_number == "5":
            tal_5 += 1
        elif cleaned_number == "6":
            tal_6 += 1
        elif cleaned_number == "7":
            tal_7 += 1
        elif cleaned_number == "8":
            tal_8 += 1
        elif cleaned_number == "9":
            tal_9 += 1

print("0: ", tal_0)
print("1: ", tal_1)
print("2: ", tal_2)
print("3: ", tal_3)
print("4: ", tal_4)
print("5: ", tal_5)
print("6: ", tal_6)
print("7: ", tal_7)
print("8: ", tal_8)
print("9: ", tal_9)

summa = tal_0 + tal_1 + tal_2 + tal_3 + tal_4 + tal_5 + tal_6 + tal_7 + tal_8 + tal_9
print("*****************************")
print("Totalt antal tal :", summa)


