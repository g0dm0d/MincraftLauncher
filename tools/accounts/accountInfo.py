import requests
import json
import sqlite3
import os


def accountinfo(token):
    headers = {"Authorization": f"Bearer {token}"}
    account = requests.get("https://api.minecraftservices.com/minecraft/profile", headers=headers)
    jsontxt = str(account.text)
    parsed = json.loads(jsontxt)
    uuid = parsed["id"]
    nick = parsed["name"]
    return uuid, nick


def getInfo(username):
    con = sqlite3.connect(os.path.dirname(__file__)+'/accounts.db')
    cur = con.cursor()
    cur.execute(f"SELECT * FROM accounts WHERE username = '{username}'")
    rows = cur.fetchall()
    for row in rows:
        return row[0], row[1], row[2]
