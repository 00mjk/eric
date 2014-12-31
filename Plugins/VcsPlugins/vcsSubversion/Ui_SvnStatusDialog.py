# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Plugins/VcsPlugins/vcsSubversion/SvnStatusDialog.ui'
#
# Created: Tue Nov 18 17:53:57 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SvnStatusDialog(object):
    def setupUi(self, SvnStatusDialog):
        SvnStatusDialog.setObjectName("SvnStatusDialog")
        SvnStatusDialog.resize(955, 646)
        self.verticalLayout = QtWidgets.QVBoxLayout(SvnStatusDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(SvnStatusDialog)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.statusFilterCombo = QtWidgets.QComboBox(SvnStatusDialog)
        self.statusFilterCombo.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.statusFilterCombo.setObjectName("statusFilterCombo")
        self.horizontalLayout_2.addWidget(self.statusFilterCombo)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.statusList = QtWidgets.QTreeWidget(SvnStatusDialog)
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
        self.commitButton = QtWidgets.QPushButton(SvnStatusDialog)
        self.commitButton.setObjectName("commitButton")
        self.horizontalLayout.addWidget(self.commitButton)
        self.line = QtWidgets.QFrame(SvnStatusDialog)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.addButton = QtWidgets.QPushButton(SvnStatusDialog)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.diffButton = QtWidgets.QPushButton(SvnStatusDialog)
        self.diffButton.setObjectName("diffButton")
        self.horizontalLayout.addWidget(self.diffButton)
        self.sbsDiffButton = QtWidgets.QPushButton(SvnStatusDialog)
        self.sbsDiffButton.setObjectName("sbsDiffButton")
        self.horizontalLayout.addWidget(self.sbsDiffButton)
        self.revertButton = QtWidgets.QPushButton(SvnStatusDialog)
        self.revertButton.setObjectName("revertButton")
        self.horizontalLayout.addWidget(self.revertButton)
        self.restoreButton = QtWidgets.QPushButton(SvnStatusDialog)
        self.restoreButton.setObjectName("restoreButton")
        self.horizontalLayout.addWidget(self.restoreButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.errorGroup = QtWidgets.QGroupBox(SvnStatusDialog)
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
        self.inputGroup = QtWidgets.QGroupBox(SvnStatusDialog)
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
        self.buttonBox = QtWidgets.QDialogButtonBox(SvnStatusDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.statusFilterCombo)

        self.retranslateUi(SvnStatusDialog)
        QtCore.QMetaObject.connectSlotsByName(SvnStatusDialog)
        SvnStatusDialog.setTabOrder(self.statusFilterCombo, self.statusList)
        SvnStatusDialog.setTabOrder(self.statusList, self.commitButton)
        SvnStatusDialog.setTabOrder(self.commitButton, self.addButton)
        SvnStatusDialog.setTabOrder(self.addButton, self.diffButton)
        SvnStatusDialog.setTabOrder(self.diffButton, self.sbsDiffButton)
        SvnStatusDialog.setTabOrder(self.sbsDiffButton, self.revertButton)
        SvnStatusDialog.setTabOrder(self.revertButton, self.restoreButton)
        SvnStatusDialog.setTabOrder(self.restoreButton, self.errors)
        SvnStatusDialog.setTabOrder(self.errors, self.input)
        SvnStatusDialog.setTabOrder(self.input, self.passwordCheckBox)
        SvnStatusDialog.setTabOrder(self.passwordCheckBox, self.sendButton)
        SvnStatusDialog.setTabOrder(self.sendButton, self.buttonBox)

    def retranslateUi(self, SvnStatusDialog):
        _translate = QtCore.QCoreApplication.translate
        SvnStatusDialog.setWindowTitle(_translate("SvnStatusDialog", "Subversion Status"))
        SvnStatusDialog.setWhatsThis(_translate("SvnStatusDialog", "<b>Subversion Status</b>\n"
"<p>This dialog shows the status of the selected file or project.</p>"))
        self.label.setText(_translate("SvnStatusDialog", "&Filter on Status:"))
        self.statusFilterCombo.setToolTip(_translate("SvnStatusDialog", "Select the status of entries to be shown"))
        self.statusList.setSortingEnabled(True)
        self.statusList.headerItem().setText(0, _translate("SvnStatusDialog", "Commit"))
        self.statusList.headerItem().setText(1, _translate("SvnStatusDialog", "Changelist"))
        self.statusList.headerItem().setText(2, _translate("SvnStatusDialog", "Status"))
        self.statusList.headerItem().setText(3, _translate("SvnStatusDialog", "Prop. Status"))
        self.statusList.headerItem().setText(4, _translate("SvnStatusDialog", "Locked"))
        self.statusList.headerItem().setText(5, _translate("SvnStatusDialog", "History"))
        self.statusList.headerItem().setText(6, _translate("SvnStatusDialog", "Switched"))
        self.statusList.headerItem().setText(7, _translate("SvnStatusDialog", "Lock Info"))
        self.statusList.headerItem().setText(8, _translate("SvnStatusDialog", "Up to date"))
        self.statusList.headerItem().setText(9, _translate("SvnStatusDialog", "Revision"))
        self.statusList.headerItem().setText(10, _translate("SvnStatusDialog", "Last Change"))
        self.statusList.headerItem().setText(11, _translate("SvnStatusDialog", "Author"))
        self.statusList.headerItem().setText(12, _translate("SvnStatusDialog", "Path"))
        self.commitButton.setToolTip(_translate("SvnStatusDialog", "Commit the selected changes"))
        self.commitButton.setText(_translate("SvnStatusDialog", "&Commit"))
        self.addButton.setToolTip(_translate("SvnStatusDialog", "Add the selected entries to the repository"))
        self.addButton.setText(_translate("SvnStatusDialog", "&Add"))
        self.diffButton.setToolTip(_translate("SvnStatusDialog", "Show differences of the selected entries to the repository"))
        self.diffButton.setText(_translate("SvnStatusDialog", "&Differences"))
        self.sbsDiffButton.setToolTip(_translate("SvnStatusDialog", "Show differences of the selected entry to the repository in a side-by-side manner"))
        self.sbsDiffButton.setText(_translate("SvnStatusDialog", "Side-b&y-Side Diff"))
        self.revertButton.setToolTip(_translate("SvnStatusDialog", "Revert the selected entries to the last revision in the repository"))
        self.revertButton.setText(_translate("SvnStatusDialog", "Re&vert"))
        self.restoreButton.setToolTip(_translate("SvnStatusDialog", "Restore the selected missing entries from the repository"))
        self.restoreButton.setText(_translate("SvnStatusDialog", "&Restore"))
        self.errorGroup.setTitle(_translate("SvnStatusDialog", "Errors"))
        self.inputGroup.setTitle(_translate("SvnStatusDialog", "Input"))
        self.sendButton.setToolTip(_translate("SvnStatusDialog", "Press to send the input to the subversion process"))
        self.sendButton.setText(_translate("SvnStatusDialog", "&Send"))
        self.sendButton.setShortcut(_translate("SvnStatusDialog", "Alt+S"))
        self.input.setToolTip(_translate("SvnStatusDialog", "Enter data to be sent to the subversion process"))
        self.passwordCheckBox.setToolTip(_translate("SvnStatusDialog", "Select to switch the input field to password mode"))
        self.passwordCheckBox.setText(_translate("SvnStatusDialog", "&Password Mode"))
        self.passwordCheckBox.setShortcut(_translate("SvnStatusDialog", "Alt+P"))

