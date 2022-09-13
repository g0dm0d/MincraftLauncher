import requests
import json
import os
import time

from ..versions.minecraftConf import readJson, versionJson
from ..versions.download import download
#'https://api.modrinth.com/v2/project/{mod}/version?loaders=["{modloader}"]&game_versions=["{gameVersion}"]'


def searchMod(mod, profile):
    version = versionJson(profile)
    req = requests.get(f'https://api.modrinth.com/v2/search?limit=20&index=relevance&query={mod}&facets=[["categories:\'fabric\'"],["project_type:mod"],["versions:{version}"]]')
    modsFind = req.json()
    modList = []
    for mods in modsFind['hits']:
        modList.append([mods['title'], mods['slug'], mods['icon_url']])
    return modList


def downloadMod(mod, profile):
    location, version = readJson(profile)
    location = os.path.join(location, 'mods')
    req = requests.get(f'https://api.modrinth.com/v2/project/{mod}/version?loaders=["fabric"]&game_versions=["{version}"]',\
            f'{mod}.jar')
    response = req.json()
    link = response[0]['files'][0]['url']
    download(link, response[0]['files'][0]['filename'],location)
