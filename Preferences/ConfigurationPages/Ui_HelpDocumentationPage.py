# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Preferences/ConfigurationPages/HelpDocumentationPage.ui'
#
# Created: Tue Nov 18 17:53:57 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HelpDocumentationPage(object):
    def setupUi(self, HelpDocumentationPage):
        HelpDocumentationPage.setObjectName("HelpDocumentationPage")
        HelpDocumentationPage.resize(526, 894)
        self.verticalLayout = QtWidgets.QVBoxLayout(HelpDocumentationPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerLabel = QtWidgets.QLabel(HelpDocumentationPage)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout.addWidget(self.headerLabel)
        self.line17 = QtWidgets.QFrame(HelpDocumentationPage)
        self.line17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line17.setObjectName("line17")
        self.verticalLayout.addWidget(self.line17)
        self.groupBox_5 = QtWidgets.QGroupBox(HelpDocumentationPage)
        self.groupBox_5.setObjectName("groupBox_5")
        self._2 = QtWidgets.QGridLayout(self.groupBox_5)
        self._2.setObjectName("_2")
        self.python2DocDirEdit = QtWidgets.QLineEdit(self.groupBox_5)
        self.python2DocDirEdit.setObjectName("python2DocDirEdit")
        self._2.addWidget(self.python2DocDirEdit, 0, 0, 1, 1)
        self.textLabel1_8_3 = QtWidgets.QLabel(self.groupBox_5)
        self.textLabel1_8_3.setWordWrap(True)
        self.textLabel1_8_3.setObjectName("textLabel1_8_3")
        self._2.addWidget(self.textLabel1_8_3, 1, 0, 1, 2)
        self.python2DocDirButton = QtWidgets.QToolButton(self.groupBox_5)
        self.python2DocDirButton.setObjectName("python2DocDirButton")
        self._2.addWidget(self.python2DocDirButton, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_5)
        self.groupBox_4 = QtWidgets.QGroupBox(HelpDocumentationPage)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridlayout = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridlayout.setObjectName("gridlayout")
        self.pythonDocDirEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.pythonDocDirEdit.setObjectName("pythonDocDirEdit")
        self.gridlayout.addWidget(self.pythonDocDirEdit, 0, 0, 1, 1)
        self.textLabel1_8_2 = QtWidgets.QLabel(self.groupBox_4)
        self.textLabel1_8_2.setWordWrap(True)
        self.textLabel1_8_2.setObjectName("textLabel1_8_2")
        self.gridlayout.addWidget(self.textLabel1_8_2, 1, 0, 1, 2)
        self.pythonDocDirButton = QtWidgets.QToolButton(self.groupBox_4)
        self.pythonDocDirButton.setObjectName("pythonDocDirButton")
        self.gridlayout.addWidget(self.pythonDocDirButton, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox_6 = QtWidgets.QGroupBox(HelpDocumentationPage)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridlayout1 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridlayout1.setObjectName("gridlayout1")
        self.qt4DocDirEdit = QtWidgets.QLineEdit(self.groupBox_6)
        self.qt4DocDirEdit.setObjectName("qt4DocDirEdit")
        self.gridlayout1.addWidget(self.qt4DocDirEdit, 0, 0, 1, 1)
        self.textLabel1_8_2_2_2 = QtWidgets.QLabel(self.groupBox_6)
        self.textLabel1_8_2_2_2.setWordWrap(True)
        self.textLabel1_8_2_2_2.setObjectName("textLabel1_8_2_2_2")
        self.gridlayout1.addWidget(self.textLabel1_8_2_2_2, 1, 0, 1, 2)
        self.qt4DocDirButton = QtWidgets.QToolButton(self.groupBox_6)
        self.qt4DocDirButton.setObjectName("qt4DocDirButton")
        self.gridlayout1.addWidget(self.qt4DocDirButton, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_6)
        self.groupBox_8 = QtWidgets.QGroupBox(HelpDocumentationPage)
        self.groupBox_8.setObjectName("groupBox_8")
        self._3 = QtWidgets.QGridLayout(self.groupBox_8)
        self._3.setObjectName("_3")
        self.qt5DocDirEdit = QtWidgets.QLineEdit(self.groupBox_8)
        self.qt5DocDirEdit.setObjectName("qt5DocDirEdit")
        self._3.addWidget(self.qt5DocDirEdit, 0, 0, 1, 1)
        self.textLabel1_8_2_2_4 = QtWidgets.QLabel(self.groupBox_8)
        self.textLabel1_8_2_2_4.setWordWrap(True)
        self.textLabel1_8_2_2_4.setObjectName("textLabel1_8_2_2_4")
        self._3.addWidget(self.textLabel1_8_2_2_4, 1, 0, 1, 2)
        self.qt5DocDirButton = QtWidgets.QToolButton(self.groupBox_8)
        self.qt5DocDirButton.setObjectName("qt5DocDirButton")
        self._3.addWidget(self.qt5DocDirButton, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_8)
        self.groupBox_7 = QtWidgets.QGroupBox(HelpDocumentationPage)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridlayout2 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridlayout2.setObjectName("gridlayout2")
        self.pyqt4DocDirEdit = QtWidgets.QLineEdit(self.groupBox_7)
        self.pyqt4DocDirEdit.setObjectName("pyqt4DocDirEdit")
        self.gridlayout2.addWidget(self.pyqt4DocDirEdit, 0, 0, 1, 1)
        self.textLabel1_8_2_2_3 = QtWidgets.QLabel(self.groupBox_7)
        self.textLabel1_8_2_2_3.setWordWrap(True)
        self.textLabel1_8_2_2_3.setObjectName("textLabel1_8_2_2_3")
        self.gridlayout2.addWidget(self.textLabel1_8_2_2_3, 1, 0, 1, 2)
        self.pyqt4DocDirButton = QtWidgets.QToolButton(self.groupBox_7)
        self.pyqt4DocDirButton.setObjectName("pyqt4DocDirButton")
        self.gridlayout2.addWidget(self.pyqt4DocDirButton, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_7)
        self.pyqt5Group = QtWidgets.QGroupBox(HelpDocumentationPage)
        self.pyqt5Group.setObjectName("pyqt5Group")
        self._4 = QtWidgets.QGridLayout(self.pyqt5Group)
        self._4.setObjectName("_4")
        self.pyqt5DocDirEdit = QtWidgets.QLineEdit(self.pyqt5Group)
        self.pyqt5DocDirEdit.setObjectName("pyqt5DocDirEdit")
        self._4.addWidget(self.pyqt5DocDirEdit, 0, 0, 1, 1)
        self.textLabel1_8_2_2_5 = QtWidgets.QLabel(self.pyqt5Group)
        self.textLabel1_8_2_2_5.setWordWrap(True)
        self.textLabel1_8_2_2_5.setObjectName("textLabel1_8_2_2_5")
        self._4.addWidget(self.textLabel1_8_2_2_5, 1, 0, 1, 2)
        self.pyqt5DocDirButton = QtWidgets.QToolButton(self.pyqt5Group)
        self.pyqt5DocDirButton.setObjectName("pyqt5DocDirButton")
        self._4.addWidget(self.pyqt5DocDirButton, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.pyqt5Group)
        self.pysideGroup = QtWidgets.QGroupBox(HelpDocumentationPage)
        self.pysideGroup.setObjectName("pysideGroup")
        self.gridlayout3 = QtWidgets.QGridLayout(self.pysideGroup)
        self.gridlayout3.setObjectName("gridlayout3")
        self.pysideDocDirEdit = QtWidgets.QLineEdit(self.pysideGroup)
        self.pysideDocDirEdit.setObjectName("pysideDocDirEdit")
        self.gridlayout3.addWidget(self.pysideDocDirEdit, 0, 0, 1, 1)
        self.textLabel1_8_2_2 = QtWidgets.QLabel(self.pysideGroup)
        self.textLabel1_8_2_2.setWordWrap(True)
        self.textLabel1_8_2_2.setObjectName("textLabel1_8_2_2")
        self.gridlayout3.addWidget(self.textLabel1_8_2_2, 1, 0, 1, 2)
        self.pysideDocDirButton = QtWidgets.QToolButton(self.pysideGroup)
        self.pysideDocDirButton.setObjectName("pysideDocDirButton")
        self.gridlayout3.addWidget(self.pysideDocDirButton, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.pysideGroup)
        spacerItem = QtWidgets.QSpacerItem(479, 41, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(HelpDocumentationPage)
        QtCore.QMetaObject.connectSlotsByName(HelpDocumentationPage)
        HelpDocumentationPage.setTabOrder(self.python2DocDirEdit, self.python2DocDirButton)
        HelpDocumentationPage.setTabOrder(self.python2DocDirButton, self.pythonDocDirEdit)
        HelpDocumentationPage.setTabOrder(self.pythonDocDirEdit, self.pythonDocDirButton)
        HelpDocumentationPage.setTabOrder(self.pythonDocDirButton, self.qt4DocDirEdit)
        HelpDocumentationPage.setTabOrder(self.qt4DocDirEdit, self.qt4DocDirButton)
        HelpDocumentationPage.setTabOrder(self.qt4DocDirButton, self.qt5DocDirEdit)
        HelpDocumentationPage.setTabOrder(self.qt5DocDirEdit, self.qt5DocDirButton)
        HelpDocumentationPage.setTabOrder(self.qt5DocDirButton, self.pyqt4DocDirEdit)
        HelpDocumentationPage.setTabOrder(self.pyqt4DocDirEdit, self.pyqt4DocDirButton)
        HelpDocumentationPage.setTabOrder(self.pyqt4DocDirButton, self.pyqt5DocDirEdit)
        HelpDocumentationPage.setTabOrder(self.pyqt5DocDirEdit, self.pyqt5DocDirButton)
        HelpDocumentationPage.setTabOrder(self.pyqt5DocDirButton, self.pysideDocDirEdit)
        HelpDocumentationPage.setTabOrder(self.pysideDocDirEdit, self.pysideDocDirButton)

    def retranslateUi(self, HelpDocumentationPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("HelpDocumentationPage", "<b>Configure help documentation</b>"))
        self.groupBox_5.setTitle(_translate("HelpDocumentationPage", "Python 2 Documentation"))
        self.python2DocDirEdit.setToolTip(_translate("HelpDocumentationPage", "Enter the Python 2 documentation directory"))
        self.textLabel1_8_3.setText(_translate("HelpDocumentationPage", "<b>Note</b>: Leave empty to use the PYTHON2DOCDIR environment variable, if set."))
        self.python2DocDirButton.setToolTip(_translate("HelpDocumentationPage", "Press to select the Python 2 documentation directory via a dialog"))
        self.groupBox_4.setTitle(_translate("HelpDocumentationPage", "Python 3 Documentation"))
        self.pythonDocDirEdit.setToolTip(_translate("HelpDocumentationPage", "Enter the Python 3 documentation directory"))
        self.textLabel1_8_2.setText(_translate("HelpDocumentationPage", "<b>Note</b>: Leave empty to use the PYTHON3DOCDIR environment variable, if set."))
        self.pythonDocDirButton.setToolTip(_translate("HelpDocumentationPage", "Press to select the Python 3 documentation directory via a dialog"))
        self.groupBox_6.setTitle(_translate("HelpDocumentationPage", "Qt4 Documentation"))
        self.qt4DocDirEdit.setToolTip(_translate("HelpDocumentationPage", "Enter the Qt4 documentation directory"))
        self.textLabel1_8_2_2_2.setText(_translate("HelpDocumentationPage", "<b>Note</b>: Leave empty to use the QT4DOCDIR environment variable, if set."))
        self.qt4DocDirButton.setToolTip(_translate("HelpDocumentationPage", "Press to select the Qt4 documentation directory via a dialog"))
        self.groupBox_8.setTitle(_translate("HelpDocumentationPage", "Qt5 Documentation"))
        self.qt5DocDirEdit.setToolTip(_translate("HelpDocumentationPage", "Enter the Qt5 documentation directory"))
        self.textLabel1_8_2_2_4.setText(_translate("HelpDocumentationPage", "<b>Note</b>: Leave empty to use the QT5DOCDIR environment variable, if set."))
        self.qt5DocDirButton.setToolTip(_translate("HelpDocumentationPage", "Press to select the Qt5 documentation directory via a dialog"))
        self.groupBox_7.setTitle(_translate("HelpDocumentationPage", "PyQt4 Documentation"))
        self.pyqt4DocDirEdit.setToolTip(_translate("HelpDocumentationPage", "Enter the PyQt4 documentation directory"))
        self.textLabel1_8_2_2_3.setText(_translate("HelpDocumentationPage", "<b>Note</b>: Leave empty to use the PYQT4DOCDIR environment variable, if set."))
        self.pyqt4DocDirButton.setToolTip(_translate("HelpDocumentationPage", "Press to select the PyQt4 documentation directory via a dialog"))
        self.pyqt5Group.setTitle(_translate("HelpDocumentationPage", "PyQt5 Documentation"))
        self.pyqt5DocDirEdit.setToolTip(_translate("HelpDocumentationPage", "Enter the PyQt5 documentation directory"))
        self.textLabel1_8_2_2_5.setText(_translate("HelpDocumentationPage", "<b>Note</b>: Leave empty to use the PYQT5DOCDIR environment variable, if set."))
        self.pyqt5DocDirButton.setToolTip(_translate("HelpDocumentationPage", "Press to select the PyQt5 documentation directory via a dialog"))
        self.pysideGroup.setTitle(_translate("HelpDocumentationPage", "PySide Documentation"))
        self.pysideDocDirEdit.setToolTip(_translate("HelpDocumentationPage", "Enter the PySide documentation directory"))
        self.textLabel1_8_2_2.setText(_translate("HelpDocumentationPage", "<b>Note</b>: Leave empty to use the PYSIDEDOCDIR environment variable, if set."))
        self.pysideDocDirButton.setToolTip(_translate("HelpDocumentationPage", "Press to select the PySide documentation directory via a dialog"))

