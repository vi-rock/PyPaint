# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class ProfileWidget(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(231, 283)
        self.user_photo = QtWidgets.QLabel(Form)
        self.user_photo.setGeometry(QtCore.QRect(40, 20, 141, 141))
        self.user_photo.setText("")
        self.user_photo.setScaledContents(True)
        self.user_photo.setObjectName("user_photo")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 180, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.user_name_label = QtWidgets.QLabel(Form)
        self.user_name_label.setGeometry(QtCore.QRect(70, 180, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.user_name_label.setFont(font)
        self.user_name_label.setObjectName("user_name_label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 210, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.user_image_count = QtWidgets.QLabel(Form)
        self.user_image_count.setGeometry(QtCore.QRect(10, 240, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.user_image_count.setFont(font)
        self.user_image_count.setAlignment(QtCore.Qt.AlignCenter)
        self.user_image_count.setObjectName("user_image_count")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "User:"))
        self.user_name_label.setText(_translate("Form", "Not log in"))
        self.label_3.setText(_translate("Form", "Image Count:"))
        self.user_image_count.setText(_translate("Form", "0"))
