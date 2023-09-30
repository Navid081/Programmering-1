# Ett annat sätt att lösa uppgift 12.4

notes = {
    "Meddelande från skolan" : "Friluftsdag på tisdag",
    "Kom ihåg!" : "Ta bilen till verkstad",
    "Inför tentamen" : "Gör alla instuderingsuppgifter"
}

key = input("Titel: ")
value = input("Text: ")

notes[key] = value

for keys in notes:
    print("----------------------")
    print("Title: ", keys)
    print("Text: ", notes[keys])
    