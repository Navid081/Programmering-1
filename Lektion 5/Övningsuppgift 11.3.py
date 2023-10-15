import os
import json
from time import sleep

# Terminalrensning
def clear_terminal():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        clear_terminal()

numbers = []

# Försöker läsa från tidigare fil om den finns
# Om den inte finns går den vidare.
try: 
    with open("numbers.txt", "r") as f:
        read_numbers = f.read()
        numbers = json.loads(read_numbers)
        if 0 in numbers:    # När man avslutar programmet sparas talet 0 i listan och sedan
            numbers.remove(0) # presenteras det vid nästa körning, här tas 0 bort så att det inte presenteras
except FileNotFoundError:
    pass

while True:
    # Användargränsnitt
    ui_width = 20
    print(".: intMEMORIZER :.")
    print("*" * ui_width)
    for i in numbers:   # Skriver ut alla tal i listan
        print("*", i)
    print("-" * ui_width)
    print("SUMM: ", sum(numbers))
    print("-" * ui_width)
    print("  enter a number")
    print("0 closing script")
    print("-" * ui_width)
    
    # Om det inte går att omvandla till int
    # alltså om man matar in en sträng istället hanteras det här.
    try:
        choice = int(input("> "))
        if choice in numbers:
            print("The number is already added, enter new number")
            input("\nPress enter to continue ")
        else:
            numbers.append(choice)
            
    except ValueError:
        print("ValueError: Enter number")
        input("\nPress enter to continue ")
        clear_terminal()
        continue
    
    if choice == 0:
        print("Exiting program...")
        sleep(3)
        break
    
    clear_terminal()
    
# När programmet avslutas läggs talen i numbers till i slutet på filen.
# Om filen inte finns skapas det en.
with open("numbers.txt", "a", encoding="utf-8") as f:
    added_numbers = json.dumps(numbers)
    f.write(added_numbers)

