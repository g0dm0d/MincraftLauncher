from pathlib import Path
from traceback import print_tb
import requests
import subprocess
import os
import json
import shutil
from xml.dom import minidom

from ..versions.download import download
from ..versions.downloadMinecraft import downloadLib


#https://meta.fabricmc.net/v2/versions/
#https://meta.fabricmc.net/v2/versions/loader
# https://maven.fabricmc.net/org/ow2/asm/asm-tree/9.3/asm-tree-9.3.jar
# 	"org.ow2.asm:asm-tree:9.3"

def downloadLib(jsonfile):
    path = Path(os.path.join(os.getenv('HOME'), '.cobalt', 'libraries'))
    for file in jsonfile['libraries']:
        liburl = file['url']
        libPath = file['name'].split(':')
        filePath = Path(os.path.join(path, *libPath))
        fileName = ''.join(libPath[-2:])+'.jar'
        if not Path(os.path.join(filePath, fileName)).exists():
            download(liburl+fileName, fileName, filePath)


def installFabric(version):
    tree = (minidom.parseString(requests.get('https://maven.fabricmc.net/net/fabricmc/fabric-installer/maven-metadata.xml').content))
    Fabversion = tree.getElementsByTagName('latest')[0].firstChild.nodeValue
    mainDir = os.path.join(os.getenv('HOME'), '.cobalt')
    req = requests.get('https://meta.fabricmc.net/v2/versions/loader')
    fabricver = req.json()
    fabricver = fabricver[0]['version']
    download(f"https://maven.fabricmc.net/net/fabricmc/fabric-installer/{Fabversion}/fabric-installer-{Fabversion}.jar",\
        f'fabric-installer-{Fabversion}.jar', mainDir)
    command = ["java", "-jar", os.path.join(mainDir, f'fabric-installer-{Fabversion}.jar'), "client", "-dir", mainDir,\
        "-mcversion", version, "-loader", fabricver, "-noprofile", "-snapshot"]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print(command, result.stdout, result.stderr)
    versionJson = json.loads(
        Path(os.path.join(mainDir, 'versions', f'fabric-loader-{fabricver}-{version}', f'fabric-loader-{fabricver}-{version}.json')).read_text())
    downloadLib(versionJson)
    shutil.copy(os.path.join(mainDir, 'versions', version, f'{version}.jar'), os.path.join(mainDir, 'versions', f'fabric-loader-{fabricver}-{version}', f'fabric-loader-{fabricver}-{version}.jar'))