import json
import os
import platform
from pathlib import Path
import subprocess


from tools.versions import const


#version = 'fabric-loader-0.14.9-1.18.1'
#username = 'test'
#uuid = 'test'
#token = 'test'
#name = 'test'


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
    if "linux" in lib["natives"] and platform.system() == "Linux":
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
        libDomain, libName, libVersion, *a = i["name"].split(":")
        jarPath = os.path.join(mcDir, "libraries", *
                               libDomain.split('.'), libName, libVersion)

        native = get_natives_string(i)
        jarFile = libName + "-" + libVersion + ".jar"
        if native != "":
            jarFile = libName + "-" + libVersion + "-" + native + ".jar"
        cp.append(os.path.join(jarPath, jarFile))

    cp.append(os.path.join(mcDir, "versions", lib["id"], f'{lib["id"]}.jar'))

    return os.pathsep.join(cp)

# i["downloads"]['artifact']['url'].split("/")
def run(username, uuid, token, name):
    clientJson = json.loads(
        Path(os.path.join(const.mcDir, f'{name}.json')).read_text())
    version = clientJson[0]['runner'][:-4]
    javapath = clientJson[0]['javapath']
    mcDir = clientJson[0]['location']
    resDir = const.mcDir
    nativesDir = os.path.join(resDir, 'versions', version, 'natives')
    versionJson = json.loads(
        Path(os.path.join(resDir, 'versions', version, f'{version}.json')).read_text())
    classPath = get_classpath(versionJson, resDir)
    mainClass = versionJson['mainClass']
    versionType = versionJson['type']
    arguments = [clientJson[0]['arguments']]
    try:
        dependence = versionJson['inheritsFrom']
        arguments+=versionJson['arguments']['game']
        mainJson = json.loads(
        Path(os.path.join(resDir, 'versions', dependence, f'{dependence}.json')).read_text())
        assetIndex = mainJson['assetIndex']['id']
        classPath = get_classpath(mainJson, resDir) + ':' + classPath
        classPath = classPath.replace(f':/.cobalt/versions/{dependence}/{dependence}.jar', '')
    except:
        assetIndex = versionJson['assetIndex']['id']

    debug(classPath)
    debug(mainClass)
    debug(versionType)
    debug(assetIndex)

    minecraft = [javapath,
        f'-Djava.library.path={nativesDir}',
        '-Dminecraft.launcher.brand=custom-launcher',
        '-Dminecraft.launcher.version=2.1',
        '-cp',
        classPath, 
        mainClass,
        '--username', username, 
        '--version', version, 
        '--gameDir', mcDir, 
        '--assetsDir', os.path.join(resDir, 'assets'),
        '--assetIndex', assetIndex, 
        '--uuid', uuid,
        '--accessToken', token,
        '--userType', 'microsoft',
        '--versionType', 'release',
    ]
    subprocess.call(minecraft + arguments)
