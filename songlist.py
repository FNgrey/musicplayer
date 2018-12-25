# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'songlist.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SongList(object):
    def setupUi(self, SongList):
        SongList.setObjectName("SongList")
        SongList.resize(871, 511)
        self.listWidget = QtWidgets.QListWidget(SongList)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 871, 511))
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(SongList)
        QtCore.QMetaObject.connectSlotsByName(SongList)

    def retranslateUi(self, SongList):
        _translate = QtCore.QCoreApplication.translate
        SongList.setWindowTitle(_translate("SongList", "Form"))

