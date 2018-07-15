# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gradeWin.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class gradingWin(QtWidgets.QWidget):
    
    def __init__(self,doctorID):
        super().__init__()
        
        self.doctorID = doctorID #--------------------对对应的医生进行打分------------------#
        self.grade = 5
        
        
        self.initUI()
    
    
    def pushButton1_turnBlue(self,QEvent):
        self.pushButton_2.setStyleSheet("background-color:white;color:black")
        self.pushButton_3.setStyleSheet("background-color:white;color:black")
        self.pushButton_4.setStyleSheet("background-color:white;color:black")
        self.pushButton_5.setStyleSheet("background-color:white;color:black")
        self.pushButton_6.setStyleSheet("background-color:white;color:black")
        
        self.pushButton_2.setStyleSheet("background-color:blue;color:white")
        
        self.grade = 1
    def pushButton2_turnBlue(self,QEvent):
        self.pushButton_2.setStyleSheet("background-color:white;color:black")
        self.pushButton_3.setStyleSheet("background-color:white;color:black")
        self.pushButton_4.setStyleSheet("background-color:white;color:black")
        self.pushButton_5.setStyleSheet("background-color:white;color:black")
        self.pushButton_6.setStyleSheet("background-color:white;color:black")
        
        self.pushButton_2.setStyleSheet("background-color:blue;color:white")
        self.pushButton_3.setStyleSheet("background-color:blue;color:white")
        
        self.grade = 2
    def pushButton3_turnBlue(self,QEvent):
        self.pushButton_2.setStyleSheet("background-color:white;color:black")
        self.pushButton_3.setStyleSheet("background-color:white;color:black")
        self.pushButton_4.setStyleSheet("background-color:white;color:black")
        self.pushButton_5.setStyleSheet("background-color:white;color:black")
        self.pushButton_6.setStyleSheet("background-color:white;color:black")
        
        self.pushButton_2.setStyleSheet("background-color:blue;color:white")
        self.pushButton_3.setStyleSheet("background-color:blue;color:white")
        self.pushButton_4.setStyleSheet("background-color:blue;color:white")
        
        self.grade = 3
    def pushButton4_turnBlue(self,QEvent):
        self.pushButton_2.setStyleSheet("background-color:white;color:black")
        self.pushButton_3.setStyleSheet("background-color:white;color:black")
        self.pushButton_4.setStyleSheet("background-color:white;color:black")
        self.pushButton_5.setStyleSheet("background-color:white;color:black")
        self.pushButton_6.setStyleSheet("background-color:white;color:black")
        
        self.pushButton_2.setStyleSheet("background-color:blue;color:white")
        self.pushButton_3.setStyleSheet("background-color:blue;color:white")
        self.pushButton_4.setStyleSheet("background-color:blue;color:white")
        self.pushButton_5.setStyleSheet("background-color:blue;color:white")
        
        self.grade = 4
    def pushButton5_turnBlue(self,QEvent):
        self.pushButton_2.setStyleSheet("background-color:blue;color:white")
        self.pushButton_3.setStyleSheet("background-color:blue;color:white")
        self.pushButton_4.setStyleSheet("background-color:blue;color:white")
        self.pushButton_5.setStyleSheet("background-color:blue;color:white")
        self.pushButton_6.setStyleSheet("background-color:blue;color:white")
        
        self.grade = 5
        
        
    def endGrading(self):
        """
        读取数据库       以1/100的权重将评分统计到数据库
        """
        sql = "SELECT 医生分数 WHERE 医生ID = %s" % self.doctorID
        sql = "UPDATE HOSPITAL_MANAGEMENT SET GRADE=%s WHERE 医生ID = %s" % (self.grade,self.doctorID)
        
        self.close()
    
    """    
    def pushButton1_turnWhite(self,QEvent):
        self.pushButton_2.setStyleSheet("background-color:white;color:white")
        self.pushButton_3.setStyleSheet("background-color:white;color:white")
        self.pushButton_4.setStyleSheet("background-color:white;color:white")
        self.pushButton_5.setStyleSheet("background-color:white;color:white")
        self.pushButton_6.setStyleSheet("background-color:white;color:white")
    def pushButton2_turnWhite(self,QEvent):
        self.pushButton_2.setStyleSheet("background-color:white;color:white")
        self.pushButton_3.setStyleSheet("background-color:white;color:white")
        self.pushButton_4.setStyleSheet("background-color:white;color:white")
        self.pushButton_5.setStyleSheet("background-color:white;color:white")
        self.pushButton_6.setStyleSheet("background-color:white;color:white")
    def pushButton3_turnWhite(self,QEvent):
        self.pushButton_2.setStyleSheet("background-color:white;color:white")
        self.pushButton_3.setStyleSheet("background-color:white;color:white")
        self.pushButton_4.setStyleSheet("background-color:white;color:white")
        self.pushButton_5.setStyleSheet("background-color:white;color:white")
        self.pushButton_6.setStyleSheet("background-color:white;color:white")
    def pushButton4_turnWhite(self,QEvent):
        self.pushButton_2.setStyleSheet("background-color:white;color:white")
        self.pushButton_3.setStyleSheet("background-color:white;color:white")
        self.pushButton_4.setStyleSheet("background-color:white;color:white")
        self.pushButton_5.setStyleSheet("background-color:white;color:white")
        self.pushButton_6.setStyleSheet("background-color:white;color:white")
    def pushButton5_turnWhite(self,QEvent):
        self.pushButton_2.setStyleSheet("background-color:white;color:white")
        self.pushButton_3.setStyleSheet("background-color:white;color:white")
        self.pushButton_4.setStyleSheet("background-color:white;color:white")
        self.pushButton_5.setStyleSheet("background-color:white;color:white")
        self.pushButton_6.setStyleSheet("background-color:white;color:white")
    """    
        
        
    def initUI(self):
        self.setObjectName("Form")
        #Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(160, 240, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.endGrading)
        
        
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 100, 61, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.enterEvent = self.pushButton1_turnBlue
        #self.pushButton_2.leaveEvent = self.pushButton1_turnWhite
        
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 100, 61, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.enterEvent = self.pushButton2_turnBlue
        #self.pushButton_3.leaveEvent = self.pushButton2_turnWhite
        
        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(180, 100, 61, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.enterEvent = self.pushButton3_turnBlue
        #self.pushButton_4.leaveEvent = self.pushButton3_turnWhite
        
        self.pushButton_5 = QtWidgets.QPushButton(self)
        self.pushButton_5.setGeometry(QtCore.QRect(260, 100, 61, 61))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.enterEvent = self.pushButton4_turnBlue
        #self.pushButton_5.leaveEvent = self.pushButton4_turnWhite
        
        self.pushButton_6 = QtWidgets.QPushButton(self)
        self.pushButton_6.setGeometry(QtCore.QRect(330, 100, 61, 61))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.enterEvent = self.pushButton5_turnBlue
        #self.pushButton_6.leaveEvent = self.pushButton5_turnWhite

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "评分界面"))
        self.pushButton.setText(_translate("Form", "完成评分"))
        self.pushButton_2.setText(_translate("Form", "1"))
        self.pushButton_3.setText(_translate("Form", "2"))
        self.pushButton_4.setText(_translate("Form", "3"))
        self.pushButton_5.setText(_translate("Form", "4"))
        self.pushButton_6.setText(_translate("Form", "5"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = gradingWin("ds")
    ex.show()
    sys.exit(app.exec_())



