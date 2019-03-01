# pass a matrix - grid
# identify neighbours for each element in the grid
# store it in a dict
# m -> Ht / row
# n -> wt / col
def init_zero_grid(m,n):
    return [[0]*n for _ in range(m)]

def init_mn_grid(m,n):
    return [[int(str(x) + str(y)) for y in range(n)] for x in range(m)]

#def list_all_neighbours(grid):

def list_neighbours(x,y,grid):
    act_grid = [[grid[m][n] for n in range(y-1, y+2)] for m in range(x-1, x+2)] 
    for row in range(x-1, x+2):
        for col in range(y-1, y+2):
            print(grid[row][col])

def run(m,n):
    # init mn_grid
    print(mn_grid = mn_grid(m,n))
    print(list_all_neighbours(mn_grid))
    
    
#act_grid = [mn_grid[m][n] for n in range(y-1, y+2) for m in range(x-1, x+2) if not(x==m and y==n) if mn_grid[m][n] !=11] 


#if '__input__' == '__main__':
    



