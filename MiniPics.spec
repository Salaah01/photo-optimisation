# -*- mode: python -*-

block_cipher = None


a = Analysis(['/Users/eyasminbasher/Documents/Salaah/Image Optimisation/image-optimisation/code/gui.py'],
             pathex=['/Users/eyasminbasher/Documents/Salaah/Image Optimisation/image-optimisation'],
             binaries=[],
             datas=[('/Users/eyasminbasher/Documents/Salaah/Image Optimisation/image-optimisation/code/gui_controls.py', '.'), ('/Users/eyasminbasher/Documents/Salaah/Image Optimisation/image-optimisation/code/img_extensions.py', '.'), ('/Users/eyasminbasher/Documents/Salaah/Image Optimisation/image-optimisation/code/logo.ico', '.'), ('/Users/eyasminbasher/Documents/Salaah/Image Optimisation/image-optimisation/code/optimise_img.py', '.')],
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
          console=False , icon='/Users/eyasminbasher/Documents/Salaah/Image Optimisation/image-optimisation/code/logo.ico')
app = BUNDLE(exe,
             name='MiniPics.app',
             icon='/Users/eyasminbasher/Documents/Salaah/Image Optimisation/image-optimisation/code/logo.ico',
             bundle_identifier=None)
