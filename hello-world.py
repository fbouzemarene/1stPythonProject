import requests
import json
import pprint

url = "https://api.mist.com/api/v1/sites/addd1bff-4b9c\
-44ee-a6c0-87920b7a9aa0/wlans"
url2 = "https://api.mist.com/api/v1/sites/addd1bff-4b9c\
-44ee-a6c0-87920b7a9aa0/wlans"
url3 = "https://api.mist.com/api/v1/sites/addd1bff-4b9c\
-44ee-a6c0-87920b7a9aa0/wlans"

headers = {
    "Content-Type": "application/json",
    "Authorization": "ej09KqSG35Q2TzbodP76AHWRV4FcJNHx4kpSj\
    FnR0GmJ4T3y3cjoqq070q9Si1ecGDAQYMwDC1o0n4aYCOcrXM8QbJR5KgtA",
}

results = requests.get(url, headers=headers)
wlans = json.loads(results.text)

pprint.pprint(wlans)

# for wlan in wlans:
#    print(wlan["ssid"], ">", wlan["id"])
