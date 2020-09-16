def show(table): # a function for showing our tables
    for i in range(9):
        for j in range(9):
            print(' %s '%table[i][j] ,end='')
            if (j+1) % 3 == 0 and j != 8:
                print('|',end='')
            elif (j+1) % 3 == 0 and j == 8:
                print('')
                if (i+1) % 3 == 0 and i != 8:
                    print('-----------------------------')
def is_valid(y, x, n): #check our choose is valid or not 
    for i in range(9): 
        if table[y][i] == n: #checks all numbers in column
            return False
    for i in range(9): 
        if table[i][x] == n: #checks all numbers in row
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(3):
        for j in range(3):
            if table[y0 + i][x0 + j] == n: #check all numbers in square
                return False
    return True

def solve(): #main function and set backtracking
    for i in range(9):
        for j in range(9):
            if table[i][j] == 0:
                for n in range(1,10):
                    if is_valid(i,j,n):
                        table[i][j] = n
                        solve()
                        table[i][j] = 0 i 
                return
    show(table)
    input('more?')
# change this table for any puzzle that you want to solve
table = [
    [5,0,0,3,0,0,0,0,1], 
    [0,2,0,0,4,0,3,6,0], 
    [0,0,3,0,8,0,7,0,0],
    [0,5,0,0,0,0,8,0,0],
    [8,0,0,1,3,4,0,0,6], 
    [0,0,9,0,0,0,0,7,0],
    [0,0,5,0,1,0,6,0,0],
    [0,1,7,0,6,0,0,8,0],
    [6,0,0,0,0,2,0,0,3]
]
#call main func
solve()
