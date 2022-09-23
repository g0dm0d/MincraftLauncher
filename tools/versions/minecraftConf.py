import json
import os
from pathlib import Path


from .config import Config
from . import const


def createJson(path: str , version: str, name: str, javapath: str, arguments='-Xmx4G') -> None:
    data =[
        {
           "location": path,
           "version": version,
           "javapath": javapath,
           "arguments": arguments,
           "runner": version
        }]
    with open (os.path.join(const.mcDir,f'{name}.json'), "w+") as file:
        file.write(json.dumps(data))


def readJson(name: str):
    mainJson = json.loads(
        Path(os.path.join(const.mcDir, f'{name}.json')).read_text())
    return Config(mainJson[0]['location'], mainJson[0]['version'],\
            mainJson[0]['javapath'], mainJson[0]['arguments'], mainJson[0]['runner'])


def versionList() -> list[str]:
    try:
        filelist= [file[:-5] for file in os.listdir(const.mcDir) if file.endswith('.json')]
        return filelist
    except:
        return ['no profile']


def updateRunner(name: str, runner: str) -> None:
    with open(os.path.join(const.mcDir, f'{name}.json'), 'r') as jsonFile:
        data = json.load(jsonFile)
    data[0]['runner'] = runner
    with open(os.path.join(const.mcDir, f'{name}.json'), 'w') as jsonFile:
        json.dump(data, jsonFile)
