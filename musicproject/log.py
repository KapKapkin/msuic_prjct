import sys
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets, uic
import os

from registration import RegistrationPage
from login import LoginPage

class StartPage(QtWidgets.QDialog):
    def __init__(self, parent):
        super(QtWidgets.QDialog, self).__init__(parent)
        

        self.parent = parent

        uic.loadUi(f'{os.getcwd()}/ui/startpage2.ui', self)
        self.setWindowTitle('Авторизация')
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        db_path = os.path.join(BASE_DIR, "database/music_db.db")

        self.con = sqlite3.connect(db_path)

        self.login_button.clicked.connect(self.login)

        self.registration_button.clicked.connect(self.registration)

    def login(self):
        self.login_page = LoginPage(self, self.parent)
        self.login_page.exec()

    def registration(self):
        self.reg_page = RegistrationPage(self)
        self.reg_page.exec()

    #! НЕ ТРОЖБ
    # позволяет перемещать безрамочное окно

    #! --------------------------------

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.old_pos = None

    def mouseMoveEvent(self, event):
        if not self.old_pos:
            return
        delta = event.pos() - self.old_pos
        self.move(self.pos() + delta)
    #! --------------------------------
