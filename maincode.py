import sys
from AppUI.startSplash import Main

from PyQt5.QtWidgets import QApplication

from gamee.gamee import Gamee

if __name__ == '__main__':
    gamee = Gamee()
    gamee.setGame("https://prizes.gamee.com/game-bot/karatekid2-5b745bc779d3a221d89de21c26422f2ee40a1725#tgShareScoreUrl=tg%3A%2F%2Fshare_game_score%3Fhash%3D92pG2bsQ1W6EwhiQ2CdVYBf-1imv_hz-hty3YZC0Fa7xUzXSKriu6XsnkMjL9bC1")
    print(gamee.initGameData())
    try:
        app = QApplication(sys.argv)
        app.setStyleSheet(open("core/ui/style.css", 'r').read())
        main = Main()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)
