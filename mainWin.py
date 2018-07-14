# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWin.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from selectDocWin import selectDocWin
from payingWin import payingWin
from chattingWin import chattingWin
from searchEssayWin import searchEssayWin
import sys

class mainWin(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.widget = QtWidgets.QWidget()
        
    #---------------------------------------------------------------#
    #                                                               #
    #              支付窗口   操作其他窗口的 按钮    响应函数         #
    #                                                               #
    #---------------------------------------------------------------#
    def on_click_payCompleted(self):#新建聊天窗口---------------------应该等聊天窗口关闭之后才能继续操作其他窗口
        self.setWindowTitle(self.win_paying.payingMethod)
        self.widget = chattingWin(self.win_selectDoc.selectedDoc)       #-------应该传医生ID进去（获取医生各种信息）
        
        self.widget.show()
    
    
    def on_click_payCanceled(self):
        #----------------cancel data in the database-------------------------------
        #----------------close current window--------------------------------------
        self.widget_payingWin.hide()
        
        self.widget_selectDocWin.show()

    #---------------------------------------------------------------#
    #                                                               #
    #          选择医生窗口   操作其他窗口的 按钮    响应函数         #
    #                                                               #
    #---------------------------------------------------------------#
    
        
    def on_click_readEssay(self):
        #--------------New a Window-----------------------
        #--------------select all essays which are written by --selectedDoc--  -------------
        self.widget_selectDocWin.hide()
        
        self.win_searchEssay = searchEssayWin(self.widget_searchEssayWin,self.win_selectDoc.selectedDoc)
        self.win_searchEssay.pushButton_back.clicked.connect(self.on_click_backto_selectDocWin)
        
        self.widget_searchEssayWin.show()
        """
        self.win_paying = payingWin(self.widget_payingWin,self.win_selectDoc.money)
        
        self.widget_payingWin.show()
        """
        
    def on_click_startChatting(self):
        #--------------New Paying Window------------------
        self.widget_selectDocWin.hide()
        
        self.win_paying = payingWin(self.widget_payingWin,self.win_selectDoc.money)
        self.win_paying.pushButton_payCanceled.clicked.connect(self.on_click_backto_selectDocWin)
        self.win_paying.pushButton_payCompleted.clicked.connect(self.on_click_payCompleted)
        #self.win_searchEssay = searchEssayWin(self.widget_searchEssayWin,self.win_selectDoc.doctor)
        self.widget_payingWin.show()
        #self.widget_searchEssayWin.show()


    #---------------------------------------------------------------#
    #                                                               #
    #          回到选择医生窗口   的 按钮  的  响应函数               #
    #                                                               #
    #---------------------------------------------------------------#        
        
        
        
    def on_click_backto_selectDocWin(self):
        
        self.widget_payingWin.hide()
        
        self.widget_searchEssayWin.hide()
        
        self.widget_selectDocWin.show()
        
        
        
        
        
        
        
    def initUI(self):
        self.setObjectName("Form")
        self.resize(1114, 715)
        
        self.widget_selectDocWin = QtWidgets.QWidget(self)
        self.widget_selectDocWin.setGeometry(QtCore.QRect(10, 10, 1101, 701))
        self.widget_selectDocWin.setObjectName("widget_selecctDocWin")
        self.win_selectDoc = selectDocWin(self.widget_selectDocWin)
        self.win_selectDoc.readEssay.clicked.connect(self.on_click_readEssay)
        self.win_selectDoc.startChatting.clicked.connect(self.on_click_startChatting)
        
        
        self.widget_searchEssayWin = QtWidgets.QWidget(self)
        self.widget_searchEssayWin.setGeometry(QtCore.QRect(10, 10, 1101, 701))
        self.widget_searchEssayWin.setObjectName("widget_searchEssayWin")
        self.widget_searchEssayWin.hide()
        
        
        
        
        self.widget_payingWin = QtWidgets.QWidget(self)
        self.widget_payingWin_pic = QtWidgets.QLabel(self.widget_payingWin)
        self.widget_payingWin_pic.setGeometry(QtCore.QRect(0,0,1101,701))
        self.temp_pic = QtGui.QPixmap("web.png")
        self.widget_payingWin_pic.setPixmap(self.temp_pic)
        self.widget_payingWin.setGeometry(QtCore.QRect(10, 10, 1101, 701))
        self.widget_payingWin.setObjectName("widget_payingWin")
        self.widget_payingWin.hide()
        
        
        

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "电子健康"))



app = QtWidgets.QApplication(sys.argv)
mainWin_ex = mainWin()
mainWin_ex.show()
sys.exit(app.exec_())
    