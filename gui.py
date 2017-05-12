
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_General(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(351, 194)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.markButton = QtWidgets.QPushButton(self.centralwidget)
        self.markButton.setGeometry(QtCore.QRect(40, 30, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.markButton.setFont(font)
        self.markButton.setObjectName("markButton")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(40, 120, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.cancelButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "General Mode"))
        self.markButton.setText(_translate("MainWindow", "Mark Attendance"))
        self.cancelButton.setText(_translate("MainWindow", "Cancel"))

class Ui_Privileged(object):
    def add(self):
        self.addWindow = QtWidgets.QMainWindow()
        self.ui = Ui_AddTeacher()
        self.ui.setupUi(self.addWindow)
        self.addWindow.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 195)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(30, 40, 111, 31))
        self.addButton.setObjectName("addButton")
        self.queryButton = QtWidgets.QPushButton(self.centralwidget)
        self.queryButton.setGeometry(QtCore.QRect(30, 80, 111, 31))
        self.queryButton.setObjectName("queryButton")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(240, 140, 81, 31))
        self.cancelButton.setObjectName("cancelButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.addButton.clicked.connect(self.add)
        self.cancelButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Privileged Mode"))
        self.addButton.setText(_translate("MainWindow", "Add New Teacher"))
        self.queryButton.setText(_translate("MainWindow", "Query"))
        self.cancelButton.setText(_translate("MainWindow", "Cancel"))

class Ui_Login(object):

    ###### Method to handle login Button #####
    def accept(self):
        if self.pass_lineEdit.text() == 'mytechworld':
            if self.gen_radioButton.isChecked():
                self.generalWindow = QtWidgets.QMainWindow()
                self.ui = Ui_General()
                self.ui.setupUi(self.generalWindow)
                self.generalWindow.show()
            if self.pri_radioButton.isChecked():
                self.privilegedwindow = QtWidgets.QMainWindow()
                self.ui = Ui_Privileged()
                self.ui.setupUi(self.privilegedwindow)
                self.privilegedwindow.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(361, 202)
        self.loginButton = QtWidgets.QPushButton(Dialog)
        self.loginButton.setGeometry(QtCore.QRect(140, 140, 75, 23))
        self.loginButton.setObjectName("loginButton")
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(230, 140, 75, 23))
        self.cancelButton.setObjectName("cancelButton")
        self.gen_radioButton = QtWidgets.QRadioButton(Dialog)
        self.gen_radioButton.setGeometry(QtCore.QRect(140, 80, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.gen_radioButton.setFont(font)
        self.gen_radioButton.setObjectName("gen_radioButton")
        self.pri_radioButton = QtWidgets.QRadioButton(Dialog)
        self.pri_radioButton.setGeometry(QtCore.QRect(140, 100, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pri_radioButton.setFont(font)
        self.pri_radioButton.setObjectName("pri_radioButton")
        self.pass_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.pass_lineEdit.setGeometry(QtCore.QRect(140, 40, 151, 20))
        self.pass_lineEdit.setText("")
        self.pass_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_lineEdit.setClearButtonEnabled(True)
        self.pass_lineEdit.setObjectName("pass_lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 40, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)

        ###################LoginButton###################
        self.loginButton.clicked.connect(self.accept)
        if self.pass_lineEdit.text() == 'mytechworld':
            self.loginButton.clicked.connect(Dialog.close)

        self.cancelButton.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.loginButton.setText(_translate("Dialog", "Login"))
        self.cancelButton.setText(_translate("Dialog", "Cancel"))
        self.gen_radioButton.setText(_translate("Dialog", "General Mode"))
        self.pri_radioButton.setText(_translate("Dialog", "Privileged Mode"))
        self.pass_lineEdit.setPlaceholderText(_translate("Dialog", "Password"))
        self.label.setText(_translate("Dialog", "Enter Password:"))
        
class Ui_AddTeacher(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(474, 229)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 90, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 160, 47, 13))
        self.label_5.setObjectName("label_5")
        self.titleDrop = QtWidgets.QComboBox(self.centralwidget)
        self.titleDrop.setGeometry(QtCore.QRect(90, 50, 41, 22))
        self.titleDrop.setObjectName("titleDrop")
        self.titleDrop.addItem("")
        self.titleDrop.addItem("")
        self.titleDrop.addItem("")
        self.firstName = QtWidgets.QLineEdit(self.centralwidget)
        self.firstName.setGeometry(QtCore.QRect(90, 90, 131, 20))
        self.firstName.setText("")
        self.firstName.setObjectName("firstName")
        self.lastName = QtWidgets.QLineEdit(self.centralwidget)
        self.lastName.setGeometry(QtCore.QRect(320, 90, 131, 20))
        self.lastName.setText("")
        self.lastName.setObjectName("lastName")
        self.designationDrop = QtWidgets.QComboBox(self.centralwidget)
        self.designationDrop.setGeometry(QtCore.QRect(90, 120, 101, 22))
        self.designationDrop.setObjectName("designationDrop")
        self.designationDrop.addItem("")
        self.designationDrop.addItem("")
        self.designationDrop.addItem("")
        self.mGender = QtWidgets.QRadioButton(self.centralwidget)
        self.mGender.setGeometry(QtCore.QRect(90, 160, 82, 17))
        self.mGender.setObjectName("mGender")
        self.fGender = QtWidgets.QRadioButton(self.centralwidget)
        self.fGender.setGeometry(QtCore.QRect(130, 160, 82, 17))
        self.fGender.setObjectName("fGender")
        self.resetBtn = QtWidgets.QPushButton(self.centralwidget)
        self.resetBtn.setGeometry(QtCore.QRect(200, 180, 75, 23))
        self.resetBtn.setObjectName("resetBtn")
        self.cancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cancelBtn.setGeometry(QtCore.QRect(290, 180, 75, 23))
        self.cancelBtn.setObjectName("cancelBtn")
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(380, 180, 75, 23))
        self.addBtn.setObjectName("addBtn")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 61, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(90, 20, 61, 16))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.cancelBtn.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add Teacher"))
        self.label.setText(_translate("MainWindow", "Title:"))
        self.label_2.setText(_translate("MainWindow", "First Name:"))
        self.label_3.setText(_translate("MainWindow", "Last Name:"))
        self.label_4.setText(_translate("MainWindow", "Designation:"))
        self.label_5.setText(_translate("MainWindow", "Gender:"))
        self.titleDrop.setItemText(0, _translate("MainWindow", "Mr."))
        self.titleDrop.setItemText(1, _translate("MainWindow", "Mrs."))
        self.titleDrop.setItemText(2, _translate("MainWindow", "Ms."))
        self.firstName.setPlaceholderText(_translate("MainWindow", "First Name"))
        self.lastName.setPlaceholderText(_translate("MainWindow", "Last Name"))
        self.designationDrop.setItemText(0, _translate("MainWindow", "Asst. Professor"))
        self.designationDrop.setItemText(1, _translate("MainWindow", "Professor"))
        self.designationDrop.setItemText(2, _translate("MainWindow", "Acct. Professor"))
        self.mGender.setText(_translate("MainWindow", "M"))
        self.fGender.setText(_translate("MainWindow", "F"))
        self.resetBtn.setText(_translate("MainWindow", "Reset"))
        self.cancelBtn.setText(_translate("MainWindow", "Cancel"))
        self.addBtn.setText(_translate("MainWindow", "Add"))
        self.label_6.setText(_translate("MainWindow", "Teacher Id:"))
        self.label_7.setText(_translate("MainWindow", "Number"))