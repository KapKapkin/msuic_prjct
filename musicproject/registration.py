import sys
import sqlite3

from PyQt5 import QtGui, QtWidgets, uic, QtCore
import os


class RegistrationPage(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(QtWidgets.QDialog, self).__init__(parent)

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        ui_path = os.path.join(BASE_DIR, "ui/registration.ui")

        uic.loadUi(ui_path, self)

        db_path = os.path.join(BASE_DIR, "database/music_db.db")

        self.con = sqlite3.connect(db_path)

        self.cur = self.con.cursor()

        self.status_label.setStyleSheet('color: #f7fdf9;')

        self.status_label.setAlignment(QtCore.Qt.AlignVCenter)

        self.accept_button.clicked.connect(self.registration_accept)
        self.setWindowTitle('Регистрация')

    def registration_accept(self):
        if len(self.name_line.text()) < 4:
            self.status_label.setText('Коротокое имя')
            return

        elif not self.email_line.text().endswith('@gmail.com'):
            self.status_label.setText('Неверный формат почты')
            return

        elif (self.email_line.text(),) in list(self.cur.execute('SELECT email FROM "users"')):
            self.status_label.setText('Такая почта уже зарегистрирована')
            return

        elif self.password_line.text() != self.password_repeat_line.text():
            self.status_label.setText('пароли разные')
            return

        elif len(self.password_line.text()) < 8:
            self.status_label.setText('Короткий пароль')
            return

        else:
            self.cur.execute(
                f'''INSERT INTO users (name, email, password) VALUES ('{self.name_line.text()}', '{self.email_line.text()}', '{self.password_line.text()}')''')
            self.con.commit()
            result = self.cur.execute(
                f'''SELECT id FROM users WHERE email = '{self.email_line.text()}' ''').fetchall()

            self.cur.execute(
                f'''CREATE TABLE 'user_{result[0][0]}'(id integer PRIMARY KEY unique, music_id integer unique)''')

            self.con.commit()
            self.con.close()
            self.close()

    
