import pprint as pp
import random
import time
import os

def get_randomized_bit():
    rdm = random.random()
    if rdm >= 0.5:
        return 0
    else:
        return 1

def dead_state(height, width):
#    return [[0]*width]*height
    return [[0]* width for _ in range(height)]

def random_state(height, width):
    grid = dead_state(height, width)
    for h in range(0,height):
        for w in range(0, width):
           grid[h][w] = (0 if random.random() <.5 else 1)
#    print(render(grid))
    return grid

def render(grid):
    pretty = ('_' * (len(grid[0])+2)) + '\n'
    for h in range(0, len(grid)):
        row = ''
        row += '|'
        for w in range(0, len(grid[h])):
            #row += ' '
            if grid[h][w]==0:
                row += ' '
            else:
                row += '#'
        row += '|'
        pretty += row + '\n'
    pretty += ('_' * (len(grid[0])+2)) + '\n'
    return pretty

def next_element_state(alive, alive_score):
    state = 0
    if alive:
        if alive_score <=1:
            state = 0
        elif 1 < alive_score <= 3:
            state = 1
        elif alive_score > 3:
            state = 0
    else:
        if alive_score == 3:
            state = 1
        else:
            state = 0
    return state

def calc_live_score(grid, x, y):
#    neighbours =  [(m, n) for n in range(y-1, y+2) for m in range(x-1, x+2) if not(x==m and y==n) if grid[m][n] ==1]
#    neighbours =  [grid[m][n] for n in range(y-1, y+2) for m in range(x-1, x+2) if not(x==m and y==n) if grid[m][n] ==1]
    m_max, n_max = len(grid), len(grid[0])
    neighbours = [grid[m if m<m_max else m%m_max][n if n<n_max else n%n_max] for n in range(y-1, y+2) for m in range(x-1, x+2) if not(x==m and y==n) if grid[m][n]==1]
    print(neighbours)
    return len(neighbours)

def next_board_state_short(grid):
    m, n = len(grid), len(grid[0])
    next_grid = dead_state(m,n)
    print('Next Grid:')
    print(next_grid)    
    for ht in range(m):
        for wt in range(n):
            next_grid[ht][wt] = next_element_state(grid[ht][wt], calc_live_score(grid, ht, wt))

    return next_grid
    
def next_board_state(grid):
    alive_neighbours = 0
    for h in range(0, len(grid)):
        for w in range(0, len(grid[h])):
            alive_score=len([x for x in valid_neighbours(h,w,grid) if x==1])
            grid[h][w] = next_element_state(grid[h][w], alive_score)
#    print(render(grid))
    return grid

# Option 1: For circle neighbours
def circle_neigh(grid, x_max, y_max, ht, wt):
    tmp_ht = ht
    tmp_wt = wt
    if ht == -1:
        ht = x_max - 1
        print("ht of grid=" + str(x_max))
    if wt == -1:
        wt = y_max - 1
        print("Wt of grid=" + str(y_max))
    print("circle_neigh: ht:{}, wt:{}; new_ht:{}, new_wt:{}".format(tmp_ht, tmp_wt, ht, wt))
    #return (ht, wt)
    return grid[ht][wt]

# Option 2: For figuring out the circle neighbours:
# Create a 3 by 3 Matrix for the element to be searched.
# For getting the -1 cols use:
# [row[-1] for row in init_board]
# For getting the -1 rows use:
# [3, 13, 23, 33]
# init_board[-1]
# Op: [30, 31, 32, 33]

def valid_neighbours(x, y, grid):
    invalid_neigh = []
    valid_neigh = []
    circle_neighs = []
    x_max = len(grid)
    y_max = len(grid[0])
    for ht in range(x-1, x+2):
        for wt in range(y-1, y+2):
            if ht==x_max or wt==y_max:
                break
            if valid_neighbour(x, y, x_max, y_max, ht, wt):
                valid_neigh.append(grid[ht][wt])
            elif ht==x and wt==y: # For x,y skip...
                continue
            else:
                invalid_neigh.append((ht, wt))
#                circle_neighs.append(circle_neigh(grid, x_max, y_max, ht, wt))
                valid_neigh.append(circle_neigh(grid, x_max, y_max, ht, wt))
    pp.pprint('valid_neighbours' + str(valid_neigh))
    pp.pprint('circle_neighbours' + str(circle_neighs))
    pp.pprint('invalid_neighbours' + str(invalid_neigh))
    return valid_neigh

def valid_neighbour(x, y, x_max, y_max, neigh_x, neigh_y):
    if neigh_x < 0 or neigh_x >= x_max or neigh_y < 0 or neigh_y >= y_max or (neigh_x == x and neigh_y == y):
        return False
    else:
        return True

def load_board_state_csv(file_name):
    file = open("./state/" + file_name,'r')
    init_state = [[int(num) for num in line.strip("\n").split(',')] for line in file.readlines()]
    return init_state

def load_board_state(file_name):
    # open the file
    init_state = []
    try:
        file = open(file_name, "r")
        init_state = [[int(num)for num in line.strip("\n")] for line in file.readlines()]
        return init_state
    
    except IOError:
        print("Could not read the file:{}".format(file_name))

if __name__ == '__main__':
    type = input("Load initial state from file (Y/n)?")
    init_grid = []
    if type=="Y":
        file_name = "./state/" + input("file name:")
        init_grid = load_board_state(file_name)
    else:
        input = input("Please enter height & width for the game matrix: ")       
        h, w = map(int, input.split())
        init_grid = random_state(h, w)

    while True:
#        os.system('clear')
        time.sleep(1)
        pp.pprint('Game of life:')
        print(render(next_board_state(init_grid)))
        pp.pprint('Hit Ctrl + c to exit')
