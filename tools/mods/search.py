import requests
import json


#'https://api.modrinth.com/v2/project/{mod}/version?loaders=["{modloader}"]&game_versions=["{gameVersion}"]'


def searchMod(mod):
    req = requests.get(f'https://api.modrinth.com/v2/search?limit=20&index=relevance&query={mod}&facets=[["categories:\'fabric\'"],["project_type:mod"]]')
    modsList = req.json()
    for mods in modsList['hits']:
        print(mods['title'], mods['author'], mods['description'])


searchMod('fabric')