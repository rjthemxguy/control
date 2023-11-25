import requests
from datetime import datetime, timedelta

def get_sunrise_sunset(state: str):
    url = f"https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400&formatted=0"

    response = requests.get(url)
    data = response.json()

    sunrise_sunset = {}

    for i in range(7):
        date = datetime.now() + timedelta(days=i)
        date_str = date.strftime("%Y-%m-%d")

        sunrise = data["results"]["sunrise"]
        sunset = data["results"]["sunset"]

        sunrise_sunset[date_str] = {"sunrise": sunrise, "sunset": sunset}

    return sunrise_sunset

# Example usage:
state = "California"
sunrise_sunset = get_sunrise_sunset(state)

for date, times in sunrise_sunset.items():
    print(f"On {date} in {state}, the sunrise is at {times['sunrise']} and the sunset is at {times['sunset']}.")
