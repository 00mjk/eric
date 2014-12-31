# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Preferences/ConfigurationPages/CooperationPage.ui'
#
# Created: Tue Nov 18 17:53:57 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CooperationPage(object):
    def setupUi(self, CooperationPage):
        CooperationPage.setObjectName("CooperationPage")
        CooperationPage.resize(508, 540)
        CooperationPage.setWindowTitle("")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(CooperationPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.headerLabel = QtWidgets.QLabel(CooperationPage)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout_2.addWidget(self.headerLabel)
        self.line11 = QtWidgets.QFrame(CooperationPage)
        self.line11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line11.setObjectName("line11")
        self.verticalLayout_2.addWidget(self.line11)
        self.serverGroup = QtWidgets.QGroupBox(CooperationPage)
        self.serverGroup.setObjectName("serverGroup")
        self.gridLayout = QtWidgets.QGridLayout(self.serverGroup)
        self.gridLayout.setObjectName("gridLayout")
        self.autostartCheckBox = QtWidgets.QCheckBox(self.serverGroup)
        self.autostartCheckBox.setObjectName("autostartCheckBox")
        self.gridLayout.addWidget(self.autostartCheckBox, 0, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.serverGroup)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.serverPortSpin = QtWidgets.QSpinBox(self.serverGroup)
        self.serverPortSpin.setMinimum(1025)
        self.serverPortSpin.setMaximum(65535)
        self.serverPortSpin.setSingleStep(1)
        self.serverPortSpin.setProperty("value", 42000)
        self.serverPortSpin.setObjectName("serverPortSpin")
        self.gridLayout.addWidget(self.serverPortSpin, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(326, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.otherPortsCheckBox = QtWidgets.QCheckBox(self.serverGroup)
        self.otherPortsCheckBox.setObjectName("otherPortsCheckBox")
        self.gridLayout.addWidget(self.otherPortsCheckBox, 2, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.serverGroup)
        self.label_2.setEnabled(False)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.portToTrySpin = QtWidgets.QSpinBox(self.serverGroup)
        self.portToTrySpin.setEnabled(False)
        self.portToTrySpin.setMinimum(10)
        self.portToTrySpin.setMaximum(1000)
        self.portToTrySpin.setObjectName("portToTrySpin")
        self.gridLayout.addWidget(self.portToTrySpin, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(326, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.serverGroup)
        self.connectionsGroup = QtWidgets.QGroupBox(CooperationPage)
        self.connectionsGroup.setObjectName("connectionsGroup")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.connectionsGroup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.autoAcceptCheckBox = QtWidgets.QCheckBox(self.connectionsGroup)
        self.autoAcceptCheckBox.setObjectName("autoAcceptCheckBox")
        self.verticalLayout.addWidget(self.autoAcceptCheckBox)
        self.verticalLayout_2.addWidget(self.connectionsGroup)
        self.bannedUsersGroup = QtWidgets.QGroupBox(CooperationPage)
        self.bannedUsersGroup.setObjectName("bannedUsersGroup")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.bannedUsersGroup)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.bannedUsersList = QtWidgets.QListWidget(self.bannedUsersGroup)
        self.bannedUsersList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.bannedUsersList.setObjectName("bannedUsersList")
        self.gridLayout_2.addWidget(self.bannedUsersList, 0, 0, 1, 3)
        self.deleteBannedUsersButton = QtWidgets.QPushButton(self.bannedUsersGroup)
        self.deleteBannedUsersButton.setEnabled(False)
        self.deleteBannedUsersButton.setObjectName("deleteBannedUsersButton")
        self.gridLayout_2.addWidget(self.deleteBannedUsersButton, 1, 0, 1, 1)
        self.bannedUserEdit = QtWidgets.QLineEdit(self.bannedUsersGroup)
        self.bannedUserEdit.setObjectName("bannedUserEdit")
        self.gridLayout_2.addWidget(self.bannedUserEdit, 1, 1, 1, 1)
        self.addBannedUserButton = QtWidgets.QPushButton(self.bannedUsersGroup)
        self.addBannedUserButton.setEnabled(False)
        self.addBannedUserButton.setObjectName("addBannedUserButton")
        self.gridLayout_2.addWidget(self.addBannedUserButton, 1, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.bannedUsersGroup)

        self.retranslateUi(CooperationPage)
        self.otherPortsCheckBox.toggled['bool'].connect(self.label_2.setEnabled)
        self.otherPortsCheckBox.toggled['bool'].connect(self.portToTrySpin.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(CooperationPage)
        CooperationPage.setTabOrder(self.autostartCheckBox, self.serverPortSpin)
        CooperationPage.setTabOrder(self.serverPortSpin, self.otherPortsCheckBox)
        CooperationPage.setTabOrder(self.otherPortsCheckBox, self.portToTrySpin)
        CooperationPage.setTabOrder(self.portToTrySpin, self.autoAcceptCheckBox)
        CooperationPage.setTabOrder(self.autoAcceptCheckBox, self.bannedUsersList)
        CooperationPage.setTabOrder(self.bannedUsersList, self.deleteBannedUsersButton)
        CooperationPage.setTabOrder(self.deleteBannedUsersButton, self.bannedUserEdit)
        CooperationPage.setTabOrder(self.bannedUserEdit, self.addBannedUserButton)

    def retranslateUi(self, CooperationPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("CooperationPage", "<b>Configure cooperation settings</b>"))
        self.serverGroup.setTitle(_translate("CooperationPage", "Server"))
        self.autostartCheckBox.setToolTip(_translate("CooperationPage", "Select to start the server automatically"))
        self.autostartCheckBox.setText(_translate("CooperationPage", "Start server automatically"))
        self.label.setText(_translate("CooperationPage", "Server Port:"))
        self.serverPortSpin.setToolTip(_translate("CooperationPage", "Enter the port number to listen on"))
        self.otherPortsCheckBox.setToolTip(_translate("CooperationPage", "Select to incrementally try other ports for the server"))
        self.otherPortsCheckBox.setText(_translate("CooperationPage", "Try other ports for server"))
        self.label_2.setText(_translate("CooperationPage", "No. ports to try:"))
        self.portToTrySpin.setToolTip(_translate("CooperationPage", "Enter the maximum number of additional ports to try"))
        self.connectionsGroup.setTitle(_translate("CooperationPage", "Connections"))
        self.autoAcceptCheckBox.setToolTip(_translate("CooperationPage", "Select to accept incomming connections automatically"))
        self.autoAcceptCheckBox.setText(_translate("CooperationPage", "Accept connections automatically"))
        self.bannedUsersGroup.setTitle(_translate("CooperationPage", "Banned Users"))
        self.bannedUsersList.setSortingEnabled(True)
        self.deleteBannedUsersButton.setToolTip(_translate("CooperationPage", "Delete the selected entries from the list of banned users"))
        self.deleteBannedUsersButton.setText(_translate("CooperationPage", "Delete"))
        self.bannedUserEdit.setToolTip(_translate("CooperationPage", "Enter the user and host of the banned user"))
        self.addBannedUserButton.setToolTip(_translate("CooperationPage", "Add the user to the list of banned users"))
        self.addBannedUserButton.setText(_translate("CooperationPage", "Add"))

