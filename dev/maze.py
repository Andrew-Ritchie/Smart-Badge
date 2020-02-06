import lvgl as lv
from widgets import *
import app
import game as g
import time


class MazeApp(app.GameApp):

    def __init__(self, disp):
        self.sprites = {}        
        ball = g.Sprite("ball",1,1)
        v_wall = g.Sprite("v-wall", 3,1)
        h_wall = g.Sprite("h-wall",1,3)

        self.sprites["ball"] = ball

        self.game_obj = g.Game(32,32)

        super().__init__("Maze", disp, self.game_obj, self.sprites)
        
        self.game_obj.add_sprite(ball,10,10)

        self.draw_screen()
        self.load_screen() 

        for i in range(10):
            time.sleep_ms(500)    
            self.move_sprite("rect",10+i,10)
