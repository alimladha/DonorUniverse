# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CRDonorUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import dataloader
from dataloader import taxonomicMap

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
        Form.resize(800, 441)
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1, 0, 800, 441))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableWidget = QtGui.QTableWidget(self.verticalLayoutWidget)
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
        high = QtCore.QString('high')
        low = QtCore.QString('low')
        hlList = QtCore.QStringList()
        hlList.append(high)
        hlList.append(low)
        box = QtGui.QComboBox()
        box.addItems(hlList)
        self.tableWidget.setCellWidget(0,0, box)
        self.addDynamicComboBoxes(0)
        self.updateKingdoms(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.line = QtGui.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        
        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.addSearchRow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.removeSearchRow)
        QtCore.QMetaObject.connectSlotsByName(Form)
 
    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "Search 1", None))
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
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_2.setText(_translate("Form", "+", None))
        self.pushButton.setText(_translate("Form", "-", None))
    
    def addSearchRow(self):
        high = QtCore.QString('high')
        low = QtCore.QString('low')
        hlList = QtCore.QStringList()
        hlList.append(high)
        hlList.append(low)
        box = QtGui.QComboBox()
        box.addItems(hlList)
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowCount)
        newRowCount = self.tableWidget.rowCount()
        searchItem = QtGui.QTableWidgetItem("Search " + str(newRowCount))
        self.tableWidget.setVerticalHeaderItem(rowCount, searchItem)
        self.tableWidget.setCellWidget(rowCount, 0 , box)
        self.addDynamicComboBoxes(rowCount)
        self.updateKingdoms(rowCount)
    
    def removeSearchRow(self):
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.removeRow(rowCount-1)
        
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
            taxonomicLevel = col - 1
            taxDict = taxonomicMap[taxonomicLevel]
            nextList = taxDict[str(text)]
            QtNextList = listToQstringList(nextList)
            nextWidget = self.tableWidget.cellWidget(row, col+1)
            nextWidget.clear()
            nextWidget.addItems(QtNextList)


def listToQstringList(inputList):
    qlist = QtCore.QStringList()
    for item in inputList:
        qitem = QtCore.QString(item)
        qlist.append(qitem)
    return qlist
    
    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    dataloader.donorInitiator()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


    
