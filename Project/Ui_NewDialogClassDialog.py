# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Project/NewDialogClassDialog.ui'
#
# Created: Tue Nov 18 17:53:58 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewDialogClassDialog(object):
    def setupUi(self, NewDialogClassDialog):
        NewDialogClassDialog.setObjectName("NewDialogClassDialog")
        NewDialogClassDialog.resize(600, 140)
        NewDialogClassDialog.setSizeGripEnabled(True)
        self._2 = QtWidgets.QVBoxLayout(NewDialogClassDialog)
        self._2.setObjectName("_2")
        self._3 = QtWidgets.QGridLayout()
        self._3.setObjectName("_3")
        self.pathnameEdit = QtWidgets.QLineEdit(NewDialogClassDialog)
        self.pathnameEdit.setObjectName("pathnameEdit")
        self._3.addWidget(self.pathnameEdit, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(NewDialogClassDialog)
        self.label.setObjectName("label")
        self._3.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(NewDialogClassDialog)
        self.label_2.setObjectName("label_2")
        self._3.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(NewDialogClassDialog)
        self.label_3.setObjectName("label_3")
        self._3.addWidget(self.label_3, 2, 0, 1, 1)
        self.classnameEdit = QtWidgets.QLineEdit(NewDialogClassDialog)
        self.classnameEdit.setObjectName("classnameEdit")
        self._3.addWidget(self.classnameEdit, 0, 1, 1, 2)
        self.filenameEdit = QtWidgets.QLineEdit(NewDialogClassDialog)
        self.filenameEdit.setObjectName("filenameEdit")
        self._3.addWidget(self.filenameEdit, 1, 1, 1, 2)
        self.pathButton = QtWidgets.QToolButton(NewDialogClassDialog)
        self.pathButton.setObjectName("pathButton")
        self._3.addWidget(self.pathButton, 2, 2, 1, 1)
        self._2.addLayout(self._3)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewDialogClassDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self._2.addWidget(self.buttonBox)
        self.label.setBuddy(self.classnameEdit)
        self.label_2.setBuddy(self.filenameEdit)
        self.label_3.setBuddy(self.pathnameEdit)

        self.retranslateUi(NewDialogClassDialog)
        self.buttonBox.accepted.connect(NewDialogClassDialog.accept)
        self.buttonBox.rejected.connect(NewDialogClassDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NewDialogClassDialog)
        NewDialogClassDialog.setTabOrder(self.classnameEdit, self.filenameEdit)
        NewDialogClassDialog.setTabOrder(self.filenameEdit, self.pathnameEdit)
        NewDialogClassDialog.setTabOrder(self.pathnameEdit, self.pathButton)
        NewDialogClassDialog.setTabOrder(self.pathButton, self.buttonBox)

    def retranslateUi(self, NewDialogClassDialog):
        _translate = QtCore.QCoreApplication.translate
        NewDialogClassDialog.setWindowTitle(_translate("NewDialogClassDialog", "New Dialog Class"))
        self.pathnameEdit.setToolTip(_translate("NewDialogClassDialog", "Enter the path of the file for the forms code"))
        self.label.setText(_translate("NewDialogClassDialog", "&Classname:"))
        self.label_2.setText(_translate("NewDialogClassDialog", "&Filename:"))
        self.label_3.setText(_translate("NewDialogClassDialog", "&Path:"))
        self.classnameEdit.setToolTip(_translate("NewDialogClassDialog", "Enter the name of the new class"))
        self.filenameEdit.setToolTip(_translate("NewDialogClassDialog", "Enter the name of the file for the forms code"))
        self.pathButton.setToolTip(_translate("NewDialogClassDialog", "Select the source file path via a directory selection dialog"))

