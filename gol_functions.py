import pprint as pp
import random
from random import seed
from random import gauss

seed(1)

def get_randomized_bit_gauss():
    rdm = gauss(0,1)
    pp.pprint('rdm=' + str(rdm))
    if rdm < 0.5:
        return 0
    else:
        return 1

def get_randomized_bit():
    rdm = random.random()
#    pp.pprint('rdm=' + str(rdm))
    if rdm >= 0.5:
        return 0
    else:
        return 1

def dead_state(height, width):
#    return [[0]*width]*height
    return [[0]* width for _ in range(height)]
    
def random_state(height, width):
    grid = dead_state(height, width)
#    print("dead_state=" + str(grid))
    for h in range(0,height):
        for w in range(0, width):
#            grid[h][w] = get_randomized_bit_gauss()
           grid[h][w] = (0 if random.random() <.35 else 1)
    print(render(grid))
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

def element_state(alive, alive_score):
    state = 0
    if alive:
        if alive_score <=1:
            state = 0
        elif 1 < alive_score <= 3:
            state = 1
            print("HURRAY we got a live one here... state:{}; alive_score:{}; alive:{}".format(state, alive_score, alive))
        elif alive_score > 3:
            state = 0
    else:
        if alive_score == 3:
            state = 1
            print("HURRAY we got a live one here... state:{}; alive_score:{}; alive:{}".format(state, alive_score, alive))
        else:
            state = 0
    pp.pprint("old_state:{}; new_state:{}; alive_score:{}".format(alive, int(state), alive_score))
    return state

def next_board_state(grid):
    alive_neighbours = 0
    for h in range(0, len(grid)):
        for w in range(0, len(grid[h])):
            alive_score=len([x for x in valid_neighbours(h,w,grid) if x==1])
            print('alive_score={}'.format(str(alive_score)))
            grid[h][w] = element_state(grid[h][w], alive_score)
#            if grid[h][w]==0:
#                row += ' '
#            else:
#                row += '#'
#        row += '|'
#        pretty += row + '\n'


def valid_neighbours(x, y, grid):
    invalid_neigh = []
    valid_neigh = []
#    neighbours = {}
    x_max = len(grid)
    y_max = len(grid[0])
#    print('x-max={}, y-max={}'.format(x_max, y_max))
    for ht in range(x-1, x+2):
        for wt in range(y-1, y+2):
            if valid_neighbour(x, y, x_max, y_max, ht, wt):
                print("valid_neighbours, x={}, y={}, x_max{}, y_max{}, ht={}, wt={}".format(x, y, x_max, y_max, ht, wt))
                valid_neigh.append(grid[ht][wt])
#                if (x, y) in neighbours:
#                    neighbours[(x, y)].append(grid[ht][wt])
#                else:
#                    neighbours[(x, y)]=[grid[ht][wt]]
            else:
                invalid_neigh.append((ht, wt))
#    pp.pprint("neighbours={}; \n invalidNeighbours={}".format(neighbours, invalid_neigh))
    return valid_neigh


def valid_neighbour(x, y, x_max, y_max, neigh_x, neigh_y):

    if neigh_x < 0 or neigh_x >= x_max or neigh_y < 0 or neigh_y >= y_max or (neigh_x == x and neigh_y == y):
        return False
    else:
        return True
    
if __name__ == '__main__':
#   input = sys.stdin.read();
    input = input("Please enter height & width for the game matrix: ")       
    h, w = map(int, input.split())
#    pp.pprint(random_state(h, w))
    random_state(h, w)
#    print(get_fibonacci_huge_naive(n, m)) 


