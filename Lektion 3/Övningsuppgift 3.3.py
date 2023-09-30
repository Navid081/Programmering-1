# 6.1

text = input("Ange en text: ")
bokstav = input("Ange bokstav: ")

antal = 0
while True:
    if bokstav in text:
        antal += 1
        print(bokstav, "förekommer", antal, "gånger")
    break