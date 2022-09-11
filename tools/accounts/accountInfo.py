import requests
import json


def accountinfo(token):
    headers = {"Authorization": f"Bearer {token}"}
    account = requests.get("https://api.minecraftservices.com/minecraft/profile", headers=headers)
    jsontxt = str(account.text)
    parsed = json.loads(jsontxt)
    uuid = parsed["id"]
    nick = parsed["name"]
    return uuid, nick