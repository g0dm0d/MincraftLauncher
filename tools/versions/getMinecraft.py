from pathlib import Path
import requests
import os


from .download import download


mcDir = os.path.join(os.getenv('HOME'), '.cobalt')


def filename(link):
    return str(link).split('/')[-1]

def mineverjson(version):
    req = requests.get('https://launchermeta.mojang.com/mc/game/version_manifest_v2.json')
    clientJson = req.json()
    for i in clientJson['versions']:
        if i['id'] == version:
            return i['url']


def minejson(jsonfile, path):
    download(jsonfile, filename(jsonfile), path)


def downloadObjects(jsonfile): # hash
    path = Path(os.path.join(os.getenv('HOME'), '.cobalt', 'assets', 'objects'))
    for file in jsonfile['objects']:
        hash = jsonfile['objects'][file]['hash']
        filePath = Path(os.path.join(path, hash[:2]))
        if not Path(os.path.join(filePath, hash)).exists():
            download(f'http://resources.download.minecraft.net/{hash[:2]}/{hash}', hash, filePath)


def downloadLib(jsonfile):
    path = Path(os.path.join(os.getenv('HOME'), '.cobalt', 'libraries'))
    for file in jsonfile['libraries']:
        libPath = file['downloads']['artifact']['path'].split('/')[:-1]
        filePath = Path(os.path.join(path, *libPath))
        fileName = (file['downloads']['artifact']['path']).split('/')[-1]
        if not Path(os.path.join(filePath, fileName)).exists():
            download(file['downloads']['artifact']['url'], fileName, filePath)
        if 'classifiers' in file['downloads']:
            if 'natives-linux' in file['downloads']['classifiers']:
                download(file['downloads']['artifact']['url'][:-4]+'-natives-linux.jar', fileName[:-4]+'-natives-linux.jar', filePath)

#"https://launchermeta.mojang.com/mc/game/version_manifest_v2.json").json()["latest"]