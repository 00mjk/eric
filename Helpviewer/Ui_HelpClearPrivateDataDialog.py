# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Helpviewer/HelpClearPrivateDataDialog.ui'
#
# Created: Tue Nov 18 17:53:58 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HelpClearPrivateDataDialog(object):
    def setupUi(self, HelpClearPrivateDataDialog):
        HelpClearPrivateDataDialog.setObjectName("HelpClearPrivateDataDialog")
        HelpClearPrivateDataDialog.resize(305, 289)
        HelpClearPrivateDataDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(HelpClearPrivateDataDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.historyCheckBox = QtWidgets.QCheckBox(HelpClearPrivateDataDialog)
        self.historyCheckBox.setChecked(True)
        self.historyCheckBox.setObjectName("historyCheckBox")
        self.verticalLayout.addWidget(self.historyCheckBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.historyCombo = QtWidgets.QComboBox(HelpClearPrivateDataDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.historyCombo.sizePolicy().hasHeightForWidth())
        self.historyCombo.setSizePolicy(sizePolicy)
        self.historyCombo.setObjectName("historyCombo")
        self.historyCombo.addItem("")
        self.historyCombo.addItem("")
        self.historyCombo.addItem("")
        self.historyCombo.addItem("")
        self.historyCombo.addItem("")
        self.horizontalLayout.addWidget(self.historyCombo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.searchCheckBox = QtWidgets.QCheckBox(HelpClearPrivateDataDialog)
        self.searchCheckBox.setChecked(True)
        self.searchCheckBox.setObjectName("searchCheckBox")
        self.verticalLayout.addWidget(self.searchCheckBox)
        self.downloadsCheckBox = QtWidgets.QCheckBox(HelpClearPrivateDataDialog)
        self.downloadsCheckBox.setChecked(True)
        self.downloadsCheckBox.setObjectName("downloadsCheckBox")
        self.verticalLayout.addWidget(self.downloadsCheckBox)
        self.cookiesCheckBox = QtWidgets.QCheckBox(HelpClearPrivateDataDialog)
        self.cookiesCheckBox.setChecked(True)
        self.cookiesCheckBox.setObjectName("cookiesCheckBox")
        self.verticalLayout.addWidget(self.cookiesCheckBox)
        self.cacheCheckBox = QtWidgets.QCheckBox(HelpClearPrivateDataDialog)
        self.cacheCheckBox.setChecked(True)
        self.cacheCheckBox.setObjectName("cacheCheckBox")
        self.verticalLayout.addWidget(self.cacheCheckBox)
        self.iconsCheckBox = QtWidgets.QCheckBox(HelpClearPrivateDataDialog)
        self.iconsCheckBox.setChecked(True)
        self.iconsCheckBox.setObjectName("iconsCheckBox")
        self.verticalLayout.addWidget(self.iconsCheckBox)
        self.passwordsCheckBox = QtWidgets.QCheckBox(HelpClearPrivateDataDialog)
        self.passwordsCheckBox.setChecked(False)
        self.passwordsCheckBox.setObjectName("passwordsCheckBox")
        self.verticalLayout.addWidget(self.passwordsCheckBox)
        self.databasesCheckBox = QtWidgets.QCheckBox(HelpClearPrivateDataDialog)
        self.databasesCheckBox.setObjectName("databasesCheckBox")
        self.verticalLayout.addWidget(self.databasesCheckBox)
        self.line = QtWidgets.QFrame(HelpClearPrivateDataDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.flashCookiesCheckBox = QtWidgets.QCheckBox(HelpClearPrivateDataDialog)
        self.flashCookiesCheckBox.setObjectName("flashCookiesCheckBox")
        self.verticalLayout.addWidget(self.flashCookiesCheckBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(HelpClearPrivateDataDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(HelpClearPrivateDataDialog)
        self.buttonBox.accepted.connect(HelpClearPrivateDataDialog.accept)
        self.buttonBox.rejected.connect(HelpClearPrivateDataDialog.reject)
        self.historyCheckBox.toggled['bool'].connect(self.historyCombo.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(HelpClearPrivateDataDialog)
        HelpClearPrivateDataDialog.setTabOrder(self.historyCheckBox, self.historyCombo)
        HelpClearPrivateDataDialog.setTabOrder(self.historyCombo, self.searchCheckBox)
        HelpClearPrivateDataDialog.setTabOrder(self.searchCheckBox, self.downloadsCheckBox)
        HelpClearPrivateDataDialog.setTabOrder(self.downloadsCheckBox, self.cookiesCheckBox)
        HelpClearPrivateDataDialog.setTabOrder(self.cookiesCheckBox, self.cacheCheckBox)
        HelpClearPrivateDataDialog.setTabOrder(self.cacheCheckBox, self.iconsCheckBox)
        HelpClearPrivateDataDialog.setTabOrder(self.iconsCheckBox, self.passwordsCheckBox)
        HelpClearPrivateDataDialog.setTabOrder(self.passwordsCheckBox, self.databasesCheckBox)
        HelpClearPrivateDataDialog.setTabOrder(self.databasesCheckBox, self.flashCookiesCheckBox)
        HelpClearPrivateDataDialog.setTabOrder(self.flashCookiesCheckBox, self.buttonBox)

    def retranslateUi(self, HelpClearPrivateDataDialog):
        _translate = QtCore.QCoreApplication.translate
        HelpClearPrivateDataDialog.setWindowTitle(_translate("HelpClearPrivateDataDialog", "Clear Private Data"))
        self.historyCheckBox.setToolTip(_translate("HelpClearPrivateDataDialog", "Select to clear the browsing history"))
        self.historyCheckBox.setText(_translate("HelpClearPrivateDataDialog", "&Browsing History"))
        self.historyCombo.setToolTip(_translate("HelpClearPrivateDataDialog", "Select the history period to be deleted"))
        self.historyCombo.setItemText(0, _translate("HelpClearPrivateDataDialog", "Last Hour"))
        self.historyCombo.setItemText(1, _translate("HelpClearPrivateDataDialog", "Last Day"))
        self.historyCombo.setItemText(2, _translate("HelpClearPrivateDataDialog", "Last Week"))
        self.historyCombo.setItemText(3, _translate("HelpClearPrivateDataDialog", "Last 4 Weeks"))
        self.historyCombo.setItemText(4, _translate("HelpClearPrivateDataDialog", "Whole Period"))
        self.searchCheckBox.setToolTip(_translate("HelpClearPrivateDataDialog", "Select to clear the search history"))
        self.searchCheckBox.setText(_translate("HelpClearPrivateDataDialog", "&Search History"))
        self.downloadsCheckBox.setToolTip(_translate("HelpClearPrivateDataDialog", "Select to clear the download history"))
        self.downloadsCheckBox.setText(_translate("HelpClearPrivateDataDialog", "Download &History"))
        self.cookiesCheckBox.setToolTip(_translate("HelpClearPrivateDataDialog", "Select to clear the cookies"))
        self.cookiesCheckBox.setText(_translate("HelpClearPrivateDataDialog", "&Cookies"))
        self.cacheCheckBox.setToolTip(_translate("HelpClearPrivateDataDialog", "Select to clear the disk cache"))
        self.cacheCheckBox.setText(_translate("HelpClearPrivateDataDialog", "Cached &Web Pages"))
        self.iconsCheckBox.setToolTip(_translate("HelpClearPrivateDataDialog", "Select to clear the website icons"))
        self.iconsCheckBox.setText(_translate("HelpClearPrivateDataDialog", "Website &Icons"))
        self.passwordsCheckBox.setToolTip(_translate("HelpClearPrivateDataDialog", "Select to clear the saved passwords"))
        self.passwordsCheckBox.setText(_translate("HelpClearPrivateDataDialog", "Saved &Passwords"))
        self.databasesCheckBox.setToolTip(_translate("HelpClearPrivateDataDialog", "Select to delete all web databases"))
        self.databasesCheckBox.setText(_translate("HelpClearPrivateDataDialog", "Web &Databases"))
        self.flashCookiesCheckBox.setToolTip(_translate("HelpClearPrivateDataDialog", "Select to clear cookies set by the Adobe Flash Player"))
        self.flashCookiesCheckBox.setText(_translate("HelpClearPrivateDataDialog", "Cookies from Adobe &Flash Player"))

