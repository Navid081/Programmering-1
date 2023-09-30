import requests
import json


i = int(input("Ange ett heltal: "))
url = "https://4bbh01oqwj.execute-api.eu-north-1.amazonaws.com/numcheck?integer=" + i

# API-hantering
r = requests.get(url)
text = r.text
text = json.loads(text)
print(text)

print("----------------------")

i = str(i)

# Om det är ett jämt tal
even = text["even"]
if even == True:
    even = "jämnt"
else:
    even = "ojämt"

# Om det är ett primtal
primtal = text["prime"]
if primtal == True:
    primtal = "är ett primtal."
else:
    primtal = "är inte ett primtal."

faktor = (text["factors"])

print(i + " är ett ", even + " nummer. Numret " + primtal + " Numrets faktorer är", faktor)

# Utskriften för faktorerna blir [....], dvs inom hakparenteser.
# 
