# -*- mode: python -*-

block_cipher = None
 

a = Analysis(['bet355_bet_history_scraper.py'],
            # pathex=['C:\\Users\\dahiggins\\Documents\\Projects\\bet365-bet-history-web-scraper\\webscraper'],
             pathex=[now_dir],
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
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='bet355_bet_history_scraper',
          debug=False,
          strip=False,
          upx=True,
          console=True )
