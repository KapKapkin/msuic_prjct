import sys
import sqlite3

from PyQt5 import QtGui, QtMultimedia, QtWidgets, uic, QtCore
import os


class TrackWidget(QtWidgets.QWidget):
    def __init__(self, id, roditel):
        super().__init__()

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        db_path = os.path.join(BASE_DIR, "database/music_db.db")

        self.con = sqlite3.connect(db_path)

        self.cur = self.con.cursor()

        track = self.cur.execute(
            f'''SELECT title, author, duration, dir FROM all_music WHERE id = {id} ''').fetchall()

        self.liked = False
        self.id = id
        self.user_id = roditel.id
        self.roditel = roditel

        if track:

            ui_path = os.path.join(BASE_DIR, "ui/track_widget.ui")

            uic.loadUi(ui_path, self)

            self.title, self.author, self.duration, self.directory = list(
                *track)
            self.track = self.directory.split('\\')[-1]

            self.record.setIcon(QtGui.QIcon('icons/record.png'))
            self.record.clicked.connect(self.play)

            self.title_label.setText(self.title)
            self.author_label.setText(self.author)
            self.duration_label.setText(str(
                int(self.duration) // 60) + ':' + (str(int(self.duration) % 60).ljust(2, '0')))

            result = list(self.cur.execute(
                f'''SELECT * FROM 'user_{self.user_id}' WHERE music_id = {self.id}'''))

            if not result:
                self.like_btn.setIcon(QtGui.QIcon('icons/like.png'))
            else:
                self.like_btn.setIcon(QtGui.QIcon('icons/liked.png'))
                self.liked = True

            self.like_btn.clicked.connect(self.like)

    def like(self):
        if not self.liked:
            self.liked = True
            self.like_btn.setIcon(QtGui.QIcon('icons/liked.png'))
            self.cur.execute(
                f'''INSERT INTO 'user_{self.user_id}' (music_id) VALUES ({self.id}) ''')
            self.con.commit()
        elif self.liked:
            self.liked = False
            self.like_btn.setIcon(QtGui.QIcon('icons/like.png'))
            self.cur.execute(
                f'''DELETE FROM 'user_{self.user_id}' WHERE music_id = {self.id} ''')
            self.con.commit()
        self.roditel.tab3_create()

    def play(self):

        if self.roditel.current_track != self:
            self.roditel.position = 0
            fullpath = QtCore.QDir.current().absoluteFilePath(
                f'tracks/{self.track}')
            url = QtCore.QUrl.fromLocalFile(fullpath)
            
            content = QtMultimedia.QMediaContent(QtCore.QUrl(url))
            self.roditel.player.setMedia(content)
            self.roditel.player.play()
            self.roditel.label.setText(self.title)
            self.roditel.label_2.setText(self.author)
            self.roditel.pause = False
            self.roditel.current_track = self
            self.roditel.slider.setEnabled(True)
            self.roditel.play_pause.setEnabled(True)
            self.roditel.next_track.setEnabled(True)
            self.roditel.previous_track.setEnabled(True)
        else:
            self.roditel.play_pause_func()
