class Sprite():
    def __init__(self, name, width=1, height=1, typ = None):
        self.x = -1
        self.y = -1
        self.width = width
        self.height = height
        self.name = name
        self.type = typ
        self.icon= None

    def set_icon(self,icon):
        self.icon = icon

class Game():
    def __init__(self, x,y,debugger=False):
        self.x = x
        self.y = y
        self.grid = []
        self.ids =["empty"]
        self.sprites = []
        self.debugger = debugger
        #Can't use numpy :-(
        #Creates grid
        self.grid = Game._make_grid(self.x,self.y)
    #Returns what is found at grid location

    #Allows for default game and sprites to be added, for game levels etc
    def add_preset_grid(grid,ids,sprites=[]):
        #Doesn't error handle case where more id numbers in grid than in self.ids
        self.grid = grid
        self.ids = ids
        self.sprites = sprites

    #Updates entire grid with new grid
    def update_grid(grid):
        self.grid = grid
    #Adds new sprite id(string)
    def add_id(ID):
        self.ids.append(ID)

    #Checks what is at a given coord
    def present_at(self,x,y):
        try:
            return self.ids[self.grid[y][x]]
        except:
            return "empty"

    #Adds item to grid, can be set to replace or not
    def add_sprite(self, sprite, x, y, replace=False):
        sprite.x = x
        sprite.y = y

        if sprite.name not in self.ids:
            self.ids.append(sprite.name)

        p = self.collision(sprite)

        if p == True:
            if not replace:
                self._debug("Something present at this location ({x},{y}), could not add {sprite_name}".format(x=str(x), y=str(y), sprite_name=sprite.name))

            else:
                self._insert_sprite(sprite)
                self._debug("Something replaced at this location({x},{y}) with {sprite_name}".format(x=str(x), y=str(y), sprite_name=sprite.name))

        else:
            self._insert_sprite(sprite)
            self._debug("added {sprite_name} at this location({x},{y})".format(x=str(x), y=str(y), sprite_name=sprite.name))


    #Removes sprite from list and coord
    def remove_sprite(sprite, replace = "empty"):
        self.sprites.remove(sprite)
        self.replace(sprite.x, sprite.y, sprite.x+sprite.height-1, sprite.y+sprite.width-1)
        return None

    #scrolls grid in given direcion, can be set to roll over or not  #TODO update sprites
    def move_all(self, direction, distance,roll_over=False, replace="empty"):
        direction = direction.upper()
        replace_id = self._get_id(replace)

        if replace_id == None:
            self.ids.append(replace)
            replace_id = self.ids.index(replace)

        if direction == "LEFT":
            self.grid = Game.shift_grid(self.grid,"HOR", -distance,roll_over, replace_id)
            for spr in self.sprites:
                spr.x -= distance
        elif direction == "RIGHT":
            self.grid = Game.shift_grid(self.grid,"HOR", distance,roll_over,replace_id)
            for spr in self.sprites:
                spr.x += distance

    #Move one sprite, given distance, currently goes 1 step at a time, may want to update this?
    def move_sprite(self, sprite, dx, dy, stop=True, replace="empty", roll_over=False, kill=False,border = False):
        replace_id = self._get_id(replace)
        sprite_id = self._get_id(sprite.name)
        count_x = abs(dx)
        count_y = abs(dy)
        try:
            sign_x = dx//count_x
        except:
            sign_x = 0
        try:
            sign_y = dy//count_y
        except:
            sign_y = 0
        for i in range(0, count_x):
            if (self.collision_edge(sprite,0,sign_x)):
                break

            if border:
                if sprite.x+sprite.width == self.x and sign_x > 0:
                    break
                elif sprite.x == 0 and sign_x < 0:
                    break
            if kill:
                if sprite.x > self.x:
                    return True
                elif (sprite.x + sprite.width) < 0:
                    return True

            self.replace(sprite.x, sprite.y, sprite.x + sprite.width -1, sprite.y + sprite.height-1)
            self.move_sprite_axis(sprite, 0, sign_x)

            if roll_over:
                if sprite.x > self.x:
                    sprite.x = 0
                    self.move_sprite_axis(sprite, 0, 0)
                elif (sprite.x + sprite.width) < 0:
                    sprite.x = self.x-sprite.width
                    self.move_sprite_axis(sprite, 0, 0)

        for j in range(0,count_y):
            if (self.collision_edge(sprite,1,sign_y)):
                break

            if border:
                if sprite.y+sprite.height == self.y and sign_y > 0:
                    break
                elif sprite.y == 0 and sign_y < 0:
                    break
            if kill:
                if sprite.y > self.y:
                    return True
                elif sprite.y + sprite.height < 0:
                    return True

            self.replace(sprite.x, sprite.y, sprite.x + sprite.width -1, sprite.y + sprite.height-1)
            self.move_sprite_axis(sprite, 1, sign_y)

            if roll_over:
                if sprite.y > self.y:
                    sprite.y = 0
                    self.move_sprite_axis(sprite, 1, 0)
                elif sprite.y + sprite.height < 0:
                    sprite.y = self.y-sprite.height
                    self.move_sprite_axis(sprite, 1, 0)
        return False

    #Move sprite along given axis
    def move_sprite_axis(self, sprite, axies, distance):
        sprite_id = self._get_id(sprite.name)
        if axies == 0:
            for i in range(sprite.y, sprite.y + sprite.height):
                for j in range(sprite.x, sprite.x + sprite.width):
                    if j + distance  >= self.x or j + distance < 0 or i >= self.y or i < 0:
                        self._debug("going off screen")
                    else:
                        self.grid[i][j+distance] = sprite_id
            sprite.x +=distance
        else:
            for i in range(sprite.y, sprite.y + sprite.height):
                for j in range(sprite.x, sprite.x + sprite.width):
                    if i + distance  >= self.y or i + distance < 0 or j >= self.x or j < 0:
                        self._debug("going off screen")
                    else:
                        self.grid[i+distance][j] = sprite_id
            sprite.y +=distance

    #Replaces ids at given coords
    def replace(self, x,y, dx, dy, name="empty"):
        replace_id = self._get_id(name)

        for i in range(x, dx+1):
            if i >= self.x:
                break
            for j in range(y, dy+1):
                if j >= self.y:
                    break
                self.grid[j][i] = replace_id

    #Detects is sprite is occupying location of another sprite
    def collision(self, sprite):
        for i in range(sprite.x,sprite.width + sprite.x):
            for j in range(sprite.y, sprite.height + sprite.y):
                p = self.present_at(i,j)
                if p != "empty":
                    return True
        return False

    #Checks if given edge of sprite will collide with an object when it moves
    def collision_edge(self, sprite, axis, direction, distance=1):
        if axis == 0:
            if direction == 1:
                for i in range(0,sprite.height):
                    if self.collision_single_point((sprite.x+sprite.width-1+distance),sprite.y+i):
                        return True
            else:
                for i in range(0,sprite.height):
                    if self.collision_single_point(sprite.x-distance,sprite.y+i):
                        return True

        else:
            if direction == 1:
                for i in range(0,sprite.width):
                    if self.collision_single_point(sprite.x+i,sprite.y+sprite.height-1+distance):
                        return True
            else:
                for i in range(0,sprite.width):
                    if self.collision_single_point(sprite.x + i,sprite.y-distance):
                        return True

        return False

    #Checks if anything would collide at given point
    def collision_single_point(self,x,y, item=0,border=False):
        try:
            return self.grid[y][x] != 0
        except:
            return border

    #Prints grid
    def print(self):
        print("[")
        for i in range(0,self.y):
            print(self.grid[i])
        print("]")

    ################### Helper functions ################################################
    #Makes array of arrays
    def _make_grid(x,y,fill=0):
        grid = []
        for i in range (0,y):
            row = []
            for j in range (0,x):
                row.append(fill)
            grid.append(row)
        return grid

    #Moves all element in grid in given direction
    def _shift_grid(grid, direction, distance,roll_over,replace):
        len_x = len(grid)
        len_y = len(grid[0])
        if direction == "HOR":
            for i in range(0,len_y):
                row = Game.make_grid(1,len_x)[0]
                if roll_over == False:
                    for j in  range(0, distance):
                        row[j] = replace
                    for k in range(distance,len_x):
                        row[k] = grid[i][k-distance]
                else:
                    for j in range(0, len_x):
                        row[(j+distance)%len_x] = grid[i][j]
                grid[i] = row
        return grid

    #Returns id of sprite or creates new id for sprite
    def _get_id(self, item):
        try:
            return self.ids.index(item)
        except:
            self._debug("ID not found, adding new one")
            return None

    #Prints to terminal if set to true
    def _debug(self, sentence):
        if self.debugger:
            print(sentence)

    #Adds sets grid coords to sprite id
    def _insert_sprite(self, sprite):
        id = self.ids.index(sprite.name)

        for i in range(sprite.y, sprite.height + sprite.y):
            for j in range(sprite.x, sprite.width + sprite.x):
                self.grid[i][j] = id
        self.sprites.append(sprite)
