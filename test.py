# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 08:01:26 2018

@author: gmx
"""
"""
import sys
from PyQt5.QtWidgets import QApplication,QWidget


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    w = QWidget()
    w.resize(250,150)
    w.move(300,300)
    w.setWindowTitle('Simple')
    w.show()
    
    sys.exit(app.exec_())
"""

"""
import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        
        self.setGeometry(300,300,300,220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
"""
"""
import sys
from PyQt5.QtWidgets import (QWidget,QToolTip,QPushButton,QApplication)
from PyQt5.QtGui import QFont


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        QToolTip.setFont(QFont('sansSerif',10))
        
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        btn = QPushButton('Button',self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')     #setToolTip方法为当前对象添加一个提示框
        btn.resize(btn.sizeHint())
        btn.move(50,50)
        
        self.setGeometry(300,300,300,220)
        self.setWindowTitle('ToolTip')
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
"""
"""

import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        
        qbtn = QPushButton('Quit',self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50,50)
        
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Quit Button')
        self.show()
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
"""
"""
import sys
from PyQt5.QtWidgets import QWidget,QMessageBox,QApplication


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Message Box')
        self.show()
        
    
    def closeEvent(self,event):
        
        reply = QMessageBox.question(self,'Message',
                                     "Are you sure to quit?",QMessageBox.Yes|
                                     QMessageBox.No,QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            
            
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
"""
"""
import sys
from PyQt5.QtWidgets import QWidget,QDesktopWidget,QApplication,QPushButton,QListWidget
from PyQt5 import QtCore

class newWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.resize(400,300)
        self.setWindowTitle('Fuck')


class Example(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.neex = newWidget()
        
    def listClicked(self):
        self.setWindowTitle(str(self.listWidget.selectedItems()[0].text()))
        print(self.listWidget.selectedItems()[0].text())
        
    def initUI(self):
        
        self.resize(250,150)
        self.center()
        
        self.setWindowTitle('Center')
        
        
        btn = QPushButton('Button',self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')   
        btn.resize(btn.sizeHint())
        btn.clicked.connect(lambda:self.on_click(btn))
        
        
        self.listWidget = QListWidget(self)
        self.listWidget.setGeometry(QtCore.QRect(30, 240, 1031, 401))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.addItems(['item1','item2'])
        self.listWidget.itemClicked.connect(self.listClicked)
        
        self.show()
    def on_click(self,butn):
        butn.setStyleSheet("background-color:blue")
        
    
    def center(self):
        
        qr = self.frameGeometry()                           #得到主窗口大小，qr是一个矩形
        cp = QDesktopWidget().availableGeometry().center()  #获得显示器分辨率，取得其中间点的位置
        qr.moveCenter(cp)                                   #把qr矩形放到cp处
        self.move(qr.topLeft())                             #把窗口左上角移动到qr左上角
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

        
"""


import socket

ip_port = ('10.6.94.3',9997)

sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
    print ('server waiting...')
    conn,addr = sk.accept()

    while True:
        data = conn.recv(1024)
        
        print(str(data,encoding='utf-8'))
        
        conn.sendall(bytes("在？KKP",encoding='utf8'))
            
    conn.close()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



