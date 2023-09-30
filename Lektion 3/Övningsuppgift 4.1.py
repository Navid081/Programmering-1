nummer = 0
minsta = None
största = None
summa = 0
antal_tal = 0


while True:
    nummer = int(input("ange ett tal: "))
    minsta = min(nummer)
    print(minsta)
    
    if nummer < 0:
        break

