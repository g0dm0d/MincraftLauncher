import json
import os
from pathlib import Path


def createJson(path, version, name, javapath, arguments='-Xmx4G'):
    data =[
        {
           "location": path,
           "version": version,
           "javapath": javapath,
           "arguments": arguments
        }]
    mcDir = os.path.join(os.getenv('HOME'), '.cobalt')
    with open (os.path.join(mcDir,f'{name}.json'), "w+") as file:
        file.write(json.dumps(data))


def readJson(name):
    mcDir = os.path.join(os.getenv('HOME'), '.cobalt')
    mainJson = json.loads(
    Path(os.path.join(mcDir, f'{name}.json')).read_text())
    return mainJson[0]['location'], mainJson[0]['version']