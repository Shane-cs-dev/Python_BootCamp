import requests
from twilio.rest import Client
#############################################
API_KEY = "c72378ff1b3ba3f0bdc611b52ac8d62e"
ACCOUNT_SID = "ACf1f38f0cb0424eb2b2b2563d35f492da"
AUTH_TOKEN = "39e6877bc1706061c516fb5ee8fb136f"
LAT = 25.032969
LONG = 121.565414
weather_parama = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "cnt": 4
}
#############################################
response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast", params=weather_parama)
response.raise_for_status()
data = response.json()
# print(data)
with open(file="../day-35/current_data.json", mode="w") as current_data:
    json.dump(data, current_data, indent=3)
#############################################
forecast_0 = data["list"][0]["weather"][0]["id"]
# print(data["list"])
#############################################
will_rain = False
for time in data["list"]:
    condition_code = time["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_="+19783500258",
        to="+886965315213",
    )
    print(message.status)


