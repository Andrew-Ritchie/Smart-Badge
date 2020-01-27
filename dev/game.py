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
        return self.ids[self.grid[x][y]]

    #Adds item to grid, can be set to replace or not
    def add_item(self, name, x, y, replace=False):
        if name not in self.ids:
            self.ids.append(name)
        p = self.present_at(x,y)
        if p != "empty":
            if not replace:
                self.debug(p + " present at this location(" + str(x) + "," + str(y) + "), could not add " + name)

            else:
                self.grid[x][y] = self.ids.index(name)
                self.debug(p + " replaced at this location(" + str(x) + "," + str(y) + ") with "+ name) 
        else:
            self.grid[x][y] = self.ids.index(name)
            self.debug("added " + name + " at this location(" + str(x) + "," + str(y) + ")")
    
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
