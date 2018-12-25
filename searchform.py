# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchform.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_searchForm(object):
    def setupUi(self, searchForm):
        searchForm.setObjectName("searchForm")
        searchForm.setWindowModality(QtCore.Qt.ApplicationModal)
        searchForm.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        searchForm.setWindowIcon(icon)
        self.layoutWidget = QtWidgets.QWidget(searchForm)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 110, 353, 69))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color:white")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.songbutton = QtWidgets.QRadioButton(self.layoutWidget)
        self.songbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.songbutton.setTabletTracking(False)
        self.songbutton.setAcceptDrops(False)
        self.songbutton.setAutoFillBackground(False)
        self.songbutton.setChecked(True)
        self.songbutton.setAutoRepeat(False)
        self.songbutton.setObjectName("songbutton")
        self.horizontalLayout_2.addWidget(self.songbutton)
        self.artbutton = QtWidgets.QRadioButton(self.layoutWidget)
        self.artbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.artbutton.setObjectName("artbutton")
        self.horizontalLayout_2.addWidget(self.artbutton)
        self.playlistbutton = QtWidgets.QRadioButton(self.layoutWidget)
        self.playlistbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.playlistbutton.setObjectName("playlistbutton")
        self.horizontalLayout_2.addWidget(self.playlistbutton)
        self.playerbutton = QtWidgets.QRadioButton(self.layoutWidget)
        self.playerbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.playerbutton.setObjectName("playerbutton")
        self.horizontalLayout_2.addWidget(self.playerbutton)
        self.exitbutton = QtWidgets.QPushButton(self.layoutWidget)
        self.exitbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitbutton.setStyleSheet("background-color:white")
        self.exitbutton.setObjectName("exitbutton")
        self.horizontalLayout_2.addWidget(self.exitbutton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(searchForm)
        QtCore.QMetaObject.connectSlotsByName(searchForm)

    def retranslateUi(self, searchForm):
        _translate = QtCore.QCoreApplication.translate
        searchForm.setWindowTitle(_translate("searchForm", "搜索"))
        self.label.setText(_translate("searchForm", "搜索："))
        self.pushButton.setText(_translate("searchForm", "确认"))
        self.songbutton.setText(_translate("searchForm", "歌曲"))
        self.artbutton.setText(_translate("searchForm", "歌手"))
        self.playlistbutton.setText(_translate("searchForm", "歌单"))
        self.playerbutton.setText(_translate("searchForm", "用户"))
        self.exitbutton.setText(_translate("searchForm", "退出"))

