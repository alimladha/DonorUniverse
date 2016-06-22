from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = ['tcl', 'tkinter', 'Tkinter'])

import sys
base = None if sys.platform=='win32' else None

executables = [
    Executable('DonorUniverseGUI_2.py', base=base)
]

setup(name='CRDonorUniverse',
      version = '1.0',
      description = 'CR Donor Universe Test v1.0',
      options = dict(build_exe = buildOptions),
      executables = executables)
