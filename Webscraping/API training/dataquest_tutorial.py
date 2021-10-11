import requests
import json
from datetime import datetime

page1 = requests.get("http://api.open-notify.org/astros.json")


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=True)
    print(text)


# jprint(page1.json())

params = {
    "lat": 40.71,
    "lon": -74
}
page2 = requests.get("http://api.open-notify.org/iss-pass.json", params=params)
pass_times = page2.json()['response']
for d in pass_times:
    time = d['risetime']
    time = datetime.fromtimestamp(time)
    print(time)