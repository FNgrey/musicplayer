# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'musicform.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MusicForm(object):
    def setupUi(self, MusicForm):
        MusicForm.setObjectName("MusicForm")
        MusicForm.resize(871, 511)
        MusicForm.setStyleSheet("")
        self.artimg = QtWidgets.QLabel(MusicForm)
        self.artimg.setGeometry(QtCore.QRect(40, 60, 300, 300))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.artimg.sizePolicy().hasHeightForWidth())
        self.artimg.setSizePolicy(sizePolicy)
        self.artimg.setText("")
        self.artimg.setPixmap(QtGui.QPixmap("icon/music.png"))
        self.artimg.setScaledContents(True)
        self.artimg.setObjectName("artimg")
        self.songlabel = QtWidgets.QLabel(MusicForm)
        self.songlabel.setGeometry(QtCore.QRect(460, 30, 321, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songlabel.sizePolicy().hasHeightForWidth())
        self.songlabel.setSizePolicy(sizePolicy)
        self.songlabel.setStyleSheet("font-family : 黑体;\n"
"font-size : 15pt;")
        self.songlabel.setTextFormat(QtCore.Qt.AutoText)
        self.songlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.songlabel.setWordWrap(True)
        self.songlabel.setObjectName("songlabel")
        self.artlabel = QtWidgets.QLabel(MusicForm)
        self.artlabel.setGeometry(QtCore.QRect(460, 90, 321, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.artlabel.sizePolicy().hasHeightForWidth())
        self.artlabel.setSizePolicy(sizePolicy)
        self.artlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.artlabel.setObjectName("artlabel")
        self.lyric = QtWidgets.QTextEdit(MusicForm)
        self.lyric.setGeometry(QtCore.QRect(390, 130, 441, 341))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lyric.sizePolicy().hasHeightForWidth())
        self.lyric.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lyric.setFont(font)
        self.lyric.setStyleSheet("background-color:transparent;\n"
"text-align:cente;")
        self.lyric.setLineWidth(1)
        self.lyric.setReadOnly(True)
        self.lyric.setObjectName("lyric")

        self.retranslateUi(MusicForm)
        QtCore.QMetaObject.connectSlotsByName(MusicForm)

    def retranslateUi(self, MusicForm):
        _translate = QtCore.QCoreApplication.translate
        MusicForm.setWindowTitle(_translate("MusicForm", "Form"))
        self.songlabel.setText(_translate("MusicForm", "歌曲"))
        self.artlabel.setText(_translate("MusicForm", "歌手"))
        self.lyric.setHtml(_translate("MusicForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

