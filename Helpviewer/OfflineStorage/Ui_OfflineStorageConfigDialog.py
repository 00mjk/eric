# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Helpviewer/OfflineStorage/OfflineStorageConfigDialog.ui'
#
# Created: Tue Nov 18 17:53:58 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OfflineStorageConfigDialog(object):
    def setupUi(self, OfflineStorageConfigDialog):
        OfflineStorageConfigDialog.setObjectName("OfflineStorageConfigDialog")
        OfflineStorageConfigDialog.resize(487, 338)
        OfflineStorageConfigDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(OfflineStorageConfigDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerLabel = QtWidgets.QLabel(OfflineStorageConfigDialog)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout.addWidget(self.headerLabel)
        self.line17 = QtWidgets.QFrame(OfflineStorageConfigDialog)
        self.line17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line17.setObjectName("line17")
        self.verticalLayout.addWidget(self.line17)
        self.databaseGroup = QtWidgets.QGroupBox(OfflineStorageConfigDialog)
        self.databaseGroup.setObjectName("databaseGroup")
        self.gridLayout = QtWidgets.QGridLayout(self.databaseGroup)
        self.gridLayout.setObjectName("gridLayout")
        self.databaseEnabledCheckBox = QtWidgets.QCheckBox(self.databaseGroup)
        self.databaseEnabledCheckBox.setObjectName("databaseEnabledCheckBox")
        self.gridLayout.addWidget(self.databaseEnabledCheckBox, 0, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.databaseGroup)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.databaseQuotaSpinBox = QtWidgets.QSpinBox(self.databaseGroup)
        self.databaseQuotaSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.databaseQuotaSpinBox.setMinimum(10)
        self.databaseQuotaSpinBox.setMaximum(999)
        self.databaseQuotaSpinBox.setObjectName("databaseQuotaSpinBox")
        self.gridLayout.addWidget(self.databaseQuotaSpinBox, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(306, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.showDatabasesButton = QtWidgets.QPushButton(self.databaseGroup)
        self.showDatabasesButton.setObjectName("showDatabasesButton")
        self.gridLayout.addWidget(self.showDatabasesButton, 1, 3, 1, 1)
        self.verticalLayout.addWidget(self.databaseGroup)
        self.applicationCacheGroup = QtWidgets.QGroupBox(OfflineStorageConfigDialog)
        self.applicationCacheGroup.setObjectName("applicationCacheGroup")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.applicationCacheGroup)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.applicationCacheEnabledCheckBox = QtWidgets.QCheckBox(self.applicationCacheGroup)
        self.applicationCacheEnabledCheckBox.setObjectName("applicationCacheEnabledCheckBox")
        self.gridLayout_2.addWidget(self.applicationCacheEnabledCheckBox, 0, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.applicationCacheGroup)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.applicationCacheQuotaSpinBox = QtWidgets.QSpinBox(self.applicationCacheGroup)
        self.applicationCacheQuotaSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.applicationCacheQuotaSpinBox.setMinimum(10)
        self.applicationCacheQuotaSpinBox.setMaximum(999)
        self.applicationCacheQuotaSpinBox.setObjectName("applicationCacheQuotaSpinBox")
        self.gridLayout_2.addWidget(self.applicationCacheQuotaSpinBox, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(288, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.applicationCacheGroup)
        self.localStorageGroup = QtWidgets.QGroupBox(OfflineStorageConfigDialog)
        self.localStorageGroup.setObjectName("localStorageGroup")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.localStorageGroup)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.localStorageEnabledCheckBox = QtWidgets.QCheckBox(self.localStorageGroup)
        self.localStorageEnabledCheckBox.setObjectName("localStorageEnabledCheckBox")
        self.gridLayout_3.addWidget(self.localStorageEnabledCheckBox, 0, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.localStorageGroup)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.localRemoteUrlsCheckBox = QtWidgets.QCheckBox(self.localStorageGroup)
        self.localRemoteUrlsCheckBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.localRemoteUrlsCheckBox.sizePolicy().hasHeightForWidth())
        self.localRemoteUrlsCheckBox.setSizePolicy(sizePolicy)
        self.localRemoteUrlsCheckBox.setObjectName("localRemoteUrlsCheckBox")
        self.gridLayout_3.addWidget(self.localRemoteUrlsCheckBox, 1, 1, 1, 1)
        self.localFileUrlsCheckBox = QtWidgets.QCheckBox(self.localStorageGroup)
        self.localFileUrlsCheckBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.localFileUrlsCheckBox.sizePolicy().hasHeightForWidth())
        self.localFileUrlsCheckBox.setSizePolicy(sizePolicy)
        self.localFileUrlsCheckBox.setObjectName("localFileUrlsCheckBox")
        self.gridLayout_3.addWidget(self.localFileUrlsCheckBox, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.localStorageGroup)
        self.buttonBox = QtWidgets.QDialogButtonBox(OfflineStorageConfigDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(OfflineStorageConfigDialog)
        self.buttonBox.accepted.connect(OfflineStorageConfigDialog.accept)
        self.buttonBox.rejected.connect(OfflineStorageConfigDialog.reject)
        self.localStorageEnabledCheckBox.toggled['bool'].connect(self.localRemoteUrlsCheckBox.setEnabled)
        self.localStorageEnabledCheckBox.toggled['bool'].connect(self.localFileUrlsCheckBox.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(OfflineStorageConfigDialog)
        OfflineStorageConfigDialog.setTabOrder(self.databaseEnabledCheckBox, self.databaseQuotaSpinBox)
        OfflineStorageConfigDialog.setTabOrder(self.databaseQuotaSpinBox, self.showDatabasesButton)
        OfflineStorageConfigDialog.setTabOrder(self.showDatabasesButton, self.applicationCacheEnabledCheckBox)
        OfflineStorageConfigDialog.setTabOrder(self.applicationCacheEnabledCheckBox, self.applicationCacheQuotaSpinBox)
        OfflineStorageConfigDialog.setTabOrder(self.applicationCacheQuotaSpinBox, self.localStorageEnabledCheckBox)
        OfflineStorageConfigDialog.setTabOrder(self.localStorageEnabledCheckBox, self.localRemoteUrlsCheckBox)
        OfflineStorageConfigDialog.setTabOrder(self.localRemoteUrlsCheckBox, self.localFileUrlsCheckBox)
        OfflineStorageConfigDialog.setTabOrder(self.localFileUrlsCheckBox, self.buttonBox)

    def retranslateUi(self, OfflineStorageConfigDialog):
        _translate = QtCore.QCoreApplication.translate
        OfflineStorageConfigDialog.setWindowTitle(_translate("OfflineStorageConfigDialog", "Offline Storage Settings"))
        self.headerLabel.setText(_translate("OfflineStorageConfigDialog", "<b>Configure offline storage</b>"))
        self.databaseGroup.setTitle(_translate("OfflineStorageConfigDialog", "Web SQL Databases"))
        self.databaseEnabledCheckBox.setToolTip(_translate("OfflineStorageConfigDialog", "Select to enable Web SQL Databases"))
        self.databaseEnabledCheckBox.setText(_translate("OfflineStorageConfigDialog", "Enable Web SQL Databases"))
        self.label.setText(_translate("OfflineStorageConfigDialog", "Default Quota:"))
        self.databaseQuotaSpinBox.setToolTip(_translate("OfflineStorageConfigDialog", "Enter the default quota for Web SQL Databases"))
        self.databaseQuotaSpinBox.setSuffix(_translate("OfflineStorageConfigDialog", " MB"))
        self.showDatabasesButton.setToolTip(_translate("OfflineStorageConfigDialog", "Press to show the Web SQL Databases"))
        self.showDatabasesButton.setText(_translate("OfflineStorageConfigDialog", "Show databases..."))
        self.applicationCacheGroup.setTitle(_translate("OfflineStorageConfigDialog", "Offline Web Application Cache"))
        self.applicationCacheEnabledCheckBox.setToolTip(_translate("OfflineStorageConfigDialog", "Select to enable Offline Web Application Caches"))
        self.applicationCacheEnabledCheckBox.setText(_translate("OfflineStorageConfigDialog", "Enable Offline Web Application Caches"))
        self.label_2.setText(_translate("OfflineStorageConfigDialog", "Default Quota:"))
        self.applicationCacheQuotaSpinBox.setToolTip(_translate("OfflineStorageConfigDialog", "Enter the default quota for Offline Web Application Caches"))
        self.applicationCacheQuotaSpinBox.setSuffix(_translate("OfflineStorageConfigDialog", " MB"))
        self.localStorageGroup.setTitle(_translate("OfflineStorageConfigDialog", "Local Web Storage"))
        self.localStorageEnabledCheckBox.setToolTip(_translate("OfflineStorageConfigDialog", "Select to enable Local Web Storage"))
        self.localStorageEnabledCheckBox.setText(_translate("OfflineStorageConfigDialog", "Enable Local Web Storage"))
        self.localRemoteUrlsCheckBox.setToolTip(_translate("OfflineStorageConfigDialog", "Select to allow local content to access remote URLs"))
        self.localRemoteUrlsCheckBox.setText(_translate("OfflineStorageConfigDialog", "Local Content can access Remote URLs"))
        self.localFileUrlsCheckBox.setToolTip(_translate("OfflineStorageConfigDialog", "Select to allow local content to access local files"))
        self.localFileUrlsCheckBox.setText(_translate("OfflineStorageConfigDialog", "Local Content can access Local Files"))

