grid = [[1,1,0,0],
        [1,0,1,1],
        [1,0,0,0],
        [0,1,1,1]]

tracker = [0,0,0,0]

walls = []

for i in range (0,len(grid)):
    wall = False
    current_wall = [i,0,0] 
    for j in range (0,(len(grid[0]))):
        if grid[i][j] == 1:
            print(j, grid[i][j])
            current_wall[2] += 1
            wall = True
        else:
            if wall == True:
                wall = False
                walls.append(tuple(current_wall))
            current_wall = [i, j, 0]
        
    if wall == True:
            walls.append(tuple(current_wall))

print(walls)
