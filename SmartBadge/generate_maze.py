def vert_wall_helper(i,j,x,y,grid, current_wall, tracker, wall_size):
    if wall_size == 1:
        for k in range (i+1, y):
            if grid[k][j-1] == 1:
                current_wall[3] +=1
                tracker[k][-1][1] = j-1
                tracker[k].append([j,x])
            else:
                break
    return tracker, current_wall

def generate_wall_list(grid):
    y = len(grid)
    x = len(grid[0])
    
    tracker = []
    for i in range(0,y):
        tracker.append([[0,x]])
    walls = []
    
    for i in range (0,y):
        for ran in tracker[i]:
            current_wall = [ran[0],i,0,1] 
            wall = False
            wall_size = 0
            for j in range (ran[0],ran[1]):
                if grid[i][j] == 1:
                    wall_size += 1
                    current_wall[2] += 1
                    wall = True
                else:
                    if wall == True:
                        wall = False
                        tracker, current_wall = vert_wall_helper(i,j,x,y,grid, current_wall, tracker, wall_size)
                        walls.append(tuple(current_wall))
                        wall_size = 0
                    current_wall = [j+1, i, 0, 1]

            if wall == True:
                wall = False
                tracker, current_wall = vert_wall_helper(i,j+1,x,y,grid, current_wall, tracker, wall_size)
                walls.append(tuple(current_wall))
                wall_size = 0
        
        if wall == True:
            wall = False
            tracker, current_wall = vert_wall_helper(i,j+1,x,y,grid, current_wall, tracker, wall_size)

            walls.append(tuple(current_wall))
            wall_size = 0
        
    return walls

def reformat_to_line(walls):
    line_points = []
    for wall in walls:
        p1 = (wall[0],wall[1])
        p2 = (wall[0]+wall[2]-1,wall[1]+wall[3]-1)
        line_points.append([p1,p2])
    return line_points