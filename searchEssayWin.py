# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchEssay.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys



class searchEssayWin(QtWidgets.QWidget):
    
    def __init__(self,doctor):
        
        super().__init__()
        
        self.doctor = doctor
        
        self.initUI()
    
    def initUI(self):
        self.setObjectName("Form")
        self.resize(1049, 668)
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 431, 241))
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 131, 201))
        self.label_3.setObjectName("label_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setGeometry(QtCore.QRect(160, 30, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(812, 157, 201, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(812, 227, 201, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.listView = QtWidgets.QListView(self)
        self.listView.setGeometry(QtCore.QRect(20, 320, 1011, 331))
        self.listView.setObjectName("listView")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(560, 100, 451, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(460, 100, 91, 31))
        font = QtGui.QFont()
        font.setFamily("华文彩云")
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(460, 150, 311, 111))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(20, 280, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 楷体 Std R")
        font.setPointSize(19)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "GroupBox"))
        self.label_3.setText(_translate("Form", "icon"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Personal     Resume</p></body></html>"))
        self.pushButton.setText(_translate("Form", "搜索"))
        self.pushButton_2.setText(_translate("Form", "结束观看并评分"))
        self.label.setText(_translate("Form", "搜索："))
        self.label_2.setText(_translate("Form", "LOGO         HERE"))
        self.label_4.setText(_translate("Form", "搜索结果："))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = searchEssayWin("shan")
    window.show()
    sys.exit(app.exec_())
    














