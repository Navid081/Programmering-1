print("Övning 3.2")
print("------------------")

name = input("Vad heter du?: ")
age = int(input("Ange din ålder: "))

if age == 1:
    print(name, "behöver 14h sömn")
elif age == 2:
    print(name, "behöver 13h sömn")
elif age == 3:
    print(name, "behöver 12h sömn")
elif age == 4:
    print(name, "behöver 11.5h sömn")
elif age == 5 or age == 6:
    print(name, "behöver 10 sömn ")
elif age == 7:
    print(name, "behöver 10h sömn")
elif age == 8 or age == 9 or age == 10:
    print(name, "behöver 10h sömn")
elif age == 11:
    print(name, "behöver 9.5h sömn")
elif age in range(12, 15):
    print(name, "behöver 9h sömn")
elif age == 16:
    print(name, "behöver 8.5h sömn")
elif age == 17 or age >= 17:
    print(name, "behöver 8h sömn")
        
         

        


