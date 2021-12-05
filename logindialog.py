# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class LoginDialogWidget(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(253, 123)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(80, 50, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.user_name_label = QtWidgets.QLineEdit(Dialog)
        self.user_name_label.setGeometry(QtCore.QRect(130, 20, 113, 20))
        self.user_name_label.setObjectName("user_name_label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.registr = QtWidgets.QPushButton(Dialog)
        self.registr.setGeometry(QtCore.QRect(170, 90, 71, 23))
        self.registr.setObjectName("registr")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "User Name"))
        self.registr.setText(_translate("Dialog", "Register"))
