import os

from AppUI.MainUI import MainUi
from AppUI.ScreenSplash import SplashScreen
from AppUI.color import *


class Main:
    start_splash: SplashScreen
    close_splash: SplashScreen
    main_ui: MainUi

    def __init__(self):
        super().__init__()
        self.start_splash = SplashScreen("core/images/start.png", 500)
        self.start_splash.alignment = start_splash_align
        self.start_splash.color = start_splash_color
        self.start_splash.save_text_show = False
        self.start_splash.set_font(start_splash_font_size)

        self.close_splash = SplashScreen("core/images/close.png", 400)
        self.close_splash.alignment = close_splash_align
        self.close_splash.color = close_splash_color
        self.close_splash.set_font(end_splash_font_size)
        self.show()

    def show(self):
        # self.start_splash.show() todo
        self.main_ui = MainUi()
        # self.start_splash.show_message("Checking Internet Connection")
        # self.start_splash.show_message("Checking Cheat Version")
        # self.start_splash.show_message("Starting Cheat System")
        # self.start_splash.finish(self.main_ui)
        self.main_ui.show()

    def close(self):
        self.main_ui.close()
        self.close_splash.show()
        self.close_splash.show_message("Closing Cheat System")
        self.close_splash.finish(self.main_ui)
        self.main_ui.close()
        os._exit(0)
