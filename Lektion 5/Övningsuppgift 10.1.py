import os
import time

ui_width = 50
message = ""

while True:
    # Rensa terminalen
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
        
    # Skylten
    print("|" + "-" * ui_width + "|")
    print("|" + " ".center(ui_width) + "|")
    print("|" + f"--- {message} ---".center(ui_width) + "|")
    print("|" + " ".center(ui_width) + "|")
    print("|" + "-" * ui_width + "|")
    print("||".center(ui_width))
    print("||".center(ui_width))
    print("||".center(ui_width))
    print("||".center(ui_width))
    print("-" * ui_width)
    print("C | Change sign message".ljust(ui_width))
    print("E | Exit program.".ljust(ui_width))

    # 2. Användarinmatning
    choice = input(">: ").upper()
    if choice == "E":
        print("Exiting program...")
        time.sleep(3)
        if os.name == "nt":
            os.system("cls")
        elif os.name == "posix":
            os.system("clear")
        exit()
    elif choice == "C":
        message = input("Enter sign message: ")
    else:
        print("Invalid input. Use 'C' to create a message or 'E' to exit.")
        input("Press enter to start again")
        
# 3. Filhantering
    with open("sign.txt", "a") as f:
        f.write(message + "\n")


