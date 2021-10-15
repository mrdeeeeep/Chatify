from PyQt5 import QtCore, QtGui, QtWidgets
import pymongo
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
import threading
import sys
import time
import asyncio
import keyboard


cluster = pymongo.MongoClient("mongodb+srv://deep:1234abcd@cluster.ds3cv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster['socialmedia']['messages']
db_log = cluster['socialmedia']['log']


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setMinimumSize(QSize(373, 624))
        self.setWindowTitle("CHATIFY")

        self.initUI()
        self.signupUI()
        self.loginUI()
        self.startupUI()

        self.update_op()
        t = threading.Thread(target=self.new_msg_check)
        t.start()

    #################################################################################################
    def signupUI(self):
        self.signup_bg = QtWidgets.QLabel(self)
        self.signup_bg.setGeometry(QtCore.QRect(10, 10, 351, 601))
        self.signup_bg.setStyleSheet("background-color: rgb(86, 86, 86);")
        self.signup_bg.setText("")

        self.username_signup = QtWidgets.QLineEdit(self)
        self.username_signup.setGeometry(QtCore.QRect(60, 220, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.username_signup.setFont(font)
        self.username_signup.setText('*username*')
        self.username_signup.setStyleSheet("color:rgb(255, 255, 255); background-color: rgb(100, 100, 100)")

        self.password_signup = QtWidgets.QLineEdit(self)
        self.password_signup.setGeometry(QtCore.QRect(60, 280, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.password_signup.setFont(font)
        self.password_signup.setText("*password*")
        self.password_signup.setStyleSheet("color:rgb(255, 255, 255); background-color: rgb(100, 100, 100)")

        self.sign_up_btn = QtWidgets.QPushButton(self)
        self.sign_up_btn.setGeometry(QtCore.QRect(80, 340, 220, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sign_up_btn.setFont(font)
        self.sign_up_btn.setText("Sign up for new account")
        self.sign_up_btn.setStyleSheet("color:rgb(255, 255, 255); background-color: rgb(100, 100, 100)")
        self.sign_up_btn.clicked.connect(self.sign_up_func)

    def sign_up_func(self):
        set_log_name =  self.username_signup.text()
        set_log_pass =  self.password_signup.text()
        if set_log_name != '*username*':
            self.remove_signupUI()
            credential = {'log_name': set_log_name, 'log_pass': set_log_pass}
            db_log.insert_one(credential)
        self.remove_signupUI()
        self.insert_loginUI()

    def remove_signupUI(self):
        self.signup_bg.setVisible(False)
        self.username_signup.setVisible(False)
        self.password_signup.setVisible(False)
        self.sign_up_btn.setVisible(False)

    def insert_signupUi(self):
        self.signup_bg.setVisible(True)
        self.username_signup.setVisible(True)
        self.password_signup.setVisible(True)
        self.sign_up_btn.setVisible(True)






    #################################################################################################
    def startupUI(self):
        self.startup_bg = QtWidgets.QLabel(self)
        self.startup_bg.setGeometry(QtCore.QRect(10, 10, 351, 601))
        self.startup_bg.setStyleSheet("background-color: rgb(86, 86, 86);")
        self.startup_bg.setText("")

        self.startup_sign_in_button = QtWidgets.QPushButton(self)
        self.startup_sign_in_button.setGeometry(QtCore.QRect(60, 220, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.startup_sign_in_button.setFont(font)
        self.startup_sign_in_button.setText('Sign In')
        self.startup_sign_in_button.setStyleSheet("color:rgb(255, 255, 255); background-color: rgb(100, 100, 100)")
        self.startup_sign_in_button.clicked.connect(self.startup_sign_in_func)

        self.startup_sign_up_button = QtWidgets.QPushButton(self)
        self.startup_sign_up_button.setGeometry(QtCore.QRect(60, 280, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.startup_sign_up_button.setFont(font)
        self.startup_sign_up_button.setText("Sign Up")
        self.startup_sign_up_button.setStyleSheet("color:rgb(255, 255, 255); background-color: rgb(100, 100, 100)")
        self.startup_sign_up_button.clicked.connect(self.startup_sign_up_func)


    def startup_sign_in_func(self):
        self.startup_sign_up_button.setVisible(False)
        self.startup_sign_in_button.setVisible(False)
        self.startup_bg.setVisible(False)
        self.remove_signupUI()
    def startup_sign_up_func(self):
        self.startup_sign_up_button.setVisible(False)
        self.startup_sign_in_button.setVisible(False)
        self.startup_bg.setVisible(False)
        self.remove_loginUI()
        self.insert_signupUi()







    #################################################################################################
    def loginUI(self):
        self.login_bg = QtWidgets.QLabel(self)
        self.login_bg.setGeometry(QtCore.QRect(10, 10, 351, 601))
        self.login_bg.setStyleSheet("background-color: rgb(86, 86, 86);")
        self.login_bg.setText("")

        self.username_login = QtWidgets.QLineEdit(self)
        self.username_login.setGeometry(QtCore.QRect(60, 220, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.username_login.setFont(font)
        self.username_login.setText('*username*')
        self.username_login.setStyleSheet("color:rgb(255, 255, 255); background-color: rgb(100, 100, 100)")

        self.password_login = QtWidgets.QLineEdit(self)
        self.password_login.setGeometry(QtCore.QRect(60, 280, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.password_login.setFont(font)
        self.password_login.setText("*password*")
        self.password_login.setStyleSheet("color:rgb(255, 255, 255); background-color: rgb(100, 100, 100)")

        self.sign_in_btn = QtWidgets.QPushButton(self)
        self.sign_in_btn.setGeometry(QtCore.QRect(120, 340, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sign_in_btn.setFont(font)
        self.sign_in_btn.setText("Sign In")
        self.sign_in_btn.setStyleSheet("color:rgb(255, 255, 255); background-color: rgb(100, 100, 100)")
        self.sign_in_btn.clicked.connect(self.sign_in_func)

        self.wrong_pass = QtWidgets.QLineEdit(self)
        self.wrong_pass.setGeometry(QtCore.QRect(110, 180, 150, 31))
        self.wrong_pass.setText("[Name/Pass didnt matched]")
        self.wrong_pass.setReadOnly(True)
        self.wrong_pass.setStyleSheet("color:rgb(255, 255, 255); background-color: rgb(100, 100, 100)")
        self.wrong_pass.setVisible(False)

    def sign_in_func(self):
        log_name = self.username_login.text()
        log_pass = self.password_login.text()
        current_user = db_log.find({})
        authority = False
        for log in current_user:
            authorised_name = log['log_name']
            authorised_pass = log['log_pass']
            if log_name == authorised_name and log_pass == authorised_pass:
                authority = True
        if authority == True:
            self.remove_loginUI()
        elif authority == False:
            self.wrong_pass.setVisible(True)

    def remove_loginUI(self):
        self.login_bg.setVisible(False)
        self.password_login.setVisible(False)
        self.username_login.setVisible(False)
        self.sign_in_btn.setVisible(False)
        self.wrong_pass.setVisible(False)

    def insert_loginUI(self):
        self.login_bg.setVisible(True)
        self.password_login.setVisible(True)
        self.username_login.setVisible(True)
        self.sign_in_btn.setVisible(True)









    #################################################################################################
    def initUI(self):

        self.text_box = QtWidgets.QLineEdit(self)
        self.text_box.setGeometry(QtCore.QRect(30, 510, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.text_box.setFont(font)
        self.text_box.setStyleSheet("color:rgb(255, 255, 255); background-color: rgb(100, 100, 100)")
        self.text_box.returnPressed.connect(self.update_db)

        self.send_btn = QtWidgets.QPushButton(self)
        self.send_btn.setGeometry(QtCore.QRect(290, 510, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.send_btn.setFont(font)
        self.send_btn.setText("SEND")
        self.send_btn.clicked.connect(self.update_db)
        self.send_btn.setStyleSheet("color:rgb(255, 255, 255); background-color: rgb(100, 100, 100)")

        self.msg_box = QtWidgets.QTextEdit(self)
        self.msg_box.setGeometry(QtCore.QRect(30, 50, 311, 451))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.msg_box.setFont(font)
        self.msg_box.setReadOnly(True)
        self.msg_box.setStyleSheet("background-color: rgb(100, 100, 100); color: rgb(255, 255, 255)")

        self.bg = QtWidgets.QLabel(self)
        self.bg.setGeometry(QtCore.QRect(10, 10, 351, 601))
        self.bg.setStyleSheet("background-color: rgb(86, 86, 86);")
        self.bg.setText("")
        self.bg.setObjectName("label")
        self.bg.lower()

        self.refresh_btn = QtWidgets.QPushButton(self)
        self.refresh_btn.setGeometry(280,15,50,30)
        self.refresh_btn.setText('Refresh')
        self.refresh_btn.clicked.connect(self.refresh)
        self.refresh_btn.setStyleSheet("color:rgb(255, 255, 255); background-color: rgb(100, 100, 100)")

        self.delete_all_btn = QtWidgets.QPushButton(self)
        self.delete_all_btn.setGeometry(30, 15, 70, 30)
        self.delete_all_btn.setText('Delete All')
        self.delete_all_btn.clicked.connect(self.delete_all)
        self.delete_all_btn.setStyleSheet("color:rgb(255, 255, 255); background-color: rgb(100, 100, 100)")

        self.new_msg = QtWidgets.QLineEdit(self)
        self.new_msg.setGeometry(120,15,150,30)
        self.new_msg.setReadOnly(True)
        self.new_msg.setText('No New Messages')
        self.new_msg.setStyleSheet("color:rgb(255, 255, 255); background-color: rgb(100, 100, 100)")

    def new_msg_check(self):
        new_m = db.estimated_document_count()
        while True:
            msg_check = db.estimated_document_count()
            if msg_check != new_m:
                self.new_msg.setText('New Message... Click Refresh')               
            new_m = db.estimated_document_count()

    def refresh(self):
        self.new_msg.setText('No New Messages')
        self.update_op()

    def delete_all(self):
        db.delete_many({})
        self.msg_box.setText('')

    def update_db(self):
        self.new_msg.setText('No New Messages')
        username = self.username_login.text()
        text = self.text_box.text()
        msg = {'alias': username, 'message': text}
        db.insert_one(msg)
        self.update_op()
        self.text_box.clear()

    def update_op(self):
        all = db.find({})
        text_database = []
        msg_count = 0
        for messages in all:
            msg_count += 1
            user = messages['alias']
            text = messages['message']
            msg = f"[{user}] {text}"
            text_database.append(msg)
        self.msg_box.setText("\n".join(text_database))




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
