# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Plugins/VcsPlugins/vcsPySvn/SvnLogDialog.ui'
#
# Created: Tue Nov 18 17:53:57 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SvnLogDialog(object):
    def setupUi(self, SvnLogDialog):
        SvnLogDialog.setObjectName("SvnLogDialog")
        SvnLogDialog.resize(751, 649)
        self.verticalLayout = QtWidgets.QVBoxLayout(SvnLogDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.contentsGroup = QtWidgets.QGroupBox(SvnLogDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.contentsGroup.sizePolicy().hasHeightForWidth())
        self.contentsGroup.setSizePolicy(sizePolicy)
        self.contentsGroup.setObjectName("contentsGroup")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.contentsGroup)
        self.vboxlayout.setObjectName("vboxlayout")
        self.contents = QtWidgets.QTextBrowser(self.contentsGroup)
        self.contents.setObjectName("contents")
        self.vboxlayout.addWidget(self.contents)
        self.verticalLayout.addWidget(self.contentsGroup)
        self.sbsCheckBox = QtWidgets.QCheckBox(SvnLogDialog)
        self.sbsCheckBox.setObjectName("sbsCheckBox")
        self.verticalLayout.addWidget(self.sbsCheckBox)
        self.errorGroup = QtWidgets.QGroupBox(SvnLogDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.errorGroup.sizePolicy().hasHeightForWidth())
        self.errorGroup.setSizePolicy(sizePolicy)
        self.errorGroup.setObjectName("errorGroup")
        self.vboxlayout1 = QtWidgets.QVBoxLayout(self.errorGroup)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.errors = QtWidgets.QTextEdit(self.errorGroup)
        self.errors.setReadOnly(True)
        self.errors.setAcceptRichText(False)
        self.errors.setObjectName("errors")
        self.vboxlayout1.addWidget(self.errors)
        self.verticalLayout.addWidget(self.errorGroup)
        self.buttonBox = QtWidgets.QDialogButtonBox(SvnLogDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SvnLogDialog)
        QtCore.QMetaObject.connectSlotsByName(SvnLogDialog)
        SvnLogDialog.setTabOrder(self.contents, self.sbsCheckBox)
        SvnLogDialog.setTabOrder(self.sbsCheckBox, self.errors)
        SvnLogDialog.setTabOrder(self.errors, self.buttonBox)

    def retranslateUi(self, SvnLogDialog):
        _translate = QtCore.QCoreApplication.translate
        SvnLogDialog.setWindowTitle(_translate("SvnLogDialog", "Subversion Log"))
        self.contentsGroup.setTitle(_translate("SvnLogDialog", "Log"))
        self.contents.setWhatsThis(_translate("SvnLogDialog", "<b>Subversion Log</b><p>This shows the output of the svn log command. By clicking on the links you may show the difference between versions.</p>"))
        self.sbsCheckBox.setToolTip(_translate("SvnLogDialog", "Select to show differences side-by-side"))
        self.sbsCheckBox.setText(_translate("SvnLogDialog", "Show differences side-by-side"))
        self.errorGroup.setTitle(_translate("SvnLogDialog", "Errors"))
        self.errors.setWhatsThis(_translate("SvnLogDialog", "<b>Subversion log errors</b><p>This shows possible error messages of the svn log command.</p>"))

