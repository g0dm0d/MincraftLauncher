from pathlib import Path
import requests
import os


from .download import download
from .getMinecraft import downloadLib, downloadObjects, mineverjson
from .getMinecraft import filename
from .minecraftConf import createJson


def downloadMinecraft(version, name, javapath, callback = None):
    path = os.path.join(os.getenv('HOME'), '.cobalt', 'assemblies', name, '.minecraft')
    req = requests.get(mineverjson(version))
    versionJson = req.json()
    req = requests.get(versionJson['assetIndex']['url'])
    assetVersion = req.json()

    download(versionJson['assetIndex']['url'], filename(versionJson['assetIndex']['url']),os.path.join(os.getenv('HOME'), '.cobalt', 'assets', 'indexes'), callback = callback)     # Download .cobalt/assets/indexes (info resource version)
    downloadObjects(assetVersion, callback = callback)                                                                                                                              # Download .cobalt/assets/objects (resource minecraft)
    downloadLib(versionJson, callback = callback)                                                                                                                                   # Download .cobalt/libraries (libraries file for minecraft)
    download(versionJson['downloads']['client']['url'], f'{version}.jar', os.path.join(os.getenv('HOME'), '.cobalt', 'versions', version), callback = callback)                     # Download .cobalt/libraries/versions (vannila minecraft .jar)
    download(mineverjson(version), f'{version}.json', os.path.join(os.getenv('HOME'), '.cobalt', 'versions', version), callback = callback)                                         # Download .cobalt/libraries/versions (vannila minecraft .json)
    createJson(path, version, name, javapath)
    Path(path).mkdir(parents=True, exist_ok=True)
