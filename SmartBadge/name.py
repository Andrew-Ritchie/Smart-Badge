import lvgl as lv
from lib.screen.widgets import *
from settings import Settings
from lib.app import App
from imagetools import get_png_info, open_png
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
        self.decoder = lv.img.decoder_create()
        self.decoder.info_cb = get_png_info
        self.decoder.open_cb = open_png

        self.load_screen()

    def get_name(self):
        settings = Settings("settings.json")
        return settings.get_str_name_and_nickname().split(" ")

    def btn_y(self, x):
        from main_menu import MainMenuApp
        MainMenuApp(self.disp, self.buttons, self.tim)

    def btn_b(self, x):
        gc.collect()
        QRCode(self.disp, self.buttons, self.tim)


class QRCode(App):

    def __init__(self, disp, buttons, tim):
        super().__init__(name="QRCode", display=disp, buttons=buttons,
                         timer=tim,
                         btn_y=self.btn_y)
        cont = self.get_cont()
        cont.set_center()
        gc.collect()
        print(gc.mem_free())

        before = gc.mem_free()

        self.decoder = lv.img.decoder_create()
        self.decoder.info_cb = get_png_info
        self.decoder.open_cb = open_png

        with open('ashwin.png', 'rb') as f:
            png_data = f.read()

        print("got data")

        png_img_dsc = lv.img_dsc_t({
            'data_size': len(png_data),
            'data': png_data})

        print("made desc")

        img1 = lv.img(self.scr)
        img1.align(self.scr, lv.ALIGN.IN_TOP_LEFT, 0, 0)
        img1.set_src(png_img_dsc)

        after = gc.mem_free()

        print("Foo object takes up", before - after, "bytes")

        self.load_screen()

    def btn_y(self, x):
        gc.collect()
        NameApp(self.disp, self.buttons, self.tim)
