# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchEssay.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import mysql.connector as mc



class searchEssayWin(QtWidgets.QWidget):
    
    def __init__(self,Dialog,doctor):
        
        super().__init__()
        
        self.doctor = doctor
        self.tags = "*"                                #要查找的关键字（从编辑框获取）
        
        self.initUI(Dialog)
    
    
    def on_click_search(self):
    #-----------------refresh   ListWidget------------------------
        strTemp = self.lineEdit.text()
        self.setWindowTitle(strTemp)
        #-------------search in DataBase---------------------
        
    
    
    
    
    #def on_click_grading(self):
    #----------------new grading Window---------------------------
    
    
    
    
    
    
    def initUI(self,Dialog):
        self.setObjectName("Form")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 431, 241))
        self.groupBox.setObjectName("groupBox")
        
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 131, 201))
        self.label_3.setObjectName("label_3")
        
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setGeometry(QtCore.QRect(160, 30, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        
        self.pushButton_search = QtWidgets.QPushButton(Dialog)
        self.pushButton_search.setGeometry(QtCore.QRect(812, 157, 201, 41))
        self.pushButton_search.setObjectName("pushButton")
        self.pushButton_search.clicked.connect(self.on_click_search)
        
        self.pushButton_grading = QtWidgets.QPushButton(Dialog)
        self.pushButton_grading.setGeometry(QtCore.QRect(812, 227, 201, 41))
        self.pushButton_grading.setObjectName("pushButton_2")
        #self.pushButton_grading.clicked.connect(self.on_click_grading)
        
        self.pushButton_back = QtWidgets.QPushButton(Dialog)
        self.pushButton_back.setGeometry(QtCore.QRect(650, 227, 201, 41))
        self.pushButton_back.setObjectName("pushButton_3")
        
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(20, 320, 1011, 331))
        self.listView.setObjectName("listView")
        
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(560, 100, 451, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText("搜索")
        
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(460, 100, 91, 31))
        font = QtGui.QFont()
        font.setFamily("华文彩云")
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(460, 150, 311, 111))
        self.label_2.setObjectName("label_2")
        
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 280, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 楷体 Std R")
        font.setPointSize(19)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self,Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "GroupBox"))
        self.label_3.setText(_translate("Form", "icon"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Personal     Resume</p></body></html>"))
        self.pushButton_search.setText(_translate("Form", "搜索"))
        self.pushButton_grading.setText(_translate("Form", "结束观看并评分"))
        self.pushButton_back.setText(_translate("Form", "返回上个界面"))
        self.label.setText(_translate("Form", "搜索："))
        self.label_2.setText(_translate("Form", "LOGO         HERE"))
        self.label_4.setText(_translate("Form", "搜索结果："))

    """
    def __init__(self,Dialog,money):
        super().__init__()
        
        self.money = money
        self.widget = QtWidgets.QWidget()
        self.payingMethod = "AliPay"
        
        self.initUI(Dialog)
    
    
    
    def on_click_payCompleted(self):
        self.setWindowTitle(self.payingMethod)
        self.widget = chattingWin(self.money)       #-------应该传医生ID进去（获取医生各种信息）
        self.widget.show()
        self.close()
    
    
    
    def on_click_payCanceled(self):
        #----------------cancel data in the database-------------------------------
        #----------------close current window--------------------------------------
        self.close()
    
    
    
    def on_click_radioBtn(self,selectedBtn):
        
        self.radioButton_aliPay.setChecked(False)
        self.radioButton_bankCard.setChecked(False)
        self.radioButton_payPal.setChecked(False)
        
        if selectedBtn == self.radioButton_aliPay:
            self.radioButton_aliPay.setChecked(True)
            self.payingMethod = "AliPay"
        elif selectedBtn == self.radioButton_bankCard:
            self.radioButton_bankCard.setChecked(True)
            self.payingMethod = "BankCard"
        elif selectedBtn == self.radioButton_payPal:
            self.radioButton_payPal.setChecked(True)
            self.payingMethod = "PayPal"
    
    
    def initUI(self,Dialog):
        self.setObjectName("Form")
        #self.resize(1055, 624)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(300, 20, 491, 91))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(24)
        
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 100, 1021, 371))
        self.groupBox.setObjectName("groupBox")
        
        
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 20, 951, 101))
        font = QtGui.QFont()
        font.setFamily("方正舒体")
        font.setPointSize(16)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        
        self.radioButton_bankCard = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_bankCard.setGeometry(QtCore.QRect(30, 40, 281, 31))
        self.radioButton_bankCard.setObjectName("radioButton")
        self.radioButton_bankCard.clicked.connect(lambda:self.on_click_radioBtn(self.radioButton_bankCard))
        
        
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(40, 130, 951, 101))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        
        self.radioButton_payPal = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_payPal.setGeometry(QtCore.QRect(30, 50, 281, 31))
        self.radioButton_payPal.setObjectName("radioButton_2")
        self.radioButton_payPal.clicked.connect(lambda:self.on_click_radioBtn(self.radioButton_payPal))
        
        
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(40, 240, 951, 101))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans Mono")
        font.setPointSize(13)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        
        self.radioButton_aliPay = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_aliPay.setGeometry(QtCore.QRect(30, 50, 281, 21))
        font = QtGui.QFont()
        font.setFamily("方正兰亭超细黑简体")
        self.radioButton_aliPay.setFont(font)
        self.radioButton_aliPay.setObjectName("radioButton_3")
        self.radioButton_aliPay.clicked.connect(lambda:self.on_click_radioBtn(self.radioButton_aliPay))
        
        
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(400, 570, 331, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(430, 500, 121, 61))
        self.label_3.setObjectName("label_3")
        
        self.pushButton_payCompleted = QtWidgets.QPushButton(Dialog)
        self.pushButton_payCompleted.setGeometry(QtCore.QRect(662, 480, 121, 51))
        self.pushButton_payCompleted.setObjectName("pushButton")
        self.pushButton_payCompleted.clicked.connect(self.on_click_payCompleted)
        
        self.pushButton_payCanceled = QtWidgets.QPushButton(Dialog)
        self.pushButton_payCanceled.setGeometry(QtCore.QRect(870, 480, 121, 51))
        self.pushButton_payCanceled.setObjectName("pushButton_2")
        self.pushButton_payCanceled.clicked.connect(self.on_click_payCanceled)
        
        
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 490, 300, 61))
        font = QtGui.QFont()
        font.setFamily("方正姚体")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self,Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Form", "支付窗口"))
        self.label.setText(_translate("Form", "          选择支付手段"))
        self.groupBox.setTitle(_translate("Form", "支付途径"))
        self.groupBox_2.setTitle(_translate("Form", "银联"))
        self.radioButton_bankCard.setText(_translate("Form", "银行卡支付"))
        self.groupBox_4.setTitle(_translate("Form", "PayPal"))
        self.radioButton_payPal.setText(_translate("Form", "PayPal支付"))
        self.groupBox_3.setTitle(_translate("Form", "AliPay"))
        self.radioButton_aliPay.setText(_translate("Form", "支付宝"))
        self.label_2.setText(_translate("Form", "支付时请保护个人信息"))
        self.label_3.setText(_translate("Form", "LOGO   HERE"))
        self.pushButton_payCompleted.setText(_translate("Form", "支付完成"))
        self.pushButton_payCanceled.setText(_translate("Form", "取消支付"))
        self.label_4.setText(_translate("Form", "总金额：  " + str(self.money) + " 元"))
    """



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = searchEssayWin("shan")
    window.show()
    sys.exit(app.exec_())
    














