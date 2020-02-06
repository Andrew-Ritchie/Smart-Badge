import lvgl as lv
from display import Display
from widgets import *

NIGHT_THEME = lv.theme_night_init(210, lv.font_roboto_16)
DEFAULT_THEME = lv.theme_default_init(210, lv.font_roboto_16)
MATERIAL_THEME = lv.theme_material_init(210, lv.font_roboto_16)

class App():

    def __init__(self, name, display, th=NIGHT_THEME):
        self.theme = th
        self.group = lv.group_create()
        lv.theme_set_current(self.theme)
        self.scr = lv.obj()
        self.name = name
        self.disp = display
        self.items = {}
        self.item_ids = {}
        self.cont = Container(self.scr)

    def set_title(self, title, font_size=None):
        self.items['title'] = Label(self.cont, title, font_size=font_size)

    def load_screen(self):
        lv.scr_load(self.scr)

    def add_item(self, name, item, selectable=False):        
        self.items[name] = item
        self.item_ids[id(item.lv_obj)] = item
        if selectable:
            lv.group_add_obj(self.group, item.lv_obj)

    def get_cont(self):
        return self.cont


class GameApp():

    def __init__(self, name, display, game, sprites, th=MATERIAL_THEME):
        self.theme = th        
        lv.theme_set_current(self.theme)
        self.scr = lv.obj()
        self.name = name
        self.disp = display
        self.game = game        
        self.sprites = sprites
        self.sprites_widget = {}

    def load_screen(self):
        lv.scr_load(self.scr)

    def draw_screen(self):
        # 160 x 128 screen
        # 5 x 4 for each element in grid
        for x in range(self.game.x):
            for y in range(self.game.y):
                if self.game.present_at(x,y) != "empty":
                    self.add_item("rect", Rectangle(self.scr, x*5, y*4, (x*5)+5, (y*4)+4))                    
    
    def update_screen(self):
        self.game.sprites[1]

    def move_sprite(self, sprite_id, x, y):
        sprite_wid = self.sprites_widget[sprite_id]
        sprite_wid.change_points(x*5, y*4, (x*5)+5, (y*4)+4)
                
    def add_item(self, name, item):        
        self.sprites_widget[name] = item        