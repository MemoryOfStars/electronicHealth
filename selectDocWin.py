# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'willingToAsk.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
from searchEssayWin import searchEssayWin
from payingWin import payingWin
import sys

class selectDocWin(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.widget = QtWidgets.QWidget()
        self.money = 0
        
        self.selectDept = "*"                 #select dept
        self.selectDocLv = "*"                #select docLv
        self.selectedDoc = None               #selected Doctor
    #-------------------------------------------
    #
    #            选择医生职称
    #
    #-------------------------------------------
    def on_click_selectDocLv(self,selectDocLvBtn):
        if selectDocLvBtn == self.pushButton_allDocLv:
            self.selectDocLv = "*"
            
            self.pushButton_allDocLv.setStyleSheet("background-color:white;color:black")
            self.pushButton_zhengGao.setStyleSheet("background-color:white;color:black")
            self.pushButton_fuGao.setStyleSheet("background-color:white;color:black")
            self.pushButton_noDocLv.setStyleSheet("background-color:white;color:black")
            
            self.pushButton_allDocLv.setStyleSheet("background-color:blue;color:white")
        
        elif selectDocLvBtn == self.pushButton_zhengGao:
            self.selectDocLv = "正高"
            
            self.pushButton_allDocLv.setStyleSheet("background-color:white;color:black")
            self.pushButton_zhengGao.setStyleSheet("background-color:white;color:black")
            self.pushButton_fuGao.setStyleSheet("background-color:white;color:black")
            self.pushButton_noDocLv.setStyleSheet("background-color:white;color:black")
            
            self.pushButton_zhengGao.setStyleSheet("background-color:blue;color:white")
        
        elif selectDocLvBtn == self.pushButton_fuGao:
            self.selectDocLv = "副高"
            
            self.pushButton_allDocLv.setStyleSheet("background-color:white;color:black")
            self.pushButton_zhengGao.setStyleSheet("background-color:white;color:black")
            self.pushButton_fuGao.setStyleSheet("background-color:white;color:black")
            self.pushButton_noDocLv.setStyleSheet("background-color:white;color:black")
            
            self.pushButton_fuGao.setStyleSheet("background-color:blue;color:white")
            
        elif selectDocLvBtn == self.pushButton_noDocLv:
            self.selectDocLv = "无职称"
            
            self.pushButton_allDocLv.setStyleSheet("background-color:white;color:black")
            self.pushButton_zhengGao.setStyleSheet("background-color:white;color:black")
            self.pushButton_fuGao.setStyleSheet("background-color:white;color:black")
            self.pushButton_noDocLv.setStyleSheet("background-color:white;color:black")
            
            self.pushButton_noDocLv.setStyleSheet("background-color:blue;color:white")
            
        #------------------SQL   查询----------------------------------------
        """
        db = mc.connect(host="localhost", user="root", password="zaq1XSW2cde3", database="electronicHealth")
        cursor = db.cursor()
        sql = "SELECT FROM 医生 \
                WHERE (科室,职称) =  \
                ('%s','%s')" % \
                (self.selectDept,self.selectDocLv)
        cursor.execute(sql)
        doctorResult = cursor.fetchall()
        """
    #-------------------------------------------
    #
    #            选择科室
    #
    #-------------------------------------------
    
    def on_click_selectDept(self,selectDeptBtn):
        if selectDeptBtn == self.pushButton_alldept:
            self.selectDept = "*"
            
            self.pushButton_alldept.setStyleSheet("background-color:white;color:black")
            self.pushButton_erBiHouKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_fuChanKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_neiKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_waiKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_guKe.setStyleSheet("background-color:white;color:black")
            
            self.pushButton_alldept.setStyleSheet("background-color:blue;color:white")
        
        elif selectDeptBtn == self.pushButton_erBiHouKe:
            self.selectDept = "耳鼻喉科"
            
            self.pushButton_alldept.setStyleSheet("background-color:white;color:black")
            self.pushButton_erBiHouKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_fuChanKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_neiKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_waiKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_guKe.setStyleSheet("background-color:white;color:black")
            
            self.pushButton_erBiHouKe.setStyleSheet("background-color:blue;color:white")
            
        elif selectDeptBtn == self.pushButton_fuChanKe:
            self.selectDept = "妇产科"
            
            self.pushButton_alldept.setStyleSheet("background-color:white;color:black")
            self.pushButton_erBiHouKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_fuChanKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_neiKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_waiKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_guKe.setStyleSheet("background-color:white;color:black")
            
            self.pushButton_fuChanKe.setStyleSheet("background-color:blue;color:white")
            
        elif selectDeptBtn == self.pushButton_neiKe:
            self.selectDept = "内科"
            
            self.pushButton_alldept.setStyleSheet("background-color:white;color:black")
            self.pushButton_erBiHouKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_fuChanKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_neiKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_waiKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_guKe.setStyleSheet("background-color:white;color:black")
            
            self.pushButton_neiKe.setStyleSheet("background-color:blue;color:white")
            
        elif selectDeptBtn == self.pushButton_waiKe:
            self.selectDept = "外科"
            
            self.pushButton_alldept.setStyleSheet("background-color:white;color:black")
            self.pushButton_erBiHouKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_fuChanKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_neiKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_waiKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_guKe.setStyleSheet("background-color:white;color:black")
            
            self.pushButton_waiKe.setStyleSheet("background-color:blue;color:white")
            
        elif selectDeptBtn == self.pushButton_guKe:
            self.selectDept = "骨科"
            
            self.pushButton_alldept.setStyleSheet("background-color:white;color:black")
            self.pushButton_erBiHouKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_fuChanKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_neiKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_waiKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_guKe.setStyleSheet("background-color:white;color:black")
            
            self.pushButton_guKe.setStyleSheet("background-color:blue;color:white")
        
    def on_click_readEssay(self):
        #--------------New a Window-----------------------
        #--------------select all essays which are written by --selectedDoc--  -------------
        self.widget = searchEssayWin(self.selectedDoc)
        self.widget.show()
    
    
    def on_click_startChatting(self):
        #--------------New Paying Window------------------
        self.money = self.selectedDoc
        self.widget = payingWin(self.money)
        self.widget.show()
        
    
    
    def listClicked(self):
        self.selectedDoc = self.listWidget.selectedItems()[0].text()
        self.setWindowTitle(self.selectedDoc)
    
    def initUI(self):
        self.setObjectName("Form")
        self.resize(1100, 684)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        self.setFont(font)
        
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 1031, 131))
        self.groupBox.setObjectName("groupBox")
        
        self.label_dept = QtWidgets.QLabel(self.groupBox)
        self.label_dept.setGeometry(QtCore.QRect(10, 30, 72, 15))
        self.label_dept.setObjectName("label")
        self.label_docLv = QtWidgets.QLabel(self.groupBox)
        self.label_docLv.setGeometry(QtCore.QRect(10, 90, 72, 15))
        self.label_docLv.setObjectName("label_2")
        #----------------------set Search prerequisites-----------------------------------
        self.pushButton_alldept = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_alldept.setGeometry(QtCore.QRect(160, 20, 93, 28))
        self.pushButton_alldept.setObjectName("pushButton")
        self.pushButton_alldept.clicked.connect(lambda:self.on_click_selectDept(self.pushButton_alldept))
        
        self.pushButton_allDocLv = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_allDocLv.setGeometry(QtCore.QRect(160, 80, 93, 28))
        self.pushButton_allDocLv.setObjectName("pushButton_2")
        self.pushButton_allDocLv.clicked.connect(lambda:self.on_click_selectDocLv(self.pushButton_allDocLv))
        
        self.pushButton_zhengGao = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_zhengGao.setGeometry(QtCore.QRect(330, 80, 93, 28))
        self.pushButton_zhengGao.setObjectName("pushButton_3")
        self.pushButton_zhengGao.clicked.connect(lambda:self.on_click_selectDocLv(self.pushButton_zhengGao))
        
        self.pushButton_neiKe = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_neiKe.setGeometry(QtCore.QRect(330, 20, 93, 28))
        self.pushButton_neiKe.setObjectName("pushButton_4")
        self.pushButton_neiKe.clicked.connect(lambda:self.on_click_selectDept(self.pushButton_neiKe))
        
        self.pushButton_waiKe = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_waiKe.setGeometry(QtCore.QRect(490, 20, 93, 28))
        self.pushButton_waiKe.setObjectName("pushButton_5")
        self.pushButton_waiKe.clicked.connect(lambda:self.on_click_selectDept(self.pushButton_waiKe))
        
        self.pushButton_fuGao = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_fuGao.setGeometry(QtCore.QRect(490, 80, 93, 28))
        self.pushButton_fuGao.setObjectName("pushButton_6")
        self.pushButton_fuGao.clicked.connect(lambda:self.on_click_selectDocLv(self.pushButton_fuGao))
        
        self.pushButton_erBiHouKe = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_erBiHouKe.setGeometry(QtCore.QRect(790, 20, 93, 28))
        self.pushButton_erBiHouKe.setObjectName("pushButton_7")
        self.pushButton_erBiHouKe.clicked.connect(lambda:self.on_click_selectDept(self.pushButton_erBiHouKe))
        
        self.pushButton_guKe = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_guKe.setGeometry(QtCore.QRect(640, 20, 93, 28))
        self.pushButton_guKe.setObjectName("pushButton_8")
        self.pushButton_guKe.clicked.connect(lambda:self.on_click_selectDept(self.pushButton_guKe))
        
        self.pushButton_noDocLv = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_noDocLv.setGeometry(QtCore.QRect(640, 80, 93, 28))
        self.pushButton_noDocLv.setObjectName("pushButton_10")
        self.pushButton_noDocLv.clicked.connect(lambda:self.on_click_selectDocLv(self.pushButton_noDocLv))
        
        self.pushButton_fuChanKe = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_fuChanKe.setGeometry(QtCore.QRect(920, 20, 93, 28))
        self.pushButton_fuChanKe.setObjectName("pushButton_11")
        self.pushButton_fuChanKe.clicked.connect(lambda:self.on_click_selectDept(self.pushButton_fuChanKe))
        #--------------------------Searching Results-----------------------------
        self.listWidget = QtWidgets.QListWidget(self)
        self.listWidget.setGeometry(QtCore.QRect(30, 240, 1031, 401))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.itemClicked.connect(self.listClicked)
                               #-------------Debug---------------#
        self.listWidget.addItems(["单晓辉","曹启明","郭鸣轩"])
        
        
        
        #--------------------------Read Essay Button-----------------------------
        self.readEssay = QtWidgets.QPushButton(self)
        self.readEssay.setGeometry(QtCore.QRect(920, 200, 93, 28))
        self.readEssay.setObjectName("pushButton_11")
        self.readEssay.clicked.connect(self.on_click_readEssay)
        
        #--------------------------Start chatting--------------------------------
        self.startChatting = QtWidgets.QPushButton(self)
        self.startChatting.setGeometry(QtCore.QRect(920, 200, 93, 28))
        self.startChatting.setObjectName("pushButton_11")
        self.startChatting.clicked.connect(self.on_click_startChatting)
        
        
        self.label_result = QtWidgets.QLabel(self)
        self.label_result.setGeometry(QtCore.QRect(480, 170, 131, 51))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(18)
        self.label_result.setFont(font)
        self.label_result.setObjectName("label_3")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "筛选条件"))
        self.label_dept.setText(_translate("Form", "科室："))
        self.label_docLv.setText(_translate("Form", "医生职称："))
        self.pushButton_alldept.setText(_translate("Form", "全部"))
        self.pushButton_allDocLv.setText(_translate("Form", "全部"))
        self.pushButton_zhengGao.setText(_translate("Form", "正高"))
        self.pushButton_neiKe.setText(_translate("Form", "内科"))
        self.pushButton_waiKe.setText(_translate("Form", "外科"))
        self.pushButton_fuGao.setText(_translate("Form", "副高"))
        self.pushButton_erBiHouKe.setText(_translate("Form", "耳鼻喉科"))
        self.pushButton_guKe.setText(_translate("Form", "骨科"))
        self.pushButton_noDocLv.setText(_translate("Form", "无职称"))
        self.pushButton_fuChanKe.setText(_translate("Form", "妇产科"))
        self.label_result.setText(_translate("Form", "查询结果"))
        self.readEssay.setText(_translate("Form","阅读文章 "))
        self.startChatting.setText(_translate("Form","付费咨询 "))
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = selectDocWin()
    win.show()
    sys.exit(app.exec_())









