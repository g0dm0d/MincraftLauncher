pyrcc5 res/launcher.qrc -o launcher_rc.py
pyuic5 -x res/launcher.ui -o launcherbg.py
pyrcc5 res/mods.qrc -o mods_rc.py
pyuic5 -x mods.ui -o modsSerch.py
