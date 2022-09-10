import sqlite3


from .UUID import uuidfinder
from .authAPI import msauth


def addAccount(nick):
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    token = msauth()
    uuid = uuidfinder(nick)
    cur.execute(f"INSERT INTO accounts (username, uuid, accessToken) VALUES ('{nick}', '{uuid}', '{token}')")
    con.commit()
