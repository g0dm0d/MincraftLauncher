import requests
def uuidfinder(username):
    url = f'https://api.mojang.com/users/profiles/minecraft/{username}?'
    response = requests.get(url)
    uuid = response.json()['id']
    return uuid