notes = {
    "Meddelande från skolan" : "Friluftsdag på tisdag",
    "Kom ihåg!" : "Ta bilen till verkstad",
    "Inför tentamen" : "Gör alla instuderingsuppgifter"
}

print("Lägg till artikel:\n")
titel = input("Titel: ")
value = input("Text: ")
notes[f"{titel}"] = f"{value}"

for key in notes:
    print("-------------------")
    print("Titel: ", key)
    print("Text: ", notes[key])
    print("-------------------")