# funktioner i python

#new*
def addera(tal1, tal2):
    summa = tal1 + tal2
    return summa

# man kan bygga eget bibliotek med funktioner

# att använda funktioner = anrope/call/invoke
addera(1, 2)

# resultatet behöver lagras någonstans
resultat = addera(1, 2)
# print( (addera(1, 2) )
print(resultat)

print("####################################################")


# Exempel från powerpoint
# en funktion som returnerar det minsta talet från en lista
# new*
def minimum(lista):
    minsta_talet = lista[0]
    for i in lista:
        if(minsta_talet > i):
            minsta_talet = i
    return minsta_talet

my_lista = [10, 2, 5, 50]
print(minimum(my_lista))


print("*********************************************")
# Anropa en funktion i en modul:
# Importera modulen.
import utils

# Exempel, referera till modulen.funktionsnamnet()
utils.greet("Lisa", "svensson")

print("------------------------------------")
# Exempel
print(utils.MAX_NUM)
