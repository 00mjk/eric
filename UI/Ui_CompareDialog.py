# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/CompareDialog.ui'
#
# Created: Tue Nov 18 17:53:58 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CompareDialog(object):
    def setupUi(self, CompareDialog):
        CompareDialog.setObjectName("CompareDialog")
        CompareDialog.resize(950, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(CompareDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.filesGroup = QtWidgets.QGroupBox(CompareDialog)
        self.filesGroup.setTitle("")
        self.filesGroup.setFlat(True)
        self.filesGroup.setObjectName("filesGroup")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.filesGroup)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textLabel1 = QtWidgets.QLabel(self.filesGroup)
        self.textLabel1.setObjectName("textLabel1")
        self.horizontalLayout_3.addWidget(self.textLabel1)
        self.file1Edit = QtWidgets.QLineEdit(self.filesGroup)
        self.file1Edit.setObjectName("file1Edit")
        self.horizontalLayout_3.addWidget(self.file1Edit)
        self.file1Button = QtWidgets.QToolButton(self.filesGroup)
        self.file1Button.setObjectName("file1Button")
        self.horizontalLayout_3.addWidget(self.file1Button)
        self.textLabel2 = QtWidgets.QLabel(self.filesGroup)
        self.textLabel2.setObjectName("textLabel2")
        self.horizontalLayout_3.addWidget(self.textLabel2)
        self.file2Edit = QtWidgets.QLineEdit(self.filesGroup)
        self.file2Edit.setObjectName("file2Edit")
        self.horizontalLayout_3.addWidget(self.file2Edit)
        self.file2Button = QtWidgets.QToolButton(self.filesGroup)
        self.file2Button.setObjectName("file2Button")
        self.horizontalLayout_3.addWidget(self.file2Button)
        self.verticalLayout.addWidget(self.filesGroup)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.file1Label = QtWidgets.QLabel(CompareDialog)
        self.file1Label.setText("")
        self.file1Label.setWordWrap(True)
        self.file1Label.setObjectName("file1Label")
        self.gridLayout.addWidget(self.file1Label, 0, 0, 1, 1)
        self.file2Label = QtWidgets.QLabel(CompareDialog)
        self.file2Label.setText("")
        self.file2Label.setWordWrap(True)
        self.file2Label.setObjectName("file2Label")
        self.gridLayout.addWidget(self.file2Label, 0, 2, 1, 1)
        self.contents_1 = QtWidgets.QTextEdit(CompareDialog)
        self.contents_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.contents_1.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.contents_1.setReadOnly(True)
        self.contents_1.setTabStopWidth(8)
        self.contents_1.setAcceptRichText(False)
        self.contents_1.setObjectName("contents_1")
        self.gridLayout.addWidget(self.contents_1, 1, 0, 1, 1)
        self.vboxlayout = QtWidgets.QVBoxLayout()
        self.vboxlayout.setObjectName("vboxlayout")
        spacerItem = QtWidgets.QSpacerItem(20, 101, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)
        self.firstButton = QtWidgets.QToolButton(CompareDialog)
        self.firstButton.setEnabled(False)
        self.firstButton.setObjectName("firstButton")
        self.vboxlayout.addWidget(self.firstButton)
        self.upButton = QtWidgets.QToolButton(CompareDialog)
        self.upButton.setEnabled(False)
        self.upButton.setObjectName("upButton")
        self.vboxlayout.addWidget(self.upButton)
        self.downButton = QtWidgets.QToolButton(CompareDialog)
        self.downButton.setEnabled(False)
        self.downButton.setObjectName("downButton")
        self.vboxlayout.addWidget(self.downButton)
        self.lastButton = QtWidgets.QToolButton(CompareDialog)
        self.lastButton.setEnabled(False)
        self.lastButton.setObjectName("lastButton")
        self.vboxlayout.addWidget(self.lastButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 101, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.vboxlayout, 1, 1, 1, 1)
        self.contents_2 = QtWidgets.QTextEdit(CompareDialog)
        self.contents_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.contents_2.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.contents_2.setReadOnly(True)
        self.contents_2.setTabStopWidth(8)
        self.contents_2.setAcceptRichText(False)
        self.contents_2.setObjectName("contents_2")
        self.gridLayout.addWidget(self.contents_2, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.synchronizeCheckBox = QtWidgets.QCheckBox(CompareDialog)
        self.synchronizeCheckBox.setChecked(True)
        self.synchronizeCheckBox.setObjectName("synchronizeCheckBox")
        self.verticalLayout.addWidget(self.synchronizeCheckBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.totalLabel = QtWidgets.QLabel(CompareDialog)
        self.totalLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.totalLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.totalLabel.setObjectName("totalLabel")
        self.horizontalLayout.addWidget(self.totalLabel)
        self.changedLabel = QtWidgets.QLabel(CompareDialog)
        self.changedLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.changedLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.changedLabel.setObjectName("changedLabel")
        self.horizontalLayout.addWidget(self.changedLabel)
        self.addedLabel = QtWidgets.QLabel(CompareDialog)
        self.addedLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.addedLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.addedLabel.setObjectName("addedLabel")
        self.horizontalLayout.addWidget(self.addedLabel)
        self.deletedLabel = QtWidgets.QLabel(CompareDialog)
        self.deletedLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.deletedLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.deletedLabel.setObjectName("deletedLabel")
        self.horizontalLayout.addWidget(self.deletedLabel)
        self.buttonBox = QtWidgets.QDialogButtonBox(CompareDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textLabel1.setBuddy(self.file1Edit)
        self.textLabel2.setBuddy(self.file1Edit)

        self.retranslateUi(CompareDialog)
        self.buttonBox.rejected.connect(CompareDialog.close)
        QtCore.QMetaObject.connectSlotsByName(CompareDialog)
        CompareDialog.setTabOrder(self.file1Edit, self.file1Button)
        CompareDialog.setTabOrder(self.file1Button, self.file2Edit)
        CompareDialog.setTabOrder(self.file2Edit, self.file2Button)
        CompareDialog.setTabOrder(self.file2Button, self.synchronizeCheckBox)
        CompareDialog.setTabOrder(self.synchronizeCheckBox, self.firstButton)
        CompareDialog.setTabOrder(self.firstButton, self.upButton)
        CompareDialog.setTabOrder(self.upButton, self.downButton)
        CompareDialog.setTabOrder(self.downButton, self.lastButton)

    def retranslateUi(self, CompareDialog):
        _translate = QtCore.QCoreApplication.translate
        CompareDialog.setWindowTitle(_translate("CompareDialog", "File Comparison"))
        self.textLabel1.setText(_translate("CompareDialog", "File &1:"))
        self.file1Edit.setToolTip(_translate("CompareDialog", "Enter the name of the first file"))
        self.file1Button.setToolTip(_translate("CompareDialog", "Press to select the file via a file selection dialog"))
        self.textLabel2.setText(_translate("CompareDialog", "File &2:"))
        self.file2Edit.setToolTip(_translate("CompareDialog", "Enter the name of the second file"))
        self.file2Button.setToolTip(_translate("CompareDialog", "Press to select the file via a file selection dialog"))
        self.firstButton.setToolTip(_translate("CompareDialog", "Press to move to the first difference"))
        self.upButton.setToolTip(_translate("CompareDialog", "Press to move to the previous difference"))
        self.downButton.setToolTip(_translate("CompareDialog", "Press to move to the next difference"))
        self.lastButton.setToolTip(_translate("CompareDialog", "Press to move to the last difference"))
        self.synchronizeCheckBox.setToolTip(_translate("CompareDialog", "Select, if the horizontal scrollbars should be synchronized"))
        self.synchronizeCheckBox.setText(_translate("CompareDialog", "&Synchronize horizontal scrollbars"))
        self.synchronizeCheckBox.setShortcut(_translate("CompareDialog", "Alt+S"))

