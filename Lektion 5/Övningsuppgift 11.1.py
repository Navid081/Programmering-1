import json


random_stuff = [1337, 13.37, "Ååh Yää!"]

# Skapar en ny fil
with open("C:\Dokument\SKOLA\DevOps\Programmering 1\Lektion 5\Övningsuppgift 11.1.json", "w") as f:
    random_stuff = json.dumps(random_stuff) # typomvandlar list till string.
    f.write(random_stuff)       # skriver in.

# Öppnar filen, default-läge är read, behöver inte anges.
with open("C:\Dokument\SKOLA\DevOps\Programmering 1\Lektion 5\Övningsuppgift 11.1.json") as f:
    contents = f.read() # lagrar innehållet i variabeln.
print(contents)



