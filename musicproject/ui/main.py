# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 542)
        MainWindow.setStyleSheet(
            "background-color: #000; font-family: Montserrat-Black;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.home = QtWidgets.QPushButton(self.centralwidget)
        self.home.setGeometry(QtCore.QRect(10, 50, 171, 41))
        self.home.setStyleSheet(
            "QPushButton:!focus {background-color: #000000; color: #fff; border-radius: 5px; font-family: \"Montserrat\";}  QPushButton:focus {background-color: #282828; color: #b3b3b3; border-radius: 5px; font-family: \"Montserrat\";}")
        self.home.setObjectName("home")
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(10, 100, 171, 41))
        self.search.setStyleSheet(
            "QPushButton:!focus {background-color: #000000; color: #fff; border-radius: 5px; font-family: \"Montserrat\";}  QPushButton:focus {background-color: #282828; color: #b3b3b3; border-radius: 5px; font-family: \"Montserrat\";}")
        self.search.setObjectName("search")
        self.my_music = QtWidgets.QPushButton(self.centralwidget)
        self.my_music.setGeometry(QtCore.QRect(10, 150, 171, 41))
        self.my_music.setStyleSheet(
            "QPushButton:!focus {background-color: #000000; color: #fff; border-radius: 5px; font-family: \"Montserrat\";}  QPushButton:focus {background-color: #282828; color: #b3b3b3; border-radius: 5px; font-family: \"Montserrat\";}")
        self.my_music.setObjectName("my_music")
        self.pod = QtWidgets.QLabel(self.centralwidget)
        self.pod.setGeometry(QtCore.QRect(-20, 410, 841, 171))
        self.pod.setTabletTracking(False)
        self.pod.setAcceptDrops(False)
        self.pod.setAutoFillBackground(False)
        self.pod.setStyleSheet(
            "background-color: #181818; border-color: #fff; border-style:outset; border-width: 1px;")
        self.pod.setText("")
        self.pod.setObjectName("pod")
        self.play_pause = QtWidgets.QPushButton(self.centralwidget)
        self.play_pause.setEnabled(False)
        self.play_pause.setGeometry(QtCore.QRect(390, 450, 40, 40))
        self.play_pause.setStyleSheet(
            "border-radius: 20px; background-color: #1db954;")
        self.play_pause.setText("")
        self.play_pause.setObjectName("play_pause")
        self.next_track = QtWidgets.QPushButton(self.centralwidget)
        self.next_track.setEnabled(False)
        self.next_track.setGeometry(QtCore.QRect(490, 450, 40, 40))
        self.next_track.setStyleSheet(
            "border-radius: 20px; background-color: #1db954;")
        self.next_track.setText("")
        self.next_track.setObjectName("next_track")
        self.previous_track = QtWidgets.QPushButton(self.centralwidget)
        self.previous_track.setEnabled(False)
        self.previous_track.setGeometry(QtCore.QRect(290, 450, 40, 40))
        self.previous_track.setStyleSheet(
            "border-radius: 20px; background-color: #1db954;")
        self.previous_track.setText("")
        self.previous_track.setObjectName("previous_track")
        self.record = QtWidgets.QPushButton(self.centralwidget)
        self.record.setEnabled(True)
        self.record.setGeometry(QtCore.QRect(10, 440, 51, 51))
        self.record.setStyleSheet(
            "background-color: #1db954; border-radius: 10px;")
        self.record.setText("")
        self.record.setObjectName("record")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 450, 201, 21))
        self.label.setStyleSheet("background-color: #181818; color: #fff;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.tab = QtWidgets.QTabWidget(self.centralwidget)
        self.tab.setGeometry(QtCore.QRect(190, -50, 471, 481))
        self.tab.setStyleSheet(
            "background-color: #121212;  border-width: 0px; border-color: #121212;")
        self.tab.setTabBarAutoHide(True)
        self.tab.setObjectName("tab")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.scroll = QtWidgets.QScrollArea(self.tab1)
        self.scroll.setGeometry(QtCore.QRect(10, 40, 441, 391))
        self.scroll.setStyleSheet("border-width:10px; border-radius: 10px;")
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setObjectName("scroll")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 441, 391))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scroll.setWidget(self.scrollAreaWidgetContents)
        self.tab.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.search_line = QtWidgets.QLineEdit(self.tab2)
        self.search_line.setGeometry(QtCore.QRect(10, 50, 271, 31))
        self.search_line.setStyleSheet(
            " QLineEdit { border-radius: 4px; color:rgb(0, 0, 0); background-color: #f7fdf9; } QLineEdit:focus { border-style:outset; border-width:4px; border-radius: 4px;  border-color: #1db954;  color: #f7fdf9; background-color: #181818; } ")
        self.search_line.setObjectName("search_line")
        self.search_btn = QtWidgets.QPushButton(self.tab2)
        self.search_btn.setGeometry(QtCore.QRect(330, 50, 93, 31))
        self.search_btn.setStyleSheet(
            "border-radius: 10px; background-color: #1db954;")
        self.search_btn.setObjectName("search_btn")
        self.search_scroll = QtWidgets.QScrollArea(self.tab2)
        self.search_scroll.setGeometry(QtCore.QRect(10, 100, 441, 341))
        self.search_scroll.setStyleSheet(
            "border-width:10px; border-radius: 10px;")
        self.search_scroll.setWidgetResizable(True)
        self.search_scroll.setObjectName("search_scroll")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(
            QtCore.QRect(0, 0, 441, 341))
        self.scrollAreaWidgetContents_2.setObjectName(
            "scrollAreaWidgetContents_2")
        self.search_scroll.setWidget(self.scrollAreaWidgetContents_2)
        self.tab.addTab(self.tab2, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setStyleSheet("border-width:10px; border-radius: 10px;")
        self.tab3.setObjectName("tab3")
        self.my_music_scroll = QtWidgets.QScrollArea(self.tab3)
        self.my_music_scroll.setGeometry(QtCore.QRect(10, 30, 441, 401))
        self.my_music_scroll.setWidgetResizable(True)
        self.my_music_scroll.setObjectName("my_music_scroll")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(
            QtCore.QRect(0, 0, 441, 401))
        self.scrollAreaWidgetContents_3.setObjectName(
            "scrollAreaWidgetContents_3")
        self.my_music_scroll.setWidget(self.scrollAreaWidgetContents_3)
        self.tab.addTab(self.tab3, "")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(753, 7, 41, 31))
        self.exit.setStyleSheet(
            "QPushButton:!hover {background-color: #000;} QPushButton:hover {background-color: #d71526;}")
        self.exit.setText("")
        self.exit.setObjectName("exit")
        self.role_up = QtWidgets.QPushButton(self.centralwidget)
        self.role_up.setGeometry(QtCore.QRect(703, 7, 41, 31))
        self.role_up.setStyleSheet(
            "QPushButton:!hover {background-color: #000;} QPushButton:hover {background-color: #181818;}")
        self.role_up.setText("")
        self.role_up.setObjectName("role_up")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(655, -20, 10, 430))
        self.line.setStyleSheet("background-color: #000; color: #fff;")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 470, 201, 21))
        self.label_2.setStyleSheet("background-color: #181818; color: #fff;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.slider = QtWidgets.QSlider(self.centralwidget)
        self.slider.setGeometry(QtCore.QRect(170, 420, 481, 22))
        self.slider.setStyleSheet("QSlider{\n"
                                  "                background: #181818;\n"
                                  "            }\n"
                                  "            QSlider::groove:horizontal {  \n"
                                  "                height: 10px;\n"
                                  "                margin: 0px;\n"
                                  "                border-radius: 5px;\n"
                                  "                background: #B0AEB1;\n"
                                  "            }\n"
                                  "            QSlider::handle:horizontal {\n"
                                  "                background: #fff;\n"
                                  "                border: 1px solid #E3DEE2;\n"
                                  "                width: 17px;\n"
                                  "                margin: -5px 0; \n"
                                  "                border-radius: 8px;\n"
                                  "            }\n"
                                  "            QSlider::sub-page:qlineargradient {\n"
                                  "                background: #1db954;\n"
                                  "                border-radius: 5px;\n"
                                  "            }")
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.sound = QtWidgets.QSlider(self.centralwidget)
        self.sound.setGeometry(QtCore.QRect(670, 420, 101, 22))
        self.sound.setStyleSheet("QSlider{\n"
                                 "                background: #181818;\n"
                                 "            }\n"
                                 "            QSlider::groove:horizontal {  \n"
                                 "                height: 10px;\n"
                                 "                margin: 0px;\n"
                                 "                border-radius: 5px;\n"
                                 "                background: #B0AEB1;\n"
                                 "            }\n"
                                 "            QSlider::handle:horizontal {\n"
                                 "                background: #fff;\n"
                                 "                border: 1px solid #E3DEE2;\n"
                                 "                width: 17px;\n"
                                 "                margin: -5px 0; \n"
                                 "                border-radius: 8px;\n"
                                 "            }\n"
                                 "            QSlider::sub-page:qlineargradient {\n"
                                 "                background: #1db954;\n"
                                 "                border-radius: 5px;\n"
                                 "            }")
        self.sound.setOrientation(QtCore.Qt.Horizontal)
        self.sound.setObjectName("sound")
        self.tab.raise_()
        self.home.raise_()
        self.search.raise_()
        self.my_music.raise_()
        self.pod.raise_()
        self.record.raise_()
        self.label.raise_()
        self.exit.raise_()
        self.role_up.raise_()
        self.line.raise_()
        self.play_pause.raise_()
        self.previous_track.raise_()
        self.next_track.raise_()
        self.label_2.raise_()
        self.slider.raise_()
        self.sound.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.home.setText(_translate("MainWindow", "Главная             "))
        self.search.setText(_translate("MainWindow", "Поиск                "))
        self.my_music.setText(_translate("MainWindow", "Моя музыка       "))
        self.tab.setTabText(self.tab.indexOf(self.tab1),
                            _translate("MainWindow", "Tab 1"))
        self.search_btn.setText(_translate("MainWindow", "Поиск"))
        self.tab.setTabText(self.tab.indexOf(self.tab2),
                            _translate("MainWindow", "Страница"))
        self.tab.setTabText(self.tab.indexOf(self.tab3),
                            _translate("MainWindow", "Tab 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
