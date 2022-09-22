from pathlib import Path
import requests
import os


from ..versions.minecraftConf import readJson
from ..versions.download import download
#'https://api.modrinth.com/v2/project/{mod}/version?loaders=["{modloader}"]&game_versions=["{gameVersion}"]'


def modsLocation(profile):
    location = readJson(profile).location
    location = os.path.join(location, 'mods')
    return location


def searchMod(mod, profile):
    version = readJson(profile).version
    req = requests.get(f'https://api.modrinth.com/v2/search?limit=20&index=relevance&query={mod}&\
            facets=[["categories:\'fabric\'"],["project_type:mod"],["versions:{version}"]]')
    modsFind = req.json()
    modList = []
    for mods in modsFind['hits']:
        modList.append([mods['title'], mods['slug'], mods['icon_url']])
    return modList


def downloadMod(mod, profile):
    version = readJson(profile).version
    location = modsLocation(profile)
    req = requests.get(f'https://api.modrinth.com/v2/project/{mod}/version?loaders=["fabric"]&game_versions=["{version}"]',\
            f'{mod}.jar')
    response = req.json()
    link = response[0]['files'][0]['url']
    download(link, response[0]['files'][0]['filename'],location)


def listMod(profile):
    location = modsLocation(profile)
    filelist = [file for file in os.listdir(location) if file.endswith('.jar') or file.endswith('.dis')]
    return filelist


def toogleMod(mod, profile):
    location = modsLocation(profile)
    if os.path.isfile(os.path.join(location, f'{mod}.jar')):
        return os.rename(Path(os.path.join(location, f'{mod}.jar')), Path(os.path.join(location, f'{mod}.dis')))
    return os.rename(Path(os.path.join(location, f'{mod}.dis')), Path(os.path.join(location, f'{mod}.jar')))


def modStatus(mod, profile) -> bool:
    location = modsLocation(profile)
    if os.path.isfile(os.path.join(location, f'{mod}.jar')):
        return True
    return False
