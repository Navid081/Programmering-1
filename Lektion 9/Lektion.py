# En klass som beskriver rektanglar

# new'
class Rectangle():
    # Attribut
    length = 0
    width = 0
    
    #Metdoer
    def area(self):
        return self.length * self.width
    
    def omkrets(self):
        return  self.length * 2 + self.width * 2
        
r1 = Rectangle()
print(r1.width)
print(r1.length)

# Ändra attribut
r1.width = 5
r1.length = 10
print("---- r1 ----")
print("Bredd: ", r1.width)
print("Längd: ", r1.length)
print("Area: ", r1.area())

r2 = Rectangle()
r2.width = 10
r2.length = 10
print("---- r2 ---- ")
print("r2 area: ", r2.area())

r3 = Rectangle()
r3.width = 50
r3.length = 100
print("---- r3 ----")
print("r3 area: ", r3.area())
print("r3 omkrets: ", r3.omkrets())

## Tänk på att skapa en lista av objekt, 52 kort till den individuella uppgiften.
    