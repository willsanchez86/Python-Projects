import requests
from twilio.rest import Client

MY_LAT = 40.42118 # Your latitude
MY_LONG = -79.788102 # Your longitude
API_KEY = '********************'

acct_sid = '***************************'
auth_token = '************************'

parameters = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': API_KEY,
    'exclude': 'current,minutely,daily',
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=parameters)
response.raise_for_status()

weather_data = response.json()
hourly_data = weather_data['hourly'][0:12]


will_rain = False

for index in hourly_data:
    if index['weather'][0]['id'] < 700:
        will_rain = True


if will_rain:
    client = Client(acct_sid, auth_token)
    message = client.messages \
        .create(
        body='BRING AN UMBRELLA!',
        from_='+***********',
        to='+**********'
    )
    print(message.status)



