# Form implementation generated from reading ui file 'D:\Document\Bachelor\UEL\ProgrammingTechniquesKTLT\KTLT-group2\project\generated-files/ui/new_interface.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(893, 497)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget_3 = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.Login_SignUp = QtWidgets.QWidget()
        self.Login_SignUp.setObjectName("Login_SignUp")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Login_SignUp)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.header_welcome = QtWidgets.QWidget(parent=self.Login_SignUp)
        self.header_welcome.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.BusyCursor))
        self.header_welcome.setObjectName("header_welcome")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header_welcome)
        self.horizontalLayout_2.setContentsMargins(0, 5, 5, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.close_window_button = QtWidgets.QPushButton(parent=self.header_welcome)
        self.close_window_button.setMinimumSize(QtCore.QSize(24, 24))
        self.close_window_button.setMaximumSize(QtCore.QSize(24, 24))
        self.close_window_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.close_window_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/feather/icons/feather/x-circle.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.close_window_button.setIcon(icon)
        self.close_window_button.setObjectName("close_window_button")
        self.horizontalLayout_2.addWidget(self.close_window_button, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_3.addWidget(self.header_welcome)
        self.body_welcome = QtWidgets.QWidget(parent=self.Login_SignUp)
        self.body_welcome.setObjectName("body_welcome")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.body_welcome)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.body_welcome)
        self.stackedWidget.setObjectName("stackedWidget")
        self.left_login_page = QtWidgets.QWidget()
        self.left_login_page.setObjectName("left_login_page")
        self.stackedWidget.addWidget(self.left_login_page)
        self.left_signup_page = QtWidgets.QWidget()
        self.left_signup_page.setObjectName("left_signup_page")
        self.stackedWidget.addWidget(self.left_signup_page)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(parent=self.body_welcome)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.right_login_page = QtWidgets.QWidget()
        self.right_login_page.setObjectName("right_login_page")
        self.label = QtWidgets.QLabel(parent=self.right_login_page)
        self.label.setGeometry(QtCore.QRect(50, 80, 311, 111))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.stackedWidget_2.addWidget(self.right_login_page)
        self.right_signup_page = QtWidgets.QWidget()
        self.right_signup_page.setObjectName("right_signup_page")
        self.stackedWidget_2.addWidget(self.right_signup_page)
        self.horizontalLayout.addWidget(self.stackedWidget_2)
        self.verticalLayout_3.addWidget(self.body_welcome)
        self.stackedWidget_3.addWidget(self.Login_SignUp)
        self.Main = QtWidgets.QWidget()
        self.Main.setObjectName("Main")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Main)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.header_main = QtWidgets.QWidget(parent=self.Main)
        self.header_main.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.BusyCursor))
        self.header_main.setObjectName("header_main")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.header_main)
        self.horizontalLayout_4.setContentsMargins(0, 5, 5, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.home_button = QtWidgets.QPushButton(parent=self.header_main)
        self.home_button.setObjectName("home_button")
        self.horizontalLayout_4.addWidget(self.home_button)
        self.restaurant_button = QtWidgets.QPushButton(parent=self.header_main)
        self.restaurant_button.setObjectName("restaurant_button")
        self.horizontalLayout_4.addWidget(self.restaurant_button)
        self.profile_button = QtWidgets.QPushButton(parent=self.header_main)
        self.profile_button.setMinimumSize(QtCore.QSize(48, 48))
        self.profile_button.setMaximumSize(QtCore.QSize(48, 48))
        self.profile_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.profile_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/feather/icons/feather/smile.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.profile_button.setIcon(icon1)
        self.profile_button.setIconSize(QtCore.QSize(32, 32))
        self.profile_button.setObjectName("profile_button")
        self.horizontalLayout_4.addWidget(self.profile_button, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_2.addWidget(self.header_main)
        self.body_main = QtWidgets.QWidget(parent=self.Main)
        self.body_main.setObjectName("body_main")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.body_main)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.stackedWidget_5 = QtWidgets.QStackedWidget(parent=self.body_main)
        self.stackedWidget_5.setObjectName("stackedWidget_5")
        self.home_page = QtWidgets.QWidget()
        self.home_page.setObjectName("home_page")
        self.label_2 = QtWidgets.QLabel(parent=self.home_page)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 311, 111))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.stackedWidget_5.addWidget(self.home_page)
        self.restaurant_page = QtWidgets.QWidget()
        self.restaurant_page.setObjectName("restaurant_page")
        self.label_3 = QtWidgets.QLabel(parent=self.restaurant_page)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 311, 111))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.stackedWidget_5.addWidget(self.restaurant_page)
        self.review_restaurant_page = QtWidgets.QWidget()
        self.review_restaurant_page.setObjectName("review_restaurant_page")
        self.label_8 = QtWidgets.QLabel(parent=self.review_restaurant_page)
        self.label_8.setGeometry(QtCore.QRect(250, 60, 361, 111))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.stackedWidget_5.addWidget(self.review_restaurant_page)
        self.inside_restaurant_page = QtWidgets.QWidget()
        self.inside_restaurant_page.setObjectName("inside_restaurant_page")
        self.body_modify_restaurant = QtWidgets.QWidget(parent=self.inside_restaurant_page)
        self.body_modify_restaurant.setGeometry(QtCore.QRect(0, 0, 875, 439))
        self.body_modify_restaurant.setObjectName("body_modify_restaurant")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.body_modify_restaurant)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.left_panel_restaurant = QtWidgets.QVBoxLayout()
        self.left_panel_restaurant.setObjectName("left_panel_restaurant")
        self.pushButton = QtWidgets.QPushButton(parent=self.body_modify_restaurant)
        self.pushButton.setObjectName("pushButton")
        self.left_panel_restaurant.addWidget(self.pushButton)
        self.horizontalLayout_6.addLayout(self.left_panel_restaurant)
        self.stackedWidget_4 = QtWidgets.QStackedWidget(parent=self.body_modify_restaurant)
        self.stackedWidget_4.setObjectName("stackedWidget_4")
        self.menu_page = QtWidgets.QWidget()
        self.menu_page.setObjectName("menu_page")
        self.label_5 = QtWidgets.QLabel(parent=self.menu_page)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 311, 111))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.stackedWidget_4.addWidget(self.menu_page)
        self.add_food_page = QtWidgets.QWidget()
        self.add_food_page.setObjectName("add_food_page")
        self.label_4 = QtWidgets.QLabel(parent=self.add_food_page)
        self.label_4.setGeometry(QtCore.QRect(30, 50, 311, 111))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.stackedWidget_4.addWidget(self.add_food_page)
        self.modify_food_page = QtWidgets.QWidget()
        self.modify_food_page.setObjectName("modify_food_page")
        self.label_10 = QtWidgets.QLabel(parent=self.modify_food_page)
        self.label_10.setGeometry(QtCore.QRect(0, 0, 311, 111))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.stackedWidget_4.addWidget(self.modify_food_page)
        self.review_food_page = QtWidgets.QWidget()
        self.review_food_page.setObjectName("review_food_page")
        self.label_11 = QtWidgets.QLabel(parent=self.review_food_page)
        self.label_11.setGeometry(QtCore.QRect(200, 120, 311, 111))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.stackedWidget_4.addWidget(self.review_food_page)
        self.horizontalLayout_6.addWidget(self.stackedWidget_4)
        self.stackedWidget_5.addWidget(self.inside_restaurant_page)
        self.horizontalLayout_5.addWidget(self.stackedWidget_5)
        self.verticalLayout_2.addWidget(self.body_main)
        self.stackedWidget_3.addWidget(self.Main)
        self.verticalLayout.addWidget(self.stackedWidget_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget_5.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Welcome back..."))
        self.home_button.setText(_translate("MainWindow", "Home"))
        self.restaurant_button.setText(_translate("MainWindow", "Restaurant"))
        self.label_2.setText(_translate("MainWindow", "HOME"))
        self.label_3.setText(_translate("MainWindow", "RESTAURANT"))
        self.label_8.setText(_translate("MainWindow", "Review Restaurant"))
        self.pushButton.setText(_translate("MainWindow", "Info"))
        self.label_5.setText(_translate("MainWindow", "Menu"))
        self.label_4.setText(_translate("MainWindow", "New Food"))
        self.label_10.setText(_translate("MainWindow", "Food Name"))
        self.label_11.setText(_translate("MainWindow", "Review food"))
