from pathlib import Path
import requests
import os


from ..versions.minecraftConf import readJson, versionJson, locationJson
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


def listMod(profile):
    location = locationJson(profile)
    location = os.path.join(location, 'mods')
    filelist = [file for file in os.listdir(location) if file.endswith('.jar') or file.endswith('.dis')]
    return filelist


def toogleMod(mod, profile):
    location = locationJson(profile)
    location = os.path.join(location, 'mods')
    status = 'jar'
    if mod[-3] == 'jar':
        status = 'dis'
    location = os.rename(Path(os.path.join(location, 'mods', mod)), Path(os.path.join(location, 'mods', f'{mod[0:-3]}{status}')))
