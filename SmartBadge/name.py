import lvgl as lv
from lib.screen.widgets import Label, Button, Image
from settings import Settings
from lib.app import App
from lib.screen.imagetools import get_png_info, open_png
import gc


class NameApp(App):

    def __init__(self, disp, buttons, tim):
        super().__init__(name="Name", display=disp, buttons=buttons,
                         timer=tim,
                         btn_b=self.btn_b,
                         btn_y=self.btn_y)
        gc.collect()

        cont = self.get_cont()
        cont.set_center()

        first, nick, last = self.get_name()

        self.add_item("firstname", Label(cont.lv_obj, first))
        self.add_item("nickname", Label(cont.lv_obj, nick, font_size=28))
        self.add_item("lastname", Label(cont.lv_obj, last))

        self.add_item("share", Button(cont.lv_obj, text="Share",
                                      width=cont.half()), selectable=True)
        decoder = lv.img.decoder_create()
        decoder.info_cb = get_png_info
        decoder.open_cb = open_png

        self.load_screen()

    def get_name(self):
        settings = Settings("settings.json")
        return settings.get_str_name_and_nickname().split(" ")

    def btn_y(self, x):
        self.qr = None
        from main_menu import MainMenuApp
        gc.collect()
        MainMenuApp(self.disp, self.buttons, self.tim)

    def btn_b(self, x):
        gc.collect()
        self.qr = Image(self.scr, "vcard.png", 0, 0)
        self.qr.centralise()
        self.add_item("code", self.qr)
