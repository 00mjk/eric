# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Plugins/VcsPlugins/vcsSubversion/SvnCommandDialog.ui'
#
# Created: Tue Nov 18 17:53:57 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SvnCommandDialog(object):
    def setupUi(self, SvnCommandDialog):
        SvnCommandDialog.setObjectName("SvnCommandDialog")
        SvnCommandDialog.resize(628, 141)
        self.vboxlayout = QtWidgets.QVBoxLayout(SvnCommandDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")
        self.textLabel1 = QtWidgets.QLabel(SvnCommandDialog)
        self.textLabel1.setToolTip("")
        self.textLabel1.setObjectName("textLabel1")
        self.gridlayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.commandCombo = QtWidgets.QComboBox(SvnCommandDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandCombo.sizePolicy().hasHeightForWidth())
        self.commandCombo.setSizePolicy(sizePolicy)
        self.commandCombo.setEditable(True)
        self.commandCombo.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.commandCombo.setDuplicatesEnabled(False)
        self.commandCombo.setObjectName("commandCombo")
        self.gridlayout.addWidget(self.commandCombo, 0, 1, 1, 2)
        self.workdirCombo = QtWidgets.QComboBox(SvnCommandDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.workdirCombo.sizePolicy().hasHeightForWidth())
        self.workdirCombo.setSizePolicy(sizePolicy)
        self.workdirCombo.setEditable(True)
        self.workdirCombo.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.workdirCombo.setDuplicatesEnabled(False)
        self.workdirCombo.setObjectName("workdirCombo")
        self.gridlayout.addWidget(self.workdirCombo, 1, 1, 1, 1)
        self.textLabel2 = QtWidgets.QLabel(SvnCommandDialog)
        self.textLabel2.setObjectName("textLabel2")
        self.gridlayout.addWidget(self.textLabel2, 1, 0, 1, 1)
        self.textLabel3 = QtWidgets.QLabel(SvnCommandDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textLabel3.sizePolicy().hasHeightForWidth())
        self.textLabel3.setSizePolicy(sizePolicy)
        self.textLabel3.setObjectName("textLabel3")
        self.gridlayout.addWidget(self.textLabel3, 2, 0, 1, 1)
        self.projectDirLabel = QtWidgets.QLabel(SvnCommandDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projectDirLabel.sizePolicy().hasHeightForWidth())
        self.projectDirLabel.setSizePolicy(sizePolicy)
        self.projectDirLabel.setObjectName("projectDirLabel")
        self.gridlayout.addWidget(self.projectDirLabel, 2, 1, 1, 2)
        self.dirButton = QtWidgets.QToolButton(SvnCommandDialog)
        self.dirButton.setObjectName("dirButton")
        self.gridlayout.addWidget(self.dirButton, 1, 2, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(SvnCommandDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(SvnCommandDialog)
        self.buttonBox.accepted.connect(SvnCommandDialog.accept)
        self.buttonBox.rejected.connect(SvnCommandDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SvnCommandDialog)
        SvnCommandDialog.setTabOrder(self.commandCombo, self.workdirCombo)
        SvnCommandDialog.setTabOrder(self.workdirCombo, self.dirButton)
        SvnCommandDialog.setTabOrder(self.dirButton, self.buttonBox)

    def retranslateUi(self, SvnCommandDialog):
        _translate = QtCore.QCoreApplication.translate
        SvnCommandDialog.setWindowTitle(_translate("SvnCommandDialog", "Subversion Command"))
        self.textLabel1.setText(_translate("SvnCommandDialog", "Subversion Command:"))
        self.commandCombo.setToolTip(_translate("SvnCommandDialog", "Enter the Subversion command to be executed with all necessary parameters"))
        self.commandCombo.setWhatsThis(_translate("SvnCommandDialog", "<b>Subversion Command</b>\n"
"<p>Enter the Subversion command to be executed including all necessary \n"
"parameters. If a parameter of the commandline includes a space you have to \n"
"surround this parameter by single or double quotes. Do not include the name \n"
"of the subversion client executable (i.e. svn).</p>"))
        self.workdirCombo.setToolTip(_translate("SvnCommandDialog", "Enter the working directory for the Subversion command"))
        self.workdirCombo.setWhatsThis(_translate("SvnCommandDialog", "<b>Working directory</b>\n"
"<p>Enter the working directory for the Subversion command.\n"
"This is an optional entry. The button to the right will open a \n"
"directory selection dialog.</p>"))
        self.textLabel2.setText(_translate("SvnCommandDialog", "Working Directory:<br>(optional)"))
        self.textLabel3.setText(_translate("SvnCommandDialog", "Project Directory:"))
        self.projectDirLabel.setToolTip(_translate("SvnCommandDialog", "This shows the root directory of the current project."))
        self.projectDirLabel.setText(_translate("SvnCommandDialog", "project directory"))
        self.dirButton.setToolTip(_translate("SvnCommandDialog", "Select the working directory via a directory selection dialog"))
        self.dirButton.setWhatsThis(_translate("SvnCommandDialog", "<b>Working directory</b>\n"
"<p>Select the working directory for the Subversion command via a directory selection dialog.</p>"))

