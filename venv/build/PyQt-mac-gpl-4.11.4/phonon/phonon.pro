TEMPLATE = lib
CONFIG += warn_on plugin
QT += phonon
CONFIG += release
CONFIG -= android_install

win32 {
    PY_MODULE = phonon.pyd
    target.files = phonon.pyd
    LIBS += -L/Users/alim/GitHub/DonorUniverseGit/venv/bin/../lib -lpython27
} else {
    PY_MODULE = phonon.so
    target.files = phonon.so
}

target.CONFIG = no_check_exist
target.path = /Users/alim/GitHub/DonorUniverseGit/venv/lib/python2.7/site-packages/PyQt4
INSTALLS += target
sip.path = /Users/alim/GitHub/DonorUniverseGit/venv/bin/../share/sip/PyQt4/phonon
sip.files = ../sip/phonon/abstractaudiooutput.sip ../sip/phonon/abstractvideooutput.sip ../sip/phonon/audiooutput.sip ../sip/phonon/backendcapabilities.sip ../sip/phonon/effect.sip ../sip/phonon/effectparameter.sip ../sip/phonon/effectwidget.sip ../sip/phonon/mediacontroller.sip ../sip/phonon/medianode.sip ../sip/phonon/mediaobject.sip ../sip/phonon/mediasource.sip ../sip/phonon/objectdescription.sip ../sip/phonon/path.sip ../sip/phonon/phononmod.sip ../sip/phonon/phononnamespace.sip ../sip/phonon/seekslider.sip ../sip/phonon/videoplayer.sip ../sip/phonon/videowidget.sip ../sip/phonon/volumeslider.sip
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

TARGET = phonon
HEADERS = sipAPIphonon.h
SOURCES = sipphononcmodule.cpp sipphononPhonon.cpp sipphononPhononAbstractAudioOutput.cpp sipphononPhononAbstractVideoOutput.cpp sipphononPhononAudioCaptureDevice.cpp sipphononPhononAudioChannelDescription.cpp sipphononPhononAudioOutput.cpp sipphononPhononAudioOutputDevice.cpp sipphononPhononAudioOutputDeviceModel.cpp sipphononPhononBackendCapabilities.cpp sipphononPhononBackendCapabilitiesNotifier.cpp sipphononPhononEffect.cpp sipphononPhononEffectDescription.cpp sipphononPhononEffectDescriptionModel.cpp sipphononPhononEffectParameter.cpp sipphononPhononEffectParameterHints.cpp sipphononPhononEffectWidget.cpp sipphononPhononMediaController.cpp sipphononPhononMediaControllerFeatures.cpp sipphononPhononMediaNode.cpp sipphononPhononMediaObject.cpp sipphononPhononMediaSource.cpp sipphononPhononPath.cpp sipphononPhononSeekSlider.cpp sipphononPhononSubtitleDescription.cpp sipphononPhononVideoPlayer.cpp sipphononPhononVideoWidget.cpp sipphononPhononVolumeSlider.cpp sipphononQHash0100QByteArray0100QVariant.cpp sipphononQList0100PhononAudioCaptureDevice.cpp sipphononQList0100PhononAudioChannelDescription.cpp sipphononQList0100PhononAudioOutputDevice.cpp sipphononQList0100PhononEffectDescription.cpp sipphononQList0100PhononEffectParameter.cpp sipphononQList0100PhononMediaSource.cpp sipphononQList0100PhononPath.cpp sipphononQList0100PhononSubtitleDescription.cpp sipphononQList0101PhononEffect.cpp sipphononQMultiMap0100QString0100QString.cpp
