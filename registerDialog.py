# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class RegisterDialogWidget(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(349, 214)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(170, 170, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.user_name_label = QtWidgets.QLineEdit(Dialog)
        self.user_name_label.setGeometry(QtCore.QRect(120, 20, 113, 20))
        self.user_name_label.setObjectName("user_name_label")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 50, 141, 141))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(170, 50, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.color_button = QtWidgets.QToolButton(Dialog)
        self.color_button.setGeometry(QtCore.QRect(230, 60, 25, 19))
        self.color_button.setObjectName("color_button")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "User Name"))
        self.label_4.setText(_translate("Dialog", "Color"))
        self.color_button.setText(_translate("Dialog", "..."))
