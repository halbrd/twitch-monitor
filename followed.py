import requests
import json

CLIENT_ID = "0gdtvatdi4u362gn7x4vpvrw3y79ka"

userId = "44322889"
url = "https://api.twitch.tv/kraken/users/{}/follows/channels".format(userId)
headers = {
    "Accept": "application/vnd.twitchtv.v5+json",
    "Client-ID": CLIENT_ID
}

r = requests.get(url, headers=headers)

out = json.dumps(json.loads(r.text), indent=4)
print(out)
