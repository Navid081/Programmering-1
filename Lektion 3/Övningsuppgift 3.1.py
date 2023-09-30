# Övning 3.1
print("---Övning 3.1---")
print("-------------------------")

tal1 = float(input("Ange ett tal: "))
tal2 = float(input("Ange ett till tal: "))
tal3 = float(input("Ange ett sista tal: "))

if tal1 >= tal2 and tal1 >= tal3:
    storsta_tal = tal1
elif tal2 >= tal1 and tal2 >= tal3:
    storsta_tal = tal2
else: 
    storsta_tal = tal3
    
print("största talet är: ", storsta_tal)