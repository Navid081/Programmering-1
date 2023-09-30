import requests
import json

# API-hantering
url_1 = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
r_1 = requests.get(url_1)
text_1 = r_1.text
text_1 = json.loads(text_1)
print(text_1)
print("-" * 25)

# Användargränssnitt
ui_width = 20
print("-" * ui_width)
print("--- ARIST DB ---".center(ui_width))

# Skriver ut listan på alla artister
for artist in text_1["artists"]:
    print(artist["name"])
print("-" * ui_width)

# Lagra artisternas ID i en dictionary för snabb åtkomst
artist_ids = {}
for elements in text_1["artists"]:
    artist_ids[elements["name"].lower()] = elements["id"]

# Användaren väljer artist
choice = input("Select artist: ").lower()
print("-" * ui_width)

# Kontrollera att valet finns i dictionaryn
if choice in artist_ids:
    artist_id = artist_ids[choice]
    
    # Nu bygger vi URL:en för den specifika artisten
    url_2 = f"https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/{artist_id}"
    r_2 = requests.get(url_2)
    artist_info = r_2.json()

    # Skriv ut artistinformationen
    print(artist_info["name"])
    print("*" * ui_width)
    print(f"Genres: {', '.join(artist_info['genres'])}")
    print(f"Years active: {artist_info['years_active']}")
    print(f"Members: {artist_info['members']}")
else:
    print("Artist not found.")