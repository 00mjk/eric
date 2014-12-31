# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Plugins/VcsPlugins/vcsSubversion/SvnRepoBrowserDialog.ui'
#
# Created: Tue Nov 18 17:53:57 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SvnRepoBrowserDialog(object):
    def setupUi(self, SvnRepoBrowserDialog):
        SvnRepoBrowserDialog.setObjectName("SvnRepoBrowserDialog")
        SvnRepoBrowserDialog.resize(650, 667)
        self.gridlayout = QtWidgets.QGridLayout(SvnRepoBrowserDialog)
        self.gridlayout.setObjectName("gridlayout")
        self.label = QtWidgets.QLabel(SvnRepoBrowserDialog)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.urlCombo = QtWidgets.QComboBox(SvnRepoBrowserDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.urlCombo.sizePolicy().hasHeightForWidth())
        self.urlCombo.setSizePolicy(sizePolicy)
        self.urlCombo.setEditable(True)
        self.urlCombo.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.urlCombo.setObjectName("urlCombo")
        self.gridlayout.addWidget(self.urlCombo, 0, 1, 1, 1)
        self.repoTree = QtWidgets.QTreeWidget(SvnRepoBrowserDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.repoTree.sizePolicy().hasHeightForWidth())
        self.repoTree.setSizePolicy(sizePolicy)
        self.repoTree.setAlternatingRowColors(True)
        self.repoTree.setAllColumnsShowFocus(True)
        self.repoTree.setColumnCount(5)
        self.repoTree.setObjectName("repoTree")
        self.gridlayout.addWidget(self.repoTree, 1, 0, 1, 2)
        self.errorGroup = QtWidgets.QGroupBox(SvnRepoBrowserDialog)
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
        self.gridlayout.addWidget(self.errorGroup, 2, 0, 1, 2)
        self.inputGroup = QtWidgets.QGroupBox(SvnRepoBrowserDialog)
        self.inputGroup.setObjectName("inputGroup")
        self.gridlayout1 = QtWidgets.QGridLayout(self.inputGroup)
        self.gridlayout1.setObjectName("gridlayout1")
        spacerItem = QtWidgets.QSpacerItem(327, 29, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridlayout1.addItem(spacerItem, 1, 1, 1, 1)
        self.sendButton = QtWidgets.QPushButton(self.inputGroup)
        self.sendButton.setObjectName("sendButton")
        self.gridlayout1.addWidget(self.sendButton, 1, 2, 1, 1)
        self.input = QtWidgets.QLineEdit(self.inputGroup)
        self.input.setObjectName("input")
        self.gridlayout1.addWidget(self.input, 0, 0, 1, 3)
        self.passwordCheckBox = QtWidgets.QCheckBox(self.inputGroup)
        self.passwordCheckBox.setObjectName("passwordCheckBox")
        self.gridlayout1.addWidget(self.passwordCheckBox, 1, 0, 1, 1)
        self.gridlayout.addWidget(self.inputGroup, 3, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(SvnRepoBrowserDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout.addWidget(self.buttonBox, 4, 0, 1, 2)

        self.retranslateUi(SvnRepoBrowserDialog)
        self.buttonBox.rejected.connect(SvnRepoBrowserDialog.reject)
        self.buttonBox.accepted.connect(SvnRepoBrowserDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(SvnRepoBrowserDialog)
        SvnRepoBrowserDialog.setTabOrder(self.urlCombo, self.repoTree)
        SvnRepoBrowserDialog.setTabOrder(self.repoTree, self.errors)
        SvnRepoBrowserDialog.setTabOrder(self.errors, self.input)
        SvnRepoBrowserDialog.setTabOrder(self.input, self.passwordCheckBox)
        SvnRepoBrowserDialog.setTabOrder(self.passwordCheckBox, self.sendButton)
        SvnRepoBrowserDialog.setTabOrder(self.sendButton, self.buttonBox)

    def retranslateUi(self, SvnRepoBrowserDialog):
        _translate = QtCore.QCoreApplication.translate
        SvnRepoBrowserDialog.setWindowTitle(_translate("SvnRepoBrowserDialog", "Subversion Repository Browser"))
        self.label.setText(_translate("SvnRepoBrowserDialog", "URL:"))
        self.urlCombo.setToolTip(_translate("SvnRepoBrowserDialog", "Enter the URL of the repository"))
        self.repoTree.setSortingEnabled(True)
        self.repoTree.headerItem().setText(0, _translate("SvnRepoBrowserDialog", "File"))
        self.repoTree.headerItem().setText(1, _translate("SvnRepoBrowserDialog", "Revision"))
        self.repoTree.headerItem().setText(2, _translate("SvnRepoBrowserDialog", "Author"))
        self.repoTree.headerItem().setText(3, _translate("SvnRepoBrowserDialog", "Size"))
        self.repoTree.headerItem().setText(4, _translate("SvnRepoBrowserDialog", "Date"))
        self.errorGroup.setTitle(_translate("SvnRepoBrowserDialog", "Errors"))
        self.errors.setWhatsThis(_translate("SvnRepoBrowserDialog", "<b>Subversion errors</b><p>This shows possible error messages of the svn list and svn info commands.</p>"))
        self.inputGroup.setTitle(_translate("SvnRepoBrowserDialog", "Input"))
        self.sendButton.setToolTip(_translate("SvnRepoBrowserDialog", "Press to send the input to the subversion process"))
        self.sendButton.setText(_translate("SvnRepoBrowserDialog", "&Send"))
        self.sendButton.setShortcut(_translate("SvnRepoBrowserDialog", "Alt+S"))
        self.input.setToolTip(_translate("SvnRepoBrowserDialog", "Enter data to be sent to the subversion process"))
        self.passwordCheckBox.setToolTip(_translate("SvnRepoBrowserDialog", "Select to switch the input field to password mode"))
        self.passwordCheckBox.setText(_translate("SvnRepoBrowserDialog", "&Password Mode"))
        self.passwordCheckBox.setShortcut(_translate("SvnRepoBrowserDialog", "Alt+P"))

