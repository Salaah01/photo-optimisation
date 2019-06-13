# -*- mode: python -*-

block_cipher = None


a = Analysis(['Optimisation\\image-optimisation\\code\\fileinfo.py', 'C:/Users/Salaah/Documents/Portfolio/Image Optimisation/image-optimisation/code/gui.py'],
             pathex=['c:\\Users\\Salaah\\Documents\\Portfolio\\Image Optimisation\\image-optimisation'],
             binaries=[],
             datas=[('C:/Users/Salaah/Documents/Portfolio/Image Optimisation/image-optimisation/code/optimise_img.py', '.'), ('C:/Users/Salaah/Documents/Portfolio/Image Optimisation/image-optimisation/code/logo.ico', '.'), ('C:/Users/Salaah/Documents/Portfolio/Image Optimisation/image-optimisation/code/img_extensions.py', '.'), ('C:/Users/Salaah/Documents/Portfolio/Image Optimisation/image-optimisation/code/gui_controls.py', '.')],
             hiddenimports=[],
             hookspath=[],
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
          name='MiniPics',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , version='C:\\Users\\Salaah\\Documents\\Portfolio\\Image', icon='C:\\Users\\Salaah\\Documents\\Portfolio\\Image Optimisation\\image-optimisation\\code\\logo.ico')
