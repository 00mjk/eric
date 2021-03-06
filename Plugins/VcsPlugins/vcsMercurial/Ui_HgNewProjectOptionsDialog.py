# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Plugins/VcsPlugins/vcsMercurial/HgNewProjectOptionsDialog.ui'
#
# Created: Tue Nov 18 17:53:57 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgNewProjectOptionsDialog(object):
    def setupUi(self, HgNewProjectOptionsDialog):
        HgNewProjectOptionsDialog.setObjectName("HgNewProjectOptionsDialog")
        HgNewProjectOptionsDialog.resize(562, 221)
        HgNewProjectOptionsDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(HgNewProjectOptionsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.textLabel1 = QtWidgets.QLabel(HgNewProjectOptionsDialog)
        self.textLabel1.setObjectName("textLabel1")
        self.gridLayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.protocolCombo = QtWidgets.QComboBox(HgNewProjectOptionsDialog)
        self.protocolCombo.setObjectName("protocolCombo")
        self.gridLayout.addWidget(self.protocolCombo, 0, 1, 1, 2)
        self.TextLabel2 = QtWidgets.QLabel(HgNewProjectOptionsDialog)
        self.TextLabel2.setObjectName("TextLabel2")
        self.gridLayout.addWidget(self.TextLabel2, 1, 0, 1, 1)
        self.vcsUrlEdit = QtWidgets.QLineEdit(HgNewProjectOptionsDialog)
        self.vcsUrlEdit.setObjectName("vcsUrlEdit")
        self.gridLayout.addWidget(self.vcsUrlEdit, 1, 1, 1, 1)
        self.vcsUrlButton = QtWidgets.QToolButton(HgNewProjectOptionsDialog)
        self.vcsUrlButton.setObjectName("vcsUrlButton")
        self.gridLayout.addWidget(self.vcsUrlButton, 1, 2, 1, 1)
        self.vcsRevisionLabel = QtWidgets.QLabel(HgNewProjectOptionsDialog)
        self.vcsRevisionLabel.setObjectName("vcsRevisionLabel")
        self.gridLayout.addWidget(self.vcsRevisionLabel, 2, 0, 1, 1)
        self.vcsRevisionEdit = QtWidgets.QLineEdit(HgNewProjectOptionsDialog)
        self.vcsRevisionEdit.setWhatsThis("")
        self.vcsRevisionEdit.setObjectName("vcsRevisionEdit")
        self.gridLayout.addWidget(self.vcsRevisionEdit, 2, 1, 1, 2)
        self.TextLabel4 = QtWidgets.QLabel(HgNewProjectOptionsDialog)
        self.TextLabel4.setObjectName("TextLabel4")
        self.gridLayout.addWidget(self.TextLabel4, 3, 0, 1, 1)
        self.vcsProjectDirEdit = QtWidgets.QLineEdit(HgNewProjectOptionsDialog)
        self.vcsProjectDirEdit.setObjectName("vcsProjectDirEdit")
        self.gridLayout.addWidget(self.vcsProjectDirEdit, 3, 1, 1, 1)
        self.projectDirButton = QtWidgets.QToolButton(HgNewProjectOptionsDialog)
        self.projectDirButton.setObjectName("projectDirButton")
        self.gridLayout.addWidget(self.projectDirButton, 3, 2, 1, 1)
        self.largeCheckBox = QtWidgets.QCheckBox(HgNewProjectOptionsDialog)
        self.largeCheckBox.setObjectName("largeCheckBox")
        self.gridLayout.addWidget(self.largeCheckBox, 4, 0, 1, 3)
        self.lfNoteLabel = QtWidgets.QLabel(HgNewProjectOptionsDialog)
        self.lfNoteLabel.setWordWrap(True)
        self.lfNoteLabel.setObjectName("lfNoteLabel")
        self.gridLayout.addWidget(self.lfNoteLabel, 5, 0, 1, 3)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgNewProjectOptionsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 6, 0, 1, 3)
        self.textLabel1.setBuddy(self.protocolCombo)
        self.TextLabel2.setBuddy(self.vcsUrlEdit)
        self.vcsRevisionLabel.setBuddy(self.vcsRevisionEdit)
        self.TextLabel4.setBuddy(self.vcsProjectDirEdit)

        self.retranslateUi(HgNewProjectOptionsDialog)
        self.buttonBox.accepted.connect(HgNewProjectOptionsDialog.accept)
        self.buttonBox.rejected.connect(HgNewProjectOptionsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HgNewProjectOptionsDialog)
        HgNewProjectOptionsDialog.setTabOrder(self.protocolCombo, self.vcsUrlEdit)
        HgNewProjectOptionsDialog.setTabOrder(self.vcsUrlEdit, self.vcsUrlButton)
        HgNewProjectOptionsDialog.setTabOrder(self.vcsUrlButton, self.vcsRevisionEdit)
        HgNewProjectOptionsDialog.setTabOrder(self.vcsRevisionEdit, self.vcsProjectDirEdit)
        HgNewProjectOptionsDialog.setTabOrder(self.vcsProjectDirEdit, self.projectDirButton)
        HgNewProjectOptionsDialog.setTabOrder(self.projectDirButton, self.largeCheckBox)
        HgNewProjectOptionsDialog.setTabOrder(self.largeCheckBox, self.buttonBox)

    def retranslateUi(self, HgNewProjectOptionsDialog):
        _translate = QtCore.QCoreApplication.translate
        HgNewProjectOptionsDialog.setWindowTitle(_translate("HgNewProjectOptionsDialog", "New Project from Repository"))
        HgNewProjectOptionsDialog.setWhatsThis(_translate("HgNewProjectOptionsDialog", "<b>New Project from Repository Dialog</b>\n"
"<p>Enter the various repository infos into the entry fields. These values are used, when the new project is retrieved from the repository. If the checkbox is selected, the URL must end in the project name. A repository layout with project/tags, project/branches and project/trunk will be assumed. In this case, you may enter a tag or branch, which must look like tags/tagname or branches/branchname. If the checkbox is not selected, the URL must contain the complete path in the repository.</p>\n"
"<p>For remote repositories the URL must contain the hostname.</p>"))
        self.textLabel1.setText(_translate("HgNewProjectOptionsDialog", "&Protocol:"))
        self.protocolCombo.setToolTip(_translate("HgNewProjectOptionsDialog", "Select the protocol to access the repository"))
        self.TextLabel2.setText(_translate("HgNewProjectOptionsDialog", "&URL:"))
        self.vcsUrlEdit.setToolTip(_translate("HgNewProjectOptionsDialog", "Enter the url path of the repository (without protocol part)"))
        self.vcsUrlButton.setToolTip(_translate("HgNewProjectOptionsDialog", "Select the repository url via a directory selection dialog"))
        self.vcsRevisionLabel.setText(_translate("HgNewProjectOptionsDialog", "&Revision:"))
        self.vcsRevisionEdit.setToolTip(_translate("HgNewProjectOptionsDialog", "Enter the revision the new project should be generated from"))
        self.TextLabel4.setText(_translate("HgNewProjectOptionsDialog", "Project &Directory:"))
        self.vcsProjectDirEdit.setToolTip(_translate("HgNewProjectOptionsDialog", "Enter the directory of the new project."))
        self.vcsProjectDirEdit.setWhatsThis(_translate("HgNewProjectOptionsDialog", "<b>Project Directory</b>\n"
"<p>Enter the directory of the new project. It will be retrieved from \n"
"the repository and be placed in this directory.</p>"))
        self.largeCheckBox.setText(_translate("HgNewProjectOptionsDialog", "Download all versions of all large files"))
        self.lfNoteLabel.setText(_translate("HgNewProjectOptionsDialog", "<b>Note:</b> This option increases the download time and volume."))

