# -*- mode: python -*-

block_cipher = None


a = Analysis(['DonorUniverseGUI_2.py'],
             pathex=['/Users/alim/GitHub/DonorUniverseGit/src'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='DonorUniverseGUI_2',
          debug=False,
          strip=False,
          upx=True,
          console=False )
app = BUNDLE(exe,
             name='DonorUniverseGUI_2.app',
             icon=None,
             bundle_identifier=None)
