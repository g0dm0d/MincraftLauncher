from pathlib import Path
import requests
import os
from typing import Optional


from .download import download
from . import const


def filename(link) -> str:
    return str(link).split('/')[-1]

def mineverjson(version) -> Optional[str]:
    req = requests.get('https://launchermeta.mojang.com/mc/game/version_manifest_v2.json')
    clientJson = req.json()
    for i in clientJson['versions']:
        if i['id'] == version:
            return i['url']


def getVersion() -> list[str]:
    req = requests.get('https://launchermeta.mojang.com/mc/game/version_manifest_v2.json')
    clientJson = req.json()
    versionlist = [version['id'] for version in clientJson['versions'] if version['type'] == 'release']
    return versionlist


def minejson(jsonfile, path) -> None:
    download(jsonfile, filename(jsonfile), path)


def downloadObjects(jsonfile, callback = None) -> None:
    for file in jsonfile['objects']:
        hash = jsonfile['objects'][file]['hash']
        filePath = Path(os.path.join(const.objectsDir, hash[:2]))
        if not Path(os.path.join(filePath, hash)).exists():
            download(f'http://resources.download.minecraft.net/{hash[:2]}/{hash}', hash, filePath, callback = callback)


def downloadLib(jsonfile, callback = None) -> None:
    for file in jsonfile['libraries']:
        libPath = file['downloads']['artifact']['path'].split('/')[:-1]
        filePath = Path(os.path.join(const.libsDir, *libPath))
        fileName = (file['downloads']['artifact']['path']).split('/')[-1]
        if not Path(os.path.join(filePath, fileName)).exists():
            download(file['downloads']['artifact']['url'], fileName, filePath)
        if 'classifiers' in file['downloads']:
            if 'natives-linux' in file['downloads']['classifiers']:
                download(file['downloads']['artifact']['url'][:-4]+'-natives-linux.jar', fileName[:-4]+'-natives-linux.jar', filePath, callback = callback)

#"https://launchermeta.mojang.com/mc/game/version_manifest_v2.json").json()["latest"]
