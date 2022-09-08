import os
import urllib
from datetime import datetime
from typing import Optional
import ctypes
from PyQt5 import uic
from PyQt5.QtCore import QObject, QSize
from PyQt5.QtGui import QIcon, QIntValidator, QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QFrame
from threading import Thread

from gamee.gamee import Gamee


class MainUi(QFrame):
    QWidget_1: Optional[QWidget]
    QWidget_2: Optional[QWidget]
    loading: Optional[QWidget]
    set_url: Optional[QPushButton]
    update_score: Optional[QPushButton]
    back: Optional[QPushButton]

    def __init__(self):
        self.onlyInt = QIntValidator(0, 200000)
        super(MainUi, self).__init__()
        uic.loadUi("core/ui/app.ui", self)
        self.setWindowTitle("Gamee")
        self.setWindowIcon(QIcon("core/images/logo.ico"))
        self.setFrameShape(QFrame.StyledPanel)
        self.loginTime = datetime.now()
        self.setMouseTracking(True)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.init_ui()
        self.gamee = Gamee()

    def setMouseTracking(self, flag):
        def recursive_set(parent):
            for child in parent.findChildren(QObject):
                try:
                    child.setMouseTracking(flag)
                except:
                    pass
                recursive_set(child)

        QWidget.setMouseTracking(self, flag)
        recursive_set(self)

    def init_ui(self):
        self.QWidget_1 = self.findChild(QWidget, "QWidget_1")
        self.QWidget_1.setVisible(True)
        self.QWidget_2 = self.findChild(QWidget, "QWidget_2")
        self.QWidget_2.setVisible(False)
        self.QWidget_3 = self.findChild(QWidget, "QWidget_3")
        self.QWidget_3.setVisible(False)
        self.set_url = self.findChild(QPushButton, "set_url")
        self.set_url.clicked.connect(self.findGame)
        self.url_input = self.findChild(QLineEdit, "url_input")
        self.gameUrl_label = self.findChild(QLabel, "gameUrl_label")
        self.logo = self.findChild(QLabel, "logo")
        self.logo.setPixmap(QPixmap('core/images/start.png').scaled(500, 500))

        self.game_logo = self.findChild(QLabel, "game_logo")
        self.border = self.findChild(QLabel, "border")
        self.game_name = self.findChild(QLineEdit, "game_name_value")
        self.game_id = self.findChild(QLineEdit, "game_id_value")
        self.game_plays = self.findChild(QLineEdit, "game_plays_value")
        self.game_likes = self.findChild(QLineEdit, "game_likes_value")
        self.game_description = self.findChild(QTextEdit, "game_descriptio_value")
        self.textEdit = self.findChild(QTextEdit, "textEdit")
        self.time = self.findChild(QLineEdit, "time_value")
        self.score = self.findChild(QLineEdit, "score_value")
        self.update_score = self.findChild(QPushButton, "update_score")
        self.update_score.clicked.connect(self.updateScore)
        self.back = self.findChild(QPushButton, "back_button")
        self.back.clicked.connect(self.gotoHome)

    def setLoading(self, flag):
        if flag:
            self.set_url.setDisabled(True)
            self.set_url.setText("Loading ...")
        else:
            self.set_url.setDisabled(False)
            self.set_url.setText("Get Game Data")

    def findGame(self):
        if self.url_input.text() is not None and self.url_input.text() != '':
            try:
                Thread(target=self.setLoading, args=(True,)).start()
                self.gamee.setGame(self.url_input.text())
                gameData = self.gamee.initGameData()
                self.QWidget_1.setVisible(False)
                self.QWidget_2.setVisible(True)
                Thread(target=self.setLoading, args=(False,)).start()
                urllib.request.urlretrieve(gameData['result']['game']['image'], "core/images/game_image.jpg")
                self.border.setPixmap(QPixmap('core/images/border.png').scaled(180, 180))
                self.game_logo.setPixmap(QPixmap('core/images/game_image.jpg').scaled(190, 190))
                self.game_name.setText(gameData['result']['game']['name'])
                self.game_id.setText(str(gameData['result']['game']['id']))
                self.game_plays.setText(str(gameData['result']['game']['gamePlays']))
                self.game_likes.setText(str(gameData['result']['game']['likes']))
                self.game_description.setText(gameData['result']['gameDescription'])
                self.time.setText(str(gameData['time']).replace("T", "  "))
            except Exception as e:
                print(e)
                self.gotoHome()

    def gotoHome(self):
        self.QWidget_1.setVisible(True)
        self.QWidget_2.setVisible(False)

    def updateScore(self):
        # try:
        #     if self.url_input.text() == '' or not self.url_input.text():
        #         ctypes.windll.user32.MessageBoxW(0, "Please fill score input", "Error in score", 0)
        #
        #     self.gamee.updateGame(int(self.score.text()))
        #     print("# game score updated!")
        # except Exception as e:
        #     print(e)

        try:
            self.QWidget_1.setVisible(False)
            self.QWidget_2.setVisible(False)
            self.QWidget_3.setVisible(True)
            self.textEdit.setText(self.gamee.gameStatus)


        except Exception as e:
            print(e)
