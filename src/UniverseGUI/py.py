# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CRDonorUniverseGui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import dataloader
from dataloader import taxonomicMap
import sequence
from test.test_logging import LEVEL_RANGE
from sequence import TaxPyramid
import search
import collections

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
        Form.resize(662, 567)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.addButton = QtGui.QPushButton(self.tab)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.gridLayout.addWidget(self.addButton, 1, 3, 1, 1)
        self.spinBox = QtGui.QSpinBox(self.tab)
        self.spinBox.setMinimum(1)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.gridLayout.addWidget(self.spinBox, 4, 2, 1, 1)
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
        self.gridLayout.addWidget(self.tableWidget_Results, 5, 0, 1, 5)
        self.subtractButton = QtGui.QPushButton(self.tab)
        self.subtractButton.setObjectName(_fromUtf8("subtractButton"))
        self.gridLayout.addWidget(self.subtractButton, 1, 4, 1, 1)
        self.searchButton = QtGui.QPushButton(self.tab)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.gridLayout.addWidget(self.searchButton, 4, 3, 1, 2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 4, 1, 1, 1)
        self.addSCFAButton = QtGui.QPushButton(self.tab)
        self.addSCFAButton.setObjectName(_fromUtf8("addSCFAButton"))
        self.gridLayout.addWidget(self.addSCFAButton, 3, 3, 1, 1)
        self.subtractSCFAButton = QtGui.QPushButton(self.tab)
        self.subtractSCFAButton.setObjectName(_fromUtf8("subtractSCFAButton"))
        self.gridLayout.addWidget(self.subtractSCFAButton, 3, 4, 1, 1)
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
        item = QtGui.QSpinBox()
        item.setRange(-10,10)
        self.tableWidget_SCFA.setCellWidget(0,1,item)
        item = getSCFAComboBox()
        self.tableWidget_SCFA.setCellWidget(0,0, item)
        self.gridLayout.addWidget(self.tableWidget_SCFA, 2, 0, 1, 5)
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
        box = QtGui.QSpinBox()
        box.setRange(-10, 10)
        self.tableWidget.setCellWidget(0,0, box)
        self.addDynamicComboBoxes(0)
        self.updateKingdoms(0)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 5)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.addButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.addSearchRow)
        QtCore.QObject.connect(self.addSCFAButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.addSearchRowSCFA)
        QtCore.QObject.connect(self.subtractSCFAButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.removeSearchRowSCFA)
        QtCore.QObject.connect(self.subtractButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.removeSearchRow)
        QtCore.QObject.connect(self.searchButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.returnResults)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "CR Donor Universe", None))
        self.addButton.setText(_translate("Form", "+", None))
        item = self.tableWidget_Results.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Result", None))
        self.subtractButton.setText(_translate("Form", "-", None))
        self.searchButton.setText(_translate("Form", "Search", None))
        self.label.setText(_translate("Form", "Number of Donors:", None))
        self.addSCFAButton.setText(_translate("Form", "+", None))
        self.subtractSCFAButton.setText(_translate("Form", "-", None))
        item = self.tableWidget_SCFA.verticalHeaderItem(0)
        item.setText(_translate("Form", "Search 1", None))
        item = self.tableWidget_SCFA.horizontalHeaderItem(0)
        item.setText(_translate("Form", "SCFA", None))
        item = self.tableWidget_SCFA.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Weight", None))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "16S and SCFA Search", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Future Features Will Appear Here", None))
        
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
        kingdoms = dataloader.taxonomicMap[0].keys()
        QtKingdoms = listToQstringList(kingdoms)
        widget.addItems(QtKingdoms) 
        
    def updateNextColumn(self, text, row, col):
        if col+1 < self.tableWidget.columnCount():
            if text != '':
                taxonomicLevel = col - 1
                taxDict = taxonomicMap[taxonomicLevel]
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
                
            
    def returnResults(self):
        searchDict = self.getSixteenS()
        if not searchDict:
            return
        searchSCFAList = self.getSCFA()
        if not searchSCFAList:
            return
        numResults = int(self.spinBox.value())
        searchResult = search.search(searchDict, dataloader.donors)
        resultSCFA = search.fattyAcidSearcher(donors, searchSCFAList)
        resultTable = self.tableWidget_Results
        headers=[]
        for i in range(0, len(searchResult)):
            headerString = '16S Search %s' % (i+1)
            headers.append(QtCore.QString(headerString))
        for i in range(0, len(resultSCFA)):
            headerString = 'SCFA Search %s' % (i+1)
            headers.append(QtCore.QString(headerString))
        #headers.append(QtCore.QString('Combined'))
        
        for col in range(resultTable.columnCount(),0, -1):
            resultTable.removeColumn(col-1)
        for row in range(resultTable.rowCount(), 0, -1):
            resultTable.removeRow(row-1)
        for row in range(0, numResults):
            resultTable.insertRow(row)
        resultTable.clear()
        
        for list in resultSCFA:
            searchResult.append(list)
        
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
def listToQstringList(inputList):
    qlist = QtCore.QStringList()
    for item in inputList:
        qitem = QtCore.QString(item)
        qlist.append(qitem)
    return qlist
def getSCFAComboBox():
    #get a list of SCFA
    for donor in dataloader.donors:
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

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    databaseDirectory = QtGui.QFileDialog.getExistingDirectory(None,QtCore.QString("Open Database Directory"),"/home", QtGui.QFileDialog.ShowDirsOnly | QtGui.QFileDialog.DontResolveSymlinks);
    donors = dataloader.donorInitiator(databaseDirectory)
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    Form.raise_()
    sys.exit(app.exec_())
