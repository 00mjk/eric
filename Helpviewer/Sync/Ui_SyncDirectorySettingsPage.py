# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Helpviewer/Sync/SyncDirectorySettingsPage.ui'
#
# Created: Tue Nov 18 17:53:58 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SyncDirectorySettingsPage(object):
    def setupUi(self, SyncDirectorySettingsPage):
        SyncDirectorySettingsPage.setObjectName("SyncDirectorySettingsPage")
        SyncDirectorySettingsPage.resize(650, 400)
        SyncDirectorySettingsPage.setWindowTitle("")
        self.verticalLayout = QtWidgets.QVBoxLayout(SyncDirectorySettingsPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(SyncDirectorySettingsPage)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.directoryEdit = QtWidgets.QLineEdit(self.groupBox)
        self.directoryEdit.setObjectName("directoryEdit")
        self.horizontalLayout.addWidget(self.directoryEdit)
        self.directoryButton = QtWidgets.QToolButton(self.groupBox)
        self.directoryButton.setObjectName("directoryButton")
        self.horizontalLayout.addWidget(self.directoryButton)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(20, 317, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(SyncDirectorySettingsPage)
        QtCore.QMetaObject.connectSlotsByName(SyncDirectorySettingsPage)

    def retranslateUi(self, SyncDirectorySettingsPage):
        _translate = QtCore.QCoreApplication.translate
        SyncDirectorySettingsPage.setTitle(_translate("SyncDirectorySettingsPage", "Synchronize to a shared directory"))
        SyncDirectorySettingsPage.setSubTitle(_translate("SyncDirectorySettingsPage", "Please enter the data for synchronization via a shared directory. All fields must be filled."))
        self.groupBox.setTitle(_translate("SyncDirectorySettingsPage", "Shared Directory Settings"))
        self.label.setText(_translate("SyncDirectorySettingsPage", "Directory Name:"))
        self.directoryEdit.setToolTip(_translate("SyncDirectorySettingsPage", "Enter the full path of the shared directory"))
        self.directoryButton.setToolTip(_translate("SyncDirectorySettingsPage", "Select the shared directory via a directory selection dialog"))

