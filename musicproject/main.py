import sys
import sqlite3
import os

import random
from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtWidgets, uic, QtCore, QtMultimedia

from log import StartPage
from track_widget import TrackWidget


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # инициализация и стиили окна

        # безрамочное окно
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.id = False

        self.hide()

        #! режим (почти)разработчика (если False)
        if 1:

            startpage = StartPage(self)
            startpage.exec()

            if self.id is False:
                sys.exit()

            # id пользователя

            # загрузка .ui и .db файлов
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        ui_path = os.path.join(BASE_DIR, "ui/main.ui")

        db_path = os.path.join(BASE_DIR, "database/music_db.db")

        uic.loadUi(ui_path, self)

        # sqlite3

        self.con = sqlite3.connect(db_path)

        self.cur = self.con.cursor()

        # стили и подключение кнопки выхода и сворачивания окна

        self.exit.setIcon(QtGui.QIcon('icons/X.png'))
        self.exit.clicked.connect(self.close_programm)

        self.role_up.setIcon(QtGui.QIcon('icons/role_up.png'))
        self.role_up.clicked.connect(self.role_up_programm)

        # стили и подключение кнопок боковой панели

        self.home.setIcon(QtGui.QIcon('icons/home.png'))
        self.home.setIconSize(QtCore.QSize(35, 35))

        self.search.setIcon(QtGui.QIcon('icons/search.png'))
        self.search.setIconSize(QtCore.QSize(30, 30))

        self.my_music.setIcon(QtGui.QIcon('icons/mymusic.png'))
        self.my_music.setIconSize(QtCore.QSize(30, 30))

        self.home.clicked.connect(self.change_tab)

        self.search.clicked.connect(self.change_tab)

        self.my_music.clicked.connect(self.change_tab)

        #! Создание плеера
        self.player = QtMultimedia.QMediaPlayer()

        self.current_track = False
        self.player.durationChanged.connect(self.change_duration)
        self.player.positionChanged.connect(self.position_changed)
        self.slider.valueChanged.connect(self.end_of_track)
        self.slider.sliderMoved.connect(self.set_position)
        self.sound.setMaximum(100)
        self.sound.setValue(50)
        self.sound.valueChanged.connect(self.sound_changed)
        self.player.setVolume(self.sound.value())
        self.pause = True

        self.slider.setEnabled(False)

        # стили и подключение кнопок нижней панели
        self.record.setIcon(QtGui.QIcon('icons/record.png'))

        self.previous_track.setIcon(QtGui.QIcon('icons/previous.png'))
        self.previous_track.clicked.connect(self.previous)

        self.play_pause.setIcon(QtGui.QIcon('icons/play.png'))
        self.play_pause.clicked.connect(self.play_pause_func)

        self.next_track.setIcon(QtGui.QIcon('icons/next.png'))
        self.next_track.clicked.connect(self.next)

        self.tab1_create()
        self.tab2_create()
        self.tab3_create()

        #! TAB 1

        # tab1 по умолчанию
        self.tab.setCurrentWidget(self.tab1)

    def tab1_create(self):

        self.scroll.verticalScrollBar().setStyleSheet('width: 0px;')
        self.scroll.setWidgetResizable(True)

        self.widget = QtWidgets.QWidget(self)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addSpacing(10)

        self.widget.setLayout(self.layout)

        result = self.cur.execute('''SELECT id FROM all_music''').fetchall()

        # создание TrackWidget для рандомных треков
        lst = []
        self.firts_tab_result = []
        while len(lst) < 10:
            num = [*random.choice(list(result))][0]

            if not num in lst:
                track = TrackWidget(num, self)
                track.setParent(self.widget)
                track.setFixedSize(412, 74)
                self.layout.addWidget(track)
                lst.append(num)
                self.firts_tab_result.append(track)

        self.scroll.setWidget(self.widget)
        self.scroll.setWidgetResizable(True)

        #! TAB 2

    def tab2_create(self):

        # спрятывание scrollbar'a
        self.search_scroll.verticalScrollBar().setStyleSheet('width: 0px;')

        self.search_scroll.setWidgetResizable(True)

        self.search_btn.setStyleSheet(
            'border-radius: 10px; background-color: #1db954;')

        self.search_widget = QtWidgets.QWidget()

        self.search_layout = QtWidgets.QVBoxLayout()

        # не дает виджетам накладываться друг на друга
        self.search_layout.addSpacing(10)

        # получение запроса из поисковой строки
        self.search_widget.setLayout(self.search_layout)

        # отправление запроса в функцию self5.show_result
        self.search_btn.clicked.connect(self.show_result)

        #! TAB3
    def tab3_create(self):
        self.my_music_scroll.verticalScrollBar().setStyleSheet('width: 0px;')
        self.my_music_scroll.setWidgetResizable(True)

        my_music_widget = QtWidgets.QWidget(self)
        my_music_layout = QtWidgets.QVBoxLayout()
        my_music_layout.addSpacing(10)

        my_music_widget.setLayout(my_music_layout)

        command = f'''SELECT music_id FROM 'user_{self.id}' '''
        result = self.cur.execute(command).fetchall()
        self.second_tab_result = []
        for i in result:
            music_id = i[0]
            track = TrackWidget(music_id, self)
            track.setFixedSize(412, 74)
            my_music_layout.addWidget(track)
            self.second_tab_result.append(track)
        self.my_music_scroll.setWidget(my_music_widget)

    # выводит на tab2 все треки подходящие по запросу

    def show_result(self):

        # предварительное удаление всех виджетов с tab2.search_scroll
        if self.search_layout.count() > 1:
            for i in reversed(range(1, self.search_layout.count())):
                self.search_layout.itemAt(i).widget().setParent(None)

        # запрос для базы данных
        response = self.search_line.text()
        result = self.cur.execute(
            f'''SELECT id FROM all_music WHERE title LIKE '%{response}%' or author LIKE '%{response}%' ''').fetchall()
        self.third_tab_result = []
        # добавление результатов на tab2.search_scroll
        for i in result:

            track = TrackWidget(i[0], self)
            track.setFixedSize(412, 74)
            self.search_layout.addWidget(track)
            self.third_tab_result.append(track)

        self.search_scroll.setWidget(self.search_widget)
        self.search_scroll.setWidgetResizable(True)

    # переключает TabWidget между tab1, tab2, tab3
    def change_tab(self):

        if self.sender() == self.home:
            self.tab.setCurrentWidget(self.tab1)
            self.tab1_create()

        if self.sender() == self.search:
            self.tab.setCurrentWidget(self.tab2)

        if self.sender() == self.my_music:
            self.tab.setCurrentWidget(self.tab3)

    def play_pause_func(self):

        if self.pause:
            self.play_func()
        else:
            self.pause_func()

    def play_func(self):
        self.player.setPosition(self.position)
        self.player.play()
        self.pause = False

    def pause_func(self):
        self.position = self.slider.value()
        self.player.stop()
        self.slider.setSliderPosition(self.position)
        self.pause = True

    def change_duration(self, duration_ms):
        self.slider.setMaximum(duration_ms)

    def set_position(self, pos):
        self.player.setPosition(pos)

    def position_changed(self, pos):
        self.slider.setValue(pos)

    def previous(self):

        par = self.current_track.parent()
        slide = par.children()
        index = slide.index(self.current_track)
        if index > 1:
            previous_track = slide[index - 1]
            previous_track.play()
        else:
            previous_track = slide[-1]
            previous_track.play()


    def next(self):

        par = self.current_track.parent()
        slide = par.children()
        index = slide.index(self.current_track)
        if len(slide) - 1 > index > 0:
            next_track = slide[index + 1]
            next_track.play()
        else:
            next_track = slide[1]
            next_track.play()

    def sound_changed(self):
        self.player.setVolume(self.sound.value())

    def end_of_track(self):
        if self.player.position() == self.slider.maximum():
            self.next()

    #! НЕ ТРОЖБ~
    # позволяет перемещать безрамочное окно

    #! --------------------------------
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = None

    def mouseMoveEvent(self, event):
        if not self.old_pos:
            return
        delta = event.pos() - self.old_pos
        self.move(self.pos() + delta)
    #! --------------------------------

    # закрытие и сворачивание программы
    def close_programm(self):
        sys.exit()

    def role_up_programm(self):
        self.setWindowState(self.windowState() | Qt.WindowMinimized)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    programm = MainWindow()
    programm.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
