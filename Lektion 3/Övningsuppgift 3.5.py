gender = input("kön: ")
hair = input("Hårfärg: ")
eye = input("Ögonfärg: ")

if gender == "man" and hair == "brun" and eye == "brun":
    print("------------------------------")
    print("Du liknar Daniel Radcliffe!")

elif gender == "man" and hair == "röd" and eye == "blå":
    print("------------------------------")
    print("Du liknar Rupert Grint!")

elif gender == "kvinna" and hair == "brun" and eye == "brun":
    print("------------------------------")
    print("Du liknar Emma Watson, Selena Gomez!")

elif gender == "man" and hair == "svart" and eye == "svart":
    print("------------------------------")
    print("Du liknar Robert De Niro!")
    
elif gender == "kvinna" and hair == "blonde" and eye == "grön":
    print("------------------------------")
    print("Du liknar Scarlett Johansson!")
    
elif gender == "man" and hair == "svart" and eye == "blå":
    print("------------------------------")
    print("Du liknar Benedict Cumberbatch!")
    
elif gender == "kvinna" and hair == "röd" and eye == "brun":
    print("------------------------------")
    print("Du liknar Karen Gillan!")
    
elif gender == "man" and hair == "blond" and eye == "blå":
    print("------------------------------")
    print("Du liknar Paul Bettany!")
    
else:
    print("------------------------------")
    print("Finns ej i register!")   