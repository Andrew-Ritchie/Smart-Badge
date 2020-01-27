class Game():
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.grid = []
        self.ids =["empty"]
        #Can't use numpy :-(
        for i in range (0,x):
            row = []
            for j in range (0,y):
                row.append(0)
            self.grid.append(row)

    def print(self):
        print("[")
        for i in range(0,self.x):
            print(self.grid[i])
        print("]")

    def add_item(self, name, x, y, replace=False):
        if name not in self.ids:
            self.ids.append(name)
        p = self.contains(x,y)
        if p != "empty":
            if not replace:
                return p + " present at this location(" + str(x) + "," + str(y) + "), could not add " + name

            else:
                self.grid[x][y] = self.ids.index(name)
                return p + " replaced at this location(" + str(x) + "," + str(y) + ") with "+ name 
        self.grid[x][y] = self.ids.index(name)
        return "added " + name + " at this location(" + str(x) + "," + str(y) + ")"
    
    def contains(self,x,y):
        return self.ids[self.grid[x][y]]




