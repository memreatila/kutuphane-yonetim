# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ödünç.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(336, 311)
        self.oduncTable = QtWidgets.QTableWidget(Form)
        self.oduncTable.setGeometry(QtCore.QRect(-10, 0, 381, 311))
        self.oduncTable.setObjectName("oduncTable")
        self.oduncTable.setColumnCount(3)
        self.oduncTable.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.oduncTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.oduncTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.oduncTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.oduncTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.oduncTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.oduncTable.setHorizontalHeaderItem(2, item)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ödünç"))
        item = self.oduncTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Üye"))
        item = self.oduncTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Kitap"))
        item = self.oduncTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Tarih"))