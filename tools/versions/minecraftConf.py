import json
import os
from pathlib import Path


mcDir = os.path.join(os.getenv('HOME'), '.cobalt')


def createJson(path, version, name, javapath, arguments='-Xmx4G'):
    data =[
        {
           "location": path,
           "version": version,
           "javapath": javapath,
           "arguments": arguments
        }]
    with open (os.path.join(mcDir,f'{name}.json'), "w+") as file:
        file.write(json.dumps(data))


def readJson(name):
    mainJson = json.loads(
        Path(os.path.join(mcDir, f'{name}.json')).read_text())
    return mainJson[0]['location'], mainJson[0]['version']


def versionJson(name):
    mainJson = json.loads(
        Path(os.path.join(mcDir, f'{name}.json')).read_text())
    return(mainJson[0]['version'])


def locationJson(name):
    mainJson = json.loads(
        Path(os.path.join(mcDir, f'{name}.json')).read_text())
    return(mainJson[0]['location'])


def versionList():
    filelist= [file[:-5] for file in os.listdir(mcDir) if file.endswith('.json')]
    return filelist
