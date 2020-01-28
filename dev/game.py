class Sprite():
    def __init__(self, name, width=1, height=1):
        self.x = -1
        self.y = -1
        self.width = width
        self.height = height
        self.name = name




class Game():
    def __init__(self, x,y,debugger=False):
        self.x = x
        self.y = y
        self.grid = []
        self.ids =["empty"]
        self.debugger = debugger
        #Can't use numpy :-(
        #Creates grid
        self.grid = Game.make_grid(self.x,self.y)
    #Returns what is found at grid location
    def present_at(self,x,y):
        try:
            return self.ids[self.grid[x][y]]
        except:
            return "empty"

    #Adds item to grid, can be set to replace or not
    def add_sprite(self, sprite, x, y, replace=False):
        sprite.x = x
        sprite.y = y

        if sprite.name not in self.ids:
            self.ids.append(sprite.name)

        p = self.colision(sprite)


        if p == True:
            if not replace:
                self.debug("Something present at this location(" + str(x) + "," + str(y) + "), could not add " + sprite.name)

            else:
                self.insert_sprite(sprite)
                self.debug("Something replaced at this location(" + str(x) + "," + str(y) + ") with "+ sprite.name)
        else:
            self.insert_sprite(sprite)
            self.debug("added " + sprite.name + " at this location(" + str(x) + "," + str(y) + ")")

    #scrolls grid in given direcion, can be set to roll over or not
    def move_all(self, direction, distance,roll_over=False, replace="empty"):
        direction = direction.upper()
        replace_id = self.get_id(replace)

        if replace_id == None:
            self.ids.append(replace)
            replace_id = self.ids.index(replace)


        if direction == "LEFT":
            self.grid = Game.shift_grid(self.grid,"HOR", -distance,roll_over, replace_id)
        elif direction == "RIGHT":
            self.grid = Game.shift_grid(self.grid,"HOR", distance,roll_over,replace_id)

    #Move one step
    def move_sprite(self, sprite, dx, dy, stop=True, replace="empty", roll_over=False, border=False, pass_through=False):
        replace_id = self.get_id(replace)
        sprite_id = self.get_id(sprite.name)
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
            if border and (sprite.x + sprite.width + sign_x > self.x or sprite.x + sign_x  < 0):
                break
            
            #sprite.x += dx
            #p = self.colision(sprite)
            #sprite.x -= dx
            #if p and pass_through == False:
                #break
            
            self.replace(sprite.x, sprite.y, sprite.x + sprite.width -1, sprite.y + sprite.height-1)
            self.move_sprite_axies(sprite, 0, sign_x)
        
        for j in range(0,count_y):
            if border and (sprite.y + sprite.height + sign_y > self.y or sprite.y + sign_y  < 0):
                break
            
            #sprite.y += dy
            #p = self.colision(sprite)
            #sprite.y -= dy
            
            #if p and pass_through == False:
                #break
            
            self.replace(sprite.x, sprite.y, sprite.x + sprite.width -1, sprite.y + sprite.height-1)
            self.move_sprite_axies(sprite, 1, sign_y)
            print(count_y, j)


    def move_sprite_axies(self, sprite, axies, distance):
        sprite_id = self.get_id(sprite.name)
        if axies == 0:
            for i in range(sprite.x, sprite.x + sprite.width):
                for j in range(sprite.y, sprite.y + sprite.height):
                    try:
                        self.grid[i+distance][j] = sprite_id
                    except:
                        self.debug("going off screen")
            sprite.x +=distance
        else:
            for i in range(sprite.x, sprite.x + sprite.width):
                for j in range(sprite.y, sprite.y + sprite.height):
                    try:
                        self.grid[i][j+distance] = sprite_id
                    except:
                        self.debug("Going off screen")
            sprite.y +=distance

    def replace(self, x,y, dx, dy, name="empty"):
        replace_id = self.get_id(name)

        for i in range(x, dx+1):
            if i >= self.x:
                break
            for j in range(y, dy+1):
                if j >= self.y:
                    break
                self.grid[i][j] = replace_id

    def colision(self, sprite):
        for i in range(sprite.x,sprite.width + sprite.x):
            for j in range(sprite.y, sprite.height + sprite.y):
                p = self.present_at(i,j)
                if p != "empty":
                    return True
        return False

    ################### Helper functions ################################################
    def make_grid(x,y,fill=0):
        grid = []
        for i in range (0,x):
            row = []
            for j in range (0,y):
                row.append(fill)
            grid.append(row)
        return grid

    def shift_grid(grid, direction, distance,roll_over,replace):
        len_x = len(grid)
        len_y = len(grid[0])
        if direction == "HOR":
            for i in range(0,len_x):
                row = Game.make_grid(1,len_y)[0]
                if roll_over == False:
                    for j in  range(0, distance):
                        row[j] = replace
                    for k in range(distance,len_y):
                        row[k] = grid[i][k-distance]
                else:
                    for j in range(0, len_y):
                        row[(j+distance)%len_y] = grid[i][j]
                grid[i] = row
        return grid

    def get_id(self, item):
        try:
            return self.ids.index(item)
        except:
            self.debug("ID not found, adding new one")
            return None

    def print(self):
        print("[")
        for i in range(0,self.x):
            print(self.grid[i])
        print("]")

    def debug(self, sentence):
        if self.debugger:
            print(sentence)

    def insert_sprite(self, sprite):
        id = self.ids.index(sprite.name)

        for i in range(sprite.x, sprite.width + sprite.x):
            for j in range(sprite.y, sprite.height + sprite.y):
                self.grid[i][j] = id
                print(self.grid[i][j])
