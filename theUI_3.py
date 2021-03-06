from PyQt5 import QtCore, QtGui, QtWidgets
import pymongo
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtCore import QSize, QThread
from threading import Thread
import sys

cluster = pymongo.MongoClient(
    host="")
db = cluster['socialmedia']['messages']
db_log = cluster['socialmedia']['log']



class MainWindow(QMainWindow):
    opened = False

    def __init__(self):
        """Opens all necessary windows and buttons as needed """
        super(MainWindow, self).__init__()
        self.setMinimumSize(QSize(373, 624))
        self.setWindowTitle("CHATIFY")

        self.initUI()
        self.signupUI()
        self.loginUI()
        self.startupUI()
        
        #self.task = QThread().started.connect(self.new_msg_check())
        #self.task.start()

    def get_messages(self) -> list:
        """gets all the messages from the server """
        for messages in db.find({}):
            yield f"[{messages['alias']}]: {messages['message']}"

    def signupUI(self):
        """UI FOR THE SIGN_UP SCREEN"""
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
        self.username_signup.setStyleSheet(
            "color:rgb(255, 255, 255); background-color: rgb(100, 100, 100)")

        self.password_signup = QtWidgets.QLineEdit(self)
        self.password_signup.setGeometry(QtCore.QRect(60, 280, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.password_signup.setFont(font)
        self.password_signup.setText("*password*")
        self.password_signup.setStyleSheet(
            "color:rgb(255, 255, 255); background-color: rgb(100, 100, 100)")

        self.sign_up_btn = QtWidgets.QPushButton(self)
        self.sign_up_btn.setGeometry(QtCore.QRect(80, 340, 220, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sign_up_btn.setFont(font)
        self.sign_up_btn.setText("Sign up for new account")
        self.sign_up_btn.setStyleSheet(
            "color:rgb(255, 255, 255); background-color: rgb(100, 100, 100)")
        self.sign_up_btn.clicked.connect(self.sign_up_func)

    '''FUNCTIONS FOR THE SIGN_UP SCREEN'''

    def sign_up_func(self):
        '''create a user account'''
        set_log_name = self.username_signup.text()
        set_log_pass = self.password_signup.text()
        if (set_log_name != '*username*') and (db_log.count_documents({'log_name': set_log_name}) ==0):
            self.remove_signupUI()
            credential = {'log_name': set_log_name, 'log_pass': set_log_pass}
            db_log.insert_one(credential)
            self.insert_loginUI()

    def remove_signupUI(self):
        '''removes the SIGNUP ui'''
        self.signup_bg.setVisible(False)
        self.username_signup.setVisible(False)
        self.password_signup.setVisible(False)
        self.sign_up_btn.setVisible(False)

    def insert_signupUi(self):
        '''displays the SIGNUP UI'''
        self.signup_bg.setVisible(True)
        self.username_signup.setVisible(True)
        self.password_signup.setVisible(True)
        self.sign_up_btn.setVisible(True)

    def startupUI(self):
        '''UI FOR THE START UP SCREEN '''
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
        self.startup_sign_in_button.setStyleSheet(
            "color:rgb(255, 255, 255); background-color: rgb(100, 100, 100)")
        self.startup_sign_in_button.clicked.connect(self.startup_sign_in_func)

        self.startup_sign_up_button = QtWidgets.QPushButton(self)
        self.startup_sign_up_button.setGeometry(QtCore.QRect(60, 280, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.startup_sign_up_button.setFont(font)
        self.startup_sign_up_button.setText("Sign Up")
        self.startup_sign_up_button.setStyleSheet(
            "color:rgb(255, 255, 255); background-color: rgb(100, 100, 100)")
        self.startup_sign_up_button.clicked.connect(self.startup_sign_up_func)

    '''FUNCTUONS FOR THE STARTUP SCREEN'''

    def startup_sign_in_func(self):
        '''takes to sign in screen'''
        self.startup_sign_up_button.setVisible(False)
        self.startup_sign_in_button.setVisible(False)
        self.startup_bg.setVisible(False)
        self.remove_signupUI()

    def startup_sign_up_func(self):
        ''' take to sign up screen'''
        self.startup_sign_up_button.setVisible(False)
        self.startup_sign_in_button.setVisible(False)
        self.startup_bg.setVisible(False)
        self.remove_loginUI()
        self.insert_signupUi()

    def loginUI(self):
        '''UI FOR THE LOGIN SCREEN'''
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
        self.username_login.setStyleSheet(
            "color:rgb(255, 255, 255); background-color: rgb(100, 100, 100)")

        self.password_login = QtWidgets.QLineEdit(self)
        self.password_login.setGeometry(QtCore.QRect(60, 280, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.password_login.setFont(font)
        self.password_login.setText("*password*")
        self.password_login.setStyleSheet(
            "color:rgb(255, 255, 255); background-color: rgb(100, 100, 100)")

        self.sign_in_btn = QtWidgets.QPushButton(self)
        self.sign_in_btn.setGeometry(QtCore.QRect(120, 340, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sign_in_btn.setFont(font)
        self.sign_in_btn.setText("Sign In")
        self.sign_in_btn.setStyleSheet(
            "color:rgb(255, 255, 255); background-color: rgb(100, 100, 100)")
        self.sign_in_btn.clicked.connect(self.sign_in_func)

        self.wrong_pass = QtWidgets.QLineEdit(self)
        self.wrong_pass.setGeometry(QtCore.QRect(110, 180, 150, 31))
        self.wrong_pass.setText("[Name/Pass didnt matched]")
        self.wrong_pass.setReadOnly(True)
        self.wrong_pass.setStyleSheet(
            "color:rgb(255, 255, 255); background-color: rgb(100, 100, 100)")
        self.wrong_pass.setVisible(False)

    '''FUNCTIONS FOR THE LOGIN SCREEN'''

    def sign_in_func(self):
        ''' logs in the user'''
        current_user = db_log.find_one(
            {'log_name': self.username_login.text(), 'log_pass': self.password_login.text()})
        if current_user:
            self.remove_loginUI()
            self.msg_box.setText("\n".join(self.get_messages()))
        else:
            self.wrong_pass.setVisible(True)

    def remove_loginUI(self):
        '''removes the login ui'''
        self.login_bg.setVisible(False)
        self.password_login.setVisible(False)
        self.username_login.setVisible(False)
        self.sign_in_btn.setVisible(False)
        self.wrong_pass.setVisible(False)
        self.opened = True

    def insert_loginUI(self):
        '''displays the login ui'''
        self.login_bg.setVisible(True)
        self.password_login.setVisible(True)
        self.username_login.setVisible(True)
        self.sign_in_btn.setVisible(True)

    def initUI(self):
        ''' UI FOR THE MAIN SCREEN'''

        self.text_box = QtWidgets.QLineEdit(self)
        self.text_box.setGeometry(QtCore.QRect(30, 510, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.text_box.setFont(font)
        self.text_box.setStyleSheet(
            "color:rgb(255, 255, 255); background-color: rgb(100, 100, 100)")
        self.text_box.returnPressed.connect(self.send)

        self.send_btn = QtWidgets.QPushButton(self)
        self.send_btn.setGeometry(QtCore.QRect(290, 510, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.send_btn.setFont(font)
        self.send_btn.setText("SEND")
        self.send_btn.clicked.connect(self.send)
        self.send_btn.setStyleSheet(
            "color:rgb(255, 255, 255); background-color: rgb(100, 100, 100)")

        self.msg_box = QtWidgets.QTextEdit(self)
        self.msg_box.setGeometry(QtCore.QRect(30, 50, 311, 451))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.msg_box.setFont(font)
        self.msg_box.setReadOnly(True)
        self.msg_box.setStyleSheet(
            "background-color: rgb(100, 100, 100); color: rgb(255, 255, 255)")

        self.bg = QtWidgets.QLabel(self)
        self.bg.setGeometry(QtCore.QRect(10, 10, 351, 601))
        self.bg.setStyleSheet("background-color: rgb(86, 86, 86);")
        self.bg.setText("")
        self.bg.setObjectName("label")
        self.bg.lower()

        self.refresh_btn = QtWidgets.QPushButton(self)
        self.refresh_btn.setGeometry(280, 15, 50, 30)
        self.refresh_btn.setText('Refresh')
        self.refresh_btn.clicked.connect(self.refresh)
        self.refresh_btn.setStyleSheet(
            "color:rgb(255, 255, 255); background-color: rgb(100, 100, 100)")

        self.delete_all_btn = QtWidgets.QPushButton(self)
        self.delete_all_btn.setGeometry(30, 15, 70, 30)
        self.delete_all_btn.setText('Delete All')
        self.delete_all_btn.clicked.connect(self.delete_all)
        self.delete_all_btn.setStyleSheet(
            "color:rgb(255, 255, 255); background-color: rgb(100, 100, 100)")

        self.new_msg = QtWidgets.QLineEdit(self)
        self.new_msg.setGeometry(120, 15, 150, 30)
        self.new_msg.setReadOnly(True)
        self.new_msg.setText('No New Messages')
        self.new_msg.setStyleSheet(
            "color:rgb(255, 255, 255); background-color: rgb(100, 100, 100)")

        #t = Thread(target=self.update_op)
        # t.start()

    '''FUNCTIONS FOR THE MAIN SCREEN'''

    def send(self):
        '''sends new messages'''
        if not self.text_box.text():
            self.text_box.clear()
            return
        self.new_msg.setText('No New Messages')

        self.update_db()

        self.msg_box.setText("\n".join(self.get_messages()))
        self.text_box.clear()

    def new_msg_check(self):
        '''checks for new messages, and displays it on the screen'''
        while True:
            db.watch([{'$match': {'operationType': 'insert'}}])
            self.msg_box.setText("\n".join(self.get_messages()))

    def refresh(self):
        '''refreshes new messages'''
        self.new_msg.setText('No New Messages')

        self.msg_box.setText("\n".join(self.get_messages()))

        self.text_box.clear()

    def delete_all(self):
        '''deletes all the messages'''
        db.delete_many({})
        self.msg_box.setText('')

    def update_db(self):
        '''inserts the new text on the database'''
        self.new_msg.setText('No New Messages')
        username = self.username_login.text()
        text = self.text_box.text()
        msg = {'alias': username, 'message': text}
        db.insert_one(msg)


    def update_op(self):
        '''updates the messages in the screen'''
        pass


if __name__ == "__main__":
    def main():
        app = QtWidgets.QApplication(sys.argv)
        mainWin = MainWindow()
        mainWin.show()
        sys.exit(app.exec_())

    main()
