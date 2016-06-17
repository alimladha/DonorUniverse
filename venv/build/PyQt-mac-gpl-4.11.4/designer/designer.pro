CONFIG      += plugin release warn_on

greaterThan(QT_MAJOR_VERSION, 4) {
    QT += designer

    # Work around QTBUG-39300.
    CONFIG -= android_install
}

lessThan(QT_MAJOR_VERSION, 5) {
    CONFIG += designer
}

TARGET      = pyqt4
TEMPLATE    = lib

INCLUDEPATH += /Library/Frameworks/Python.framework/Versions/2.7/include/python2.7
LIBS        += -L/Library/Frameworks/Python.framework/Versions/2.7/lib -lpython2.7
DEFINES     += PYTHON_LIB=\\\"Python.framework/Versions/2.7/Python\\\"

SOURCES     = pluginloader.cpp
HEADERS     = pluginloader.h

# Install.
target.path = /usr/local/Cellar/qt/4.8.7_2/plugins/designer

python.path = /usr/local/Cellar/qt/4.8.7_2/plugins/designer
python.files = python

INSTALLS    += target python

INCLUDEPATH += /Users/alim/GitHub/DonorUniverseGit/venv/build/PyQt-mac-gpl-4.11.4/designer
VPATH = /Users/alim/GitHub/DonorUniverseGit/venv/build/PyQt-mac-gpl-4.11.4/designer

