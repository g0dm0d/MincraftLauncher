import sqlite3
import os


from .accountInfo import accountinfo 
from .authAPI import msauth


def addAccount() -> None:
    con = sqlite3.connect(os.path.dirname(__file__)+'/accounts.db')
    cur = con.cursor()
    token = msauth()
    if token != None:
        uuid, nick = accountinfo(token)
        cur.execute(f"INSERT INTO accounts (username, uuid, accessToken) VALUES ('{nick}', '{uuid}', '{token}')")
        con.commit()
