# -*- mode: python -*-
#-----------------------------------------------------------------------------
# Copyright (c) 2013-2016, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------


__testname__ = 'test_requests'

a = Analysis([__testname__ + '.py'],
             pathex=[])
pyz = PYZ(a.pure)

TOC_custom = [('test_requests_server.pem','test_requests_server.pem','DATA')]

exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=__testname__ + '.exe',
          debug=True,
          strip=False,
          upx=True,
          console=True )

coll = COLLECT( exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               TOC_custom,
               strip=False,
               upx=True,
               name=__testname__)
