# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Project/SpellingPropertiesDialog.ui'
#
# Created: Tue Nov 18 17:53:58 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SpellingPropertiesDialog(object):
    def setupUi(self, SpellingPropertiesDialog):
        SpellingPropertiesDialog.setObjectName("SpellingPropertiesDialog")
        SpellingPropertiesDialog.resize(600, 213)
        SpellingPropertiesDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(SpellingPropertiesDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.textLabel1_3 = QtWidgets.QLabel(SpellingPropertiesDialog)
        self.textLabel1_3.setObjectName("textLabel1_3")
        self.gridLayout.addWidget(self.textLabel1_3, 0, 0, 1, 1)
        self.spellingComboBox = QtWidgets.QComboBox(SpellingPropertiesDialog)
        self.spellingComboBox.setObjectName("spellingComboBox")
        self.gridLayout.addWidget(self.spellingComboBox, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(SpellingPropertiesDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.pwlEdit = QtWidgets.QLineEdit(SpellingPropertiesDialog)
        self.pwlEdit.setObjectName("pwlEdit")
        self.gridLayout.addWidget(self.pwlEdit, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(SpellingPropertiesDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.pelEdit = QtWidgets.QLineEdit(SpellingPropertiesDialog)
        self.pelEdit.setObjectName("pelEdit")
        self.gridLayout.addWidget(self.pelEdit, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(SpellingPropertiesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 7, 0, 1, 2)
        self.pwlButton = QtWidgets.QToolButton(SpellingPropertiesDialog)
        self.pwlButton.setObjectName("pwlButton")
        self.gridLayout.addWidget(self.pwlButton, 3, 1, 1, 1)
        self.pelButton = QtWidgets.QToolButton(SpellingPropertiesDialog)
        self.pelButton.setObjectName("pelButton")
        self.gridLayout.addWidget(self.pelButton, 5, 1, 1, 1)
        self.textLabel1_3.setBuddy(self.spellingComboBox)
        self.label.setBuddy(self.pwlEdit)
        self.label_2.setBuddy(self.pelEdit)

        self.retranslateUi(SpellingPropertiesDialog)
        self.buttonBox.accepted.connect(SpellingPropertiesDialog.accept)
        self.buttonBox.rejected.connect(SpellingPropertiesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SpellingPropertiesDialog)
        SpellingPropertiesDialog.setTabOrder(self.spellingComboBox, self.pwlEdit)
        SpellingPropertiesDialog.setTabOrder(self.pwlEdit, self.pwlButton)
        SpellingPropertiesDialog.setTabOrder(self.pwlButton, self.pelEdit)
        SpellingPropertiesDialog.setTabOrder(self.pelEdit, self.pelButton)
        SpellingPropertiesDialog.setTabOrder(self.pelButton, self.buttonBox)

    def retranslateUi(self, SpellingPropertiesDialog):
        _translate = QtCore.QCoreApplication.translate
        SpellingPropertiesDialog.setWindowTitle(_translate("SpellingPropertiesDialog", "Spelling Properties"))
        self.textLabel1_3.setText(_translate("SpellingPropertiesDialog", "Project &Language:"))
        self.spellingComboBox.setToolTip(_translate("SpellingPropertiesDialog", "Select the project\'s language"))
        self.label.setText(_translate("SpellingPropertiesDialog", "Project &Word List:"))
        self.pwlEdit.setToolTip(_translate("SpellingPropertiesDialog", "Enter the filename of the project word list"))
        self.label_2.setText(_translate("SpellingPropertiesDialog", "Project E&xclude List:"))
        self.pelEdit.setToolTip(_translate("SpellingPropertiesDialog", "Enter the filename of the project exclude list"))
        self.pwlButton.setToolTip(_translate("SpellingPropertiesDialog", "Select the project word list file via a file selection dialog"))
        self.pelButton.setToolTip(_translate("SpellingPropertiesDialog", "Select the project exclude list file via a file selection dialog"))

