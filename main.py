import json
import time

import requests as requests

EXPO_SERVER_URL = 'https://exp.host/--/api/v2/push/send'
token1 = 'ExponentPushToken[sq62WdJukpCP5A0_A5iGZf]'
token2 = 'ExponentPushToken[6EsjURJd2Nl7LsyY9tBJVy]'
with open("data3.json", "r") as read_file:
    data = json.load(read_file)
for x in range(len(data)):
    requests.post(EXPO_SERVER_URL, {"to": token1, "title": data[x]['title'],
                                    "body": data[x]['body']})
    requests.post(EXPO_SERVER_URL, {"to": token2, "title": data[x]['title'],
                                    "body": data[x]['body']})
    print((data[x]['title']))
    if x != len(data)-2:
        time.sleep(600)
