import requests
from twilio.rest import Client

api_key = "45dc8efe4f1b82c0ad5318545b46f0fd"
account_sid = "ACbb5fe55657e67c77a74de2b721985f53"
auth_token = "ef77490674686da58f602685b99395e8"

params = {
    "lat": 54.35,
    "lon": 18.64,
    "exclude": "current,minutely,daily,alerts",
    "appid": api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=params)
response.raise_for_status()

weather_data = response.json()
twelve_hours_data = weather_data["hourly"][:12]

will_rain = False

for hour in twelve_hours_data:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂️ .",
        from_='+18304520698',
        to='+48883965983'
    )

    print(message.status)

