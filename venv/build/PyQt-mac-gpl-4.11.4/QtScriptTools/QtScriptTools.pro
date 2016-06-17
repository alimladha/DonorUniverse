TEMPLATE = lib
CONFIG += warn_on plugin
QT += scripttools script
CONFIG += release
CONFIG -= android_install

win32 {
    PY_MODULE = QtScriptTools.pyd
    target.files = QtScriptTools.pyd
    LIBS += -L/Users/alim/GitHub/DonorUniverseGit/venv/bin/../lib -lpython27
} else {
    PY_MODULE = QtScriptTools.so
    target.files = QtScriptTools.so
}

target.CONFIG = no_check_exist
target.path = /Users/alim/GitHub/DonorUniverseGit/venv/lib/python2.7/site-packages/PyQt4
INSTALLS += target
sip.path = /Users/alim/GitHub/DonorUniverseGit/venv/bin/../share/sip/PyQt4/QtScriptTools
sip.files = ../sip/QtScriptTools/qscriptenginedebugger.sip ../sip/QtScriptTools/QtScriptToolsmod.sip
INSTALLS += sip
QMAKE_CXXFLAGS += -fno-exceptions
DEFINES += SIP_PROTECTED_IS_PUBLIC protected=public
INCLUDEPATH += .
INCLUDEPATH += /Users/alim/GitHub/DonorUniverseGit/venv/bin/../include/python2.7
INCLUDEPATH += /Library/Frameworks/Python.framework/Versions/2.7/include/python2.7

win32 {
    QMAKE_POST_LINK = $(COPY_FILE) $(DESTDIR_TARGET) $$PY_MODULE
} else {
    QMAKE_POST_LINK = $(COPY_FILE) $(TARGET) $$PY_MODULE
}
macx {
    QMAKE_LFLAGS += "-undefined dynamic_lookup"
}

TARGET = QtScriptTools
HEADERS = sipAPIQtScriptTools.h
SOURCES = sipQtScriptToolscmodule.cpp sipQtScriptToolsQScriptEngineDebugger.cpp
