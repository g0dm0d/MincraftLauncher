# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['/home/godmod/Documents/work/enelix/launcher.py'],
             pathex=[],
             binaries=[],
             datas=[('/home/godmod/Documents/work/enelix/res', 'res/'), ('/home/godmod/Documents/work/enelix/authAPI.py', '.'), ('/home/godmod/Documents/work/enelix/game.py', '.'), ('/home/godmod/Documents/work/enelix/launcher.ui', '.'), ('/home/godmod/Documents/work/enelix/UUID.py', '.')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='Enelix Launcher',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='/home/godmod/Documents/work/enelix/icon.ico')
