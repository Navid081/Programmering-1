notes = {
    "Meddelande från skolan" : "Friluftsdag på tisdag",
    "Kom ihåg!" : "Ta bilen till verkstad",
    "Inför tentamen" : "Gör alla instuderingsuppgifter"
}

print("-----------------------")
print("Anteckningar: ")
print("-----------------------")
for anteck in notes:
    print("-", anteck)
print("-----------------------")
choice = input("Vilken anteckning vill du veta mer om?: ")
print("-----------------------")

if choice in notes:
    print(notes[choice])
    print("-----------------------")
elif choice not in notes:
    print("Fel: Anteckning finns inte")
    print("-----------------------")
