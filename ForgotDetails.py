# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ForgotDetails.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ForgotDetails_assistance(object):
    def setupUi(self, ForgotDetails_assistance):
        ForgotDetails_assistance.setObjectName("ForgotDetails_assistance")
        ForgotDetails_assistance.setEnabled(True)
        ForgotDetails_assistance.resize(380, 180)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ForgotDetails_assistance.sizePolicy().hasHeightForWidth())
        ForgotDetails_assistance.setSizePolicy(sizePolicy)
        ForgotDetails_assistance.setMinimumSize(QtCore.QSize(380, 180))
        ForgotDetails_assistance.setMaximumSize(QtCore.QSize(380, 180))
        ForgotDetails_assistance.setAcceptDrops(False)
        self.getAssistance_btn = QtWidgets.QPushButton(ForgotDetails_assistance)
        self.getAssistance_btn.setGeometry(QtCore.QRect(110, 130, 151, 31))
        self.getAssistance_btn.setAutoFillBackground(False)
        self.getAssistance_btn.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"font: 15pt \"Ubuntu\";")
        self.getAssistance_btn.setObjectName("getAssistance_btn")
        self.instagram_handle = QtWidgets.QLineEdit(ForgotDetails_assistance)
        self.instagram_handle.setGeometry(QtCore.QRect(60, 80, 271, 25))
        self.instagram_handle.setStyleSheet("background-color: rgb(252, 175, 62);")
        self.instagram_handle.setObjectName("instagram_handle")
        self.instagram_handle.setPlaceholderText("Your instagram handle here")
        self.label = QtWidgets.QLabel(ForgotDetails_assistance)
        self.label.setGeometry(QtCore.QRect(20, 20, 341, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.access_EmailId = QtWidgets.QLineEdit(ForgotDetails_assistance)
        self.access_EmailId.setGeometry(QtCore.QRect(60, 50, 271, 25))
        self.access_EmailId.setStyleSheet("background-color: rgb(252, 175, 62);")
        self.access_EmailId.setObjectName("access_EmailId")
        self.access_EmailId.setPlaceholderText("Your registered Email")
        self.Message_from_machine = QtWidgets.QLabel(ForgotDetails_assistance)
        self.Message_from_machine.setGeometry(QtCore.QRect(40, 110, 381, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Message_from_machine.setFont(font)
        self.Message_from_machine.setStyleSheet("color: rgb(204, 0, 0);")
        self.Message_from_machine.setObjectName("Message_from_machine")

        self.retranslateUi(ForgotDetails_assistance)
        QtCore.QMetaObject.connectSlotsByName(ForgotDetails_assistance)

    def retranslateUi(self, ForgotDetails_assistance):
        _translate = QtCore.QCoreApplication.translate
        ForgotDetails_assistance.setWindowTitle(_translate("ForgotDetails_assistance", "Assistance Provider"))
        self.getAssistance_btn.setText(_translate("ForgotDetails_assistance", "Get Assistance"))
        self.label.setText(_translate("ForgotDetails_assistance", "Please provide some details for the support team"))
        self.Message_from_machine.setText(_translate("ForgotDetails_assistance", "Please give correct information only."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ForgotDetails_assistance = QtWidgets.QWidget()
    ui = Ui_ForgotDetails_assistance()
    ui.setupUi(ForgotDetails_assistance)
    ForgotDetails_assistance.show()
    sys.exit(app.exec_())

