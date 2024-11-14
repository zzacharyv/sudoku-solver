import display
import time

def find_empty_cell(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i,j)
    return None

def get_row(board,i,j):
    list = []
    for a in range(len(board)):
        list.append(board[i][a])
    return list

def get_column(board,i,j):
    list = []
    for a in range(len(board)):
        list.append(board[a][j])
    return list

def get_sector(board,i,j):
    y = (int)(j/3)*3
    x = (int)(i/3)*3
    list = []
    for a in range(x,x+3):
        for b in range(y,y+3):
            list.append(board[a][b])
    return list

def get_constraints(board,i,j):
    return [*set(get_sector(board,i,j)+(get_row(board,i,j))+(get_column(board,i,j)))]

def get_possiblities(board,i,j):
    constraints = get_constraints(board,i,j)
    list = []
    if board[i][j] == 0:
        for x in range(0,10):
            if x not in constraints:
                list.append(x)
    return list

def get_board_domains(board):
    b = [[[] for i in range(9)] for j in range(9)]
    for i in range(len(board)):
        for j in range(len(board[i])):
            b[i][j] = get_possiblities(board,i,j)
    return b

def forward_check_domains(domains,val,i,j):
    for a in range(len(domains)):
        # row
        if a != j:
            if val in domains[i][a]:
                domains[i][a].remove(val)
        # column
        if a != i:
            if val in domains[a][j]:
                domains[a][j].remove(val)
    # sector
    x = (int)(i/3)*3
    y = (int)(j/3)*3
    for a in range(x,x+3):
        for b in range(y,y+3):
            if b != i or a != j:
                if val in domains[a][b]:
                    domains[a][b].remove(val)
    return domains

def fill_single_domain_cells(board,domains):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if len(domains[i][j]) == 1:
                count+=1
                val = domains[i][j][0]
                forward_check_domains(domains,val,i,j)
                board[i][j] = val
                domains[i][j] = []
    return count

# last resort assigns a value and hopes it is correct
def free_choice(board,domains):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if domains[i][j] != []:
                val = domains[i][j][0] 
                board[i][j] = val
                domains[i][j].remove(val)  
                return

# looks for domain value in row col and sector that is unique, if found it assigns it to the board
def find_and_assign_unique_domain(board, domains):
    for i in range(len(board)):
        for j in range(len(board[i])):
            row = get_row(domains,i,j)
            column = get_column(domains,i,j)
            sector = get_sector(domains,i,j)
            list = []
            for a in row,column,sector:
                for b in a:
                    for c in b:
                        list.append(c)
            for a in domains[i][j]:
                if list.count(a) == 3:
                    board[i][j] = a
                    domains[i][j] = []

def solve(board):
    running = True
    domains = get_board_domains(board)
    for x in range(100):
        cell = find_empty_cell(board)
        if cell == None:
            running = False
            continue
        if fill_single_domain_cells(board,domains) == 0:            
            find_and_assign_unique_domain(board,domains)
            free_choice(board,domains)
    return board

def solve_and_display(board,screen):
    running = True
    domains = get_board_domains(board)
    for x in range(100):
        cell = find_empty_cell(board)
        if cell == None:
            running = False
            continue
        time.sleep(.3)
        if fill_single_domain_cells(board,domains) == 0:
            display.draw_board(screen, board, 504, 504)
            time.sleep(.3)           
            find_and_assign_unique_domain(board,domains)
            display.draw_board(screen, board, 504, 504)
            time.sleep(.3)
            free_choice(board,domains)
            display.draw_board(screen, board, 504, 504)
            time.sleep(.3)
    display.draw_board(screen, board, 504, 504)
    time.sleep(.3)
    return board