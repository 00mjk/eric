# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Plugins/WizardPlugins/QRegularExpressionWizard/QRegularExpressionWizardCharactersDialog.ui'
#
# Created: Tue Nov 18 17:53:58 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QRegularExpressionWizardCharactersDialog(object):
    def setupUi(self, QRegularExpressionWizardCharactersDialog):
        QRegularExpressionWizardCharactersDialog.setObjectName("QRegularExpressionWizardCharactersDialog")
        QRegularExpressionWizardCharactersDialog.resize(850, 500)
        QRegularExpressionWizardCharactersDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(QRegularExpressionWizardCharactersDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.negativeCheckBox = QtWidgets.QCheckBox(QRegularExpressionWizardCharactersDialog)
        self.negativeCheckBox.setObjectName("negativeCheckBox")
        self.verticalLayout.addWidget(self.negativeCheckBox)
        self.groupBox = QtWidgets.QGroupBox(QRegularExpressionWizardCharactersDialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.wordCharCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.wordCharCheckBox.setObjectName("wordCharCheckBox")
        self.gridLayout.addWidget(self.wordCharCheckBox, 0, 0, 1, 1)
        self.digitsCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.digitsCheckBox.setObjectName("digitsCheckBox")
        self.gridLayout.addWidget(self.digitsCheckBox, 0, 1, 1, 1)
        self.newlineCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.newlineCheckBox.setObjectName("newlineCheckBox")
        self.gridLayout.addWidget(self.newlineCheckBox, 0, 2, 1, 1)
        self.nonWordCharCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.nonWordCharCheckBox.setObjectName("nonWordCharCheckBox")
        self.gridLayout.addWidget(self.nonWordCharCheckBox, 1, 0, 1, 1)
        self.nonDigitsCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.nonDigitsCheckBox.setObjectName("nonDigitsCheckBox")
        self.gridLayout.addWidget(self.nonDigitsCheckBox, 1, 1, 1, 1)
        self.nonNewlineCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.nonNewlineCheckBox.setObjectName("nonNewlineCheckBox")
        self.gridLayout.addWidget(self.nonNewlineCheckBox, 1, 2, 1, 1)
        self.whitespaceCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.whitespaceCheckBox.setObjectName("whitespaceCheckBox")
        self.gridLayout.addWidget(self.whitespaceCheckBox, 2, 0, 1, 1)
        self.horizontalWhitespaceCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.horizontalWhitespaceCheckBox.setObjectName("horizontalWhitespaceCheckBox")
        self.gridLayout.addWidget(self.horizontalWhitespaceCheckBox, 2, 1, 1, 1)
        self.verticalWhitespaceCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.verticalWhitespaceCheckBox.setObjectName("verticalWhitespaceCheckBox")
        self.gridLayout.addWidget(self.verticalWhitespaceCheckBox, 2, 2, 1, 1)
        self.nonWhitespaceCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.nonWhitespaceCheckBox.setObjectName("nonWhitespaceCheckBox")
        self.gridLayout.addWidget(self.nonWhitespaceCheckBox, 3, 0, 1, 1)
        self.nonHorizontalWhitespaceCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.nonHorizontalWhitespaceCheckBox.setObjectName("nonHorizontalWhitespaceCheckBox")
        self.gridLayout.addWidget(self.nonHorizontalWhitespaceCheckBox, 3, 1, 1, 1)
        self.nonVerticalWhitespaceCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.nonVerticalWhitespaceCheckBox.setObjectName("nonVerticalWhitespaceCheckBox")
        self.gridLayout.addWidget(self.nonVerticalWhitespaceCheckBox, 3, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.singlesBox = QtWidgets.QGroupBox(QRegularExpressionWizardCharactersDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.singlesBox.sizePolicy().hasHeightForWidth())
        self.singlesBox.setSizePolicy(sizePolicy)
        self.singlesBox.setObjectName("singlesBox")
        self.verticalLayout.addWidget(self.singlesBox)
        self.rangesBox = QtWidgets.QGroupBox(QRegularExpressionWizardCharactersDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rangesBox.sizePolicy().hasHeightForWidth())
        self.rangesBox.setSizePolicy(sizePolicy)
        self.rangesBox.setObjectName("rangesBox")
        self.verticalLayout.addWidget(self.rangesBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(QRegularExpressionWizardCharactersDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(QRegularExpressionWizardCharactersDialog)
        self.buttonBox.accepted.connect(QRegularExpressionWizardCharactersDialog.accept)
        self.buttonBox.rejected.connect(QRegularExpressionWizardCharactersDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(QRegularExpressionWizardCharactersDialog)
        QRegularExpressionWizardCharactersDialog.setTabOrder(self.negativeCheckBox, self.wordCharCheckBox)
        QRegularExpressionWizardCharactersDialog.setTabOrder(self.wordCharCheckBox, self.nonWordCharCheckBox)
        QRegularExpressionWizardCharactersDialog.setTabOrder(self.nonWordCharCheckBox, self.digitsCheckBox)
        QRegularExpressionWizardCharactersDialog.setTabOrder(self.digitsCheckBox, self.nonDigitsCheckBox)
        QRegularExpressionWizardCharactersDialog.setTabOrder(self.nonDigitsCheckBox, self.newlineCheckBox)
        QRegularExpressionWizardCharactersDialog.setTabOrder(self.newlineCheckBox, self.nonNewlineCheckBox)
        QRegularExpressionWizardCharactersDialog.setTabOrder(self.nonNewlineCheckBox, self.whitespaceCheckBox)
        QRegularExpressionWizardCharactersDialog.setTabOrder(self.whitespaceCheckBox, self.nonWhitespaceCheckBox)
        QRegularExpressionWizardCharactersDialog.setTabOrder(self.nonWhitespaceCheckBox, self.horizontalWhitespaceCheckBox)
        QRegularExpressionWizardCharactersDialog.setTabOrder(self.horizontalWhitespaceCheckBox, self.nonHorizontalWhitespaceCheckBox)
        QRegularExpressionWizardCharactersDialog.setTabOrder(self.nonHorizontalWhitespaceCheckBox, self.verticalWhitespaceCheckBox)
        QRegularExpressionWizardCharactersDialog.setTabOrder(self.verticalWhitespaceCheckBox, self.nonVerticalWhitespaceCheckBox)
        QRegularExpressionWizardCharactersDialog.setTabOrder(self.nonVerticalWhitespaceCheckBox, self.buttonBox)

    def retranslateUi(self, QRegularExpressionWizardCharactersDialog):
        _translate = QtCore.QCoreApplication.translate
        QRegularExpressionWizardCharactersDialog.setWindowTitle(_translate("QRegularExpressionWizardCharactersDialog", "Editor for character sets"))
        self.negativeCheckBox.setText(_translate("QRegularExpressionWizardCharactersDialog", "The defined characters should not match"))
        self.groupBox.setTitle(_translate("QRegularExpressionWizardCharactersDialog", "Predefined character ranges"))
        self.wordCharCheckBox.setText(_translate("QRegularExpressionWizardCharactersDialog", "Word character"))
        self.digitsCheckBox.setText(_translate("QRegularExpressionWizardCharactersDialog", "Digit"))
        self.newlineCheckBox.setText(_translate("QRegularExpressionWizardCharactersDialog", "Newline"))
        self.nonWordCharCheckBox.setText(_translate("QRegularExpressionWizardCharactersDialog", "Non-word character"))
        self.nonDigitsCheckBox.setText(_translate("QRegularExpressionWizardCharactersDialog", "Non-digit"))
        self.nonNewlineCheckBox.setText(_translate("QRegularExpressionWizardCharactersDialog", "Non-newline"))
        self.whitespaceCheckBox.setText(_translate("QRegularExpressionWizardCharactersDialog", "Whitespace character"))
        self.horizontalWhitespaceCheckBox.setText(_translate("QRegularExpressionWizardCharactersDialog", "Horizontal whitespace character"))
        self.verticalWhitespaceCheckBox.setText(_translate("QRegularExpressionWizardCharactersDialog", "Vertical whitespace character"))
        self.nonWhitespaceCheckBox.setText(_translate("QRegularExpressionWizardCharactersDialog", "Non-whitespace character"))
        self.nonHorizontalWhitespaceCheckBox.setText(_translate("QRegularExpressionWizardCharactersDialog", "Non-horizontal whitespace character"))
        self.nonVerticalWhitespaceCheckBox.setText(_translate("QRegularExpressionWizardCharactersDialog", "Non-vertical whitespace character"))
        self.singlesBox.setTitle(_translate("QRegularExpressionWizardCharactersDialog", "Single character"))
        self.rangesBox.setTitle(_translate("QRegularExpressionWizardCharactersDialog", "Character ranges"))

