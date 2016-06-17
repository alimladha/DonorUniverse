TEMPLATE = subdirs
CONFIG += ordered nostrip
SUBDIRS = QtCore QtGui QtHelp QtMultimedia QtNetwork QtDeclarative QtScript QtScriptTools QtXml QtOpenGL QtSql QtSvg QtTest QtWebKit QtXmlPatterns phonon QtDesigner Qt pylupdate pyrcc designer

init_py.files = /Users/alim/GitHub/DonorUniverseGit/venv/build/PyQt-mac-gpl-4.11.4/__init__.py
init_py.path = /Users/alim/GitHub/DonorUniverseGit/venv/lib/python2.7/site-packages/PyQt4
INSTALLS += init_py

uic_package.files = /Users/alim/GitHub/DonorUniverseGit/venv/build/PyQt-mac-gpl-4.11.4/pyuic/uic
uic_package.path = /Users/alim/GitHub/DonorUniverseGit/venv/lib/python2.7/site-packages/PyQt4
INSTALLS += uic_package

pyuic4.files = pyuic4
pyuic4.path = /Users/alim/GitHub/DonorUniverseGit/venv/bin/../bin
INSTALLS += pyuic4
