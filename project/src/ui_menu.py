# Form implementation generated from reading ui file 'D:\Kythuatlaptrinh\Project\KTLT_K23416_Group2\project\generated-files/ui/new_menu.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(971, 662)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setStyleSheet("background-color:#8E9299")
        self.widget.setObjectName("widget")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(197, 68, 752, 450))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.gridLayoutWidget)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout_20.setSpacing(5)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\Kythuatlaptrinh\\Project\\KTLT_K23416_Group2\\project\\generated-files/ui\\../image/ic_filter24.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(30, 20))
        self.pushButton_4.setShortcut("")
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_20.addWidget(self.pushButton_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem)
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 243, 228);\n"
"border-color: rgb(255, 134, 47);")
        self.pushButton_8.setDefault(True)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_20.addWidget(self.pushButton_8)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 165, 90);\n"
"background-color: rgb(255, 243, 228);")
        self.pushButton_3.setDefault(True)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_20.addWidget(self.pushButton_3)
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 165, 90);\n"
"background-color: rgb(255, 243, 228);")
        self.pushButton_9.setDefault(True)
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_20.addWidget(self.pushButton_9)
        self.verticalLayout_13.addLayout(self.horizontalLayout_20)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(750, 400))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 167772))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("\n"
"background-color: rgb(255, 243, 228);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 134, 47))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 134, 47))
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 134, 47))
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 134, 47))
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 134, 47))
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.verticalLayout_13.addWidget(self.tableWidget)
        self.widget_3 = QtWidgets.QWidget(parent=self.widget)
        self.widget_3.setGeometry(QtCore.QRect(11, 68, 179, 426))
        self.widget_3.setStyleSheet("background-color:#FF862F;border-top-right-radius:20;border-bottom-right-radius:20")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(parent=self.widget_3)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(-1, 25, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(6, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.restaurant_photo_label = QtWidgets.QLabel(parent=self.widget_2)
        self.restaurant_photo_label.setMinimumSize(QtCore.QSize(80, 80))
        self.restaurant_photo_label.setMaximumSize(QtCore.QSize(80, 80))
        self.restaurant_photo_label.setStyleSheet("border-radius:40;border:1px solid black")
        self.restaurant_photo_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.restaurant_photo_label.setObjectName("restaurant_photo_label")
        self.horizontalLayout.addWidget(self.restaurant_photo_label)
        spacerItem2 = QtWidgets.QSpacerItem(7, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.widget_2)
        self.restaurant_name_label = QtWidgets.QLabel(parent=self.widget_3)
        self.restaurant_name_label.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.restaurant_name_label.setFont(font)
        self.restaurant_name_label.setStyleSheet("color:white")
        self.restaurant_name_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.restaurant_name_label.setObjectName("restaurant_name_label")
        self.verticalLayout.addWidget(self.restaurant_name_label)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 78, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.restaurant_info_button = QtWidgets.QPushButton(parent=self.widget_3)
        self.restaurant_info_button.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.restaurant_info_button.setFont(font)
        self.restaurant_info_button.setStyleSheet("background:transparent; color:white")
        self.restaurant_info_button.setObjectName("restaurant_info_button")
        self.verticalLayout_2.addWidget(self.restaurant_info_button)
        self.restaurant_menu_button = QtWidgets.QPushButton(parent=self.widget_3)
        self.restaurant_menu_button.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.restaurant_menu_button.setFont(font)
        self.restaurant_menu_button.setStyleSheet("background:transparent; color:white")
        self.restaurant_menu_button.setObjectName("restaurant_menu_button")
        self.verticalLayout_2.addWidget(self.restaurant_menu_button)
        self.restaurant_review_button = QtWidgets.QPushButton(parent=self.widget_3)
        self.restaurant_review_button.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.restaurant_review_button.setFont(font)
        self.restaurant_review_button.setStyleSheet("background:transparent; color:white")
        self.restaurant_review_button.setObjectName("restaurant_review_button")
        self.verticalLayout_2.addWidget(self.restaurant_review_button)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 77, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.verticalLayout_5.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 971, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_8.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_8.setText(_translate("MainWindow", "Add"))
        self.pushButton_3.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Edit</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "Edit"))
        self.pushButton_9.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Edit</span></p></body></html>"))
        self.pushButton_9.setText(_translate("MainWindow", "Delete"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "FOOD"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "RATE"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "PRICE"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "DESCRIPTION"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "REVIEW"))
        self.restaurant_photo_label.setText(_translate("MainWindow", "TextLabel"))
        self.restaurant_name_label.setText(_translate("MainWindow", "Name Restaurant"))
        self.restaurant_info_button.setText(_translate("MainWindow", "Info"))
        self.restaurant_menu_button.setText(_translate("MainWindow", "Menu"))
        self.restaurant_review_button.setText(_translate("MainWindow", "Review"))
