# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CRDonorUniverseGui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
from PyQt4 import QtCore, QtGui
#added Code
import dataloader
from sequence import TaxPyramid
import search
import collections
import time
import qdarkstyle
#added Code

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1280, 751)
        self.horizontalLayout_5 = QtGui.QHBoxLayout(Form)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.scrollArea = QtGui.QScrollArea(self.tab_3)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 1208, 1037))
        self.scrollAreaWidgetContents_3.setObjectName(_fromUtf8("scrollAreaWidgetContents_3"))
        self.gridLayout_17 = QtGui.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_17.setObjectName(_fromUtf8("gridLayout_17"))
        self.searchButtonDonor = QtGui.QPushButton(self.scrollAreaWidgetContents_3)
        self.searchButtonDonor.setObjectName(_fromUtf8("searchButtonDonor"))
        self.gridLayout_17.addWidget(self.searchButtonDonor, 4, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(713, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_17.addItem(spacerItem, 4, 0, 1, 1)
        self.tableWidgetDonor = QtGui.QTableWidget(self.scrollAreaWidgetContents_3)
        self.tableWidgetDonor.setMinimumSize(QtCore.QSize(0, 300))
        self.tableWidgetDonor.setObjectName(_fromUtf8("tableWidgetDonor"))
        self.tableWidgetDonor.setColumnCount(1)
        self.tableWidgetDonor.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetDonor.setHorizontalHeaderItem(0, item)
        self.tableWidgetDonor.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidgetDonor.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_17.addWidget(self.tableWidgetDonor, 5, 0, 1, 4)
        self.exportToSixteenSButton = QtGui.QPushButton(self.scrollAreaWidgetContents_3)
        self.exportToSixteenSButton.setObjectName(_fromUtf8("exportToSixteenSButton"))
        self.gridLayout_17.addWidget(self.exportToSixteenSButton, 7, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(441, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_17.addItem(spacerItem1, 7, 0, 1, 1)
        self.exportToLogisticsButton = QtGui.QPushButton(self.scrollAreaWidgetContents_3)
        self.exportToLogisticsButton.setObjectName(_fromUtf8("exportToLogisticsButton"))
        self.gridLayout_17.addWidget(self.exportToLogisticsButton, 7, 2, 1, 2)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.donorCheck = QtGui.QCheckBox(self.scrollAreaWidgetContents_3)
        self.donorCheck.setObjectName(_fromUtf8("donorCheck"))
        self.gridLayout_3.addWidget(self.donorCheck, 1, 0, 1, 1)
        self.clinicalInfoCheck = QtGui.QCheckBox(self.scrollAreaWidgetContents_3)
        self.clinicalInfoCheck.setObjectName(_fromUtf8("clinicalInfoCheck"))
        self.gridLayout_3.addWidget(self.clinicalInfoCheck, 10, 2, 1, 1)
        self.prodRateCheck = QtGui.QCheckBox(self.scrollAreaWidgetContents_3)
        self.prodRateCheck.setObjectName(_fromUtf8("prodRateCheck"))
        self.gridLayout_3.addWidget(self.prodRateCheck, 17, 0, 1, 1)
        self.waistCheck = QtGui.QCheckBox(self.scrollAreaWidgetContents_3)
        self.waistCheck.setObjectName(_fromUtf8("waistCheck"))
        self.gridLayout_3.addWidget(self.waistCheck, 7, 2, 1, 1)
        self.bmiCheck = QtGui.QCheckBox(self.scrollAreaWidgetContents_3)
        self.bmiCheck.setObjectName(_fromUtf8("bmiCheck"))
        self.gridLayout_3.addWidget(self.bmiCheck, 7, 0, 1, 1)
        self.safetyHeader = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.safetyHeader.setObjectName(_fromUtf8("safetyHeader"))
        self.gridLayout_3.addWidget(self.safetyHeader, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.sdiCheck = QtGui.QCheckBox(self.scrollAreaWidgetContents_3)
        self.sdiCheck.setObjectName(_fromUtf8("sdiCheck"))
        self.horizontalLayout_2.addWidget(self.sdiCheck)
        self.sdiCombo = QtGui.QComboBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sdiCombo.sizePolicy().hasHeightForWidth())
        self.sdiCombo.setSizePolicy(sizePolicy)
        self.sdiCombo.setObjectName(_fromUtf8("sdiCombo"))
        self.sdiCombo.addItem(_fromUtf8(""))
        self.sdiCombo.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.sdiCombo)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 21, 1, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.bmiULSpin = QtGui.QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.bmiULSpin.setDecimals(1)
        self.bmiULSpin.setObjectName(_fromUtf8("bmiULSpin"))
        self.gridLayout_4.addWidget(self.bmiULSpin, 0, 1, 1, 1)
        self.bmiULcheck = QtGui.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bmiULcheck.sizePolicy().hasHeightForWidth())
        self.bmiULcheck.setSizePolicy(sizePolicy)
        self.bmiULcheck.setObjectName(_fromUtf8("bmiULcheck"))
        self.gridLayout_4.addWidget(self.bmiULcheck, 0, 0, 1, 1)
        self.bmiLLCheck = QtGui.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bmiLLCheck.sizePolicy().hasHeightForWidth())
        self.bmiLLCheck.setSizePolicy(sizePolicy)
        self.bmiLLCheck.setObjectName(_fromUtf8("bmiLLCheck"))
        self.gridLayout_4.addWidget(self.bmiLLCheck, 1, 0, 1, 1)
        self.bmiLLSpin = QtGui.QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.bmiLLSpin.setDecimals(1)
        self.bmiLLSpin.setObjectName(_fromUtf8("bmiLLSpin"))
        self.gridLayout_4.addWidget(self.bmiLLSpin, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 7, 1, 1, 1)
        self.materialCheck = QtGui.QCheckBox(self.scrollAreaWidgetContents_3)
        self.materialCheck.setObjectName(_fromUtf8("materialCheck"))
        self.gridLayout_3.addWidget(self.materialCheck, 16, 0, 1, 1)
        self.shippingCheck = QtGui.QCheckBox(self.scrollAreaWidgetContents_3)
        self.shippingCheck.setObjectName(_fromUtf8("shippingCheck"))
        self.gridLayout_3.addWidget(self.shippingCheck, 15, 2, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.maleRadio = QtGui.QRadioButton(self.scrollAreaWidgetContents_3)
        self.maleRadio.setObjectName(_fromUtf8("maleRadio"))
        self.verticalLayout_3.addWidget(self.maleRadio)
        self.femaleRadio = QtGui.QRadioButton(self.scrollAreaWidgetContents_3)
        self.femaleRadio.setObjectName(_fromUtf8("femaleRadio"))
        self.verticalLayout_3.addWidget(self.femaleRadio)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 8, 3, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.jsdCheck = QtGui.QCheckBox(self.scrollAreaWidgetContents_3)
        self.jsdCheck.setObjectName(_fromUtf8("jsdCheck"))
        self.horizontalLayout.addWidget(self.jsdCheck)
        self.jsdCombo = QtGui.QComboBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jsdCombo.sizePolicy().hasHeightForWidth())
        self.jsdCombo.setSizePolicy(sizePolicy)
        self.jsdCombo.setObjectName(_fromUtf8("jsdCombo"))
        self.jsdCombo.addItem(_fromUtf8(""))
        self.jsdCombo.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.jsdCombo)
        self.gridLayout_3.addLayout(self.horizontalLayout, 21, 2, 1, 1)
        self.logisticsHeader = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logisticsHeader.sizePolicy().hasHeightForWidth())
        self.logisticsHeader.setSizePolicy(sizePolicy)
        self.logisticsHeader.setObjectName(_fromUtf8("logisticsHeader"))
        self.gridLayout_3.addWidget(self.logisticsHeader, 12, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.fprowCheck = QtGui.QCheckBox(self.scrollAreaWidgetContents_3)
        self.fprowCheck.setObjectName(_fromUtf8("fprowCheck"))
        self.horizontalLayout_3.addWidget(self.fprowCheck)
        self.fprowCombo = QtGui.QComboBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fprowCombo.sizePolicy().hasHeightForWidth())
        self.fprowCombo.setSizePolicy(sizePolicy)
        self.fprowCombo.setObjectName(_fromUtf8("fprowCombo"))
        self.fprowCombo.addItem(_fromUtf8(""))
        self.fprowCombo.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.fprowCombo)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 21, 3, 1, 1)
        self.safetyRatingCheck = QtGui.QCheckBox(self.scrollAreaWidgetContents_3)
        self.safetyRatingCheck.setObjectName(_fromUtf8("safetyRatingCheck"))
        self.gridLayout_3.addWidget(self.safetyRatingCheck, 5, 0, 1, 1)
        self.safetyRatingCombo = QtGui.QComboBox(self.scrollAreaWidgetContents_3)
        self.safetyRatingCombo.setObjectName(_fromUtf8("safetyRatingCombo"))
        self.safetyRatingCombo.addItem(_fromUtf8(""))
        self.safetyRatingCombo.addItem(_fromUtf8(""))
        self.safetyRatingCombo.addItem(_fromUtf8(""))
        self.safetyRatingCombo.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.safetyRatingCombo, 5, 1, 1, 1)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.waistLLCheck = QtGui.QCheckBox(self.scrollAreaWidgetContents_3)
        self.waistLLCheck.setObjectName(_fromUtf8("waistLLCheck"))
        self.gridLayout_6.addWidget(self.waistLLCheck, 1, 0, 1, 1)
        self.waistULCheck = QtGui.QCheckBox(self.scrollAreaWidgetContents_3)
        self.waistULCheck.setObjectName(_fromUtf8("waistULCheck"))
        self.gridLayout_6.addWidget(self.waistULCheck, 0, 0, 1, 1)
        self.waistULSpin = QtGui.QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.waistULSpin.setDecimals(1)
        self.waistULSpin.setObjectName(_fromUtf8("waistULSpin"))
        self.gridLayout_6.addWidget(self.waistULSpin, 0, 1, 1, 1)
        self.waistLLSpin = QtGui.QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.waistLLSpin.setDecimals(1)
        self.waistLLSpin.setObjectName(_fromUtf8("waistLLSpin"))
        self.gridLayout_6.addWidget(self.waistLLSpin, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_6, 7, 3, 1, 1)
        self.genderCheck = QtGui.QCheckBox(self.scrollAreaWidgetContents_3)
        self.genderCheck.setObjectName(_fromUtf8("genderCheck"))
        self.gridLayout_3.addWidget(self.genderCheck, 8, 2, 1, 1)
        self.ageCheck = QtGui.QCheckBox(self.scrollAreaWidgetContents_3)
        self.ageCheck.setObjectName(_fromUtf8("ageCheck"))
        self.gridLayout_3.addWidget(self.ageCheck, 8, 0, 1, 1)
        self.shippingCombo = QtGui.QComboBox(self.scrollAreaWidgetContents_3)
        self.shippingCombo.setObjectName(_fromUtf8("shippingCombo"))
        self.shippingCombo.addItem(_fromUtf8(""))
        self.shippingCombo.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.shippingCombo, 15, 3, 1, 1)
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.ageULSpin = QtGui.QSpinBox(self.scrollAreaWidgetContents_3)
        self.ageULSpin.setObjectName(_fromUtf8("ageULSpin"))
        self.gridLayout_7.addWidget(self.ageULSpin, 0, 1, 1, 1)
        self.ageULCheck = QtGui.QCheckBox(self.scrollAreaWidgetContents_3)
        self.ageULCheck.setObjectName(_fromUtf8("ageULCheck"))
        self.gridLayout_7.addWidget(self.ageULCheck, 0, 0, 1, 1)
        self.ageLLCheck = QtGui.QCheckBox(self.scrollAreaWidgetContents_3)
        self.ageLLCheck.setObjectName(_fromUtf8("ageLLCheck"))
        self.gridLayout_7.addWidget(self.ageLLCheck, 1, 0, 1, 1)
        self.ageLLSpin = QtGui.QSpinBox(self.scrollAreaWidgetContents_3)
        self.ageLLSpin.setObjectName(_fromUtf8("ageLLSpin"))
        self.gridLayout_7.addWidget(self.ageLLSpin, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_7, 8, 1, 1, 1)
        self.gridLayout_9 = QtGui.QGridLayout()
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.unitsLabel_2 = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.unitsLabel_2.setObjectName(_fromUtf8("unitsLabel_2"))
        self.gridLayout_9.addWidget(self.unitsLabel_2, 1, 0, 1, 1)
        self.materialTypeLabel_2 = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.materialTypeLabel_2.setObjectName(_fromUtf8("materialTypeLabel_2"))
        self.gridLayout_9.addWidget(self.materialTypeLabel_2, 0, 0, 1, 1)
        self.materialTypeCombo_2 = QtGui.QComboBox(self.scrollAreaWidgetContents_3)
        self.materialTypeCombo_2.setObjectName(_fromUtf8("materialTypeCombo_2"))
        self.gridLayout_9.addWidget(self.materialTypeCombo_2, 0, 1, 1, 1)
        self.unitsSpin_2 = QtGui.QSpinBox(self.scrollAreaWidgetContents_3)
        self.unitsSpin_2.setObjectName(_fromUtf8("unitsSpin_2"))
        self.gridLayout_9.addWidget(self.unitsSpin_2, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_9, 16, 2, 1, 1)
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.materialTypeLabel_1 = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.materialTypeLabel_1.setObjectName(_fromUtf8("materialTypeLabel_1"))
        self.gridLayout_8.addWidget(self.materialTypeLabel_1, 0, 0, 1, 1)
        self.materialTypeCombo_1 = QtGui.QComboBox(self.scrollAreaWidgetContents_3)
        self.materialTypeCombo_1.setObjectName(_fromUtf8("materialTypeCombo_1"))
        self.gridLayout_8.addWidget(self.materialTypeCombo_1, 0, 1, 1, 1)
        self.unitsLabel_1 = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.unitsLabel_1.setObjectName(_fromUtf8("unitsLabel_1"))
        self.gridLayout_8.addWidget(self.unitsLabel_1, 1, 0, 1, 1)
        self.unitsSpin_1 = QtGui.QSpinBox(self.scrollAreaWidgetContents_3)
        self.unitsSpin_1.setObjectName(_fromUtf8("unitsSpin_1"))
        self.gridLayout_8.addWidget(self.unitsSpin_1, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_8, 16, 1, 1, 1)
        self.gridLayout_10 = QtGui.QGridLayout()
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.materialTypeLabel_3 = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.materialTypeLabel_3.setObjectName(_fromUtf8("materialTypeLabel_3"))
        self.gridLayout_10.addWidget(self.materialTypeLabel_3, 0, 0, 1, 1)
        self.unitsLabel_3 = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.unitsLabel_3.setObjectName(_fromUtf8("unitsLabel_3"))
        self.gridLayout_10.addWidget(self.unitsLabel_3, 1, 0, 1, 1)
        self.materialTypeCombo_3 = QtGui.QComboBox(self.scrollAreaWidgetContents_3)
        self.materialTypeCombo_3.setObjectName(_fromUtf8("materialTypeCombo_3"))
        self.gridLayout_10.addWidget(self.materialTypeCombo_3, 0, 1, 1, 1)
        self.unitsSpin_3 = QtGui.QSpinBox(self.scrollAreaWidgetContents_3)
        self.unitsSpin_3.setObjectName(_fromUtf8("unitsSpin_3"))
        self.gridLayout_10.addWidget(self.unitsSpin_3, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_10, 16, 3, 1, 1)
        self.sixteenSHeader = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.sixteenSHeader.setObjectName(_fromUtf8("sixteenSHeader"))
        self.gridLayout_3.addWidget(self.sixteenSHeader, 20, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_3.addWidget(self.label_12, 22, 0, 1, 1)
        self.processStatusCheck = QtGui.QCheckBox(self.scrollAreaWidgetContents_3)
        self.processStatusCheck.setObjectName(_fromUtf8("processStatusCheck"))
        self.gridLayout_3.addWidget(self.processStatusCheck, 15, 0, 1, 1)
        self.processStatusCombo = QtGui.QComboBox(self.scrollAreaWidgetContents_3)
        self.processStatusCombo.setObjectName(_fromUtf8("processStatusCombo"))
        self.processStatusCombo.addItem(_fromUtf8(""))
        self.processStatusCombo.addItem(_fromUtf8(""))
        self.processStatusCombo.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.processStatusCombo, 15, 1, 1, 1)
        self.sixteenSHeader_2 = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.sixteenSHeader_2.setObjectName(_fromUtf8("sixteenSHeader_2"))
        self.gridLayout_3.addWidget(self.sixteenSHeader_2, 21, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.totalSCFACheck = QtGui.QCheckBox(self.scrollAreaWidgetContents_3)
        self.totalSCFACheck.setObjectName(_fromUtf8("totalSCFACheck"))
        self.horizontalLayout_4.addWidget(self.totalSCFACheck)
        self.totalSCFACombo = QtGui.QComboBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.totalSCFACombo.sizePolicy().hasHeightForWidth())
        self.totalSCFACombo.setSizePolicy(sizePolicy)
        self.totalSCFACombo.setObjectName(_fromUtf8("totalSCFACombo"))
        self.totalSCFACombo.addItem(_fromUtf8(""))
        self.totalSCFACombo.addItem(_fromUtf8(""))
        self.horizontalLayout_4.addWidget(self.totalSCFACombo)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 22, 1, 1, 1)
        self.line_3 = QtGui.QFrame(self.scrollAreaWidgetContents_3)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_3.addWidget(self.line_3, 18, 0, 1, 4)
        self.line = QtGui.QFrame(self.scrollAreaWidgetContents_3)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_3.addWidget(self.line, 2, 0, 1, 4)
        self.donorSpin = QtGui.QSpinBox(self.scrollAreaWidgetContents_3)
        self.donorSpin.setMaximum(1000)
        self.donorSpin.setObjectName(_fromUtf8("donorSpin"))
        self.gridLayout_3.addWidget(self.donorSpin, 1, 1, 1, 1)
        self.screeningGroupCheck = QtGui.QCheckBox(self.scrollAreaWidgetContents_3)
        self.screeningGroupCheck.setObjectName(_fromUtf8("screeningGroupCheck"))
        self.gridLayout_3.addWidget(self.screeningGroupCheck, 17, 2, 1, 1)
        self.line_2 = QtGui.QFrame(self.scrollAreaWidgetContents_3)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_3.addWidget(self.line_2, 11, 0, 1, 4)
        self.screeningGroupCombo = QtGui.QComboBox(self.scrollAreaWidgetContents_3)
        self.screeningGroupCombo.setObjectName(_fromUtf8("screeningGroupCombo"))
        self.gridLayout_3.addWidget(self.screeningGroupCombo, 17, 3, 1, 1)
        self.currentStudiesCheck = QtGui.QCheckBox(self.scrollAreaWidgetContents_3)
        self.currentStudiesCheck.setObjectName(_fromUtf8("currentStudiesCheck"))
        self.gridLayout_3.addWidget(self.currentStudiesCheck, 10, 0, 1, 1)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.currentStudiesULCheck = QtGui.QCheckBox(self.scrollAreaWidgetContents_3)
        self.currentStudiesULCheck.setObjectName(_fromUtf8("currentStudiesULCheck"))
        self.gridLayout_5.addWidget(self.currentStudiesULCheck, 0, 0, 1, 1)
        self.currentStudiesLLCheck = QtGui.QCheckBox(self.scrollAreaWidgetContents_3)
        self.currentStudiesLLCheck.setObjectName(_fromUtf8("currentStudiesLLCheck"))
        self.gridLayout_5.addWidget(self.currentStudiesLLCheck, 1, 0, 1, 1)
        self.currentStudiesULSpin = QtGui.QSpinBox(self.scrollAreaWidgetContents_3)
        self.currentStudiesULSpin.setObjectName(_fromUtf8("currentStudiesULSpin"))
        self.gridLayout_5.addWidget(self.currentStudiesULSpin, 0, 1, 1, 1)
        self.currentStudiesLLSpin = QtGui.QSpinBox(self.scrollAreaWidgetContents_3)
        self.currentStudiesLLSpin.setObjectName(_fromUtf8("currentStudiesLLSpin"))
        self.gridLayout_5.addWidget(self.currentStudiesLLSpin, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_5, 10, 1, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_3, 3, 0, 1, 4)
        self.clearDonor = QtGui.QPushButton(self.scrollAreaWidgetContents_3)
        self.clearDonor.setObjectName(_fromUtf8("clearDonor"))
        self.gridLayout_17.addWidget(self.clearDonor, 4, 2, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_2.addWidget(self.scrollArea, 3, 2, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.searchButton = QtGui.QPushButton(self.tab)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.gridLayout.addWidget(self.searchButton, 4, 6, 1, 2)
        self.tableWidget = QtGui.QTableWidget(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        #added code
        box = QtGui.QSpinBox()
        box.setRange(-10, 10)
        self.tableWidget.setCellWidget(0,0, box)
        self.addDynamicComboBoxes(0)
        self.updateKingdoms(0)
        #added code
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 8)
        self.spinBox = QtGui.QSpinBox(self.tab)
        self.spinBox.setMinimum(1)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.gridLayout.addWidget(self.spinBox, 4, 5, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.tableWidget_SCFA = QtGui.QTableWidget(self.tab)
        self.tableWidget_SCFA.setObjectName(_fromUtf8("tableWidget_SCFA"))
        self.tableWidget_SCFA.setColumnCount(2)
        self.tableWidget_SCFA.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_SCFA.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_SCFA.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_SCFA.setHorizontalHeaderItem(1, item)
        self.tableWidget_SCFA.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_SCFA.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_SCFA.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_SCFA.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tableWidget_SCFA, 2, 0, 1, 8)
        #added Code
        item = QtGui.QSpinBox()
        item.setRange(-10,10)
        self.tableWidget_SCFA.setCellWidget(0,1,item)
        item = getSCFAComboBox()
        self.tableWidget_SCFA.setCellWidget(0,0, item)
        #added code
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 4, 4, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 4, 3, 1, 1)
        self.addButton = QtGui.QPushButton(self.tab)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.gridLayout.addWidget(self.addButton, 1, 6, 1, 1)
        self.resetDonorPoolButton = QtGui.QPushButton(self.tab)
        self.resetDonorPoolButton.setObjectName(_fromUtf8("resetDonorPoolButton"))
        self.gridLayout.addWidget(self.resetDonorPoolButton, 4, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 4, 1, 1)
        self.donorPoolStaticLabel = QtGui.QLabel(self.tab)
        self.donorPoolStaticLabel.setObjectName(_fromUtf8("donorPoolStaticLabel"))
        self.gridLayout.addWidget(self.donorPoolStaticLabel, 3, 0, 1, 1)
        self.clear16Search = QtGui.QPushButton(self.tab)
        self.clear16Search.setObjectName(_fromUtf8("clear16Search"))
        self.gridLayout.addWidget(self.clear16Search, 4, 1, 1, 1)
        self.donorPoolLabel = QtGui.QLabel(self.tab)
        self.donorPoolLabel.setObjectName(_fromUtf8("donorPoolLabel"))
        self.gridLayout.addWidget(self.donorPoolLabel, 3, 1, 1, 1)
        self.subtractButton = QtGui.QPushButton(self.tab)
        self.subtractButton.setObjectName(_fromUtf8("subtractButton"))
        self.gridLayout.addWidget(self.subtractButton, 1, 7, 1, 1)
        self.addSCFAButton = QtGui.QPushButton(self.tab)
        self.addSCFAButton.setObjectName(_fromUtf8("addSCFAButton"))
        self.gridLayout.addWidget(self.addSCFAButton, 3, 6, 1, 1)
        self.tableWidget_Results = QtGui.QTableWidget(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_Results.sizePolicy().hasHeightForWidth())
        self.tableWidget_Results.setSizePolicy(sizePolicy)
        self.tableWidget_Results.setObjectName(_fromUtf8("tableWidget_Results"))
        self.tableWidget_Results.setColumnCount(1)
        self.tableWidget_Results.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Results.setHorizontalHeaderItem(0, item)
        self.tableWidget_Results.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_Results.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget_Results.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_Results.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_Results.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_Results.verticalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget_Results, 5, 0, 1, 8)
        self.subtractSCFAButton = QtGui.QPushButton(self.tab)
        self.subtractSCFAButton.setObjectName(_fromUtf8("subtractSCFAButton"))
        self.gridLayout.addWidget(self.subtractSCFAButton, 3, 7, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 4, 2, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
            #added Code
        QtCore.QObject.connect(self.addButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.addSearchRow)
        QtCore.QObject.connect(self.addSCFAButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.addSearchRowSCFA)
        QtCore.QObject.connect(self.subtractSCFAButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.removeSearchRowSCFA)
        QtCore.QObject.connect(self.subtractButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.removeSearchRow)
        QtCore.QObject.connect(self.searchButton, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda: self.returnResults(donorList))
        QtCore.QObject.connect(self.searchButtonDonor, QtCore.SIGNAL(_fromUtf8('clicked()')), self.searchDonors)
        QtCore.QObject.connect(self.exportToSixteenSButton, QtCore.SIGNAL(_fromUtf8('clicked()')), self.exportSixteenS)
        QtCore.QObject.connect(self.resetDonorPoolButton, QtCore.SIGNAL(_fromUtf8('clicked()')), self.resetDonorPool)
        QtCore.QObject.connect(self.clearDonor, QtCore.SIGNAL(_fromUtf8('clicked()')), self.resetDonorSearch)
        QtCore.QObject.connect(self.clear16Search, QtCore.SIGNAL(_fromUtf8('clicked()')), self.resetSequenceSearch)
        #added Code
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "CR Donor Universe", None))
        self.searchButtonDonor.setText(_translate("Form", "Search", None))
        item = self.tableWidgetDonor.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Results", None))
        self.exportToSixteenSButton.setText(_translate("Form", "Export List for 16S and SCFA Search", None))
        self.exportToLogisticsButton.setText(_translate("Form", "Export List for Logistic Search", None))
        self.label_2.setText(_translate("Form", "Donor Search:", None))
        self.donorCheck.setText(_translate("Form", "Donor ID", None))
        self.clinicalInfoCheck.setText(_translate("Form", "Clinical Information", None))
        self.prodRateCheck.setText(_translate("Form", "Production Rate", None))
        self.waistCheck.setText(_translate("Form", "Waist Circumference (Inches)", None))
        self.bmiCheck.setText(_translate("Form", "BMI", None))
        self.safetyHeader.setText(_translate("Form", "Safety and Profile:", None))
        self.sdiCheck.setText(_translate("Form", "SDI", None))
        self.sdiCombo.setItemText(0, _translate("Form", "Above Average", None))
        self.sdiCombo.setItemText(1, _translate("Form", "Below Average", None))
        self.bmiULcheck.setText(_translate("Form", "Upper Limit", None))
        self.bmiLLCheck.setText(_translate("Form", "Lower Limit", None))
        self.materialCheck.setText(_translate("Form", "Material Inventory", None))
        self.shippingCheck.setText(_translate("Form", "Shipping Status", None))
        self.maleRadio.setText(_translate("Form", "Male", None))
        self.femaleRadio.setText(_translate("Form", "Female", None))
        self.jsdCheck.setText(_translate("Form", "JSD", None))
        self.jsdCombo.setItemText(0, _translate("Form", "Above Average", None))
        self.jsdCombo.setItemText(1, _translate("Form", "Below Average", None))
        self.logisticsHeader.setText(_translate("Form", "Logistics:", None))
        self.fprowCheck.setText(_translate("Form", "F Prow", None))
        self.fprowCombo.setItemText(0, _translate("Form", "Above Average", None))
        self.fprowCombo.setItemText(1, _translate("Form", "Below Average", None))
        self.safetyRatingCheck.setText(_translate("Form", "Safety Rating", None))
        self.safetyRatingCombo.setItemText(0, _translate("Form", "Approved", None))
        self.safetyRatingCombo.setItemText(1, _translate("Form", "Conditional", None))
        self.safetyRatingCombo.setItemText(2, _translate("Form", "Restricted", None))
        self.safetyRatingCombo.setItemText(3, _translate("Form", "Rejected", None))
        self.waistLLCheck.setText(_translate("Form", "Lower Limit", None))
        self.waistULCheck.setText(_translate("Form", "Upper Limit", None))
        self.genderCheck.setText(_translate("Form", "Gender", None))
        self.ageCheck.setText(_translate("Form", "Age", None))
        self.shippingCombo.setItemText(0, _translate("Form", "Available", None))
        self.shippingCombo.setItemText(1, _translate("Form", "Hold", None))
        self.ageULCheck.setText(_translate("Form", "Upper Limit", None))
        self.ageLLCheck.setText(_translate("Form", "Lower Limit", None))
        self.unitsLabel_2.setText(_translate("Form", "Min #Units", None))
        self.materialTypeLabel_2.setText(_translate("Form", "Type", None))
        self.materialTypeLabel_1.setText(_translate("Form", "Type", None))
        self.unitsLabel_1.setText(_translate("Form", "Min #Units", None))
        self.materialTypeLabel_3.setText(_translate("Form", "Type", None))
        self.unitsLabel_3.setText(_translate("Form", "Min #Units", None))
        self.sixteenSHeader.setText(_translate("Form", "16S and SCFA:", None))
        self.label_12.setText(_translate("Form", "SCFA", None))
        self.processStatusCheck.setText(_translate("Form", "Processing Status", None))
        self.processStatusCombo.setItemText(0, _translate("Form", "Online", None))
        self.processStatusCombo.setItemText(1, _translate("Form", "Hold", None))
        self.processStatusCombo.setItemText(2, _translate("Form", "Retired", None))
        self.sixteenSHeader_2.setText(_translate("Form", "16S:", None))
        self.totalSCFACheck.setText(_translate("Form", "Total SCFA Score", None))
        self.totalSCFACombo.setItemText(0, _translate("Form", "Above Average", None))
        self.totalSCFACombo.setItemText(1, _translate("Form", "Below Average", None))
        self.screeningGroupCheck.setText(_translate("Form", "Screening Group", None))
        self.currentStudiesCheck.setText(_translate("Form", "Current Studies", None))
        self.currentStudiesULCheck.setText(_translate("Form", "Upper Limit", None))
        self.currentStudiesLLCheck.setText(_translate("Form", "Lower Limit", None))
        self.clearDonor.setText(_translate("Form", "Clear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Donor Search", None))
        self.searchButton.setText(_translate("Form", "Search", None))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "Search 1", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Weight", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Kingdom", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Phylum", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Class", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Order", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Family", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Genus", None))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Species", None))
        item = self.tableWidget_SCFA.verticalHeaderItem(0)
        item.setText(_translate("Form", "Search 1", None))
        item = self.tableWidget_SCFA.horizontalHeaderItem(0)
        item.setText(_translate("Form", "SCFA", None))
        item = self.tableWidget_SCFA.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Weight", None))
        self.label.setText(_translate("Form", "Number of Donors:", None))
        self.addButton.setText(_translate("Form", "+", None))
        self.resetDonorPoolButton.setText(_translate("Form", "Reset Donor Pool", None))
        self.donorPoolStaticLabel.setText(_translate("Form", "Current Donor Pool:", None))
        self.clear16Search.setText(_translate("Form", "Clear", None))
        self.donorPoolLabel.setText(_translate("Form", "All Donors", None))
        self.subtractButton.setText(_translate("Form", "-", None))
        self.addSCFAButton.setText(_translate("Form", "+", None))
        item = self.tableWidget_Results.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Results", None))
        self.subtractSCFAButton.setText(_translate("Form", "-", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "16S and SCFA Search", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Logistics Search", None))
        #added codes
        screeningGroupList = QtCore.QStringList()
        for group in dataloader.screeningGroups:
            screeningGroupList.append(QtCore.QString(group))
        self.screeningGroupCombo.addItems(screeningGroupList)

    def addSearchRow(self):
        box = QtGui.QSpinBox()
        box.setRange(-10, 10)
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowCount)
        newRowCount = self.tableWidget.rowCount()
        searchItem = QtGui.QTableWidgetItem("Search " + str(newRowCount))
        self.tableWidget.setVerticalHeaderItem(rowCount, searchItem)
        self.tableWidget.setCellWidget(rowCount, 0 , box)
        self.addDynamicComboBoxes(rowCount)
        self.updateKingdoms(rowCount)
        
    def addSearchRowSCFA(self):
        box = QtGui.QSpinBox()
        box.setRange(-10, 10)
        rowCount = self.tableWidget_SCFA.rowCount()
        self.tableWidget_SCFA.insertRow(rowCount)
        newRowCount = self.tableWidget_SCFA.rowCount()
        searchItem = QtGui.QTableWidgetItem("Search " + str(newRowCount))
        self.tableWidget_SCFA.setVerticalHeaderItem(rowCount, searchItem)
        self.tableWidget_SCFA.setCellWidget(rowCount, 1 , box)
        comboBox = getSCFAComboBox()
        self.tableWidget_SCFA.setCellWidget(rowCount, 0, comboBox)
        
    def removeSearchRow(self):
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.removeRow(rowCount-1)
    
    def removeSearchRowSCFA(self):
        rowCount = self.tableWidget_SCFA.rowCount()
        self.tableWidget_SCFA.removeRow(rowCount-1)

    def addDynamicComboBoxes(self, rowNum):
        numCols = self.tableWidget.columnCount()
        box = QtGui.QComboBox()
        self.tableWidget.setCellWidget(rowNum, 1, box)
        box.activated['QString'].connect(lambda: self.updateNextColumn(self.tableWidget.cellWidget(rowNum, 1).currentText(), rowNum, 1)) 
        box = QtGui.QComboBox()
        self.tableWidget.setCellWidget(rowNum, 2, box)
        box.activated['QString'].connect(lambda: self.updateNextColumn(self.tableWidget.cellWidget(rowNum, 2).currentText(), rowNum, 2)) 
        box = QtGui.QComboBox()  
        self.tableWidget.setCellWidget(rowNum, 3, box)
        box.activated['QString'].connect(lambda: self.updateNextColumn(self.tableWidget.cellWidget(rowNum, 3).currentText(), rowNum, 3)) 
        box = QtGui.QComboBox()  
        self.tableWidget.setCellWidget(rowNum, 4, box)
        box.activated['QString'].connect(lambda: self.updateNextColumn(self.tableWidget.cellWidget(rowNum, 4).currentText(), rowNum, 4)) 
        box = QtGui.QComboBox()  
        self.tableWidget.setCellWidget(rowNum, 5, box)
        box.activated['QString'].connect(lambda: self.updateNextColumn(self.tableWidget.cellWidget(rowNum, 5).currentText(), rowNum, 5))  
        box = QtGui.QComboBox() 
        self.tableWidget.setCellWidget(rowNum, 6, box)
        box.activated['QString'].connect(lambda: self.updateNextColumn(self.tableWidget.cellWidget(rowNum, 6).currentText(), rowNum, 6))  
        box = QtGui.QComboBox() 
        self.tableWidget.setCellWidget(rowNum, 7, box)
        box.activated['QString'].connect(lambda: self.updateNextColumn(self.tableWidget.cellWidget(rowNum, 7).currentText(), rowNum, 7))
        box = QtGui.QComboBox() 
        
    def updateKingdoms(self, rowNum):
        kingdomCol = 1
        widget = self.tableWidget.cellWidget(rowNum, kingdomCol)
        if dataloader.taxonomicMap == False:
            return
        try:
            kingdoms = dataloader.taxonomicMap[0].keys()
            QtKingdoms = listToQstringList(kingdoms)
            widget.addItems(QtKingdoms) 
        except:
            return
        
    def updateNextColumn(self, text, row, col):
        if col+1 < self.tableWidget.columnCount():
            if text != '':
                taxonomicLevel = col - 1
                taxDict = dataloader.taxonomicMap[taxonomicLevel]
                nextList = taxDict[str(text)]
                nextList.add('')
                QtNextList = listToQstringList(nextList)
                for x in range(col+1, self.tableWidget.columnCount()):
                    nextWidget = self.tableWidget.cellWidget(row, x)
                    nextWidget.clear()
                nextWidget = self.tableWidget.cellWidget(row, col+1)
                nextWidget.addItems(QtNextList)
            else:
                for x in range(col+1, self.tableWidget.columnCount()):
                    nextWidget = self.tableWidget.cellWidget(row, x)
                    nextWidget.clear()
                
            
    def returnResults(self, donors):
        weights = []
        searchDict = self.getSixteenS()
        if not searchDict:
            return
        for weightItem in searchDict.values():
            weights.append(weightItem[1])
        searchSCFAList = self.getSCFA()
        if not searchSCFAList and int(self.tableWidget_SCFA.rowCount())>0:
            return
        for scfaSearch in searchSCFAList:
            weights.append(scfaSearch[1])
        numResults = int(self.spinBox.value())
        searchResult = search.search(searchDict, donors)
        resultSCFA = search.fattyAcidSearcher(donors, searchSCFAList)
        resultTable = self.tableWidget_Results
        headers=[]
        for i in range(0, len(searchResult)):
            headerString = '16S Search %s' % (i+1)
            headers.append(QtCore.QString(headerString))
        for i in range(0, len(resultSCFA)):
            headerString = 'SCFA Search %s' % (i+1)
            headers.append(QtCore.QString(headerString))
        headers.append(QtCore.QString('Combined'))
        
        for col in range(resultTable.columnCount(),0, -1):
            resultTable.removeColumn(col-1)
        for row in range(resultTable.rowCount(), 0, -1):
            resultTable.removeRow(row-1)
        for row in range(0, numResults):
            resultTable.insertRow(row)
        resultTable.clear()
        
        for list in resultSCFA:
            searchResult.append(list)
            
        combinedResult = search.overallProfileRanker(searchResult, weights)
        if not combinedResult:
            error = QtGui.QErrorMessage()
            error.showMessage(QtCore.QString("No Donors Fit Combined Profile!"))
            error.exec_()
        searchResult.append(combinedResult)
        
        i=0
        for header in headers:
            numCols = resultTable.columnCount()
            resultTable.insertColumn(numCols)
            item=QtGui.QTableWidgetItem()
            resultTable.setHorizontalHeaderItem(numCols, item)
            item.setText(header)
            resList = searchResult[i]
            for j in range(0,numResults):
                if j<len(resList):
                    item = QtGui.QTableWidgetItem()
                    item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                    if header == QtCore.QString('Combined'):
                        item.setData(QtCore.Qt.DisplayRole, resList[j][0])
                    else:
                        item.setText(QtCore.QString(resList[j].toString()))
                    resultTable.setItem(j,i, item)
            i=i+1
        resultTable.resizeColumnsToContents()

    def getSixteenS(self):
        searchDict = collections.OrderedDict()
        numRows = self.tableWidget.rowCount()
        searchDict = collections.OrderedDict()
        numCols = self.tableWidget.columnCount()
        numResults = int(self.spinBox.value())
        for row in range(0, numRows):
            spinWidget = self.tableWidget.cellWidget(row, 0)
            weight = spinWidget.value()
            if int(weight)==0:
                errorZero = QtGui.QErrorMessage()
                errorZero.showMessage(QtCore.QString('Zero Weight is invalid. Please enter a non-zero weight!'))
                errorZero.exec_()
                return
            level = 0
            value = ''
            for col,prevCol in zip(range(1,numCols), range(0, numCols-1)):
                boxWidget = self.tableWidget.cellWidget(row, col)
                if(boxWidget.currentText()==''):
                    level = prevCol-1
                    boxWidget = self.tableWidget.cellWidget(row, prevCol)
                    if not isinstance(boxWidget, QtGui.QComboBox):
                        return
                    value = str(boxWidget.currentText())
                    break
            if not searchDict.has_key(value):
                searchDict[value] = (TaxPyramid[level], int(weight))
            else:
                errorMultipleSameSearches = QtGui.QErrorMessage()
                errorMultipleSameSearches.showMessage(QtCore.QString('Duplicate searches are not allowed!'))
                errorMultipleSameSearches.exec_()
                return
        return searchDict  
    def getSCFA(self):
        scfaList = []
        for row in range(0, self.tableWidget_SCFA.rowCount()):
            scfaLabel = str(self.tableWidget_SCFA.cellWidget(row, 0).currentText())
            if scfaLabel == '':
                return
            scfaWeight = int(self.tableWidget_SCFA.cellWidget(row, 1).value())
            if scfaWeight==0:
                errorZero = QtGui.QErrorMessage()
                errorZero.showMessage(QtCore.QString('Zero Weight is invalid. Please enter a non-zero weight!'))
                errorZero.exec_()
                return
            for item in scfaList:
                if item[0] == scfaLabel:
                    errorMultipleSameSCFA = QtGui.QErrorMessage()
                    errorMultipleSameSCFA.showMessage(QtCore.QString('Duplicate searches are not allowed!'))
                    errorMultipleSameSCFA.exec_()
                    return
            scfaList.append((scfaLabel,scfaWeight))
        return scfaList

    def searchDonors(self):
        resetResultsTable(self.tableWidgetDonor)
        answers = self.getFormInfo()
        donorResults = search.findMatches(self, answers, allDonors)
        if not donorResults:
            error = QtGui.QErrorMessage()
            error.showMessage(QtCore.QString("No Donors Found"))
            error.exec_()
            return
        global donorSearchResults
        donorSearchResults = donorResults
        displayProductionRate = answers[self.prodRateCheck]
        headerBoxes = [self.donorCheck, self.safetyRatingCheck, self.bmiCheck, self.waistCheck, self.ageCheck,
                       self.genderCheck, self.clinicalInfoCheck, self.currentStudiesCheck, self.processStatusCheck, self.shippingCheck, self.materialCheck, 
                       self.screeningGroupCheck, self.sdiCheck, self.jsdCheck, self.fprowCheck, self.totalSCFACheck]
        if displayProductionRate:
            headerBoxes.append(self.prodRateCheck)
        search.displayHeaders(self.tableWidgetDonor, headerBoxes, self.clinicalInfoCheck)
        for donor in donorResults:
            headerToFunc = { self.donorCheck: donor.getDonorID, self.safetyRatingCheck: donor.getSafetyRating, self.bmiCheck: donor.getBMI, 
                            self.waistCheck: donor.getWaistCircumference, self.ageCheck: donor.getAge,
                            self.genderCheck: donor.getGender, self.processStatusCheck: donor.getProcessingStatus,
                            self.shippingCheck: donor.getShippingStatus, self.materialCheck: donor.getMaterialAvailable,
                            self.sdiCheck: donor.getSDI, self.jsdCheck: donor.getJSD, self.fprowCheck: donor.getFPROW,
                            self.totalSCFACheck: donor.getTotalSCFA, self.currentStudiesCheck: donor.getCurrentStudies,
                            self.prodRateCheck: donor.getProductionRate, self.clinicalInfoCheck: donor.getClinicalInfo,
                            self.screeningGroupCheck: donor.getScreeningGroup}
            search.displayDonors(self.tableWidgetDonor, headerBoxes, headerToFunc, self.clinicalInfoCheck)
        self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())
    def getFormInfo(self):
        formFields = [self.clinicalInfoCheck, self.screeningGroupCheck, self.screeningGroupCombo, self.donorCheck, self.donorSpin, self.safetyRatingCheck, self.safetyRatingCombo, self.currentStudiesCheck, self.bmiCheck, 
                     self.bmiULcheck, self.bmiULSpin, self.bmiLLCheck, self.bmiLLSpin, self.waistCheck, self.waistULCheck, 
                     self.waistULSpin, self.waistLLCheck, self.waistLLSpin, self.ageCheck, self.ageULCheck, self.ageLLCheck,
                     self.ageLLSpin, self.ageULSpin, self.genderCheck, self.maleRadio, self.femaleRadio, self.processStatusCheck,
                     self.processStatusCombo, self.shippingCheck, self.shippingCombo, self.materialCheck,
                     self.materialTypeCombo_1, self.materialTypeCombo_2, self.materialTypeCombo_3, self.unitsSpin_1,
                     self.unitsSpin_2, self.unitsSpin_3, self.prodRateCheck, self.sdiCheck, self.sdiCombo, self.jsdCheck, self.jsdCombo,
                     self.fprowCheck, self.fprowCombo, self.totalSCFACheck, self.totalSCFACombo, self.currentStudiesLLCheck,
                     self.currentStudiesLLSpin, self.currentStudiesULCheck, self.currentStudiesULSpin]
        formAnswer={}
        for field in formFields:
            if isinstance(field, QtGui.QCheckBox):
                formAnswer[field] = field.isChecked()
            elif isinstance(field, QtGui.QComboBox):
                formAnswer[field] = str(field.currentText())
            elif isinstance(field, QtGui.QSpinBox):
                formAnswer[field] = int(field.value())
            elif isinstance(field, QtGui.QDoubleSpinBox):
                formAnswer[field] = float(field.value())
            elif isinstance(field, QtGui.QRadioButton):
                formAnswer[field] = field.isChecked()
        return formAnswer
    
    def exportSixteenS(self):
        sequenceResults = []
        for donor in donorSearchResults:
            donorSequenceData = donor.getSequences()
            if donorSequenceData:
                for sequenceResult in donorSequenceData:
                    sequenceResults.append(sequenceResult)
        dataloader.taxMapper(sequenceResults)
        global donorList
        donorList = donorSearchResults
        self.resetSequenceSearch()
        resetResultsTable(self.tableWidget_Results)
        self.donorPoolLabel.setText(QtCore.QString("Most Recent Donor Search"))
    
    def resetDonorPool(self):
        global donorList 
        donorList = allDonors
        sequenceResults = []
        for donor in allDonors:
            donorSequenceData = donor.getSequences()
            if donorSequenceData:
                for sequenceResult in donorSequenceData:
                    sequenceResults.append(sequenceResult)            
        dataloader.taxMapper(sequenceResults)
        self.resetSequenceSearch()
        resetResultsTable(self.tableWidget_Results)
        self.donorPoolLabel.setText(QtCore.QString("All Donors"))
        
    def resetSequenceSearch(self):
        numSixteenSearches = int(self.tableWidget.rowCount())
        if numSixteenSearches >0:
            while numSixteenSearches>0:
                self.tableWidget.removeRow(numSixteenSearches-1)
                numSixteenSearches=numSixteenSearches-1
        numSCFASearches = int(self.tableWidget_SCFA.rowCount())
        if numSCFASearches >0:
            while numSCFASearches>0:
                self.tableWidget_SCFA.removeRow(numSCFASearches-1)
                numSCFASearches=numSCFASearches-1 
            
    def resetDonorSearch(self):
        formFields = [self.clinicalInfoCheck, self.screeningGroupCheck, self.screeningGroupCombo, self.donorCheck, self.donorSpin, self.safetyRatingCheck, self.safetyRatingCombo, self.currentStudiesCheck, self.bmiCheck, 
                      self.bmiULcheck, self.bmiULSpin, self.bmiLLCheck, self.bmiLLSpin, self.waistCheck, self.waistULCheck, 
                      self.waistULSpin, self.waistLLCheck, self.waistLLSpin, self.ageCheck, self.ageULCheck, self.ageLLCheck,
                      self.ageLLSpin, self.ageULSpin, self.genderCheck, self.maleRadio, self.femaleRadio, self.processStatusCheck,
                      self.processStatusCombo, self.shippingCheck, self.shippingCombo, self.materialCheck,
                      self.materialTypeCombo_1, self.materialTypeCombo_2, self.materialTypeCombo_3, self.unitsSpin_1,
                      self.unitsSpin_2, self.unitsSpin_3, self.prodRateCheck, self.sdiCheck, self.sdiCombo, self.jsdCheck, self.jsdCombo,
                      self.fprowCheck, self.fprowCombo, self.totalSCFACheck, self.totalSCFACombo, self.currentStudiesLLCheck,
                      self.currentStudiesLLSpin, self.currentStudiesULCheck, self.currentStudiesULSpin]  
        for field in formFields:
            if isinstance(field, QtGui.QCheckBox):
                field.setCheckState(QtCore.Qt.Unchecked)
            if isinstance(field, QtGui.QRadioButton):
                field.setChecked(False)
def listToQstringList(inputList):
    qlist = QtCore.QStringList()
    for item in inputList:
        qitem = QtCore.QString(item)
        qlist.append(qitem)
    return qlist
def getSCFAComboBox():
    #get a list of SCFA
    dictSCFA = {}
    for donor in donorList:
        if donor.shortChainFattyAcids:
            dictSCFA = donor.shortChainFattyAcids
            break
    listSCFA = QtCore.QStringList()
    for key in dictSCFA:
        fattyAcidQString = QtCore.QString(key)
        listSCFA.append(fattyAcidQString)
    comboBox = QtGui.QComboBox()
    comboBox.addItems(listSCFA)
    return comboBox

def raiseFileError():
    error = QtGui.QErrorMessage()
    error.showMessage(QtCore.QString('File directory chosen does not include required files'))
    error.exec_()
    return showFileOpener()
    
def raiseLimitError():
    error = QtGui.QErrorMessage()
    error.showMessage(QtCore.QString('Something is wrong with the upper and lower limits set on one of your searches!'))
    error.exec_()
    raise ValueError('Limit Problem')

def showFileOpener():
    databaseDirectory = QtGui.QFileDialog.getExistingDirectory(None,QtCore.QString("Open Database Directory"),"/home", QtGui.QFileDialog.ShowDirsOnly | QtGui.QFileDialog.DontResolveSymlinks)
    return databaseDirectory

def resetResultsTable(table):
    numCols = int(table.columnCount())
    numRows = int(table.rowCount())
    while numCols > 1:
        table.removeColumn(numCols-1)
        numCols = numCols-1
    while numRows > 0:
        table.removeRow(numRows-1)
        numRows = numRows - 1
    item = QtGui.QTableWidgetItem()
    item.setText(QtCore.QString("Results"))
    table.setHorizontalHeaderItem(0, item)
    
def quitApp():
    QtGui.QApplication.quit()
    
    
def openActualWindow(self, driveData, otherData):
    #import sys
    #app = QtGui.QApplication(sys.argv)
    self.Form_2 = QtGui.QWidget()
    #app.setStyleSheet(qdarkstyle.load_stylesheet(pyside=False))
    #pixmap = QtGui.QPixmap(QtCore.QString("../images/DonorUniverseSplash.png"))
    #splashScreen= QtGui.QSplashScreen(pixmap)
    #splashScreen.show()
    #time.sleep(4)
    #splashScreen.finish(Form_2);
    if driveData == False or otherData == True:
        databaseDirectory = showFileOpener()
        donors = dataloader.donorInitiator(driveData, otherData, databaseDirectory)
    else:
        donors = dataloader.donorInitiator(driveData = driveData, otherData = otherData)
    if otherData == True:
        dataloader.loadOtherData(donors)
    
    global donorList
    global allDonors
    donorList = donors
    allDonors = donors
    ui = Ui_Form()
    ui.setupUi(self.Form_2)
    self.Form_2.show()
    self.Form_2.activateWindow()
    self.Form_2.raise_()
    #sys.exit(app.exec_())

