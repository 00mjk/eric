# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Plugins/VcsPlugins/vcsMercurial/HgStatusDialog.ui'
#
# Created: Tue Nov 18 17:53:57 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgStatusDialog(object):
    def setupUi(self, HgStatusDialog):
        HgStatusDialog.setObjectName("HgStatusDialog")
        HgStatusDialog.resize(955, 646)
        self.verticalLayout = QtWidgets.QVBoxLayout(HgStatusDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(HgStatusDialog)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.statusFilterCombo = QtWidgets.QComboBox(HgStatusDialog)
        self.statusFilterCombo.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.statusFilterCombo.setObjectName("statusFilterCombo")
        self.horizontalLayout_2.addWidget(self.statusFilterCombo)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.statusList = QtWidgets.QTreeWidget(HgStatusDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.statusList.sizePolicy().hasHeightForWidth())
        self.statusList.setSizePolicy(sizePolicy)
        self.statusList.setAlternatingRowColors(True)
        self.statusList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.statusList.setRootIsDecorated(False)
        self.statusList.setObjectName("statusList")
        self.verticalLayout.addWidget(self.statusList)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.commitButton = QtWidgets.QPushButton(HgStatusDialog)
        self.commitButton.setObjectName("commitButton")
        self.horizontalLayout.addWidget(self.commitButton)
        self.buttonsLine = QtWidgets.QFrame(HgStatusDialog)
        self.buttonsLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.buttonsLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.buttonsLine.setObjectName("buttonsLine")
        self.horizontalLayout.addWidget(self.buttonsLine)
        self.addButton = QtWidgets.QPushButton(HgStatusDialog)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.diffButton = QtWidgets.QPushButton(HgStatusDialog)
        self.diffButton.setObjectName("diffButton")
        self.horizontalLayout.addWidget(self.diffButton)
        self.sbsDiffButton = QtWidgets.QPushButton(HgStatusDialog)
        self.sbsDiffButton.setObjectName("sbsDiffButton")
        self.horizontalLayout.addWidget(self.sbsDiffButton)
        self.revertButton = QtWidgets.QPushButton(HgStatusDialog)
        self.revertButton.setObjectName("revertButton")
        self.horizontalLayout.addWidget(self.revertButton)
        self.forgetButton = QtWidgets.QPushButton(HgStatusDialog)
        self.forgetButton.setObjectName("forgetButton")
        self.horizontalLayout.addWidget(self.forgetButton)
        self.restoreButton = QtWidgets.QPushButton(HgStatusDialog)
        self.restoreButton.setObjectName("restoreButton")
        self.horizontalLayout.addWidget(self.restoreButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.errorGroup = QtWidgets.QGroupBox(HgStatusDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.errorGroup.sizePolicy().hasHeightForWidth())
        self.errorGroup.setSizePolicy(sizePolicy)
        self.errorGroup.setObjectName("errorGroup")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.errorGroup)
        self.vboxlayout.setObjectName("vboxlayout")
        self.errors = QtWidgets.QTextEdit(self.errorGroup)
        self.errors.setReadOnly(True)
        self.errors.setAcceptRichText(False)
        self.errors.setObjectName("errors")
        self.vboxlayout.addWidget(self.errors)
        self.verticalLayout.addWidget(self.errorGroup)
        self.inputGroup = QtWidgets.QGroupBox(HgStatusDialog)
        self.inputGroup.setObjectName("inputGroup")
        self.gridlayout = QtWidgets.QGridLayout(self.inputGroup)
        self.gridlayout.setObjectName("gridlayout")
        spacerItem2 = QtWidgets.QSpacerItem(327, 29, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem2, 1, 1, 1, 1)
        self.sendButton = QtWidgets.QPushButton(self.inputGroup)
        self.sendButton.setObjectName("sendButton")
        self.gridlayout.addWidget(self.sendButton, 1, 2, 1, 1)
        self.input = QtWidgets.QLineEdit(self.inputGroup)
        self.input.setObjectName("input")
        self.gridlayout.addWidget(self.input, 0, 0, 1, 3)
        self.passwordCheckBox = QtWidgets.QCheckBox(self.inputGroup)
        self.passwordCheckBox.setObjectName("passwordCheckBox")
        self.gridlayout.addWidget(self.passwordCheckBox, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.inputGroup)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgStatusDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.statusFilterCombo)

        self.retranslateUi(HgStatusDialog)
        QtCore.QMetaObject.connectSlotsByName(HgStatusDialog)
        HgStatusDialog.setTabOrder(self.statusFilterCombo, self.statusList)
        HgStatusDialog.setTabOrder(self.statusList, self.commitButton)
        HgStatusDialog.setTabOrder(self.commitButton, self.addButton)
        HgStatusDialog.setTabOrder(self.addButton, self.diffButton)
        HgStatusDialog.setTabOrder(self.diffButton, self.sbsDiffButton)
        HgStatusDialog.setTabOrder(self.sbsDiffButton, self.revertButton)
        HgStatusDialog.setTabOrder(self.revertButton, self.forgetButton)
        HgStatusDialog.setTabOrder(self.forgetButton, self.restoreButton)
        HgStatusDialog.setTabOrder(self.restoreButton, self.errors)
        HgStatusDialog.setTabOrder(self.errors, self.input)
        HgStatusDialog.setTabOrder(self.input, self.passwordCheckBox)
        HgStatusDialog.setTabOrder(self.passwordCheckBox, self.sendButton)
        HgStatusDialog.setTabOrder(self.sendButton, self.buttonBox)

    def retranslateUi(self, HgStatusDialog):
        _translate = QtCore.QCoreApplication.translate
        HgStatusDialog.setWindowTitle(_translate("HgStatusDialog", "Mercurial Status"))
        HgStatusDialog.setWhatsThis(_translate("HgStatusDialog", "<b>Mercurial Status</b>\n"
"<p>This dialog shows the status of the selected file or project.</p>"))
        self.label.setText(_translate("HgStatusDialog", "&Filter on Status:"))
        self.statusFilterCombo.setToolTip(_translate("HgStatusDialog", "Select the status of entries to be shown"))
        self.statusList.setSortingEnabled(True)
        self.statusList.headerItem().setText(0, _translate("HgStatusDialog", "Commit"))
        self.statusList.headerItem().setText(1, _translate("HgStatusDialog", "Status"))
        self.statusList.headerItem().setText(2, _translate("HgStatusDialog", "Path"))
        self.commitButton.setToolTip(_translate("HgStatusDialog", "Commit the selected changes"))
        self.commitButton.setText(_translate("HgStatusDialog", "&Commit"))
        self.addButton.setToolTip(_translate("HgStatusDialog", "Add the selected entries to the repository"))
        self.addButton.setText(_translate("HgStatusDialog", "&Add"))
        self.diffButton.setToolTip(_translate("HgStatusDialog", "Show differences of the selected entries to the repository"))
        self.diffButton.setText(_translate("HgStatusDialog", "&Differences"))
        self.sbsDiffButton.setToolTip(_translate("HgStatusDialog", "Show differences of the selected entry to the repository in a side-by-side manner"))
        self.sbsDiffButton.setText(_translate("HgStatusDialog", "Side-b&y-Side Diff"))
        self.revertButton.setToolTip(_translate("HgStatusDialog", "Revert the selected entries to the last revision in the repository"))
        self.revertButton.setText(_translate("HgStatusDialog", "Re&vert"))
        self.forgetButton.setToolTip(_translate("HgStatusDialog", "Forget about the selected missing entries"))
        self.forgetButton.setText(_translate("HgStatusDialog", "For&get"))
        self.restoreButton.setToolTip(_translate("HgStatusDialog", "Restore the selected missing entries from the repository"))
        self.restoreButton.setText(_translate("HgStatusDialog", "&Restore"))
        self.errorGroup.setTitle(_translate("HgStatusDialog", "Errors"))
        self.inputGroup.setTitle(_translate("HgStatusDialog", "Input"))
        self.sendButton.setToolTip(_translate("HgStatusDialog", "Press to send the input to the hg process"))
        self.sendButton.setText(_translate("HgStatusDialog", "&Send"))
        self.sendButton.setShortcut(_translate("HgStatusDialog", "Alt+S"))
        self.input.setToolTip(_translate("HgStatusDialog", "Enter data to be sent to the hg process"))
        self.passwordCheckBox.setToolTip(_translate("HgStatusDialog", "Select to switch the input field to password mode"))
        self.passwordCheckBox.setText(_translate("HgStatusDialog", "&Password Mode"))
        self.passwordCheckBox.setShortcut(_translate("HgStatusDialog", "Alt+P"))

