# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Plugins/DocumentationPlugins/Ericapi/EricapiConfigDialog.ui'
#
# Created: Tue Nov 18 17:53:58 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EricapiConfigDialog(object):
    def setupUi(self, EricapiConfigDialog):
        EricapiConfigDialog.setObjectName("EricapiConfigDialog")
        EricapiConfigDialog.resize(500, 600)
        EricapiConfigDialog.setSizeGripEnabled(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(EricapiConfigDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")
        self.outputFileEdit = QtWidgets.QLineEdit(EricapiConfigDialog)
        self.outputFileEdit.setObjectName("outputFileEdit")
        self.gridlayout.addWidget(self.outputFileEdit, 0, 1, 1, 1)
        self.TextLabel6 = QtWidgets.QLabel(EricapiConfigDialog)
        self.TextLabel6.setObjectName("TextLabel6")
        self.gridlayout.addWidget(self.TextLabel6, 0, 0, 1, 1)
        self.outputFileButton = QtWidgets.QToolButton(EricapiConfigDialog)
        self.outputFileButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.outputFileButton.setObjectName("outputFileButton")
        self.gridlayout.addWidget(self.outputFileButton, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridlayout)
        self.groupBox_2 = QtWidgets.QGroupBox(EricapiConfigDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.languagesList = QtWidgets.QListWidget(self.groupBox_2)
        self.languagesList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.languagesList.setObjectName("languagesList")
        self.verticalLayout.addWidget(self.languagesList)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.textLabel1_3 = QtWidgets.QLabel(EricapiConfigDialog)
        self.textLabel1_3.setObjectName("textLabel1_3")
        self.hboxlayout.addWidget(self.textLabel1_3)
        self.sourceExtEdit = QtWidgets.QLineEdit(EricapiConfigDialog)
        self.sourceExtEdit.setObjectName("sourceExtEdit")
        self.hboxlayout.addWidget(self.sourceExtEdit)
        self.verticalLayout_2.addLayout(self.hboxlayout)
        self.gridlayout1 = QtWidgets.QGridLayout()
        self.gridlayout1.setObjectName("gridlayout1")
        spacerItem = QtWidgets.QSpacerItem(31, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridlayout1.addItem(spacerItem, 0, 1, 1, 1)
        self.recursionCheckBox = QtWidgets.QCheckBox(EricapiConfigDialog)
        self.recursionCheckBox.setObjectName("recursionCheckBox")
        self.gridlayout1.addWidget(self.recursionCheckBox, 0, 0, 1, 1)
        self.includePrivateCheckBox = QtWidgets.QCheckBox(EricapiConfigDialog)
        self.includePrivateCheckBox.setObjectName("includePrivateCheckBox")
        self.gridlayout1.addWidget(self.includePrivateCheckBox, 1, 0, 1, 2)
        self.verticalLayout_2.addLayout(self.gridlayout1)
        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.label = QtWidgets.QLabel(EricapiConfigDialog)
        self.label.setObjectName("label")
        self.hboxlayout1.addWidget(self.label)
        self.baseEdit = QtWidgets.QLineEdit(EricapiConfigDialog)
        self.baseEdit.setObjectName("baseEdit")
        self.hboxlayout1.addWidget(self.baseEdit)
        self.verticalLayout_2.addLayout(self.hboxlayout1)
        self.hboxlayout2 = QtWidgets.QHBoxLayout()
        self.hboxlayout2.setObjectName("hboxlayout2")
        self.label_2 = QtWidgets.QLabel(EricapiConfigDialog)
        self.label_2.setObjectName("label_2")
        self.hboxlayout2.addWidget(self.label_2)
        self.excludeFilesEdit = QtWidgets.QLineEdit(EricapiConfigDialog)
        self.excludeFilesEdit.setObjectName("excludeFilesEdit")
        self.hboxlayout2.addWidget(self.excludeFilesEdit)
        self.verticalLayout_2.addLayout(self.hboxlayout2)
        self.groupBox = QtWidgets.QGroupBox(EricapiConfigDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridlayout2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridlayout2.setObjectName("gridlayout2")
        self.ignoreDirEdit = QtWidgets.QLineEdit(self.groupBox)
        self.ignoreDirEdit.setObjectName("ignoreDirEdit")
        self.gridlayout2.addWidget(self.ignoreDirEdit, 1, 2, 1, 1)
        self.addButton = QtWidgets.QPushButton(self.groupBox)
        self.addButton.setObjectName("addButton")
        self.gridlayout2.addWidget(self.addButton, 1, 1, 1, 1)
        self.deleteButton = QtWidgets.QPushButton(self.groupBox)
        self.deleteButton.setObjectName("deleteButton")
        self.gridlayout2.addWidget(self.deleteButton, 1, 0, 1, 1)
        self.ignoreDirsList = QtWidgets.QListWidget(self.groupBox)
        self.ignoreDirsList.setObjectName("ignoreDirsList")
        self.gridlayout2.addWidget(self.ignoreDirsList, 0, 0, 1, 4)
        self.ignoreDirButton = QtWidgets.QToolButton(self.groupBox)
        self.ignoreDirButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ignoreDirButton.setObjectName("ignoreDirButton")
        self.gridlayout2.addWidget(self.ignoreDirButton, 1, 3, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(EricapiConfigDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(EricapiConfigDialog)
        self.buttonBox.accepted.connect(EricapiConfigDialog.accept)
        self.buttonBox.rejected.connect(EricapiConfigDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EricapiConfigDialog)
        EricapiConfigDialog.setTabOrder(self.outputFileEdit, self.languagesList)
        EricapiConfigDialog.setTabOrder(self.languagesList, self.sourceExtEdit)
        EricapiConfigDialog.setTabOrder(self.sourceExtEdit, self.recursionCheckBox)
        EricapiConfigDialog.setTabOrder(self.recursionCheckBox, self.includePrivateCheckBox)
        EricapiConfigDialog.setTabOrder(self.includePrivateCheckBox, self.baseEdit)
        EricapiConfigDialog.setTabOrder(self.baseEdit, self.excludeFilesEdit)
        EricapiConfigDialog.setTabOrder(self.excludeFilesEdit, self.ignoreDirEdit)
        EricapiConfigDialog.setTabOrder(self.ignoreDirEdit, self.addButton)
        EricapiConfigDialog.setTabOrder(self.addButton, self.ignoreDirsList)
        EricapiConfigDialog.setTabOrder(self.ignoreDirsList, self.deleteButton)
        EricapiConfigDialog.setTabOrder(self.deleteButton, self.buttonBox)

    def retranslateUi(self, EricapiConfigDialog):
        _translate = QtCore.QCoreApplication.translate
        EricapiConfigDialog.setWindowTitle(_translate("EricapiConfigDialog", "Ericapi Configuration"))
        self.outputFileEdit.setToolTip(_translate("EricapiConfigDialog", "Enter an output filename"))
        self.outputFileEdit.setWhatsThis(_translate("EricapiConfigDialog", "<b>Output Filename</b><p>Enter the filename of the output file. A \'%L\' placeholder is replaced by the language of the API file.</p>"))
        self.TextLabel6.setText(_translate("EricapiConfigDialog", "Output File:"))
        self.outputFileButton.setToolTip(_translate("EricapiConfigDialog", "Press to open a file selection dialog"))
        self.groupBox_2.setTitle(_translate("EricapiConfigDialog", "Languages"))
        self.languagesList.setToolTip(_translate("EricapiConfigDialog", "Select the languages of the  APIs to generate"))
        self.textLabel1_3.setText(_translate("EricapiConfigDialog", "Additional source extensions:"))
        self.sourceExtEdit.setToolTip(_translate("EricapiConfigDialog", "Enter additional source extensions separated by a comma"))
        self.recursionCheckBox.setToolTip(_translate("EricapiConfigDialog", "Select to recurse into subdirectories"))
        self.recursionCheckBox.setText(_translate("EricapiConfigDialog", "Recurse into subdirectories"))
        self.includePrivateCheckBox.setToolTip(_translate("EricapiConfigDialog", "Select to include private classes, methods and functions in the API file"))
        self.includePrivateCheckBox.setText(_translate("EricapiConfigDialog", "Include private classes, methods and functions"))
        self.label.setText(_translate("EricapiConfigDialog", "Base package name:"))
        self.baseEdit.setToolTip(_translate("EricapiConfigDialog", "Enter the name of the base package"))
        self.label_2.setText(_translate("EricapiConfigDialog", "Exclude Files:"))
        self.excludeFilesEdit.setToolTip(_translate("EricapiConfigDialog", "Enter filename patterns of files to be excluded separated by a comma"))
        self.groupBox.setTitle(_translate("EricapiConfigDialog", "Exclude Directories"))
        self.ignoreDirEdit.setToolTip(_translate("EricapiConfigDialog", "Enter a directory basename to be ignored"))
        self.addButton.setToolTip(_translate("EricapiConfigDialog", "Press to add the entered directory to the list"))
        self.addButton.setText(_translate("EricapiConfigDialog", "Add"))
        self.deleteButton.setToolTip(_translate("EricapiConfigDialog", "Press to delete the selected directory from the list"))
        self.deleteButton.setText(_translate("EricapiConfigDialog", "Delete"))
        self.ignoreDirsList.setToolTip(_translate("EricapiConfigDialog", "List of directory basenames to be ignored"))
        self.ignoreDirButton.setToolTip(_translate("EricapiConfigDialog", "Press to open a directory selection dialog"))

