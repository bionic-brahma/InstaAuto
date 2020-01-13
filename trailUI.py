# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from GUIs.InstaEngine import InstaAuto


class Ui_TrailForm(object):
    def __init__(self):
        self.instaAuto = InstaAuto()

    def setupUi(self, TrailForm):
        TrailForm.setObjectName("TrailForm")
        TrailForm.setEnabled(True)
        TrailForm.resize(380, 180)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TrailForm.sizePolicy().hasHeightForWidth())
        TrailForm.setSizePolicy(sizePolicy)
        TrailForm.setMinimumSize(QtCore.QSize(380, 180))
        TrailForm.setMaximumSize(QtCore.QSize(380, 180))
        TrailForm.setAcceptDrops(False)
        self.startEngine_btn = QtWidgets.QPushButton(TrailForm)
        self.startEngine_btn.setGeometry(QtCore.QRect(110, 130, 151, 31))
        self.startEngine_btn.setAutoFillBackground(False)
        self.startEngine_btn.setStyleSheet("background-color: rgb(239, 41, 41);\n"
                                           "font: 15pt \"Ubuntu\";")
        self.startEngine_btn.setObjectName("startEngine_btn")
        self.Insta_password = QtWidgets.QLineEdit(TrailForm)
        self.Insta_password.setGeometry(QtCore.QRect(60, 80, 271, 25))
        self.Insta_password.setStyleSheet("background-color: rgb(252, 175, 62);")
        self.Insta_password.setObjectName("Insta_password")
        self.Insta_password.setPlaceholderText("Instagram password here")
        self.label = QtWidgets.QLabel(TrailForm)
        self.label.setGeometry(QtCore.QRect(20, 20, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Insta_username = QtWidgets.QLineEdit(TrailForm)
        self.Insta_username.setGeometry(QtCore.QRect(60, 50, 271, 25))
        self.Insta_username.setStyleSheet("background-color: rgb(252, 175, 62);")
        self.Insta_username.setObjectName("Insta_username")
        self.Insta_username.setPlaceholderText("Give your instagram username here")
        self.Message_from_machine = QtWidgets.QLabel(TrailForm)
        self.Message_from_machine.setGeometry(QtCore.QRect(40, 110, 381, 16))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.Message_from_machine.setFont(font)
        self.Message_from_machine.setStyleSheet("color: rgb(204, 0, 0);")
        self.Message_from_machine.setObjectName("Message_from_machine")

        self.retranslateUi(TrailForm)
        QtCore.QMetaObject.connectSlotsByName(TrailForm)
        self.startEngine_btn.clicked.connect(self.Insta_GO)

    def retranslateUi(self, TrailForm):
        _translate = QtCore.QCoreApplication.translate
        TrailForm.setWindowTitle(_translate("TrailForm", "Trial For InstaAuto"))
        self.startEngine_btn.setText(_translate("TrailForm", "Start Engine"))
        self.label.setText(_translate("TrailForm", "Please Enter Instgram Credentials"))
        self.Message_from_machine.setText(_translate("TrailForm",
                                                     "This is one time use for your ID for trial. Please follow premium package for further use"))

    def Insta_GO(self):
        if self.Insta_username.text() != "" and self.Insta_password.text() != "":
            self.instaAuto.insta_auto_start(self.Insta_password.text(), self.Insta_username.text(), 20)
        else:
            self.Message_from_machine.setText("Credentials are required.")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    TrailForm = QtWidgets.QWidget()
    ui = Ui_TrailForm()
    ui.setupUi(TrailForm)
    TrailForm.show()
    sys.exit(app.exec_())
