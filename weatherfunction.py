import requests
def get_weather(latitude, longitude):
    response=requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m")
    data=response.json()
    return data["current"]["temperature_2m"]
paristemp=get_weather(48.85,2.35)
londontemp=get_weather(51.50,-0.12)
tokyotemp=get_weather(35.68,139.69)

print(f"paris:{paristemp} degree C")
print(f"London:{londontemp} degree C")
print(f"Tokyo:{tokyotemp} degree C")