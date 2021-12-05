# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets


class BrushSettingsWidget(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(102, 531)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 0, 21, 31))
        self.label.setObjectName("label")
        self.sizelSlider = QtWidgets.QSlider(Form)
        self.sizelSlider.setGeometry(QtCore.QRect(10, 30, 22, 160))
        self.sizelSlider.setMinimum(1)
        self.sizelSlider.setMaximum(50)
        self.sizelSlider.setProperty("value", 10)
        self.sizelSlider.setOrientation(QtCore.Qt.Vertical)
        self.sizelSlider.setObjectName("sizelSlider")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 190, 81, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.fillBox = QtWidgets.QCheckBox(Form)
        self.fillBox.setGeometry(QtCore.QRect(50, 30, 41, 17))
        self.fillBox.setObjectName("fillBox")
        self.styleBox = QtWidgets.QCheckBox(Form)
        self.styleBox.setGeometry(QtCore.QRect(50, 50, 51, 17))
        self.styleBox.setObjectName("styleBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Size:"))
        self.fillBox.setText(_translate("Form", "Fill"))
        self.styleBox.setText(_translate("Form", "Style"))
