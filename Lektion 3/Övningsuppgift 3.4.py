angivet_land = input("Ange ett land: ").lower().capitalize()


if angivet_land == "Sverige" or \
    angivet_land == "Norge" or \
    angivet_land == "Danmark" or \
    angivet_land == "Island" or \
    angivet_land == "finland":
    print (angivet_land, "tillhör Norden!")

elif angivet_land == "England" or \
    angivet_land == "Skottland" or \
    angivet_land == "Whales" or \
    angivet_land == "Nordirland":
    print(angivet_land, "tillhör Storbrittanien")
    
else:
    print("Landet ligger utanför Norden eller Storbrittanien")
