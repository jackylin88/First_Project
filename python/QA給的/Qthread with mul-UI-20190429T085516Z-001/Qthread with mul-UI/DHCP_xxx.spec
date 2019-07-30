# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\Calvin\\Downloads\\Qthread with mul-UI-20180502T051355Z-001\\Qthread with mul-UI'],
             binaries=[],
             datas=[],
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
 Tree('C:\\Users\\Calvin\\Downloads\\Qthread with mul-UI-20180502T051355Z-001\\Qthread with mul-UI', prefix="\\"),
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='DHCP_xxx',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='ic.ico')
