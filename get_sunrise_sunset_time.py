import requests
import pytz
from datetime import datetime



local_tz = pytz.timezone('America/Los_Angeles')


long = -116.290394
lat = 33.747325
url = 'https://api.sunrise-sunset.org/json?lat={}&lng={}&formatted=0'.format(lat,long)
r = requests.get(url)
sunrise = (r.json().get('results').get('sunrise'))
sunrise = datetime.strptime(sunrise, '%Y-%m-%dT%H:%M:%S+00:00').replace(tzinfo=pytz.utc).astimezone(local_tz)
sunset = (r.json().get('results').get('sunset'))
sunset = datetime.strptime(sunset, '%Y-%m-%dT%H:%M:%S+00:00').replace(tzinfo=pytz.utc).astimezone(local_tz)


sunrise_int = sunrise.hour + 1
sunset_int = sunset.hour - 1

data = [
	sunrise_int,
	sunset_int
]

with open('data.txt', 'w') as f:
    for item in data:
        f.write("%s\n" % item)