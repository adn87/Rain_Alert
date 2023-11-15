import requests



api_key = "997ad037d80540468b7d78af67b5a659"
# api_key2 = "f1fe3508cdc2fe6512875d3f8f70e37b"
MY_LONG = 45.079163
MY_LAT = 23.885942
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key
}

response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)
response.raise_for_status()
data = response.json()
print(data)

# https://api.openweathermap.org/data/3.0/onecall?lat=24.71&lon=46.68&appid=f1fe3508cdc2fe6512875d3f8f70e37b