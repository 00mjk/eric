# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './MultiProject/AddProjectDialog.ui'
#
# Created: Tue Nov 18 17:53:58 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddProjectDialog(object):
    def setupUi(self, AddProjectDialog):
        AddProjectDialog.setObjectName("AddProjectDialog")
        AddProjectDialog.resize(569, 378)
        AddProjectDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(AddProjectDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(AddProjectDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(AddProjectDialog)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(AddProjectDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.filenameEdit = QtWidgets.QLineEdit(AddProjectDialog)
        self.filenameEdit.setObjectName("filenameEdit")
        self.gridLayout.addWidget(self.filenameEdit, 1, 1, 1, 1)
        self.fileButton = QtWidgets.QToolButton(AddProjectDialog)
        self.fileButton.setObjectName("fileButton")
        self.gridLayout.addWidget(self.fileButton, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(AddProjectDialog)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.descriptionEdit = QtWidgets.QTextEdit(AddProjectDialog)
        self.descriptionEdit.setTabChangesFocus(True)
        self.descriptionEdit.setAcceptRichText(False)
        self.descriptionEdit.setObjectName("descriptionEdit")
        self.gridLayout.addWidget(self.descriptionEdit, 2, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(AddProjectDialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.categoryComboBox = QtWidgets.QComboBox(AddProjectDialog)
        self.categoryComboBox.setEditable(True)
        self.categoryComboBox.setObjectName("categoryComboBox")
        self.gridLayout.addWidget(self.categoryComboBox, 3, 1, 1, 2)
        self.masterCheckBox = QtWidgets.QCheckBox(AddProjectDialog)
        self.masterCheckBox.setObjectName("masterCheckBox")
        self.gridLayout.addWidget(self.masterCheckBox, 4, 0, 1, 3)
        self.buttonBox = QtWidgets.QDialogButtonBox(AddProjectDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 3)
        self.label.setBuddy(self.nameEdit)
        self.label_2.setBuddy(self.filenameEdit)
        self.label_3.setBuddy(self.descriptionEdit)
        self.label_4.setBuddy(self.categoryComboBox)

        self.retranslateUi(AddProjectDialog)
        self.buttonBox.accepted.connect(AddProjectDialog.accept)
        self.buttonBox.rejected.connect(AddProjectDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddProjectDialog)
        AddProjectDialog.setTabOrder(self.nameEdit, self.filenameEdit)
        AddProjectDialog.setTabOrder(self.filenameEdit, self.fileButton)
        AddProjectDialog.setTabOrder(self.fileButton, self.descriptionEdit)
        AddProjectDialog.setTabOrder(self.descriptionEdit, self.categoryComboBox)
        AddProjectDialog.setTabOrder(self.categoryComboBox, self.masterCheckBox)
        AddProjectDialog.setTabOrder(self.masterCheckBox, self.buttonBox)

    def retranslateUi(self, AddProjectDialog):
        _translate = QtCore.QCoreApplication.translate
        AddProjectDialog.setWindowTitle(_translate("AddProjectDialog", "Add Project"))
        self.label.setText(_translate("AddProjectDialog", "&Name:"))
        self.nameEdit.setToolTip(_translate("AddProjectDialog", "Enter the name of the project"))
        self.label_2.setText(_translate("AddProjectDialog", "Project&file:"))
        self.filenameEdit.setToolTip(_translate("AddProjectDialog", "Enter the name of the project file"))
        self.fileButton.setToolTip(_translate("AddProjectDialog", "Select the project file via a file selection dialog"))
        self.label_3.setText(_translate("AddProjectDialog", "&Description:"))
        self.descriptionEdit.setToolTip(_translate("AddProjectDialog", "Enter a short description for the project"))
        self.label_4.setText(_translate("AddProjectDialog", "&Category:"))
        self.categoryComboBox.setToolTip(_translate("AddProjectDialog", "Select a project category"))
        self.masterCheckBox.setToolTip(_translate("AddProjectDialog", "Select to make this project the main project"))
        self.masterCheckBox.setText(_translate("AddProjectDialog", "Is &main project"))

