import lvgl as lv
from display import Display
from widgets import *
import game as g

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

    def __init__(self, name, display, th=MATERIAL_THEME):
        self.theme = th        
        lv.theme_set_current(self.theme)
        self.scr = lv.obj()
        self.name = name
        self.disp = display
        self.game = g.Game(32,32)
        self.sprites = {}
        self.sprites_widget = {}
        for k in self.sprites:
            self.sprites_widget[k] = []
        self.load_screen()
        self.draw_screen()

    def load_screen(self):
        lv.scr_load(self.scr)

    def draw_screen(self):
        # 160 x 128 screen
        # 5 x 4 for each element in grid
        for x in range(self.game.x):
            for y in range(self.game.y):
                if self.game.present_at(x,y) == "ball":
                    # Rectangle(self.scr, x*5, y*4, (x*5)+5, (y*4)+4)
                    Ball(self.scr, 10*5, 10*4, x*5, y*4)
    
    def draw_initial_sprite(self,sprite):
        x = sprite.x
        y = sprite.y
        width = sprite.width
        height = sprite.height
        self.add_item(sprite.name, Ball(self.scr, width*5 ,height*4, (x)*5, (y)*4))
        # for i in range(sprite.width):
        #    for j in range(sprite.height):
        #            self.add_item(sprite.name, Ball(self.scr, 50,40, (x+i)*5, (y+j)*4))
    
    def add_sprite(self,name,x,y,width=1,height=1):
        spr = g.Sprite(name,width,height)
        self.sprites[name] = spr
        self.sprites_widget[name] = []
        self.game.add_sprite(spr,x,y)
        self.draw_initial_sprite(spr)

    def move_sprite(self, sprite_id, dx, dy):
        sprite_rects = self.sprites_widget[sprite_id]
        spr = self.sprites[sprite_id]
        self.game.move_sprite(spr, dx,dy)
        x = spr.x
        y = spr.y
        
        rec = 0
        sprite_rects[rec].move(x*5,y*4)
        # for i in range(spr.width):
        #    for j in range(spr.height):
        #         # sprite_rects[rec].change_points((x+i)*5, (y+j)*4, ((x+i)*5)+5, ((y+j)*4)+4)
        #         sprite_rects[rec].move((x+i)*5, (y+j)*4)
        #         rec += 1
                
    def add_item(self, name, item):
        print("added item")
        self.sprites_widget[name].append(item)        
