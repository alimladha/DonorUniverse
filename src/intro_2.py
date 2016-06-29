# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'donorUniverseIntro.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import qdarkstyle
import DonorUniverseGUI_5
driveData = False
otherData = True
DriveButton = 0
LocalButton = 1
YesButton = 0
NoButton = 1
import time
import file_setter

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class IntroForm(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(372, 293)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(Form)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 11, 0, 1, 1)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        
        #added code
        self.otherDataGroup = QtGui.QButtonGroup(Form)
        self.otherYesRadio = QtGui.QRadioButton(Form)
        self.otherYesRadio.setObjectName(_fromUtf8("otherYesRadio"))
        self.otherDataGroup.addButton(self.otherYesRadio, YesButton)
        self.horizontalLayout_2.addWidget(self.otherYesRadio)
        self.otherNoRadio = QtGui.QRadioButton(Form)
        self.otherNoRadio.setObjectName(_fromUtf8("otherNoRadio"))
        self.otherDataGroup.addButton(self.otherNoRadio, NoButton)
        #added Code
        
        self.horizontalLayout_2.addWidget(self.otherNoRadio)
        self.gridLayout.addLayout(self.horizontalLayout_2, 8, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.donorButtonGroup = QtGui.QButtonGroup(Form)
        self.driveRadio = QtGui.QRadioButton(Form)
        self.driveRadio.setObjectName(_fromUtf8("driveRadio"))
        self.donorButtonGroup.addButton(self.driveRadio, DriveButton)
        self.horizontalLayout.addWidget(self.driveRadio)
        self.localRadio = QtGui.QRadioButton(Form)
        self.localRadio.setObjectName(_fromUtf8("localRadio"))
        self.donorButtonGroup.addButton(self.localRadio, LocalButton)
        self.horizontalLayout.addWidget(self.localRadio)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 1)
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 5, 0, 1, 1)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 10, 0, 1, 1)
        self.line_3 = QtGui.QFrame(Form)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 9, 0, 1, 1)
        self.donorDataLabel = QtGui.QLabel(Form)
        self.donorDataLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.donorDataLabel.setObjectName(_fromUtf8("donorDataLabel"))
        self.gridLayout.addWidget(self.donorDataLabel, 2, 0, 1, 1)
        self.otherDataLabel = QtGui.QLabel(Form)
        self.otherDataLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.otherDataLabel.setObjectName(_fromUtf8("otherDataLabel"))
        self.gridLayout.addWidget(self.otherDataLabel, 6, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.buttonBox.button(QtGui.QDialogButtonBox.Ok), QtCore.SIGNAL(_fromUtf8('clicked()')),lambda: self.getUserInput(Form))
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.otherYesRadio.setText(_translate("Form", "Yes*", None))
        self.otherNoRadio.setText(_translate("Form", "No", None))
        self.driveRadio.setText(_translate("Form", "Google Drive", None))
        self.localRadio.setText(_translate("Form", "Local*", None))
        self.label.setText(_translate("Form", "*Directory Chooser will open", None))
        self.donorDataLabel.setText(_translate("Form", "Donor Data", None))
        self.otherDataLabel.setText(_translate("Form", "16S and SCFA Data", None))


    def getUserInput(self, Form):
        donorButtonID = self.donorButtonGroup.checkedId()
        dataButtonID = self.otherDataGroup.checkedId()
        if donorButtonID == DriveButton:
            global driveData
            driveData = True
        if dataButtonID == NoButton:
            global otherData
            otherData = False
        DonorUniverseGUI_5.openActualWindow(self, driveData, otherData)
        Form.close()
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(pyside=False))
    pixmap = QtGui.QPixmap(QtCore.QString(file_setter.resource_path("DonorUniverseSplash.png")))
    splashScreen= QtGui.QSplashScreen(pixmap)
    splashScreen.show()
    time.sleep(4)
    Form = QtGui.QWidget()
    splashScreen.finish(Form)
    ui = IntroForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    #DonorUniverseGUI_5.openActualWindow()
