# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/Previewers/PreviewerQSS.ui'
#
# Created: Tue Nov 18 17:53:58 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PreviewerQSS(object):
    def setupUi(self, PreviewerQSS):
        PreviewerQSS.setObjectName("PreviewerQSS")
        PreviewerQSS.resize(500, 600)
        PreviewerQSS.setWindowTitle("")
        self.verticalLayout = QtWidgets.QVBoxLayout(PreviewerQSS)
        self.verticalLayout.setObjectName("verticalLayout")
        self.previewLabel = QtWidgets.QLabel(PreviewerQSS)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.previewLabel.setFont(font)
        self.previewLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.previewLabel.setObjectName("previewLabel")
        self.verticalLayout.addWidget(self.previewLabel)
        self.scrollArea = QtWidgets.QScrollArea(PreviewerQSS)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 463, 538))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.radioButton = QtWidgets.QRadioButton(self.tab_1)
        self.radioButton.setText("RadioButton")
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_4.addWidget(self.radioButton, 0, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.tab_1)
        self.checkBox.setText("CheckBox")
        self.checkBox.setTristate(True)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_4.addWidget(self.checkBox, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setText("PushButton")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 1, 0, 1, 1)
        self.toolButton = QtWidgets.QToolButton(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)
        self.toolButton.setText("ToolButton")
        self.toolButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_4.addWidget(self.toolButton, 1, 1, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.tab_1)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_4.addWidget(self.spinBox, 2, 0, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout_4.addWidget(self.doubleSpinBox, 2, 1, 1, 1)
        self.timeEdit = QtWidgets.QTimeEdit(self.tab_1)
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout_4.addWidget(self.timeEdit, 3, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.tab_1)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_4.addWidget(self.dateEdit, 3, 1, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(self.tab_1)
        self.lcdNumber.setDigitCount(10)
        self.lcdNumber.setProperty("intValue", 1234567890)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout_4.addWidget(self.lcdNumber, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_1)
        self.label.setText("Label with <a href=\"http://google.com\">link</a>")
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 4, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.progressBar = QtWidgets.QProgressBar(self.tab_1)
        self.progressBar.setMaximum(20)
        self.progressBar.setProperty("value", 10)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.readOnlyComboBox = QtWidgets.QComboBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.readOnlyComboBox.sizePolicy().hasHeightForWidth())
        self.readOnlyComboBox.setSizePolicy(sizePolicy)
        self.readOnlyComboBox.setObjectName("readOnlyComboBox")
        self.readOnlyComboBox.addItem("")
        self.readOnlyComboBox.setItemText(0, "1")
        self.readOnlyComboBox.addItem("")
        self.readOnlyComboBox.setItemText(1, "2")
        self.readOnlyComboBox.addItem("")
        self.readOnlyComboBox.setItemText(2, "3")
        self.horizontalLayout.addWidget(self.readOnlyComboBox)
        self.editableComboBox = QtWidgets.QComboBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editableComboBox.sizePolicy().hasHeightForWidth())
        self.editableComboBox.setSizePolicy(sizePolicy)
        self.editableComboBox.setEditable(True)
        self.editableComboBox.setObjectName("editableComboBox")
        self.editableComboBox.addItem("")
        self.editableComboBox.setItemText(0, "1")
        self.editableComboBox.addItem("")
        self.editableComboBox.setItemText(1, "2")
        self.editableComboBox.addItem("")
        self.editableComboBox.setItemText(2, "3")
        self.horizontalLayout.addWidget(self.editableComboBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit.setText("Line edit")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.passwordEdit = QtWidgets.QLineEdit(self.tab_1)
        self.passwordEdit.setText("Password")
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")
        self.horizontalLayout_4.addWidget(self.passwordEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.tab_1)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.verticalLayout_3.addWidget(self.dateTimeEdit)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.tab_1)
        self.commandLinkButton.setText("CommandLinkButton")
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.verticalLayout_3.addWidget(self.commandLinkButton)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLine = QtWidgets.QFrame(self.tab_1)
        self.horizontalLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.horizontalLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horizontalLine.setObjectName("horizontalLine")
        self.gridLayout.addWidget(self.horizontalLine, 0, 2, 1, 1)
        self.verticalLine = QtWidgets.QFrame(self.tab_1)
        self.verticalLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.verticalLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLine.setObjectName("verticalLine")
        self.gridLayout.addWidget(self.verticalLine, 1, 0, 2, 1)
        self.verticalSlider = QtWidgets.QSlider(self.tab_1)
        self.verticalSlider.setProperty("value", 30)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.verticalSlider.setObjectName("verticalSlider")
        self.gridLayout.addWidget(self.verticalSlider, 1, 1, 2, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
        self.horizontalSlider.setProperty("value", 30)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 1, 2, 1, 1)
        self.dial = QtWidgets.QDial(self.tab_1)
        self.dial.setNotchesVisible(True)
        self.dial.setObjectName("dial")
        self.gridLayout.addWidget(self.dial, 2, 2, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        spacerItem1 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.tabWidget.addTab(self.tab_1, "Tab 1")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.tab_2)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        item.setText("I1")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/battery.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setText("I2")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/image-sunset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setText("I3")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setText("I4")
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setText("I5")
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setText("I6")
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setText("I7")
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setText("I8")
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setText("I9")
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setText("I10")
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setText("I11")
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setText("I12")
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setText("I14")
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setText("I15")
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setText("I16")
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setText("I17")
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setText("I18")
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setText("I19")
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setText("I20")
        self.listWidget.addItem(item)
        self.gridLayout_2.addWidget(self.listWidget, 0, 0, 1, 1)
        self.iconsListWidget = QtWidgets.QListWidget(self.tab_2)
        self.iconsListWidget.setAlternatingRowColors(True)
        self.iconsListWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.iconsListWidget.setViewMode(QtWidgets.QListView.IconMode)
        self.iconsListWidget.setObjectName("iconsListWidget")
        self.gridLayout_2.addWidget(self.iconsListWidget, 0, 1, 1, 1)
        self.table = QtWidgets.QTableWidget(self.tab_2)
        self.table.setAlternatingRowColors(True)
        self.table.setObjectName("table")
        self.table.setColumnCount(2)
        self.table.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        item.setText("R1")
        self.table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("R2")
        self.table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("R3")
        self.table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("C1")
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("C2")
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("1,1")
        self.table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("1,2")
        self.table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("2,1")
        self.table.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("2,2")
        self.table.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("3,1")
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
        self.table.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("2,3")
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
        self.table.setItem(2, 1, item)
        self.table.horizontalHeader().setSortIndicatorShown(True)
        self.table.verticalHeader().setSortIndicatorShown(True)
        self.gridLayout_2.addWidget(self.table, 1, 0, 1, 1)
        self.tree = QtWidgets.QTreeWidget(self.tab_2)
        self.tree.setAlternatingRowColors(True)
        self.tree.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tree.setAllColumnsShowFocus(True)
        self.tree.setObjectName("tree")
        self.tree.headerItem().setText(0, "C1")
        self.tree.headerItem().setText(1, "C2")
        item_0 = QtWidgets.QTreeWidgetItem(self.tree)
        self.tree.topLevelItem(0).setText(0, "R1")
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.tree.topLevelItem(0).child(0).setText(0, "C1")
        item_1.setCheckState(0, QtCore.Qt.Checked)
        self.tree.topLevelItem(0).child(0).setText(1, "X1")
        item_1.setCheckState(1, QtCore.Qt.Checked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.tree.topLevelItem(0).child(1).setText(0, "C2")
        item_1.setCheckState(0, QtCore.Qt.PartiallyChecked)
        self.tree.topLevelItem(0).child(1).setText(1, "X2")
        item_1.setCheckState(1, QtCore.Qt.PartiallyChecked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.tree.topLevelItem(0).child(2).setText(0, "C3")
        self.tree.topLevelItem(0).child(2).setText(1, "X3")
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
        item_0 = QtWidgets.QTreeWidgetItem(self.tree)
        self.tree.topLevelItem(1).setText(0, "R2")
        item_0.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
        self.tree.header().setSortIndicatorShown(True)
        self.gridLayout_2.addWidget(self.tree, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "Tab 2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser.setUndoRedoEnabled(True)
        self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Text </span><span style=\" font-size:10pt; font-weight:600;\">browser</span><span style=\" font-size:10pt;\"> </span><span style=\" font-size:10pt; font-style:italic;\">with</span><span style=\" font-size:10pt;\"> </span><span style=\" font-size:10pt; text-decoration: underline;\">some</span><span style=\" font-size:10pt;\"> </span><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">text </span><span style=\" font-size:10pt;\">and </span><a href=\"http://google.com\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">links</span></a></p></body></html>")
        self.textBrowser.setOpenLinks(False)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_8.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Text edit</span></p></body></html>")
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_8.addWidget(self.textEdit, 0, 1, 1, 1)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.tab_3)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout_8.addWidget(self.calendarWidget, 0, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle("GroupBox")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 399, 275))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setText("Frame")
        self.label_2.setObjectName("label_2")
        self.gridLayout_10.addWidget(self.label_2, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 46, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem3, 1, 0, 1, 1)
        self.gridLayout_9.addWidget(self.frame, 0, 1, 1, 1)
        self.toolBox = QtWidgets.QToolBox(self.scrollAreaWidgetContents_2)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 69, 203))
        self.page.setObjectName("page")
        self.toolBox.addItem(self.page, "Toolbox1")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.page_2.setObjectName("page_2")
        self.toolBox.addItem(self.page_2, "Toolbox2")
        self.gridLayout_9.addWidget(self.toolBox, 0, 0, 2, 1)
        self.dockWidget = QtWidgets.QDockWidget(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setWindowTitle("Dock widget")
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.dockWidget.setWidget(self.dockWidgetContents_3)
        self.gridLayout_9.addWidget(self.dockWidget, 0, 2, 1, 1)
        self.mdiArea = QtWidgets.QMdiArea(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.mdiArea.sizePolicy().hasHeightForWidth())
        self.mdiArea.setSizePolicy(sizePolicy)
        self.mdiArea.setObjectName("mdiArea")
        self.gridLayout_9.addWidget(self.mdiArea, 1, 1, 1, 2)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox, 1, 0, 1, 3)
        self.tabWidget.addTab(self.tab_3, "Tab 3")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(PreviewerQSS)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PreviewerQSS)

    def retranslateUi(self, PreviewerQSS):
        _translate = QtCore.QCoreApplication.translate
        self.previewLabel.setText(_translate("PreviewerQSS", "Preview Style"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.iconsListWidget.setSortingEnabled(True)
        self.table.setSortingEnabled(True)
        __sortingEnabled = self.table.isSortingEnabled()
        self.table.setSortingEnabled(False)
        self.table.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.tree.isSortingEnabled()
        self.tree.setSortingEnabled(False)
        self.tree.setSortingEnabled(__sortingEnabled)

