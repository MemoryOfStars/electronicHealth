# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chating.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import mysql.connector as mc

import threading

import time
import socket
import sys








class chattingWin(QtWidgets.QWidget):
    def __init__(self,doctorID):
        super().__init__()
        self.doctorID = doctorID
        #---------------------患者端---------------------#
        """
        sql = 'SELECT ip FROM DOCTOR\
                WHERE 医生ID = doctorID'
        db = mc.connect(host="localhost", user="root", password="zaq1XSW2cde3", database="electronicHealth")
        cursor = db.cursor()
        
        cursor.execute(sql)
        
        self.ip_port = cursor.fetchall()[0][0]
        
        self.sk = socket.socket()
        
        self.sk.connect(ip_port)
        """
        
        #--------------------医生端---------------------#
        self.ip_port = ('10.6.94.3',9999)

        self.sk = socket.socket()
        self.sk.bind(self.ip_port)
        self.sk.listen(10)
        
        #-----------------医生端/患者端--都要新建线程来接受socket的消息------------------#
        
        t= threading.Thread(target=self.waiting_msg,args=(111,112))#创建线程
        t.setDaemon(True)#设置为后台线程，这里默认是False，设置为True之后则主线程不用等待子线程
        t.start()#开启线程
        
        
        
        
        self.initUI()
        
    
    def waiting_msg(self):
        
        #-------------------医生端----------------------------#
        """
        while True:
            print ('server waiting...')
            self.conn,self.addr = self.sk.accept()

            while True:
                data = conn.recv(1024)
                #----------------在大的TextEdit里面显示----------------#
                print(str(data,encoding='utf-8'))
        
            conn.close()
        """
        #------------------患者端-----------------------------#
        
        while True:
            reply_msg = self.sk.recv(1024)
            #-------------------在打的TextEdit里面显示-----------------#
            print(str(reply_msg,encoding='utf-8'))
    
    #--------按 发送 Button 之后，读取输入框的内容并发送给另一端，同时显示在打的TextEdit中--------#
    def on_click_sendMess(self):
        send_mes = self.textEdit_input.text()
        #------------------患者端-----------------------------#
        self.sk.sendall(bytes(send_mes,encoding='utf8'))
        #------------------医生端-----------------------------#
        """
        self.conn.sendall(bytes(send_mes,encoding='utf8'))
        """
    
    
    
    
    
    
    
    def initUI(self):
        self.setObjectName("Chatting")
        self.resize(794, 575)
        #self.setWindowTitle("咨询聊天")
        
        
        self.textEdit_chat = QtWidgets.QTextEdit(self)
        self.textEdit_chat.setGeometry(QtCore.QRect(150, 10, 631, 411))
        self.textEdit_chat.setObjectName("textEdit_chat")
        
        
        self.textEdit_input = QtWidgets.QTextEdit(self)
        self.textEdit_input.setGeometry(QtCore.QRect(150, 470, 631, 101))
        self.textEdit_input.setObjectName("textEdit_2")
        
        self.pushButton_sendPic = QtWidgets.QPushButton(self)
        self.pushButton_sendPic.setGeometry(QtCore.QRect(150, 430, 93, 28))
        self.pushButton_sendPic.setObjectName("pushButton")
        
        self.pushButton_send = QtWidgets.QPushButton(self)
        self.pushButton_send.setGeometry(QtCore.QRect(260, 430, 93, 28))
        self.pushButton_send.setObjectName("pushButton_2")
        
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 131, 531))
        self.groupBox.setObjectName("groupBox")
        
        self.label_docPic = QtWidgets.QLabel(self.groupBox)
        self.label_docPic.setGeometry(QtCore.QRect(10, 40, 101, 171))
        self.label_docPic.setObjectName("label")
        self.gif = QtGui.QMovie('canvas.png')
        self.label_docPic.setMovie(self.gif)
        self.gif.start()
        

        
        self.label_docResume = QtWidgets.QLabel(self.groupBox)
        self.label_docResume.setGeometry(QtCore.QRect(20, 260, 81, 191))
        self.label_docResume.setObjectName("label_2")
        
        self.pushButton_endChat = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_endChat.setGeometry(QtCore.QRect(20, 490, 93, 28))
        self.pushButton_endChat.setObjectName("pushButton_3")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Chatting", self.doctorID))
        self.textEdit_input.setHtml(_translate("Chatting", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_sendPic.setText(_translate("Chatting", "发送图片"))
        self.pushButton_send.setText(_translate("Chatting", "发送"))
        self.groupBox.setTitle(_translate("Chatting", "医生信息"))
        #self.label_docPic.setText(_translate("Chatting", "pictures here"))
        #self.label_docPic.setPixmap(_translate("Chatting",self.png))
        self.label_docResume.setText(_translate("Chatting", "Resumes Here"))
        self.pushButton_endChat.setText(_translate("Chatting", "结束咨询"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    ex = chattingWin()
    ex.show()
    sys.exit(app.exec_())





