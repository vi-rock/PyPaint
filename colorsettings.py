# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets


class ColorSettingsWidget(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(94, 502)
        self.base_color = QtWidgets.QLabel(Form)
        self.base_color.setGeometry(QtCore.QRect(10, 12, 71, 31))
        self.base_color.setText("")
        self.base_color.setObjectName("base_color")
        self.extra_color = QtWidgets.QLabel(Form)
        self.extra_color.setGeometry(QtCore.QRect(10, 80, 71, 31))
        self.extra_color.setText("")
        self.extra_color.setObjectName("extra_color")
        self.base_button = QtWidgets.QPushButton(Form)
        self.base_button.setGeometry(QtCore.QRect(10, 50, 75, 23))
        self.base_button.setObjectName("base_button")
        self.extra_button = QtWidgets.QPushButton(Form)
        self.extra_button.setGeometry(QtCore.QRect(10, 120, 75, 23))
        self.extra_button.setObjectName("extra_button")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 150, 71, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.base_button.setText(_translate("Form", "Base Color"))
        self.extra_button.setText(_translate("Form", "Extra Color"))
