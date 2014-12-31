# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './E5Gui/E5ErrorMessageFilterDialog.ui'
#
# Created: Tue Nov 18 17:53:58 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_E5ErrorMessageFilterDialog(object):
    def setupUi(self, E5ErrorMessageFilterDialog):
        E5ErrorMessageFilterDialog.setObjectName("E5ErrorMessageFilterDialog")
        E5ErrorMessageFilterDialog.resize(500, 350)
        E5ErrorMessageFilterDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(E5ErrorMessageFilterDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.searchEdit = E5ClearableLineEdit(E5ErrorMessageFilterDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchEdit.sizePolicy().hasHeightForWidth())
        self.searchEdit.setSizePolicy(sizePolicy)
        self.searchEdit.setMinimumSize(QtCore.QSize(300, 0))
        self.searchEdit.setObjectName("searchEdit")
        self.gridLayout_2.addWidget(self.searchEdit, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)
        self.addButton = QtWidgets.QPushButton(E5ErrorMessageFilterDialog)
        self.addButton.setAutoDefault(False)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 0, 1, 1, 1)
        self.line = QtWidgets.QFrame(E5ErrorMessageFilterDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 1, 1, 1)
        self.removeButton = QtWidgets.QPushButton(E5ErrorMessageFilterDialog)
        self.removeButton.setAutoDefault(False)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout.addWidget(self.removeButton, 2, 1, 1, 1)
        self.removeAllButton = QtWidgets.QPushButton(E5ErrorMessageFilterDialog)
        self.removeAllButton.setAutoDefault(False)
        self.removeAllButton.setObjectName("removeAllButton")
        self.gridLayout.addWidget(self.removeAllButton, 3, 1, 1, 1)
        self.filterList = E5ListView(E5ErrorMessageFilterDialog)
        self.filterList.setAlternatingRowColors(True)
        self.filterList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.filterList.setObjectName("filterList")
        self.gridLayout.addWidget(self.filterList, 0, 0, 5, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(E5ErrorMessageFilterDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(E5ErrorMessageFilterDialog)
        self.buttonBox.accepted.connect(E5ErrorMessageFilterDialog.accept)
        self.buttonBox.rejected.connect(E5ErrorMessageFilterDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(E5ErrorMessageFilterDialog)
        E5ErrorMessageFilterDialog.setTabOrder(self.searchEdit, self.filterList)
        E5ErrorMessageFilterDialog.setTabOrder(self.filterList, self.addButton)
        E5ErrorMessageFilterDialog.setTabOrder(self.addButton, self.removeButton)
        E5ErrorMessageFilterDialog.setTabOrder(self.removeButton, self.removeAllButton)
        E5ErrorMessageFilterDialog.setTabOrder(self.removeAllButton, self.buttonBox)

    def retranslateUi(self, E5ErrorMessageFilterDialog):
        _translate = QtCore.QCoreApplication.translate
        E5ErrorMessageFilterDialog.setWindowTitle(_translate("E5ErrorMessageFilterDialog", "Error Messages Filter"))
        self.searchEdit.setToolTip(_translate("E5ErrorMessageFilterDialog", "Enter search term for message"))
        self.addButton.setToolTip(_translate("E5ErrorMessageFilterDialog", "Press to add filter to the list"))
        self.addButton.setText(_translate("E5ErrorMessageFilterDialog", "&Add..."))
        self.removeButton.setToolTip(_translate("E5ErrorMessageFilterDialog", "Press to remove the selected entries"))
        self.removeButton.setText(_translate("E5ErrorMessageFilterDialog", "&Remove"))
        self.removeAllButton.setToolTip(_translate("E5ErrorMessageFilterDialog", "Press to remove all entries"))
        self.removeAllButton.setText(_translate("E5ErrorMessageFilterDialog", "R&emove All"))

from E5Gui.E5LineEdit import E5ClearableLineEdit
from E5Gui.E5ListView import E5ListView
