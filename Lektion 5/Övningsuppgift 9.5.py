# 9.5
# Köer - först in, först ut. Dvs, index positionen "0" ska ut först.

# Stack - Sist in, först ut.
# metoderna som används är:
# push / .append() - för att lägga till.
# pop / .pop() - för att ta bort.

import os

lista = [
    "Mercedes",
    "Volvo",
    "Toyota"
]

ui_width = 25

while True:
    os.system("cls")                    # rensa terminalen efter varje loop
    print(".: STACKMASTER v1.33.7 :.")
    print("-" * ui_width)
    for name in lista:                  # iterera över varje element (bilmärke) i lista
         print("-", name)               # skriv ut varje element
    print("-" * ui_width)
    print(" | MENU |".center(ui_width))     # centrerar MENU
    print("-" * ui_width)
    print("push | Push element to stack")
    print("pull | Pull element to stack")
    print("exit | Exit program")
    print("-" * ui_width)
    choice = input("Vad vill du göra?: ").lower()
    if choice == "push":
        push = input("Vad vill du lägga till?: ")
        lista.append(push)                              # lägger till det som sparas i push
    elif choice == "pull":
        lista.pop()                                     # tar bort sista elementet i listan
    elif choice == "exit".lower():
        break

# Uppgiften är löst men kan förbättras med t ex. felhantering, bekräfta att åtgärder lyckades..det finns säkert fler.
#