# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Plugins/VcsPlugins/vcsMercurial/QueuesExtension/HgQueuesGuardsSelectionDialog.ui'
#
# Created: Tue Nov 18 17:53:57 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgQueuesGuardsSelectionDialog(object):
    def setupUi(self, HgQueuesGuardsSelectionDialog):
        HgQueuesGuardsSelectionDialog.setObjectName("HgQueuesGuardsSelectionDialog")
        HgQueuesGuardsSelectionDialog.resize(300, 300)
        HgQueuesGuardsSelectionDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(HgQueuesGuardsSelectionDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.guardsList = QtWidgets.QListWidget(HgQueuesGuardsSelectionDialog)
        self.guardsList.setAlternatingRowColors(True)
        self.guardsList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.guardsList.setObjectName("guardsList")
        self.verticalLayout.addWidget(self.guardsList)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgQueuesGuardsSelectionDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(HgQueuesGuardsSelectionDialog)
        self.buttonBox.accepted.connect(HgQueuesGuardsSelectionDialog.accept)
        self.buttonBox.rejected.connect(HgQueuesGuardsSelectionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HgQueuesGuardsSelectionDialog)
        HgQueuesGuardsSelectionDialog.setTabOrder(self.guardsList, self.buttonBox)

    def retranslateUi(self, HgQueuesGuardsSelectionDialog):
        _translate = QtCore.QCoreApplication.translate
        HgQueuesGuardsSelectionDialog.setWindowTitle(_translate("HgQueuesGuardsSelectionDialog", "Select Guards"))

