import requests
import json

CLIENT_ID = "0gdtvatdi4u362gn7x4vpvrw3y79ka"

def getFollows(userId):
	url = "https://api.twitch.tv/kraken/users/{}/follows/channels".format(userId)
	headers = {
		"Accept": "application/vnd.twitchtv.v5+json",
		"Client-ID": CLIENT_ID
	}

	total = json.loads(requests.get(url, headers=headers).text)["_total"]

	queryParams = {
		"limit": total,
		"offset": 0
	}
	return json.loads(requests.get(url, headers=headers, data=queryParams).text)["follows"]

follows = getFollows("44322889")

print([x["channel"]["display_name"] for x in follows])
