import requests
import json
import sqlite3
import os
from typing import Optional


from account import Account


def accountinfo(token: str):
    headers = {"Authorization": f"Bearer {token}"}
    account = requests.get("https://api.minecraftservices.com/minecraft/profile", headers=headers)
    jsontxt = str(account.text)
    parsed = json.loads(jsontxt)
    uuid = parsed["id"]
    nick = parsed["name"]
    return uuid, nick


def getInfo(username: str) -> Optional[Account]:
    con = sqlite3.connect(os.path.dirname(__file__)+'/accounts.db')
    cur = con.cursor()
    cur.execute(f"SELECT * FROM accounts WHERE username = '{username}'")
    rows = cur.fetchall()
    for row in rows:
        return Account(row[0], row[1], row[2])
