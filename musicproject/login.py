import sys
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets, uic
import os


class LoginPage(QtWidgets.QDialog):
    def __init__(self, parent, main):
        super(QtWidgets.QDialog, self).__init__(parent)

        self.main = main
        
        self.parent = parent

        

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        ui_path = os.path.join(BASE_DIR, "ui/login.ui")

        db_path = os.path.join(BASE_DIR, "database/music_db.db")

        uic.loadUi(ui_path, self)
        self.setWindowTitle('Вход')
        self.con = sqlite3.connect(db_path)

        self.cur = self.con.cursor()

        self.accept_button.clicked.connect(self.login_accept)

    def login_accept(self):

        result = self.cur.execute(
            f'''SELECT id FROM users WHERE email = '{self.email_line.text()}' ''').fetchall()

        if result:
            self.close()
            self.parent.close()

            self.main.id = result[0][0]

    #! НЕ ТРОЖБ
    # позволяет перемещать безрамочное окно

   