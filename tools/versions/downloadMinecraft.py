from pathlib import Path
import requests
import os


import const
from .download import download
from .getMinecraft import downloadLib, downloadObjects, mineverjson
from .getMinecraft import filename
from .minecraftConf import createJson


def downloadMinecraft(version, name, javapath, callback = None) -> None:
    path = os.path.join(os.getenv('HOME'), '.cobalt', 'assemblies', name, '.minecraft') # type: ignore
    req = requests.get(mineverjson(version)) # type: ignore
    versionJson = req.json()
    req = requests.get(versionJson['assetIndex']['url'])
    assetVersion = req.json()

    
    # Download .cobalt/assets/indexes (info resource version)
    download(versionJson['assetIndex']['url'], filename(versionJson['assetIndex']['url']),os.path.join(os.getenv('HOME'), '.cobalt', 'assets', 'indexes'), callback = callback) # type: ignore
    # Download .cobalt/assets/objects (resource minecraft)
    downloadObjects(assetVersion, callback = callback)
    # Download .cobalt/libraries (libraries file for minecraft)
    downloadLib(versionJson, callback = callback)
    # Download .cobalt/libraries/versions (vannila minecraft .jar)
    download(versionJson['downloads']['client']['url'], f'{version}.jar', os.path.join(const.versionsDir, version), callback = callback)
    # Download .cobalt/libraries/versions (vannila minecraft .json)
    download(mineverjson(version), f'{version}.json', os.path.join(const.versionsDir, version), callback = callback)
    createJson(path, version, name, javapath)
    Path(path).mkdir(parents=True, exist_ok=True)
