from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = ['tcl', 'ttk', 'tkinter', 'Tkinter', 'Tcl'])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('py.py', base=base)
]

setup(name='CR Donor Universe',
      version = '1.0',
      description = 'Testing of CR Donor Univesse',
      options = dict(build_exe = buildOptions),
      executables = executables)
