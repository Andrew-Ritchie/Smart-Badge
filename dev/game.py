class Game:
    def __init__(self, sprites):
        self.sprites = sprites
        #draw sprites
    
    def _open_highscore(self):
        pass

    def _write_highscore(self):
        pass

    def add_sprite(self,sprite):
        pass

    def remove_sprite(self,sprite):
        pass

    def display_leaderboard(self):


class Sprite(self):
     def __init__(self, x,y,lx,ly):
         self.x = x
         self.y = y
         self.lx = x
         self.ly = ly

     def destroy(self):
         pass

    def move(self, x, y,movement=coords):
        if movement = coords:
            self.x = x
            self.y = y
        else:
            self.x += x
            self.y += y
        #update/redraw    

    def check_collision(self, sprites):
        for sprite in sprites:
           pass  
