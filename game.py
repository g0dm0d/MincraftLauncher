import json
import os
import platform
from pathlib import Path
import subprocess
from sys import argv

versionlaun, usernamelaun, uuidlaun, accessTokenlaun = argv

def debug(str):
    if os.getenv('DEBUG') != None:
        print(str)

def get_natives_string(lib):
    arch = ""
    if platform.architecture()[0] == "64bit":
        arch = "64"
    elif platform.architecture()[0] == "32bit":
        arch = "32"
    else:
        raise Exception("Architecture not supported")

    nativesFile=""
    if not "natives" in lib:
        return nativesFile

    if "windows" in lib["natives"] and platform.system() == 'Windows':
        nativesFile = lib["natives"]["windows"].replace("${arch}", arch)
    elif "osx" in lib["natives"] and platform.system() == 'Darwin':
        nativesFile = lib["natives"]["osx"].replace("${arch}", arch)
    elif "linux" in lib["natives"] and platform.system() == "Linux":
        nativesFile = lib["natives"]["linux"].replace("${arch}", arch)
    else:
        raise Exception("Platform not supported")

    return nativesFile

def should_use_library(lib):
    def rule_says_yes(rule):
        useLib = None

        if rule["action"] == "allow":
            useLib = False
        elif rule["action"] == "disallow":
            useLib = True

        if "os" in rule:
            for key, value in rule["os"].items():
                os = platform.system()
                if key == "name":
                    if value == "windows" and os != 'Windows':
                        return useLib
                    elif value == "osx" and os != 'Darwin':
                        return useLib
                    elif value == "linux" and os != 'Linux':
                        return useLib
                elif key == "arch":
                    if value == "x86" and platform.architecture()[0] != "32bit":
                        return useLib

        return not useLib

    if not "rules" in lib:
        return True

    shouldUseLibrary = False
    for i in lib["rules"]:
        if rule_says_yes(i):
            return True

    return shouldUseLibrary

def get_classpath(lib, mcDir):
    cp = []

    for i in lib["libraries"]:
        if not should_use_library(i):
            continue

        libDomain, libName, libVersion = i["name"].split(":")
        jarPath = os.path.join(mcDir, "libraries", *
                               libDomain.split('.'), libName, libVersion)

        native = get_natives_string(i)
        jarFile = libName + "-" + libVersion + ".jar"
        if native != "":
            jarFile = libName + "-" + libVersion + "-" + native + ".jar"

        cp.append(os.path.join(jarPath, jarFile))

    cp.append(os.path.join(mcDir, "versions", lib["id"], f'{lib["id"]}.jar'))

    return os.pathsep.join(cp)

version = versionlaun
username = usernamelaun
uuid = uuidlaun
accessToken = accessTokenlaun

mcDir = os.path.join(os.getenv('HOME'), '.minecraft')
nativesDir = os.path.join(os.getenv('HOME'), 'versions', version, 'natives')
clientJson = json.loads(
    Path(os.path.join(mcDir, 'versions', version, f'{version}.json')).read_text())
classPath = get_classpath(clientJson, mcDir)
mainClass = clientJson['mainClass']
versionType = clientJson['type']
assetIndex = clientJson['assetIndex']['id']

debug(classPath)
debug(mainClass)
debug(versionType)
debug(assetIndex)

subprocess.call([
    '/usr/bin/java',
    f'-Djava.library.path={nativesDir}',
    '-Dminecraft.launcher.brand=custom-launcher',
    '-Dminecraft.launcher.version=2.1',
    '-cp',
    classPath,
    'net.minecraft.client.main.Main',
    '--username',
    username,
    '--version',
    version,
    '--gameDir',
    mcDir,
    '--assetsDir',
    os.path.join(mcDir, 'assets'),
    '--assetIndex',
    assetIndex,
    '--uuid',
    uuid,
    '--accessToken',
    accessToken,
    '--userType',
    'legacy',
    '--versionType',
    'release'
])