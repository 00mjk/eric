# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Plugins/VcsPlugins/vcsSubversion/SvnPropSetDialog.ui'
#
# Created: Tue Nov 18 17:53:57 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SvnPropSetDialog(object):
    def setupUi(self, SvnPropSetDialog):
        SvnPropSetDialog.setObjectName("SvnPropSetDialog")
        SvnPropSetDialog.resize(494, 385)
        SvnPropSetDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtWidgets.QVBoxLayout(SvnPropSetDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.textLabel1 = QtWidgets.QLabel(SvnPropSetDialog)
        self.textLabel1.setObjectName("textLabel1")
        self.hboxlayout.addWidget(self.textLabel1)
        self.propNameEdit = QtWidgets.QLineEdit(SvnPropSetDialog)
        self.propNameEdit.setObjectName("propNameEdit")
        self.hboxlayout.addWidget(self.propNameEdit)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.groupBox = QtWidgets.QGroupBox(SvnPropSetDialog)
        self.groupBox.setObjectName("groupBox")
        self.gridlayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridlayout.setObjectName("gridlayout")
        self.fileRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.fileRadioButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fileRadioButton.setObjectName("fileRadioButton")
        self.gridlayout.addWidget(self.fileRadioButton, 2, 0, 1, 2)
        self.textRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.textRadioButton.setChecked(True)
        self.textRadioButton.setObjectName("textRadioButton")
        self.gridlayout.addWidget(self.textRadioButton, 0, 0, 1, 2)
        self.propTextEdit = QtWidgets.QTextEdit(self.groupBox)
        self.propTextEdit.setTabChangesFocus(True)
        self.propTextEdit.setAcceptRichText(False)
        self.propTextEdit.setObjectName("propTextEdit")
        self.gridlayout.addWidget(self.propTextEdit, 1, 0, 1, 2)
        self.propFileEdit = QtWidgets.QLineEdit(self.groupBox)
        self.propFileEdit.setEnabled(False)
        self.propFileEdit.setObjectName("propFileEdit")
        self.gridlayout.addWidget(self.propFileEdit, 3, 0, 1, 1)
        self.fileButton = QtWidgets.QToolButton(self.groupBox)
        self.fileButton.setEnabled(False)
        self.fileButton.setObjectName("fileButton")
        self.gridlayout.addWidget(self.fileButton, 3, 1, 1, 1)
        self.vboxlayout.addWidget(self.groupBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(SvnPropSetDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(SvnPropSetDialog)
        self.textRadioButton.toggled['bool'].connect(self.propTextEdit.setEnabled)
        self.fileRadioButton.toggled['bool'].connect(self.propFileEdit.setEnabled)
        self.buttonBox.accepted.connect(SvnPropSetDialog.accept)
        self.buttonBox.rejected.connect(SvnPropSetDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SvnPropSetDialog)
        SvnPropSetDialog.setTabOrder(self.propNameEdit, self.textRadioButton)
        SvnPropSetDialog.setTabOrder(self.textRadioButton, self.propTextEdit)
        SvnPropSetDialog.setTabOrder(self.propTextEdit, self.propFileEdit)
        SvnPropSetDialog.setTabOrder(self.propFileEdit, self.fileButton)

    def retranslateUi(self, SvnPropSetDialog):
        _translate = QtCore.QCoreApplication.translate
        SvnPropSetDialog.setWindowTitle(_translate("SvnPropSetDialog", "Set Subversion Property"))
        self.textLabel1.setText(_translate("SvnPropSetDialog", "Property Name:"))
        self.propNameEdit.setToolTip(_translate("SvnPropSetDialog", "Enter the name of the property to be set"))
        self.groupBox.setTitle(_translate("SvnPropSetDialog", "Select property source"))
        self.fileRadioButton.setText(_translate("SvnPropSetDialog", "File"))
        self.textRadioButton.setText(_translate("SvnPropSetDialog", "Text"))
        self.propTextEdit.setToolTip(_translate("SvnPropSetDialog", "Enter text of the property"))
        self.propFileEdit.setToolTip(_translate("SvnPropSetDialog", "Enter the name of a file for the property"))
        self.fileButton.setToolTip(_translate("SvnPropSetDialog", "Press to select the file via a file selection dialog"))

