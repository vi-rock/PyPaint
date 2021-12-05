# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class InfoWidget(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 349)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 10, 200, 200))
        font = QtGui.QFont()
        font.setFamily("Lobster")
        font.setPointSize(50)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 230, 381, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Save -     <span style=\" font-weight:600;\">Ctrl + S</span><br />New -     <span style=\" font-weight:600;\">Ctrl + N</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Undo -     <span style=\" font-weight:600;\">Ctrl + Z</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Redo -     <span style=\" font-weight:600;\">Ctrl + Y</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Brush -     <span style=\" font-weight:600;\">Ctrl + 0 ... 6</span></p></body></html>"))
