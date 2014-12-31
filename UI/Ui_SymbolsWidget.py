# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/SymbolsWidget.ui'
#
# Created: Tue Nov 18 17:53:58 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SymbolsWidget(object):
    def setupUi(self, SymbolsWidget):
        SymbolsWidget.setObjectName("SymbolsWidget")
        SymbolsWidget.resize(268, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(SymbolsWidget)
        self.verticalLayout.setContentsMargins(0, 4, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableCombo = QtWidgets.QComboBox(SymbolsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableCombo.sizePolicy().hasHeightForWidth())
        self.tableCombo.setSizePolicy(sizePolicy)
        self.tableCombo.setObjectName("tableCombo")
        self.verticalLayout.addWidget(self.tableCombo)
        self.symbolsTable = QtWidgets.QTableView(SymbolsWidget)
        self.symbolsTable.setAlternatingRowColors(True)
        self.symbolsTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.symbolsTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.symbolsTable.setTextElideMode(QtCore.Qt.ElideNone)
        self.symbolsTable.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.symbolsTable.setObjectName("symbolsTable")
        self.symbolsTable.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.symbolsTable)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(SymbolsWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.symbolSpinBox = QtWidgets.QSpinBox(SymbolsWidget)
        self.symbolSpinBox.setMaximum(65535)
        self.symbolSpinBox.setSingleStep(32)
        self.symbolSpinBox.setObjectName("symbolSpinBox")
        self.horizontalLayout_2.addWidget(self.symbolSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(SymbolsWidget)
        QtCore.QMetaObject.connectSlotsByName(SymbolsWidget)
        SymbolsWidget.setTabOrder(self.tableCombo, self.symbolsTable)
        SymbolsWidget.setTabOrder(self.symbolsTable, self.symbolSpinBox)

    def retranslateUi(self, SymbolsWidget):
        _translate = QtCore.QCoreApplication.translate
        SymbolsWidget.setWindowTitle(_translate("SymbolsWidget", "Symbols"))
        self.tableCombo.setToolTip(_translate("SymbolsWidget", "Select the table to be shown"))
        self.label.setText(_translate("SymbolsWidget", "Symbol code:"))
        self.symbolSpinBox.setToolTip(_translate("SymbolsWidget", "Enter the symbol code"))

