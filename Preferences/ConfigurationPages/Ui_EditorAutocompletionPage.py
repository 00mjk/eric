# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Preferences/ConfigurationPages/EditorAutocompletionPage.ui'
#
# Created: Tue Nov 18 17:53:57 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditorAutocompletionPage(object):
    def setupUi(self, EditorAutocompletionPage):
        EditorAutocompletionPage.setObjectName("EditorAutocompletionPage")
        EditorAutocompletionPage.resize(506, 294)
        self.verticalLayout = QtWidgets.QVBoxLayout(EditorAutocompletionPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerLabel = QtWidgets.QLabel(EditorAutocompletionPage)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout.addWidget(self.headerLabel)
        self.line6 = QtWidgets.QFrame(EditorAutocompletionPage)
        self.line6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line6.setObjectName("line6")
        self.verticalLayout.addWidget(self.line6)
        self.acEnabledCheckBox = QtWidgets.QCheckBox(EditorAutocompletionPage)
        self.acEnabledCheckBox.setObjectName("acEnabledCheckBox")
        self.verticalLayout.addWidget(self.acEnabledCheckBox)
        self.groupBox = QtWidgets.QGroupBox(EditorAutocompletionPage)
        self.groupBox.setEnabled(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.acCaseSensitivityCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.acCaseSensitivityCheckBox.setObjectName("acCaseSensitivityCheckBox")
        self.gridLayout.addWidget(self.acCaseSensitivityCheckBox, 0, 0, 1, 1)
        self.acReplaceWordCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.acReplaceWordCheckBox.setObjectName("acReplaceWordCheckBox")
        self.gridLayout.addWidget(self.acReplaceWordCheckBox, 0, 1, 1, 1)
        self._2 = QtWidgets.QHBoxLayout()
        self._2.setObjectName("_2")
        self.textLabel1_2 = QtWidgets.QLabel(self.groupBox)
        self.textLabel1_2.setObjectName("textLabel1_2")
        self._2.addWidget(self.textLabel1_2)
        self.acThresholdSlider = QtWidgets.QSlider(self.groupBox)
        self.acThresholdSlider.setMaximum(10)
        self.acThresholdSlider.setProperty("value", 2)
        self.acThresholdSlider.setOrientation(QtCore.Qt.Horizontal)
        self.acThresholdSlider.setTickInterval(1)
        self.acThresholdSlider.setObjectName("acThresholdSlider")
        self._2.addWidget(self.acThresholdSlider)
        self.lCDNumber4 = QtWidgets.QLCDNumber(self.groupBox)
        self.lCDNumber4.setDigitCount(2)
        self.lCDNumber4.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lCDNumber4.setProperty("value", 2.0)
        self.lCDNumber4.setObjectName("lCDNumber4")
        self._2.addWidget(self.lCDNumber4)
        self.gridLayout.addLayout(self._2, 1, 0, 1, 2)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(456, 51, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(EditorAutocompletionPage)
        self.acThresholdSlider.valueChanged['int'].connect(self.lCDNumber4.display)
        self.acEnabledCheckBox.toggled['bool'].connect(self.groupBox.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(EditorAutocompletionPage)

    def retranslateUi(self, EditorAutocompletionPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("EditorAutocompletionPage", "<b>Configure Autocompletion</b>"))
        self.acEnabledCheckBox.setToolTip(_translate("EditorAutocompletionPage", "Select this to enable autocompletion"))
        self.acEnabledCheckBox.setWhatsThis(_translate("EditorAutocompletionPage", "<b>Autocompletion Enabled</b><p>Select to enable autocompletion. In order to get autocompletion from alternative autocompletion providers (if installed), these have to be enabled on their respective configuration page. Only one alternative provider might be enabled.</p>"))
        self.acEnabledCheckBox.setText(_translate("EditorAutocompletionPage", "Autocompletion Enabled"))
        self.groupBox.setTitle(_translate("EditorAutocompletionPage", "General"))
        self.acCaseSensitivityCheckBox.setToolTip(_translate("EditorAutocompletionPage", "Select this to have case sensitive auto-completion lists"))
        self.acCaseSensitivityCheckBox.setText(_translate("EditorAutocompletionPage", "Case sensitive"))
        self.acReplaceWordCheckBox.setToolTip(_translate("EditorAutocompletionPage", "Select this, if the word to the right should be replaced by the selected entry"))
        self.acReplaceWordCheckBox.setText(_translate("EditorAutocompletionPage", "Replace word"))
        self.textLabel1_2.setText(_translate("EditorAutocompletionPage", "Threshold:"))
        self.acThresholdSlider.setToolTip(_translate("EditorAutocompletionPage", "Move to set the threshold for display of an autocompletion list"))
        self.lCDNumber4.setToolTip(_translate("EditorAutocompletionPage", "Displays the selected autocompletion threshold"))

