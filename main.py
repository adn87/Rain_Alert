import requests
import smtplib

MY_EMAIL = "[your own email]"
MY_PASS = "[your own password]"

api_key = "[Your Own API key"
MY_LONG = 45.079163
MY_LAT = 23.885942
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["list"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="[recipient email]",
                            msg="Subject: It's raining\n\nit's going to rain take an umbrella"
                            )
