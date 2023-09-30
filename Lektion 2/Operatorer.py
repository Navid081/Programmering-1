#operatorer
print(1+2)
print(1-2)
print(1*2)
print(1/2)
print("Heltalsdivision -", 10//3) #Dubbla divisionstecken gör kvoten till ett heltal, heltalsdivision
print("Modulo -", 10%3) #Modulo, skriver ut resten av heltalsdivision. //
print("Potenser -", 2**3) # dubbla gånger tecken = upphöjt till.
print("------------------------------------")

# x = x + 3 --> x += 3
x = 3
x += 3
print(x)

y = 6
y -= 3
print(y)

# Programmering har samma prioriteringsregler som i matte
# Parenteser
# Potenser
# division och multiplikation
# addition och subtraktion

z = int(3.14) # x blir 3
z2 = float("5.6") # y blir 5.6

print(int(3.9)) # float typomvandla/konverteras till ett heltal
print(float("3.233")) # typomvlandas/konvertas till ett float
