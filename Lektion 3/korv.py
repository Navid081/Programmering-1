vanlig2 = int(input("Hur många vill äta 2 vanliga korvar?: "))
vanlig3 = int(input("Hur många vill äta 3 vanliga korvar?: "))
vegansk2 = int(input("Hur många vill äta 2 veganska korvar?: "))
vegansk3 = int(input("Hur många vill äta 3 veganska korvar?: "))
drycker = vanlig2 + vanlig3 + vegansk2 + vegansk3 # antalet elever
print("Hej hej hej")

a = (vanlig2*2) + (vanlig3*3) # antalet vanliga korvar
b = (vegansk2*2) + (vegansk3*3) # antalet veganska korvar

vanligpkt = round(a / 8)           #hur många vanliga paket avrundad uppöjt
veganskpkt = round(b / 4)          #hur många vanliga paket avrundad uppöjt


pris = (vanligpkt*20.95) + (veganskpkt * 34.95)
kostdryck = drycker * 13.95
print("Kostnaden för maten blir: ", pris, "kr")
print("Kostnaden för drycken blir: ", kostdryck,"kr")

