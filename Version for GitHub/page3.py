# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page3.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_3(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(499, 872)
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(0, 0, 501, 871))
        self.listView.setStyleSheet("border-image: url(:/image/3.png);")
        self.listView.setObjectName("listView")
        self.single_Button = QtWidgets.QPushButton(Form)
        self.single_Button.setGeometry(QtCore.QRect(160, 630, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(15)
        self.single_Button.setFont(font)
        self.single_Button.setObjectName("single_Button")
        self.multi_Button = QtWidgets.QPushButton(Form)
        self.multi_Button.setGeometry(QtCore.QRect(160, 710, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(15)
        self.multi_Button.setFont(font)
        self.multi_Button.setObjectName("multi_Button")

        self.retranslateUi(Form)
        self.single_Button.clicked.connect(Form.page3_4) # type: ignore
        self.multi_Button.clicked.connect(Form.page3_4_1) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Lab2_Bobing"))
        self.single_Button.setText(_translate("Form", "single player"))
        self.multi_Button.setText(_translate("Form", "multi-player"))
import picture
