import os
import csv      # Hitta ej länken till vart jag fick det här ifrån.
import time     # Hitta ej länken, används på rad 61

ui_width = 40

# Användargränssnitt och terminalrensning
while True:
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    print("*" * ui_width)
    print(" .: PEOPLES DATABASE :. ")
    print("-" * ui_width)
    print("get_id | Get person by ID")
    print("scan_f | List people by FORENAME")
    print("scan_s | List people by SURENAME")
    print("scan_a | List all people in Database")
    print("exit   | Exit program")
    print("*" * ui_width)
    
    # Användarinmatning och filhantering, öppnas i read-läge, trots att det inte behövs då det är default.
    with open("Database.csv", "r", encoding="utf-8") as f:
        content = csv.reader(f, delimiter=",")  # google

        choice = input(">: ").lower()
        print("-" * ui_width)
        
        if choice == "scan_f":
            forename = input("FORENAME: ").capitalize()     # första bokstaven blir versal.
            print("-" * ui_width)
            for row in content:         # itererar över varje rad i filen
                if forename in row:     # om förnamnet förekommer i raden
                    row = ", ".join(row)         # omformatterar listorna med strängar i csv filen till 
                    print(row)
            input("\nPress enter to continue\n")    # Bekräftelse innan terminalen rensas.
            
        elif choice == "scan_s":
            surname = input("SURNAME: ").capitalize()
            print("-" * ui_width)
            for row in content:
                if surname in row:
                    row = ", ".join(row)
                    print(row)
            input("\nPress enter to continue\n")
        
        elif choice == "get_id":
            get_id = input("ID: ")
            print("-" * ui_width)
            for row in content:
                if get_id in row:                   # Varje rad i csv-filen är en lista. Varje element skrivs ut med indexering.
                    print("ID: ".ljust(20), row[0]) #.ljust() används för att stapla utskrifterna ovanpå varandra.
                    print("FORENAME: ".ljust(20), row[1])
                    print("SURNAME: ".ljust(20), row[2])
                    print("GENDER: ".ljust(20), row[3])
                    print("YEAR: ".ljust(20), row[4])
            input("\nPress enter to continue\n")
        
        elif choice == "scan_a":
            with open("Database.csv", "r", encoding="utf-8") as f:
                content = csv.reader(f, delimiter=",")
                for row in content:
                    print(", ".join(row))
                    input("\nPress enter to continue\n")
        
        elif choice == "exit":
            from time import sleep
            print("Avslutar programmet...")
            sleep(5)
            if os.name == "nt":
                os.system("cls")
            elif os.name == "posix":
                os.system("clear")
            exit()
        
        else:
            print("Wrong input. Try again")
            input("\nPress enter to continue\n")
            
# Avslutningsvis:
# Om man först matar in t ex. scan_f, kan man när den frågar efter FORNAME ange id nummer istället för förnamn.
# Det beror på att programmet skriver ut hela raden för det man söker efter vid andra inmatningen.

