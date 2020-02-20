import lvgl as lv
import widgets as w
import icons as i
import game as g
import time as t

NIGHT_THEME = lv.theme_night_init(210, lv.font_roboto_16)
DEFAULT_THEME = lv.theme_default_init(210, lv.font_roboto_16)
MATERIAL_THEME = lv.theme_material_init(210, lv.font_roboto_16)

DISP_SCALE_X = 5
DISP_SCALE_Y = 4


class App():

    def __init__(self, name, display, th=NIGHT_THEME):
        self.theme = th
        self.group = lv.group_create()
        # lv.theme_set_current(self.theme)
        self.scr = lv.obj()
        self.name = name
        self.disp = display
        self.items = {}
        self.item_ids = {}
        self.cont = w.Container(self.scr)

    def set_title(self, title, font_size=None):
        self.items['title'] = w.Label(
            self.cont.lv_obj, title, font_size=font_size)

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

    def __init__(self, name, display, th=MATERIAL_THEME, debug=False, roll_over=False, border=False, kill=False):
        self.theme = th
        lv.theme_set_current(self.theme)
        self.scr = lv.obj()
        self.name = name
        self.disp = display
        self.game = g.Game(32, 32, debugger=debug)
        self.sprites = {}
        self.roll_over = roll_over
        self.border = border
        self.kill = kill
        self.load_screen()
        # self.draw_screen()

    def load_screen(self):
        lv.scr_load(self.scr)

    def draw_screen(self):
        # 160 x 128 screen
        for x in range(self.game.x):
            for y in range(self.game.y):
                if self.game.present_at(x, y) != "ball":
                    w.Rectangle(self.scr, x*DISP_SCALE_X, y *
                                DISP_SCALE_Y, (x*DISP_SCALE_X)+DISP_SCALE_X, (y*DISP_SCALE_Y)+DISP_SCALE_Y)

    def draw_initial_sprite(self, sprite):
        x = sprite.x
        y = sprite.y
        width = sprite.width
        height = sprite.height
        if sprite.type == "BALL":
            sprite.set_icon(
                i.Ball(self.scr, width*DISP_SCALE_X, height*DISP_SCALE_Y, x*DISP_SCALE_X, y*DISP_SCALE_Y))
        elif sprite.type == "PADDLE":
            sprite.set_icon(i.PongBoard(self.scr, width*DISP_SCALE_X,
                                        height*DISP_SCALE_Y, x*DISP_SCALE_X, y*DISP_SCALE_Y))
        elif sprite.type == "WALL":
            sprite.set_icon(i.Grid(self.scr, width, height, x, y))
        else:
            print("Undefined sprite type requested, defaulting to grid of squares")
            sprite.set_icon(i.Grid(self.scr, width, height, x, y))

    def _add_spr(self, spr, x, y):
        self.sprites[spr.name] = spr
        self.game.add_sprite(spr, x, y)
        self.draw_initial_sprite(spr)

    def add_sprite(self, name, x, y, width=1, height=1, typ=None):
        sprite = g.Sprite(name, width, height, typ)
        self._add_spr(sprite, x, y)
        return sprite

    def add_custom_sprite(self, sprite, x, y):
        self._add_spr(sprite, x, y)

    def move_sprite(self, sprite_id, dx, dy):
        spr = self.sprites[sprite_id]
        killed = self.game.move_sprite(
            spr, dx, dy, roll_over=self.roll_over, border=self.border, kill=self.kill)
        x = spr.x
        y = spr.y

        if killed:
            del self.sprites[sprite_id]
            return (spr.name, sprite_id)

        if spr.type != None:
            spr.icon.move(x*DISP_SCALE_X, y*DISP_SCALE_Y)

    def sprite_wait(self, length_of_time):
        inital = t.time()
        x = False
        while not x:
            current = t.time()
            x = (current - inital) > length_of_time

    def _debug(self, string):
        self.game._debug(string)
