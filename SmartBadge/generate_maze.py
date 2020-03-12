grid = [[1,1,0,0,1,1,1,1,0],
        [1,0,0,0,1,0,1,1,0],
        [1,0,0,0,1,0,0,0,0],
        [1,1,1,0,1,1,1,1,0],
        [1,0,0,0,0,0,1,1,0],
        [0,0,0,0,0,0,0,0,0],
        [1,1,0,0,1,1,1,1,0],
        [1,0,0,0,0,0,1,1,0],
        [1,0,0,0,0,0,0,0,0]]

results = [(0,0,2,1),
           (0,4,4,1),
           (1,0,1,4),
           (1,4,1,3),
           (1,6,2,1),  
           (3,1,2,1),
           (3,5,3,1),
           (4,6,2,1),
           (6,0,2,1), 
           (6,4,4,1),
           (7,0,1,2), 
           (7,6,2,1),
           ]
def generate_wall_list(grid):
    y = len(grid)
    x = len(grid[0])
    
    tracker = []
    for i in range(0,y):
        tracker.append([[0,x]])
        
    walls = []
    
    for i in range (0,y):
        for ran in tracker[i]:
            current_wall = [i,ran[0],0,1] 
            wall = False
            wall_size = 0
            for j in range (ran[0],ran[1]):
                if grid[i][j] == 1:
                    wall_size += 1
                    current_wall[2] += 1
                    wall = True
                else:
                    if wall == True:
                        if wall_size == 1:
                            for k in range (i+1, y):
                                if grid[k][j-1] == 1:
                                    current_wall[3] +=1
                                    tracker[k][-1][1] = j-1
                                    tracker[k].append([j,x])
                                else:
                                    break
                        wall = False
                        walls.append(tuple(current_wall))
                    wall_size = 0
                    current_wall = [i, j+1, 0, 1]
        
            if wall == True:
                walls.append(tuple(current_wall))
    return walls

w = generate_wall_list(grid)

print(w)
print(len(w))
