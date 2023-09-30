import requests
import json

i = input("Ange stad: ")
url = "https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/" + i

r = requests.get(url)
text = r.text
text = json.loads(text)

ui_width = 30
print("-" * ui_width)
print("FORECASTS".center(ui_width))
print("*" * ui_width)
for i in range(len(text["forecasts"])):
    print(text["forecasts"][i]["date"], text["forecasts"][i]["forecast"].capitalize())
print("-" * ui_width)