from pathlib import Path
import requests
import subprocess
import os
import json
import shutil
from xml.dom import minidom


from ..versions import const
from ..versions.download import download
from ..versions.minecraftConf import updateRunner, readJson

#https://meta.fabricmc.net/v2/versions/
#https://meta.fabricmc.net/v2/versions/loader
# https://maven.fabricmc.net/org/ow2/asm/asm-tree/9.3/asm-tree-9.3.jar
# 	"org.ow2.asm:asm-tree:9.3"

def downloadLib(jsonfile, callback = None):
    path = const.libsDir
    for file in jsonfile['libraries']:
        liburl = file['url']
        libPath = file['name'].split(':')
        filePath = Path(os.path.join(path, *libPath))
        fileName = ''.join(libPath[-2:])+'.jar'
        if not Path(os.path.join(filePath, fileName)).exists():
            download(liburl+fileName, fileName, filePath, callback = callback)


def installFabric(name, callback = None):
    version = readJson(name).version
    tree = (minidom.parseString(requests.get('https://maven.fabricmc.net/net/fabricmc/fabric-installer/maven-metadata.xml').content))
    fabversion = tree.getElementsByTagName('latest')[0].firstChild.nodeValue
    mainDir = const.mcDir
    req = requests.get('https://meta.fabricmc.net/v2/versions/loader')
    fabricver = req.json()
    fabricver = fabricver[0]['version']
    download(f"https://maven.fabricmc.net/net/fabricmc/fabric-installer/{fabversion}/fabric-installer-{fabversion}.jar",\
        f'fabric-installer-{fabversion}.jar', mainDir, callback = callback)
    command = ["java", "-jar", os.path.join(mainDir, f'fabric-installer-{fabversion}.jar'), "client", "-dir", mainDir,\
        "-mcversion", version, "-loader", fabricver, "-noprofile", "-snapshot"]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print(command, result.stdout, result.stderr)
    versJson = json.loads(
        Path(os.path.join(mainDir, 'versions', f'fabric-loader-{fabricver}-{version}', f'fabric-loader-{fabricver}-{version}.json')).read_text())
    downloadLib(versJson, callback = callback)
    shutil.copy(os.path.join(mainDir, 'versions', version, f'{version}.jar'), os.path.join(mainDir, 'versions', f'fabric-loader-{fabricver}-{version}', f'fabric-loader-{fabricver}-{version}.jar'))
    updateRunner(name, f'fabric-loader-{fabricver}-{version}.jar')
