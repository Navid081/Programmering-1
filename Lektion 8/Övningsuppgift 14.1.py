# 1 mile = 1.609344 kilometers
# 1 km = 0.621371192 miles

def km_to_mile(km):
    mile = km * 0.621371192
    return mile

def mile_to_km(mile):
    km = mile * 1.609344
    return km

distans = input("Ange distans: ")
siffror = ""

for tecken in distans:  # går igenom alla tecken
    if tecken.isdigit(): # om tecknet är ett tal
        siffror += tecken   # läggs talet till i variabeln
        
siffror = int(siffror)

if "km" in distans:
    print(f"{distans} blir till {km_to_mile(siffror)} miles")

elif "mile" in distans or "miles" in distans:
    print(f"{distans} blir till {mile_to_km(siffror)} km")
    