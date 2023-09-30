# Öppna en befintlig fil. Default är att den öppnas i läsläge.
# r- i början av strängen står för "rå", backslash tolkas inte då inte som escape-sekvens.
# utf-8, texten i dokumentet är kodad konstigt, utf-8 öppnar filen med rätt kodning.
textfil = open(r"C:\Users\Navid\Desktop\Datordelar.txt", encoding="utf-8")

# Läs innehållet
content = textfil.read()

# Skriv ut innehållet
print("Före: ")
print(content)

# Stäng filen
textfil.close()
print("*****************************************")


# Öppna samma fil, denna gång i append-läge för att lägga till text.
textfil_2 = open(r"C:\Users\Navid\Desktop\Datordelar.txt", "a", encoding="utf-8")

# lägg till text.
textfil_2.write("\nVäska\nLaddare")

#Stänger filen som är öppnad i appendläge
textfil_2.close()
print("*****************************************")

# Öppna filen igen i läsläge, för att skriva ut dess nya innhåll. antingen genom "r" eller ingenting.
# den öppnas i läs-läge ("r", read) av default.
textfil_3 = open(r"C:\Users\Navid\Desktop\Datordelar.txt", encoding="utf-8")

# Läs innehållet
content_3 = textfil_3.read()

# Skriv ut innehållet
print("Efter: ")
print(content_3)

#Stäng filen
textfil_2.close()
