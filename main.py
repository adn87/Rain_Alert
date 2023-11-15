import requests


api_key = "997ad037d80540468b7d78af67b5a659"
MY_LONG = -75.697189
MY_LAT = 45.421532
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
# weather_data["list"][0]["weather"][0]["id"]
weather_slice = weather_data["list"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

if will_rain:
    print("Bring an Umbrella")
# print(weather_slice)
