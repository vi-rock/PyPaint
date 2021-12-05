# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class TextDialogWidget(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(328, 421)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(170, 380, 141, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(36, 22, 261, 131))
        self.label.setStyleSheet("background-color:rgb(208, 208, 208)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horBox = QtWidgets.QComboBox(Dialog)
        self.horBox.setGeometry(QtCore.QRect(20, 160, 91, 22))
        self.horBox.setEditable(False)
        self.horBox.setModelColumn(0)
        self.horBox.setObjectName("horBox")
        self.horBox.addItem("")
        self.horBox.addItem("")
        self.horBox.addItem("")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(20, 190, 291, 191))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Hello"))
        self.horBox.setItemText(0, _translate("Dialog", "Left"))
        self.horBox.setItemText(1, _translate("Dialog", "Center"))
        self.horBox.setItemText(2, _translate("Dialog", "Right"))
