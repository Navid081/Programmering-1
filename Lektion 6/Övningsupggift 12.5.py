notes = {
    "Meddelande från skolan" : "Friluftsdag på tisdag",
    "Kom ihåg!" : "Ta bilen till verkstad",
    "Inför tentamen" : "Gör alla instuderingsuppgifter"
}
print("- Före: ")
print("***********************")
for keys in notes:
    print("Titel: " + keys)
    print("Text: " + notes[keys])
    print("- - - - - - - - - - -")
    
key = input("Ta bort artikel, ange titel: ")
del notes[key]

print("-----------------------")
print("- Efter: ")
print("***********************")
for keys in notes:
    print("Titel: " + keys)
    print("Text: " +  notes[keys])
    print("- - - - - - - - - - -")