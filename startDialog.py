# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets


class StartDialogWidget(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 245)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 210, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.size_x = QtWidgets.QSpinBox(Dialog)
        self.size_x.setGeometry(QtCore.QRect(240, 10, 61, 21))
        self.size_x.setMinimum(300)
        self.size_x.setMaximum(1024)
        self.size_x.setObjectName("size_x")
        self.size_y = QtWidgets.QSpinBox(Dialog)
        self.size_y.setGeometry(QtCore.QRect(330, 10, 61, 21))
        self.size_y.setMinimum(300)
        self.size_y.setMaximum(1024)
        self.size_y.setObjectName("size_y")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(310, 10, 16, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(66, 10, 161, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.basic_color = QtWidgets.QLabel(Dialog)
        self.basic_color.setGeometry(QtCore.QRect(10, 10, 61, 41))
        self.basic_color.setText("")
        self.basic_color.setObjectName("basic_color")
        self.extra_color = QtWidgets.QLabel(Dialog)
        self.extra_color.setGeometry(QtCore.QRect(10, 90, 61, 41))
        self.extra_color.setText("")
        self.extra_color.setObjectName("extra_color")
        self.extr_button = QtWidgets.QPushButton(Dialog)
        self.extr_button.setGeometry(QtCore.QRect(10, 140, 75, 23))
        self.extr_button.setObjectName("extr_button")
        self.basic_button = QtWidgets.QPushButton(Dialog)
        self.basic_button.setGeometry(QtCore.QRect(10, 60, 75, 23))
        self.basic_button.setObjectName("basic_button")
        self.file_path = QtWidgets.QLineEdit(Dialog)
        self.file_path.setGeometry(QtCore.QRect(220, 60, 131, 20))
        self.file_path.setReadOnly(True)
        self.file_path.setObjectName("file_path")
        self.choose_file = QtWidgets.QPushButton(Dialog)
        self.choose_file.setGeometry(QtCore.QRect(360, 60, 21, 23))
        self.choose_file.setObjectName("choose_file")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(130, 60, 71, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.view = QtWidgets.QLabel(Dialog)
        self.view.setGeometry(QtCore.QRect(220, 90, 160, 90))
        self.view.setText("")
        self.view.setObjectName("view")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "X"))
        self.label_2.setText(_translate("Dialog", "Size of canvas"))
        self.extr_button.setText(_translate("Dialog", "Extra color"))
        self.basic_button.setText(_translate("Dialog", "Base color"))
        self.choose_file.setText(_translate("Dialog", "..."))
        self.label_3.setText(_translate("Dialog", "Custom image"))