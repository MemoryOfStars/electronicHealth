# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc


class Ui_Login(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setupUi()
    
    def setupUi(self):
        self.resize(477, 332)
        
        self.pushButton = QtWidgets.QPushButton('LoginButton',self)
        self.pushButton.setGeometry(QtCore.QRect(160, 260, 141, 51))
        
        self.groupBox = QtWidgets.QGroupBox('Login',self)
        self.groupBox.setGeometry(QtCore.QRect(40, 40, 361, 201))

        
        self.label = QtWidgets.QLabel('',self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 60, 72, 15))
        
        
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 72, 15))
        self.label_2.setObjectName("label_2")
        
        self.plainTextEdit_Num = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit_Num.setGeometry(QtCore.QRect(70, 50, 251, 31))
        self.plainTextEdit_Num.setObjectName("plainTextEdit")
        self.plainTextEdit_Pwd = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit_Pwd.setGeometry(QtCore.QRect(70, 120, 251, 31))
        self.plainTextEdit_Pwd.setObjectName("plainTextEdit_2")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Form"))
        self.pushButton.setText(_translate("Login", "Login"))
        self.groupBox.setTitle(_translate("Login", "用户登录"))
        self.label.setText(_translate("Login", "账号："))
        self.label_2.setText(_translate("Login", "密码："))

